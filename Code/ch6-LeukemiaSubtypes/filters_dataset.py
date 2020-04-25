import numpy as np
import sys
import os
from PIL import Image, ImageEnhance 
import cv2


# Contrast
def enhance_contrast(directory): 
	for file_name in os.listdir(directory):
		im = Image.open(directory+file_name)
		enhancer = ImageEnhance.Contrast(im)
		enhanced_im = enhancer.enhance(4.0)
		enhanced_im.save(directory+file_name)

# Histogram equalizer
def histogram_equalizer(directory):
	for file_name in os.listdir(directory):
		img = cv2.imread(directory+file_name)

		img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)

		# equalize the histogram of the Y channel
		img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])
		# convert the YUV image back to RGB format
		img_output = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)

		cv2.imwrite(directory+file_name,img_output)


def main(): 
	directory = "LEUK-SUBTYPES/resized_im_hist_eq/"
	#enhance_contrast(directory)
	histogram_equalizer(directory)
	
if __name__ == "__main__":
   main()