import numpy as np 
import scipy.ndimage
from scipy.misc.pilutil import Image
import scipy.misc



image_path="/Users/Parth Gautam/Desktop/CT_Project-master/masked_dicom_images/026.png"
#Opening the image and converting it to the grayscale
a=Image.open(image_path).convert('L')

#Applying median-filter
b=scipy.ndimage.filters.median_filter(a,size=5,footprint=None,output=None,mode='Reflect,cval=0.0,origin=0')

#Converting the ndarray to an image
b=scipy.misc.toimage(b)

#Saving image 
b.save("/Users/Parth Gautam/Desktop/CT_Project-master/masked_images_after_filter/026_1.png")
