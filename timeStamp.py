# Embedding the graphs in tkinter window
import os
from tkinter import *
import matplotlib
from matplotlib.figure import Figure
import csv
import numpy as np
import tkinter as tk
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.widgets import Cursor
import numpy as np
import matplotlib.pyplot as plt
from tkinter import simpledialog
import matplotlib.lines as lines
from matplotlib.lines import Line2D


# Creating tkinter window
file = open("t092616_sample_hold.txt", "r+b")
outFile = open("timeStampBytes.txt", "w")

fig, ax = plt.subplots()

y = []
x = []
count = 0

while True:
    #with open("test5t.txt", "r+b") as input:
        #data = file.readline()
    byte = file.read(2)
    val = int.from_bytes(byte, "little", signed="True")
    count += 1

    x.append(count)
    y.append(val)
    #print(val)
    outFile.write(str(byte))
    outFile.write('\n')

    if count > 1000000:
        #if count >= 100000:
        break

print("file parsed")

#print(x)

ax.plot(x, y)

ax.set(xlabel='time (s)', ylabel='Force',
       title='Test Graph')
ax.grid()

fig.savefig("test.png")
plt.show()

# Plotting the graph inside the Figure
