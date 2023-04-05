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
image_r = Image.open("ribu.jpeg")

#teint en gris

#image_r = image_r.convert("L")
#image_triangle = image_triangle.convert("L")

#filtre gaussien rend plus nette l'image

#image_r = image_r.filter(ImageFilter.GaussianBlur(radius=2))
#image_triangle = image_triangle.filter(ImageFilter.GaussianBlur(radius=2))

#affiche les contour de l'images
#image_triangle = image_triangle.filter(ImageFilter.FIND_EDGES)
#image_r = image_r.filter(ImageFilter.FIND_EDGES)

#sauvegarde image
image_triangle.save("triangle_test.jpg")
image_r.save("ribu_test.jpg")




#utilisation du module histogram pour comparer la distrutivité
#couleurs entre deux images
hist1 = image_triangle.histogram()
hist2 = image_r.histogram()

sum_min = sum(min(a,b) for a,b in zip(hist1,hist2))
sum_hist1 = sum(hist1)
sum_hist2 = sum(hist2)
distance = 1-(sum_min/min(sum_hist1,sum_hist2))
print(distance)