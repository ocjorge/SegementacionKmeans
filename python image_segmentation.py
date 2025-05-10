import numpy as np
import cv2
import matplotlib.pyplot as plt
from tkinter import Tk, filedialog, simpledialog, Scale, Button, Frame, Label, HORIZONTAL
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def select_image():
    root = Tk()
    root.withdraw()  # Ocultar la ventana principal

    # Abrir diálogo de archivo para seleccionar una imagen
    file_path = filedialog.askopenfilename(
        title="Selecciona una imagen",
        filetypes=[
            ("Archivos de Imagen", "*.jpg *.jpeg *.png *.bmp *.tiff *.gif"),
            ("Todos los archivos", "*.*")
        ]
    )

    root.destroy()
    return file_path


def get_k_value():
    root = Tk()
    root.withdraw()  # Ocultar la ventana principal

    # Solicitar el valor de k
    k = simpledialog.askinteger("Valor de K", "Ingrese el número de clusters (k) inicial:",
                                minvalue=2, maxvalue=50)

    root.destroy()
    return k


def segment_image(image_rgb, k):
    # Redimensionar la imagen a un array 2D de píxeles
    pixels = image_rgb.reshape((-1, 3))

    # Convertir a tipo float para k-means
    pixels = np.float32(pixels)

    # Definir criterios y aplicar k-means
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
    _, labels, centers = cv2.kmeans(pixels, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    # Convertir de vuelta a uint8
    centers = np.uint8(centers)

    # Mapear etiquetas a valores centrales
    segmented_image = centers[labels.flatten()]

    # Redimensionar de vuelta a las dimensiones originales de la imagen
    segmented_image = segmented_image.reshape(image_rgb.shape)

    return segmented_image


def interactive_segmentation():
    # Seleccionar archivo de imagen
    image_path = select_image()

    if not image_path:
        print("No se seleccionó ninguna imagen. Saliendo...")
        return

    # Obtener valor inicial de k
    initial_k = get_k_value()

    if not initial_k:
        print("No se ingresó un valor de k. Saliendo...")
        return

    # Leer la imagen
    image = cv2.imread(image_path)

    # Convertir a RGB (OpenCV usa BGR por defecto)
    original_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Realizar la segmentación inicial
    segmented_image = segment_image(original_image, initial_k)

    # Crear una ventana Tkinter
    root = tk.Tk()
    root.title("Segmentación de Imagen con K-Means Interactivo")

    # Crear un marco para los controles
    control_frame = Frame(root)
    control_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

    # Etiqueta para el slider
    k_label = Label(control_frame, text=f"Valor de K: {initial_k}")
    k_label.pack(side=tk.LEFT, padx=5)

    # Crear una figura matplotlib
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    # Mostrar imagen original
    ax1.imshow(original_image)
    ax1.set_title('Imagen Original')
    ax1.axis('off')

    # Mostrar imagen segmentada
    segmented_plot = ax2.imshow(segmented_image)
    ax2.set_title(f'Imagen Segmentada (K={initial_k})')
    ax2.axis('off')

    # Integrar la figura matplotlib en Tkinter
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    # Función para actualizar la segmentación
    def update_segmentation(k_value):
        k_value = int(k_value)
        k_label.config(text=f"Valor de K: {k_value}")

    # Función para aplicar la nueva segmentación
    def apply_segmentation():
        k_value = int(k_slider.get())
        new_segmented_image = segment_image(original_image, k_value)

        # Actualizar la imagen segmentada
        segmented_plot.set_data(new_segmented_image)
        ax2.set_title(f'Imagen Segmentada (K={k_value})')
        canvas.draw()

        print(f"Segmentación actualizada con K={k_value}")

    # Crear un slider para ajustar el valor de K
    k_slider = Scale(control_frame, from_=2, to=50, orient=HORIZONTAL,
                     length=200, command=update_segmentation)
    k_slider.set(initial_k)
    k_slider.pack(side=tk.LEFT, padx=5)

    # Botón para aplicar la nueva segmentación
    apply_button = Button(control_frame, text="Aplicar", command=apply_segmentation)
    apply_button.pack(side=tk.LEFT, padx=5)

    # Añadir un botón de cerrar
    close_button = Button(root, text="Cerrar", command=root.destroy)
    close_button.pack(pady=10)

    # Iniciar el bucle de eventos de Tkinter
    root.mainloop()


def main():
    interactive_segmentation()


if __name__ == "__main__":
    main()
