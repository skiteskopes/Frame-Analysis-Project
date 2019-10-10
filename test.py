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
    dummy_dict = IR_dict
    final_dict = IR_dict
    for image in IR_dict:
        dummy_dict.pop(image)
        a = image
        for i in dummy_dict:
            b = i
            m = mean_squared_error(a,b)
            s = ssim(a,b)
            if m: # some sort of condition
                final_dict.pop(i)
            if s: # some sort of condition
                final_dict.pop(i)
    return final_dict   
compare_images()
