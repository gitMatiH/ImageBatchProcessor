# refactor:
# renombrar a batchCrop
# hacer método con definicion y con __name__ == "__main__"

from PIL import Image
#Using os library to walk through folders
import os

img_number = 1

# pedirle a usuario los píxels por linea de comandos
# el siguiente paso sería transformar la entrada por línea de comandos en una GUI donde seleccionas gráficamente el píxel
x1 = 1080
y1 = 820
x2 = 3000
y2 = 1790

for root, dirs, files in os.walk("batch"):
    for name in files:    
        print (os.path.join(root, name)) # will print path of files 
        path = os.path.join(root, name)
        im = Image.open(path)
        cropped = im.crop((x1,y1,x2,y2))
        cropped.save("batchprocessed/"+str(img_number)+".png", "PNG")
        img_number +=1
