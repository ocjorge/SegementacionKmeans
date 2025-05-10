# Segmentación de Imágenes con K-Means

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green)
![scikit--learn](https://img.shields.io/badge/scikit--learn-1.0%2B-orange)
![NumPy](https://img.shields.io/badge/NumPy-1.20%2B-yellow)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.5%2B-red)
![Tkinter](https://img.shields.io/badge/Tkinter-Incluido-lightgrey)
![License](https://img.shields.io/badge/License-MIT-blue)

Una aplicación interactiva en Python que segmenta imágenes utilizando el algoritmo de agrupamiento K-Means. Esta herramienta permite a los usuarios seleccionar una imagen, ajustar el número de clusters (k) en tiempo real y visualizar tanto la imagen original como la segmentada.

## 📋 Características

- Selección interactiva de imágenes mediante cuadro de diálogo
- Ajuste dinámico del valor de k mediante un slider interactivo
- Regeneración de la segmentación en tiempo real
- Visualización lado a lado de la imagen original y segmentada
- Soporte para varios formatos de imagen (JPG, PNG, BMP, TIFF, GIF)
- Interfaz gráfica intuitiva con controles interactivos

## 🔧 Requisitos

- Python 3.7+
- OpenCV
- NumPy
- scikit-learn
- Matplotlib
- Tkinter (incluido en la instalación estándar de Python)

## 💻 Instalación

1. Clonar este repositorio:
   git clone [https://github.com/yourusername/image-segmentation-kmeans.git](https://github.com/yourusername/image-segmentation-kmeans.git)
cd image-segmentation-kmeans

2. Instalar las dependencias requeridas:
pip install numpy opencv-python scikit-learn matplotlib


## 🚀 Uso

Ejecutar el script:
\`\`\`
python image_segmentation.py
\`\`\`

### Pasos:
1. Aparecerá un cuadro de diálogo de archivo - seleccione un archivo de imagen
2. Ingrese el número inicial de clusters (k) en el cuadro de diálogo
3. La aplicación mostrará la imagen original y la segmentada lado a lado
4. Ajuste el valor de k utilizando el slider en la parte superior
5. Presione el botón "Aplicar" para regenerar la segmentación con el nuevo valor de k
6. Experimente con diferentes valores para encontrar la segmentación óptima
7. Cierre la aplicación con el botón "Cerrar" cuando haya terminado

## 🔍 Cómo Funciona

La aplicación utiliza el algoritmo de agrupamiento K-Means para agrupar píxeles en la imagen basándose en su similitud de color. Los pasos son:

1. Cargar la imagen seleccionada
2. Redimensionar la imagen en un array 2D de píxeles
3. Aplicar el agrupamiento K-Means con el valor k especificado
4. Mapear cada píxel a su centro de cluster correspondiente
5. Redimensionar el resultado a las dimensiones originales de la imagen
6. Mostrar tanto la imagen original como la segmentada
7. Permitir al usuario ajustar el valor de k y regenerar la segmentación

### Algoritmo K-Means:
- **Inicialización**: Se seleccionan k centros de cluster aleatorios
- **Asignación**: Cada píxel se asigna al centro de cluster más cercano
- **Actualización**: Los centros de cluster se recalculan como el promedio de todos los píxeles asignados a ese cluster
- **Iteración**: Los pasos de asignación y actualización se repiten hasta la convergencia

## 📊 Ejemplos de Resultados

Al ejecutar la aplicación con diferentes valores de k:

- **Valores bajos de k (2-3)**: Resulta en una segmentación básica de colores, útil para separar objetos principales del fondo
- **Valores medios de k (5-10)**: Proporciona un equilibrio entre detalle y simplificación, ideal para la mayoría de las aplicaciones
- **Valores altos de k (15+)**: Preserva más detalles pero puede ser menos distinguible de la original, útil para análisis detallado

## 🔬 Aplicaciones

- Procesamiento de imágenes médicas
- Análisis de imágenes satelitales
- Reconocimiento de objetos
- Compresión de imágenes
- Segmentación de objetos en fotografías
- Análisis de textura y color

## 📝 Notas Técnicas

- El algoritmo K-Means utiliza la distancia euclidiana en el espacio de color RGB
- La convergencia se determina por un número máximo de iteraciones (100) o un umbral de error (0.2)
- La inicialización de los centros de cluster utiliza el método KMEANS_RANDOM_CENTERS de OpenCV

## 📄 Licencia

Este proyecto está licenciado bajo la Licencia MIT - consulte el archivo LICENSE para más detalles.

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Si desea contribuir:

1. Haga un Fork del proyecto
2. Cree una rama para su característica (`git checkout -b feature/nueva-caracteristica`)
3. Haga commit de sus cambios (`git commit -m 'Añadir nueva característica'`)
4. Haga Push a la rama (`git push origin feature/nueva-caracteristica`)
5. Abra un Pull Request




