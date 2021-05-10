from tkinter import *
from tkinter import filedialog
from tkinter import simpledialog, ttk 
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
NavigationToolbar2Tk) 
import matplotlib.pyplot as plt
import csv
import numpy as np


Counter = 0
modCounter = 0

x1 = []
y1 = []
xLA = []
xMod = []


index = 0
intIndex = 0

#values = range(len(x1))

with open('test3.txt', 'r') as csvfile:  # Set file designation
        plots1 = csv.reader(csvfile)
        for row in plots1:
            y1.append(int(row[0]))  # Using data points as y-axis points
            x1.append(Counter)
            if row:
                Counter += 1  # Counting rows in text file and using them for x-axis

print(Counter)
index = Counter / 8
intIndex = (int(index))


#xMod.append(0)
"""
for i in x1:
    if i % 250 == 0:            # Every 250 data points per Second
        modCounter += 1
        if modCounter % 10 == 0:
            xLA.append(modCounter)
"""            
for i in x1:
    if i % intIndex == 0:            # Every 250 data points per Second
        xMod.append(int(i / 250))
        #if modCounter % 10 == 0:
            #xLA.append(modCounter)

#print(modCounter)	
	           
print(intIndex)
print(xMod)



ax = plt.axes()
#values = range(len(x1)/250)

plt.plot(x1,y1,marker="o")

#plt.plot(x1,y1,marker="o")
#ax.xlabel("X-Axis")
#ax.ylabel("Y-Axis")
#ax.title("Set X labels in Matplotlib Plot")
#ax.xticks(np.arange(min(x1), max(x1)+1, 1.0))
#ax.set_xticks(ticL)
ax.set_xticklabels(xMod)
#ax.set_xticks(arange(0, xLA))
#ax.set_xticks(xLA)
#plt.xticks(x1)
plt.show()