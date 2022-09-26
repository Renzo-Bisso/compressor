# Llamo a la libreria Pillow que nos permite poder comprimir las imagenes
from PIL import Image
from os import mkdir
import shutil
import os  # Iportamos OS que nos permite poder leer los archivos de la carpetas

# verificamos si existe la carpeta, si no existe la creamos
aux = os.path.isdir(r"../../../Downloads/comprimido/")

if aux == False:
    mkdir("../../../Downloads/comprimido/")

# definimos la ruta de destino
file_destination = ("../../../Downloads/comprimido/")
# definimos la carpeta a donde vamos a buscar los archivos descargados
downloadsFolder = "../../../Downloads/"


if __name__ == "__main__":  # preguntamos si el archivo que estamos ejecutando desde la terminal
    # iteramos todos los rchivos que se encuentran dentro de esta carpeta y le damos el nombre de filename
    for filename in os.listdir(downloadsFolder):
        # tomamos el nombre del archivo y luego lo separamos entre el nombre del archivo y su exension
        name, extension = os.path.splitext(downloadsFolder + filename)
        if extension in [".jpg", ".jpeg", ".png"]:  # preguntamos su extencion
            # abrimos esta imagen, la intruccion de open permite manipularlo mejor  el codigo
            picture = Image.open(downloadsFolder + filename)
            picture.save(file_destination + "comprimido_" +
                         filename, optimize=True, quality=60)  # lo guardamos en la carpeta que creamos anteriormente pero agregamos la palabra comprimido al archivo
