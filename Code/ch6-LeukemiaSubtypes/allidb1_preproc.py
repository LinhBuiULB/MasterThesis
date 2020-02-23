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
	if os.path.exists("resizedALLIDB1.csv"):
  		os.remove("resizedALLIDB1.csv")

	with open("resizedALLIDB1.csv", 'w') as f:
		writer = csv.writer(f)
		first_line = ""
		for i in range(10000):
			first_line += str(i)
			first_line += ","
		writer.writerow([first_line])

	for file in myFileList:
	    print(file)
	    img_file = Image.open(file)
	    #img_file.show()

	    # get original image parameters...
	    width, height = img_file.size
	    format = img_file.format
	    mode = img_file.mode

	    # Make image Greyscale
	    img_grey = img_file.convert('L')
	    #img_grey.save('result.png')
	    #img_grey.show()

	    # Save Greyscale values
	    value = np.asarray(img_grey.getdata(), dtype=np.int).reshape((img_grey.size[1], img_grey.size[0]))
	    value = value.flatten()
	    print(value)
	    with open("resizedALLIDB1.csv", 'a') as f:
	        writer = csv.writer(f)
	        writer.writerow(value)

def get_yLabels(myFileList):
	yLabels = [] 
	for file in myFileList: 
		fileName = os.path.basename(file)
		yLabels.append([int(fileName[6])])
	return yLabels

def resize_folder(directory):
	for file_name in os.listdir(directory):
		print("Processing %s" % file_name)
		image = Image.open(os.path.join(directory, file_name))

		x,y = image.size
		print(x,y)
		new_dimensions = (100, 100)
		output = image.resize(new_dimensions, Image.ANTIALIAS)

		output_file_name = os.path.join(directory, "small_" + file_name)
		output.save(output_file_name, "JPEG", quality = 95)
	print("All done")


def main(): 
	# Resize img folder
	#resize_folder("Datasets/ALL_IDB1/im")
	
	# Create CSV from img folder
	myFileList = createFileList('Datasets/ALL_IDB1/resized_im') 
	data_to_CSV(myFileList)

	# get Y labels from the data 
	myFileListForY = createFileList('Datasets/ALL_IDB1/im') 
	y = get_yLabels(myFileListForY)
	print(y)
	
if __name__ == "__main__":
   main()