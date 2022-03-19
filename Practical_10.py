#20ce082 Harsh Patel
"""
Learned how to convert .png of image file into pdf
"""
#import os
from PIL import Img  # importing the module

#Import the image file with the image path
image = Img.open(r'Users\harshpatel\Desktop\myproject\result.png')#depends upon your path

# getting the data from .png file
picture_1 = image.convert('RGB')

# creating .pdf file at particular location
picture_1.save(r'Users\harshpatel\Desktop\result.pdf')