from PIL import Image

filename = "img/yosemite_clustered.jpg"
img = Image.open(filename)
width, height = img.size

area = (0, 0, width, height)
img = img.crop(area) 

img = img.resize((64, 64))

img.save("img/yosemite_downsampled.jpg")
