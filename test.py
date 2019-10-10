import tifffile
import numpy as np
import cv2
import os
import argparse
global IR_dict, height, width, directory
from skimage.measure import compare_ssim as ssim
directory = r'E:/test'
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
def compare_images():
    length = len(IR_dict)
    print(length)
    for x in range(length):
        a = list(IR_dict)[x]
        a_matrix = IR_dict[a]
        for y in range(x+1,length):
                b = list(IR_dict)[y]
                b_matrix = IR_dict[b]
                m = mean_squared_error(a_matrix,b_matrix)
                s = ssim(a_matrix,b_matrix)
                print(m,s)

compare_images()
