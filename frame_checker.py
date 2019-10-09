import cv2
import numpy as np
import os
import shutil
import tifffile as tiff
import math
import gc
import argparse
import ffmpy

parser = argparse.ArgumentParser()
parser.add_argument("-d","--directory", type=str, required=True, help = "directory where files are stored")
parser.add_argument("-s","--similarity", type=float, help = "similarity filter from 0.0 to 1.0, with 0.0 being filter all", default = 0.95)
args = parser.parse_args()
class frame_checker():
    def __init__(self, frame_directory,  similarity_setting):
        self.frame_directory = frame_directory
        self.similarity_setting = similarity_setting

    def frame_opener(self):
        print(self.frame_directory)
