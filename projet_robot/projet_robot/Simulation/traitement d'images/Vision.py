from PIL import Image,ImageFilter

#création image
#dimensions
dim_fond_image_width = 300
dim_fond_image_height = 200

pos_pixelx1 = 120
pos_pixelx2 = 150
pos_pixely1 = 120
pos_pixely2 = 150

#couleur motif
couleur = (255,0,0)
#création du fond
new = Image.new("RGB",(dim_fond_image_width,dim_fond_image_height))

#céation du motif
for x in range(pos_pixelx1,pos_pixelx2):
    for y in range(pos_pixely1,pos_pixely2):
        new.putpixel((x,y),couleur)

#save image    
new.save("test.jpg")

#load image 
image_triangle = Image.open("triangle.jpeg")
image_triangle = image_triangle.convert("L")
image_triangle = image_triangle.filter(ImageFilter.FIND_EDGES)
image_triangle.save("triangle_test.jpg")

image_r = Image.open("ribu.jpeg")
image_r = image_r.convert("L")
image_r = image_r.filter(ImageFilter.FIND_EDGES)
image_r.save("ribu_test.jpg")