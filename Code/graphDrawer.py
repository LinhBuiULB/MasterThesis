import matplotlib.pyplot as plt


# Dropout 

x_values = [0,0.1,0.2,0.4]
accuracy = [76.13, 76.51, 77.140, 59.890] 
accuracy_sample = [63.490, 55.530, 57.840, 45.140] 

plt.plot(x_values, accuracy, label="Without sampling")
plt.plot(x_values, accuracy_sample, label="With sampling") 
plt.ylabel('Accuracy (%)')
plt.xlabel('Dropout value')
plt.title('Model performance regarding dropout values')
plt.legend(loc='best')
plt.show()



# Weight decay 
'''
x_values = [0, 0.001, 0.01]
accuracy = [76.13, 77.470, 76.090] 
accuracy_sample = [63.490,  64.190, 60.140] 

plt.plot(x_values, accuracy, label="Without sampling")
plt.plot(x_values, accuracy_sample, label="With sampling") 
plt.ylabel('Accuracy (%)')
plt.xlabel('Weight decay value')
plt.title('Model performance regarding weight decay values')
plt.legend(loc='best')
plt.show()
'''

'''
# Noise 
x_values = [0, 0.1, 0.2, 0.4]
accuracy = [76.13, 75.520, 75.960, 75.230] 
accuracy_sample = [63.490, 64.760, 60.710, 62.080] 

plt.plot(x_values, accuracy, label="Without sampling")
plt.plot(x_values, accuracy_sample, label="With sampling") 
plt.ylabel('Accuracy (%)')
plt.xlabel('Gaussian noise rate')
plt.title('Model performance regarding gaussian noise rate')
plt.legend(loc='best')
plt.show()
'''