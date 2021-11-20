from PIL import Image

width = 600
height = 400
r = 209
g = 123
b = 193

img  = Image.new( mode = "RGB", size = (width, height), color = (r, g, b))
img.show()