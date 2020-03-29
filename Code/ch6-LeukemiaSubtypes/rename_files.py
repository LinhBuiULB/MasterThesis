# Pythono3 code to rename multiple  
# files in a directory or folder 
  
# importing os module 
import os 
  
# Function to rename multiple files 
def main(): 
    i = 731
      
    for filename in os.listdir("DEMIR-LEUKEMIA/CML"):
        '''
        if i < 10: 
            dst = "Im00" + str(i) + "_2" + ".jpg" # Im001_1.jpg 
        elif i >= 10 and i < 100: 
            dst = "Im0" + str(i) + "_2" + ".jpg" # Im010_1.jpg 
        else:
        '''
        dst = "Im" + str(i) + "_4" + ".jpg" # Im100_1.jpg 
        
        src = "DEMIR-LEUKEMIA/CML/" + filename 
        dst = "DEMIR-LEUKEMIA/CML/" + dst
        # rename() function will 
        # rename all the files
        print(src, dst) 
        os.rename(src, dst) 
        i += 1
  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 