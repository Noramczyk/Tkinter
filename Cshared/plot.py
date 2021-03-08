from matplotlib.widgets import Cursor
import numpy as np
import matplotlib.pyplot as plt
import csv
from ctypes import *
import time

#./C:\Users\Noramczyk\Desktop\Python\Cshared\myCalc.dll")
#myCalc.connect()
#myCalc = WinDLL('myCalc.dll')
myCalc = cdll('myCalc.dll')
#dynamic link library
#myCalc = WinDLL('\Users\Noramczyk\Desktop\Python\Cshared\myCalc.dll')
#myCalc = ctypes.cdll.LoadLibrary("./myCalc.dll")
myCalc.connect()
myCalc.Main()

#time.sleep(2)

Counter = 0
x = []
y = []

with open('Iwalk2.txt','r') as csvfile:                        # Set file designation
    plots = csv.reader(csvfile)
    for row in plots:
        y.append(int(row[0]))
        x.append(Counter)
        if row:
            Counter += 1

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, facecolor='#FFFFCC')


plt.plot(x,y, label='Loaded from file!')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()

cursor = Cursor(ax, useblit=True, color='red', linewidth=2)

plt.show()
