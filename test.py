import tifffile
import numpy as np
import cv2
import os
import argparse
global IR_hash, height, width
directory = r'E:/20190919_022250'
os.chdir(directory)
irfile = r'E:/20190919_022250/20190919_022255_858_IR.TIFF'
array = tifffile.imread(irfile)
print(array)
height, width = array.shape
print(height,width)
IR_hash = []
def image_opener():
    '''opens an image and then stores the array in a dictionary'''
    for image in directory:
        array = tiffile.imread(image)
        height, width = array.shape
        IR_hash[]
def mean_squared_error(a,b):
    # the 'Mean Squared Error' between the two images is the
	# sum of the squared difference between the two images;
	# NOTE: the two images must have the same dimension
    h1,w1 = a.shape
    h2,w2 = b.shape
    if h1 != h2 or w1 != w2:
        print('ERROR: Mean squared test failed because image.shape are of different dimensions')
    else:
         err = np.sum((a.astype("float") - b.astype("float")) ** 2)
	     err /= float(a.shape[0] * a.shape[1])


    
