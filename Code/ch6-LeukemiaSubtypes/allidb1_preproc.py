# Convert images dataset into CSV file. 
from PIL import Image
import numpy as np
import sys
import os
import csv 

#Useful function
def createFileList(myDir, format='.jpg'):
	fileList = []
	print(myDir)
	for root, dirs, files in os.walk(myDir, topdown=False):
		for name in files:
			if name.endswith(format):
				fullName = os.path.join(root, name)
				fileList.append(fullName)
	return fileList

def data_to_CSV(myFileList):
	csv_file_name = "csv/resizedLEUKSUBTYPES-200x200.csv"
	if os.path.exists(csv_file_name):
  		os.remove(csv_file_name)

	with open(csv_file_name, 'w') as f:
		writer = csv.writer(f, delimiter=' ', escapechar=' ', quoting=csv.QUOTE_NONE)
		newline = '' 
		for i in range(40000):
			newline += str(i)
			if(i != 39999):
				newline += ","
		writer.writerow([newline])


	for file in myFileList:
	    print(file)
	    img_file = Image.open(file)
	    #img_file.show()

	    # get original image parameters...
	    width, height = img_file.size
	    format = img_file.format
	    mode = img_file.mode

	    # Format img (color or greyscale)
	    img_format = img_file.convert('P') # parameter 'L' = greyscale , 'P' = color
	    #img_format.save('result.png')
	    #img_format.show()

	    # Save values
	    value = np.asarray(img_format.getdata(), dtype=np.int).reshape((img_format.size[1], img_format.size[0]))
	    value = value.flatten()
	    print(value)
	    with open(csv_file_name, 'a') as f:
	        writer = csv.writer(f)
	        writer.writerow(value)

def get_yLabels(myFileList):
	yLabels = [] 
	for file in myFileList: 
		fileName = os.path.basename(file)
		yLabels.append([int(fileName[12])])
	return yLabels

def resize_folder(directory):
	for file_name in os.listdir(directory):
		print("Processing %s" % file_name)
		image = Image.open(os.path.join(directory, file_name))
		if image.mode != 'RGB':
			image = image.convert('RGB')
		x,y = image.size
		print(x,y)
		new_dimensions = (200, 200)
		output = image.resize(new_dimensions, Image.ANTIALIAS)

		output_file_name = os.path.join(directory, "small_" + file_name)
		output.save(output_file_name, "JPEG", quality = 95)
	print("All done")


def main(): 
	# Resize img folder
	#resize_folder("LEUK-SUBTYPES/im")
	
	# Create CSV from img folder
	myFileList = createFileList('LEUK-SUBTYPES/resized_im_200x200') 
	data_to_CSV(myFileList)

	# get Y labels from the data 
	#myFileListForY = createFileList('ALL_IDB1/im') 
	#y = get_yLabels(myFileListForY)
	#print(y)
	
if __name__ == "__main__":
   main()