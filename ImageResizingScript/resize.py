import os
from PIL import Image
resize_method = Image.ANTIALIAS
    #Image.NEAREST)  # use nearest neighbour
    #Image.BILINEAR) # linear interpolation in a 2x2 environment
    #Image.BICUBIC) # cubic spline interpolation in a 4x4 environment
    #Image.ANTIALIAS) # best down-sizing filter


new_height= 128
new_width= 128
new_resolution = (new_width, new_height)
extensions= ['JPG']

path= os.path.abspath(".")
	
if __name__ == "__main__":
    for f in os.listdir(path):
        if os.path.isfile(os.path.join(path,f)):
            f_text, f_ext= os.path.splitext(f)
            f_ext= f_ext[1:].upper()
            if f_ext in extensions:
                image = Image.open(os.path.join(path,f))
                width, height= image.size
                if width != new_width and height != new_height: 
                    image = image.resize(new_resolution, resize_method)
                    image.save(os.path.join(path,f))