import matplotlib.pyplot as plt
import numpy as np
import csv

#fig, ax = plt.subplots()

size = 0.3
#vals = np.array([[80., 32.], [37., 40.], [29., 10.]])
vals = np.array([[10., 10.],[80., 80.], [10.,10.]]) # 						Two divided up
vals2 = np.array([[20., 20.],[80., 80.], [20.,20.]]) # 

#subplot2grid(shape:(row,col)pos:(row, col))

plot1 = plt.subplot2grid((3, 3), (2, 0), rowspan = 2, colspan = 4)  	# (1,0)
plot2 = plt.subplot2grid((3, 3), (0, 0), rowspan = 2) 			  		# (0,0)
plot3 = plt.subplot2grid((3, 3), (0, 2), rowspan = 2) 					# (0,2)


cmap = plt.get_cmap("tab20c")
outer_colors = cmap(np.arange(3)*4)
inner_colors = cmap([1, 2, 5, 6, 9, 10])

x = []
y = []

Counter = 0
threshold = 1200

with open('test.txt','r') as csvfile:                        # Set file designation
    plots = csv.reader(csvfile)
    for row in plots:
        y.append(int(row[0]))
        x.append(Counter)
        if row:
            Counter += 1


#plt.ion()
plot1.plot(x,y, label='Loaded from file!')
plot1.plot([0., Counter], [threshold, threshold], "k--")
plot1.set_xlabel('Time')
plot1.set_ylabel('Force')
#plot1.set_title('Selected Data Set')
#plt.scatter(x,y)
#plot1.legend()
#plt.show()
"""
canvas = FigureCanvasTkAgg(fig, master=window)
canvas.draw()
canvas.get_tk_widget().grid(row=3, column=1, rowspan = 4, padx = 5, pady = 5)

                                                                                # navigation toolbar
toolbarFrame = Frame(master=window)
toolbarFrame.grid(row=7,column=1)
toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)

window.cursor = Cursor(window.ax, useblit=True, color='red', linewidth=2)  

"""

plot2.pie(vals.sum(axis=1), radius=1, colors=outer_colors,			# Outer plot
		wedgeprops=dict(width=size, edgecolor='w'))

plot3.pie(vals2.sum(axis=1), radius=1, colors=outer_colors,			# Outer plot
       wedgeprops=dict(width=size, edgecolor='w'))

"""
ax.pie(vals.flatten(), radius=1-size, colors=inner_colors,		# Inner circle
       wedgeprops=dict(width=size, edgecolor='w'))

"""


#ax.set(aspect="equal", title='Pie plot with `ax.pie`')
plt.tight_layout()
plt.show()