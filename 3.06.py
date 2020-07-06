##########################################################################################################
##############################              'pillow' library             #################################
##########################################################################################################

# library - 

# pillow library  : useful for - Editing images : 
#                changing img extensions,resize,sharpness,brightness,color,contrast,image blur,GuassianBlur


#######################################     pillow library   ##############################################

# from PIL import Image

# img1 = Image.open('dog0.jpg')      # object
# print(img1)         # <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=2048x1174 at 0x7F357ED345C0>

# img1.save('Images/cutedog.png')
# img1.save('Images/cutedog.pdf')           # if exists doesn't create new one

# img1.show()   # used to show img1     # ERROR =>  Segmentation fault (core dumped) => install Imagemagick


# img1.thumbnail((400,400))                  # thumbnail(tuple)  => maxSize = (250,250)
# img1.save('Images/lovelydog.jpg')
# img1.show()

###################################################################

#################

# from PIL import Image
# import os

# for item in os.listdir('/home/jerry/🃏 Start/python 0.0/Images'):          
#     if item.endswith('.jpg'):
#         print(item)
#         img0 = Image.open(f'/home/jerry/🃏 Start/python 0.0/Images/{item}')
#         imgname , extension = os.path.splitext(item)
#         img0.save(f'/home/jerry/🃏 Start/python 0.0/Images/{imgname}.png')

################## --------- Sharpness ----------

# from PIL import Image,ImageEnhance

# img1 = Image.open('Images/dog3.jpg')

# enhancer = ImageEnhance.Sharpness(img1)         # => object
# # print(enhancer)                               # <PIL.ImageEnhance.Sharpness object at 0x7fcb88e8b518>

############# Error :=> if  "enhancer = ImageEnhance.Sharpness(img1)"
# ###########          =>>># enhancer = ImageEnhance.Sharpness (img.convert('RGB'))

# enhancer.enhance(50).save('enhancedImg.jpg')    # 0-little bit blur # 1-original
# # enhancer.enhance(50).show()

################## --------- color ----------

# from PIL import Image,ImageEnhance

# img1 = Image.open('Images/dog3.jpg')

# enhancer = ImageEnhance.Color(img1)              
 
# enhancer.enhance(0).save('Images/enhancedImg.jpg')      # 0-black and white # 1-original

################## --------- brightness ----------

# from PIL import Image,ImageEnhance

# img1 = Image.open('Images/dog0.jpg')

# enhancer = ImageEnhance.Brightness(img1)              
 
# enhancer.enhance(0.5).show()     # 0-complete black  # 1-original

################## --------- Blur ----------

# from PIL import Image,ImageEnhance,ImageFilter

# img1 = Image.open('Images/dog0.jpg')

# img1.filter(ImageFilter.GaussianBlur(radius=8)).show()


##########################################################################################################
##########################################################################################################