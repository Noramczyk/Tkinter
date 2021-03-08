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
win = Tk()

#subplot(nrows, ncols, index, **kwargs)


# Creating Figure.
fig = Figure(figsize = (7,7), dpi = 110)			#dpi = zoom in or out


size = 0.3
#vals = np.array([[80., 32.], [37., 40.], [29., 10.]])
vals = np.array([[10., 10.],[80., 80.], [10.,10.]]) # 						Two divided up
vals2 = np.array([[20., 20.],[80., 80.], [20.,20.]]) # 



y = []
x = []

Counter = 0
threshold = 1000


cmap = plt.get_cmap("tab20c")
outer_colors = cmap(np.arange(3)*4)
inner_colors = cmap([1, 2, 5, 6, 9, 10])

l1 = tk.Button(win,
           text = "Data Selection",
           font = "bold")

l1.grid(row = 1, column = 0, pady = 10)


with open('test.txt','r') as csvfile:                        # Set file designation
        plots = csv.reader(csvfile)
        for row in plots:
            y.append(int(row[0]))
            x.append(Counter)
            if row:
                Counter += 1

# Plotting the graph inside the Figure
plt.ion()
a = fig.add_subplot(413)					#438
a.plot(x,y, label = "Data")
a.set_xlabel("Time")
a.set_ylabel("Force")
a.set_title("Graph_Tk")
a.plot([0., Counter], [threshold, threshold], "k--")
a.legend()
a.grid()


b = fig.add_subplot(441)					#441

b.pie(vals.sum(axis=1), radius=1, colors=outer_colors,			# Outer plot
		wedgeprops=dict(width=size, edgecolor='w'))

c = fig.add_subplot(444)					#444	

c.pie(vals2.sum(axis=1), radius=1, colors=outer_colors,			# Outer plot
       wedgeprops=dict(width=size, edgecolor='w'))


# Creating Canvas
canv = FigureCanvasTkAgg(fig, master = win)
canv.draw()
canv.get_tk_widget().grid(row=3, column=2, rowspan = 4, padx = 20, pady = 20)

#get_widz = canv.get_tk_widget()
#get_widz.pack()

win.mainloop()