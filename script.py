# Llamo a la libreria Pillow que nos permite poder comprimir las imagenes
from PIL import Image
import os  # Iportamos OS que nos permite poder leer los archivos de la carpetas

# definimos la carpeta a donde vamos asir a bucar los archivos descargados
downloadsFolder = "../../../Downloads/"

if __name__ == "__main__":  # preguntamos si el archivo que estamos ejecutando desde la terminal
    # iteramos todos loarchivos que se encuentran dentro de esta carpeta y le damos el nombre de filename
    for filename in os.listdir(downloadsFolder):
        # tomamos el nombre del archivo y luego lo separamos entre el nombr edel archivo y su exension
        name, extension = os.path.splitext(downloadsFolder + filename)
        if extension in [".jpg", ".jpeg", ".png"]:  # preguntamos su extencion
            # abrimos esta imagen, la intruccion de open permite manipularlo mejor  el codigo
            picture = Image.open(downloadsFolder + filename)
            picture.save(downloadsFolder + "comprimido_" +
                         filename, optimize=True, quality=60)  # lo guardamos en la misma carpeta pero agregamos la palabra comprimido al archivo
