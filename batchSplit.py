# https://www.codespeedy.com/get-the-basic-image-information-with-pillow-python/
from PIL import Image
# Using os library to walk through folders
import os

img_number = 1
# agregar comando h (horizontally) y v (vertically) por el argumento de la funcion, v sería por defecto


for root, dirs, files in os.walk("batch"):
    for name in files:    
        print (os.path.join(root, name)) # will print path of files 
        path = os.path.join(root, name)
        im = Image.open(path)
	#tomar medidas de la imagen dinámicamente
	x1 = 1080
	y1 = 820
	x2 = 3000
	y2 = 1790
        cropped = im.crop((x1,y1,x1/2,y2))
        cropped.save("batchprocessed/"+str(img_number)+".png", "PNG")
        img_number +=1
