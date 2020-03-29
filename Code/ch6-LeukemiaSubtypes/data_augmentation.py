# Based from the Code of Thomas Himblot 
# https://gist.github.com/tomahim/9ef72befd43f5c106e592425453cb6ae 

import os
import random
from scipy import ndarray, ndimage

# image processing library
import skimage as sk
from skimage import transform
from skimage import util
from skimage import io
from skimage import exposure
from skimage import img_as_ubyte
from skimage.transform import AffineTransform, warp

def random_rotation(image_array: ndarray):
	# pick a random degree of rotation between 25% on the left and 25% on the right
	random_degree = random.uniform(-25, 25)
	return sk.transform.rotate(image_array, random_degree)

def random_noise(image_array: ndarray):
	# add random noise to the image
	return sk.util.random_noise(image_array)

def blur(image_array: ndarray): 
	return ndimage.uniform_filter(image_array, size=(11, 11, 1))

def horizontal_flip(image_array: ndarray):
	# horizontal flip doesn't need skimage, it's easy as flipping the image array of pixels !
	return image_array[:, ::-1]

def vertical_flip(image_array: ndarray):
	# vertical flip doesn't need skimage, it's easy as flipping the image array of pixels !
	return image_array[::-1, :]

def random_gamma(image_array: ndarray): 
	return exposure.adjust_gamma(image_array, gamma=random.uniform(0,3),gain=1)

# pas de crop car peut enlever des info importantes, pareil pour shift

# dictionary of the transformations we defined earlier
available_transformations = {
	#'rotate': random_rotation
	#'noise': random_noise,
	#'blur': blur,
	#'horizontal_flip': horizontal_flip,
	#'vertical_flip': vertical_flip,
	'random_gamma': random_gamma,
}

folder_path = 'LEUK-SUBTYPES/resized_im'
num_files_desired = 10000

# find all files paths from the folder
images = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

num_generated_files = 0
while num_generated_files <= num_files_desired:
	# random image from the folder
	image_path = random.choice(images)
	print(image_path)
	image_file_name = image_path[25:41] # get image file name (20-33 for ALL-IDB, 25-41 for LEUK-SUBTYPES)
	print(image_file_name)
	# read image as an two dimensional array of pixels
	image_to_transform = sk.io.imread(image_path)
	# random num of transformation to apply
	num_transformations_to_apply = random.randint(1, len(available_transformations))

	num_transformations = 0
	transformed_image = None
	while num_transformations <= num_transformations_to_apply:
		# random transformation to apply for a single image
		key = random.choice(list(available_transformations))
		transformed_image = available_transformations[key](image_to_transform)
		num_transformations += 1

	new_file_path = '%s/%s_augmented_image.jpg' % (folder_path, image_file_name)

	# write image to the disk
	io.imsave(new_file_path, img_as_ubyte(transformed_image))
	num_generated_files += 1