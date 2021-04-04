# importing libraries 
import matplotlib.pyplot as plt 
import numpy as np 
import math 
import csv
  
# Get the angles from 0 to 2 pie (360 degree) in narray object 
X = np.arange(0, math.pi*2, 0.05) 

x = []
y = []

x2 = []
y2 = []

s2 = 5000
f2 = 9000

row1 = 0
row2 = 10000

Counter = 0
Counter2 = 0

start, end = 500, 1500


with open('test1.txt','r') as csvfile:                        # Set file designation
    plots = csv.reader(csvfile)
    for row1 in plots:
        y.append(int(row1[0]))
        x.append(Counter)
        if row1:
            Counter += 1

x2 = (x[s2:f2])			# List slicing!!
y2 = (y[s2:f2])

#print(x2)
#print(y2)


# Using built-in trigonometric function we can directly plot 
# the given cosine wave for the given angles 
#Y1 = np.sin(X) 
Y2 = np.cos(X) 
Y3 = np.tan(X) 
Y4 = np.tanh(X) 
  
# Initialise the subplot function using number of rows and columns 
figure, axis = plt.subplots(2, 2) 
  
# For Sine Function 
axis[0, 0].plot(x, y) 
axis[0, 0].set_title("Sine Function") 
  
# For Cosine Function 
axis[0, 1].plot(x2, y2) 
axis[0, 1].set_title("Cosine Function") 
  
# For Tangent Function 
axis[1, 0].plot(X, Y3) 
axis[1, 0].set_title("Tangent Function") 
  
# For Tanh Function 
axis[1, 1].plot(X, Y4) 
axis[1, 1].set_title("Tanh Function") 
  
# Combine all the operations and display 
plt.show() 