from PIL import Image

img=Image.open("h.jpeg")
img.resize(100, 100)
img.show()