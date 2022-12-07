from sys import argv
from PIL import Image, ImageOps
from pylab import *

def main():
    img_name = argv[1]
    img = Image.open(img_name)
    img = ImageOps.exif_transpose(img)
    img = img.convert('L')
    img.save('gray_'+img_name)
    img.show()
    #im=array(img)
    #figure()
    #hist(im.flatten(), 16)
    #show()

    print("well done!")

if __name__ == "__main__":
    main()

