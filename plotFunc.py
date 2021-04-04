from tkinter import *
from tkinter import filedialog
from tkinter import simpledialog, ttk 
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
NavigationToolbar2Tk) 
import matplotlib.pyplot as plt
import csv
  
# plot function is created for  
# plotting the graph in  
# tkinter window 
def plot(): 

    secCounter = 0
    Counter = 0

    x1 = []
    x2 = []
    y1 = []
    y2 = []

	
    fileone = simpledialog.askstring(" ", "Enter File name: ")  # FINALLY !!!
    filetwo = simpledialog.askstring(" ", "Enter File name: ")  # FINALLY !!!


    with open(fileone, 'r') as csvfile:  # Set file designation
        plots1 = csv.reader(csvfile)
        for row in plots1:
            y1.append(int(row[0]))  # Using data points as y-axis points
            x1.append(Counter)
            if row:
                Counter += 1  # Counting rows in text file and using them for x-axis
                		
    with open(filetwo, 'r') as csvfile:  # Set file designation
        plots2 = csv.reader(csvfile)
        for row in plots2:
            y2.append(int(row[0]))  # Using data points as y-axis points
            x2.append(secCounter)
            if row:
                secCounter += 1  # Counting rows in text file and using them for x-axis
        

    fig, ax = plt.subplots(1, figsize=(8, 6))
  
  
    
    # plotting the graph 
    ax.plot(x1, y1, color="r") 
    ax.plot(x2, y2, color="g")
  
    # creating the Tkinter canvas 
    # containing the Matplotlib figure 
    canvas = FigureCanvasTkAgg(fig, 
                               master = window)   
    canvas.draw() 
  
    # placing the canvas on the Tkinter window 
    canvas.get_tk_widget().pack() 
  
    # creating the Matplotlib toolbar 
    toolbar = NavigationToolbar2Tk(canvas, 
                                   window) 
    toolbar.update() 
  
    # placing the toolbar on the Tkinter window 
    canvas.get_tk_widget().pack() 
  
# the main Tkinter window 
window = Tk() 
  
# setting the title  
window.title('Plotting in Tkinter') 
  
# dimensions of the main window 
window.geometry("500x500") 
  
# button that displays the plot 
plot_button = Button(master = window,  
                     command = plot, 
                     height = 2,  
                     width = 10, 
                     text = "Plot") 
  
# place the button  
# in main window 
plot_button.pack() 
  
# run the gui 
window.mainloop()