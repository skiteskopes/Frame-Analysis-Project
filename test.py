import tifffile
import numpy as np
import cv2
import os
import argparse
global IR_dict, height, width, directory
from skimage.measure import compare_ssim as ssim
directory = r'E:/20190919_022250'
os.chdir(directory)
IR_dict = {}
def image_opener():
    '''opens an image and then stores the array in a dictionary'''
    for image in os.listdir(directory):
        if image.endswith(".TIFF"):
            array = tifffile.imread(image)
            IR_dict[image]=array
    print(IR_dict)
image_opener()
def mean_squared_error(a,b):
    # the 'Mean Squared Error' between the two images is the
	# sum of the squared difference between the two images;
	# NOTE: the two images must have the same dimension
    h1,w1 = a.shape
    h2,w2 = b.shape
    if h1 != h2 or w1 != w2:
        print('ERROR: Mean squared test failed because image.shape are of different dimensions')
        return 1
    else:
        err = np.sum((a.astype("float") - b.astype("float")) ** 2)
        err /= float(a.shape[0] * a.shape[1])
    return err
image_opener()
def compare_images():
    for image in IR_dict: 
        print(image)

compare_images()
