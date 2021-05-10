from tkinter import *
from tkinter import filedialog
from tkinter import simpledialog, ttk 
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
NavigationToolbar2Tk) 
import matplotlib.pyplot as plt
import csv
import numpy as np
  
# plot function is created for  
# plotting the graph in  
# tkinter window 


xCounter = 0
yCounter = 0
Counter = 0

x1 = []
x2 = []
y1 = []
y2 = []

j = 0
#values = range(len(x))

#fileone = simpledialog.askstring(" ", "Enter File name: ")  # FINALLY !!!
#filetwo = simpledialog.askstring(" ", "Enter File name: ")  # FINALLY !!!


with open("test1.txt", 'r') as csvfile:  # Set file designation
    plots1 = csv.reader(csvfile)
    for row in plots1:
    		y1.append(int(row[0]))
    		x1.append(Counter)
    		if row:
    			Counter += 1

    			

y2.append(0)

while j < (len(y1)):
	j += 1
	if j % 250 == 0:
		y2.append(y1[j])
		yCounter += 1


for i in x1:
	if i % 250 == 0:
		minMod = i / 250
		x2.append(minMod)
		xCounter += 1

print(" ", y2)
print(" ", x2)

print("xLen: ", len(x2))
print("yLen: ", len(y2))
print("X: ", xCounter)
print("Y: ", yCounter)

#print(arrY)

#fig, ax = plt.subplots(1, figsize=(8, 6))



# plotting the graph 
plt.plot(x2, y2, 'o', color="r") 
#ax.xlabel("X-Axis")
#ax.ylabel("Y-Axis")
#ax.title("Set X labels in Matplotlib Plot")
#ax.set_xticks(np.arange(0, len(x1)+1, 250))

#ax.plot(x2, y2, color="g")
plt.show()

  
