import tkinter as tk
from tkinter.ttk import *
from tkinter import *
import os
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.widgets import Cursor
import numpy as np
import matplotlib.pyplot as plt
import csv
from tkinter import simpledialog
import matplotlib.lines as lines
from matplotlib.lines import Line2D
from tkinter import filedialog


global newVal

def new_window(_class):                                 # Needed to create new window (Patient / Phys) Views
        new = tk.Toplevel(main_screen)                          
        _class(new)


class logSuccess:
    def __init__(self, window):

        self.window = window
        
        
        Counter = 0
        threshold = 1100
        impactThreshold = 0
        threshCounter = 0
        impactCounter = 0
        threshTot = 0
        seconds = 0
        totalCount = 0

        size = 0.3  
        yVal = 800 
                                            
                
        menubar = Menu(window)
        window.config(menu=menubar)
        window.geometry("1500x1500")                                    # Set overall size of screen

        fileMenu = Menu(menubar)                                        # Sets drop down menu just exit is implemented right now
        fileMenu.add_command(label="Exit", command = window.quit)
        menubar.add_cascade(label="Menu", menu = fileMenu)

                            
        #val2=np.array([[20.,20.],[80.,80.],[20.,20.]]) 
        threshold = 1200

        cmap = plt.get_cmap("tab20c")
        outer_colors = cmap(np.arange(3)*4)                             # Random color generated for pie charts
        inner_colors = cmap([1, 2, 5, 6, 9, 10])                        # Not being used but could at more depth for more data

        y = []                                                      # x and y lists used to fill file data
        x = []
       
                
        with open("test.txt",'r') as csvfile:                         # Set file designation
            plots = csv.reader(csvfile)
            for row in plots:
                y.append(int(row[0]))                               # Using data points as y-axis points
                x.append(Counter)
                if row:                                             
                    Counter += 1                                    # Counting rows in text file and using them for x-axis

        for i in y:                                                 #  Number of impacts over set threshold
            if i > threshold:
                threshCounter += 1
                continue

        for i in y:                                                 #  Number of impacts over ZERO
            if i > impactThreshold:
                impactCounter += 1
                continue

        for i in x:                                                 #  Number of impacts 
            totalCount += 1
            continue

        
        second = totalCount / 250

          
        threshCalc = threshCounter / Counter                        # % Calc
        threshTot = 1 - threshCalc                                  
   
        print("Total Above: ", threshCounter)                       # Output to make sure everything is right
        print("Total Impacts: ", impactCounter)
        print("Total Points: ", Counter)
        print("Threshold %: ", threshCalc)
        print("Total Thresh %: ", threshTot)
        print("Impact Counter: ", impactCounter)
        print("Total Count: ", totalCount)
        print("Seconds total: ", second)

        def setFunc():                                                                   # Not functioning correctly (still needs work!!!)

            plt.ion()

            threshold = simpledialog.askinteger("Theshold Value ", "Enter new value: ")    # FINALLY !!!

            a.plot([0., Counter], [threshold, threshold], "k--")
            print(threshold)



    # ******************************************************************
        def clear():                                                                    # Not being called as of now
            #plt.ion()
            #threshold = 0
            newVal = simpledialog.askstring("Theshold Value ", "Enter new value: ")
            print(newVal)

        

        vals = np.array([[10., 10.], [threshCounter,threshCounter]])                #  Setting pie chart %           
        vals2 = np.array([[50., 50.], [10.,10.]]) # 

        sizesB = [threshCalc, threshTot]                                            # Setting pie b (Threshold) chart labels
        labelsB = 'Above %', 'Total %'

        sizesC = [7, 93]                                                            # Setting pie c (Impact) chart labels
        labelsC = 'Above %', 'Total %'

        
        l1 = Label(window,
                text = "Threshold Exceeded: ",
                font = "bold")

        l2 = Label(window, 
                borderwidth = 10,
                width = 20,
                bg = "mint cream",                      # sets background color
                relief = "flat",                        # flat, grooved, raised, solid, sunken for different looks in gui
                text = "Patient ID - Name")
        l3 = Label(window, 
                borderwidth = 10,
                width = 20,
                bg = "mint cream",
                relief = "flat",
                text = "Data Set - Primary")
        l4 = Label(window, 
                borderwidth = 10,
                width = 20,
                bg = "mint cream",
                relief = "flat",
                text = "Data Set - Secondary")

        l5 = Label(window,
                text = "Total Activity: ",
                font = "bold")


        R2 = Label(window,
                text = "Analysis Tools",
                font = "bold")

        checkbutton=Checkbutton(window, text="Autoscale")

        R3 = Label(window, 
                borderwidth = 10,
                width = 20,
                relief = "flat",
                bg = "mint cream",
                text = threshCounter)               # One way to display a calculated value
        
        """
        R4 = tk.Button(window, 
                borderwidth = 2,
                width = 20,
                text = "Clear",
                bg = "mint cream",
                command = clear)
        """
                  
        R5 = Label(window, 
                borderwidth = 10,
                width = 20,
                relief = "flat",
                bg = "mint cream",
                text = impactCounter)

        setThreshold = tk.Button(window,
                text="Set Threshold",
                bg = "mint cream",
                command = setFunc)                  # command calls any function you want!

        l1.grid(row = 2, column = 4, pady = 5)                 
        l2.grid(row = 2, column = 0, pady = 5)
        l3.grid(row = 3, column = 0, pady = 5)
        l4.grid(row = 4, column = 0, pady = 5)
        l5.grid(row = 3, column = 4, pady = 5)
        R3.grid(row = 2, column = 5, pady = 5)
        R5.grid(row = 3, column = 5, pady = 5)

        #checkbutton.grid(row = 2, column = 6, pady = 5)
        setThreshold.grid(row = 4, column = 5, pady = 5)
       
        fig1 = plt.figure(figsize=(7,6), dpi = 95)                      # Instances of individual figures for alignment
        fig2 = plt.figure(figsize=(4,3), dpi = 95)                      # figsize sets overall size of each figure 
        fig3 = plt.figure(figsize=(4,3), dpi = 95)                      # dpi zooms out and in with a change of value
    
        #plt.ion()
        a = fig1.add_subplot(1,1,1)                                     # Analysis View Graph plot
        #a.subplots_adjust(bottom=0.1, right=0.8, top=0.9)             
        a.plot(x,y, label='Loaded from file!')
        a.plot([0., Counter], [threshold, threshold], "k--")            # Plotting threshold designation     
        a.set_xlabel('Time(seconds)')                                   # Set X axis title
        a.set_ylabel('Force in Newtons')                                # Set Y axis title
        #a.set_xticks(['0','10','20','30','40','50','60','70','80'])
        a.set_xticklabels(['0','10','20','30','40','50','60','70','80'])    
        a.set_yticks([0,250,500,750,1000,1250,1500,1750,2000])
        #a.xticks(x,values)
 
        
        b = fig2.add_subplot(1,1,1)                                             # Pie chart for client               
        b.set_title("High Activity Peaks", fontsize = 12)
        b.pie(sizesB, labels=labelsB, autopct='%1.1f%%', colors=outer_colors,   # startangle sets starting point of % divisions
                    radius=1.2, shadow=True, startangle=180,                    # colors are random right now calling outer_colors
                    wedgeprops=dict(width=size, edgecolor='w'),
                    textprops={'fontsize': 7})
  
        c = fig3.add_subplot(1,1,1)          
        c.set_title("Total Recorded Impacts", fontsize = 12)
        c.pie(sizesC, labels=labelsC, autopct='%1.1f%%', colors=outer_colors,
                    radius=1.2, shadow=True, startangle=180,
                    wedgeprops=dict(width=size, edgecolor='w'),
                    textprops={'fontsize': 7})


        # Instances of figs included into a single Canvas
        
        canvas1 = FigureCanvasTkAgg(fig1, master=window)                        
        canvas1.draw()
        canvas1.get_tk_widget().grid(row=1, column=3, rowspan = 4, padx = 10, pady = 150)  # Setting positions of Analysis graph    

        canvas2 = FigureCanvasTkAgg(fig2, master=window)
        canvas2.draw()
        canvas2.get_tk_widget().grid(row=0, column=2, rowspan = 4, padx = 10, pady = 150)   # Setting position of Pie chart threshold         

        canvas3 = FigureCanvasTkAgg(fig3, master=window)
        canvas3.draw()
        canvas3.get_tk_widget().grid(row=3, column=2, rowspan = 4, padx = 10, pady = 150)   # Setting posision of Pie chart Impacts     

                                                                                            # navigational toolbar setup & pos
        toolbarFrame = Frame(master=window)
        toolbarFrame.grid(row=0,column=3)
        toolbar = NavigationToolbar2Tk(canvas1, toolbarFrame)
        
        window.cursor = Cursor(a, useblit=True, color='red', linewidth=2)       #   Used for Analysis graph cursor


def main_account_screen():
    global main_screen
    main_screen = tk.Tk()
    
    main_screen.geometry("300x250")
    main_screen.title("Account Login")
    Label(text="Select Your Choice", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()

    Label(text="").pack()
    """

    Button(text="GO!",
            height="2", width="30",
            command=new_window(logSuccess)).pack()
    
    """

    new_window(logSuccess)

    main_screen.mainloop()
 
 
 
main_account_screen()
