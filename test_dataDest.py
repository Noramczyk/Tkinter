import csv
import os
import tkinter as tk
from tkinter.ttk import *
from tkinter import *
from tkinter import filedialog
from tkinter import simpledialog, ttk
import mysql
from sshtunnel import SSHTunnelForwarder
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.widgets import Cursor
import mysql.connector as db
#from HexToDec import HexToDec
import matplotlib.gridspec as gridspec
from scipy import stats
import re
import pytest_check as check
import pytest


global newVal
global line_1
global line_2
#global fname_entry
#global lname_entry


"""
tunnelfile = open("ssh.txt", 'r')
sacUser = tunnelfile.readline()
sacPass = tunnelfile.readline()

sacUser = re.sub(r"[\n\t\s]*", "", sacUser)
sacPass = re.sub(r"[\n\t\s]*", "", sacPass)


#sacUser = input('SacLink username: ')
#sacPass = input('SacLink password: ')

server = SSHTunnelForwarder(
    ("ecs-pw-proj-web.ecs.csus.edu", 22),
    ssh_host_key=None,
    ssh_username= sacUser,  # username goes here!
    ssh_password=sacPass,  # password goes here!
    remote_bind_address=("10.115.234.32", 3306))

server.start()

global cnx

cnx = mysql.connector.connect(user='bruteforce_user',
                              password='bruteforce_db',
                              host="127.0.0.1",
                              port=server.local_bind_port,
                              database='team_bruteforce')

if cnx is not None:
    print("Server connected")

db_cursor = cnx.cursor(buffered=True)

db_cursor.execute("SELECT * FROM TEST")
db_cursor.execute("SELECT * FROM TEST")
result = db_cursor.fetchall()

for row in result:
    print(row)
    print("\n")

"""
# Creates a new window for patient and physician views
def new_window(_class):
    new = tk.Toplevel(main_screen)
    _class(new)


def test_file1_method1():
	x=5
	y=6
	assert x+1 == y,"test failed"
	#assert x == y,"test failed"

def test_file1_method2():
	x=5
	y=6
	assert x+1 == y,"test failed" 

def test_filename():
    assert filename != "", "Initial file selection failed"  

def test_PrimSec():
    assert fileone != "", "file in PrimSec failed"    

def test_length():
    assert len(x) - len(y) == 0

def test_thresholds():
    assert highthreshCounter < 0, "Test failed"
    assert lowthreshCounter < 0, " Test failed"

"""
def verifyData(testCounter):

    tX = []
    tY = []
    testcounter = 0

    with open(filename, 'r') as csvfile:  # Set file designation
               plots = csv.reader(csvfile)
               for row in plots:
                   tY.append(int(row[0]))  # Using data points as y-axis points
                   tX.append(Counter)
                   if row:
                       testcounter += 1  # Counting rows in text file and using them for x-axis
    
    return testcounter
"""

# ---------- Start ---------- User Login --------------------
# Creates foundation for login display.
def main_account_screen():
    global main_screen
    main_screen = tk.Tk()
    # menubar = Menu(main_screen)
    # main_screen.config(menu = menubar)

    main_screen.geometry("300x250+0+0")
    #main_screen.minsize(5, 5)
    main_screen.title("Account Login")

    Label(text="Select Your Choice",
                        bg="#42e9f5", 
                        width="300", 
                        height="2", 
                        font=("Calibri", 13)).pack(side = TOP, pady = 10)

    #Label(text="").pack()

    Button(text="Login", height="2",
           width="30",
           command=login).pack()  # calls function login

    #Label(text="").pack()

    Button(text="Register",
           height="2", width="30",
           command=register).pack()  # calls function register
    """
    Button(text="Exit Application",
           command=exit(0)).pack()  # Button to exit app
    
    
    Button(text = 'Close the window',
            command = quit).pack()
    """
    
 

    main_screen.mainloop()



# After initializing login display it asks for the user's info.
# From there appropriate methods are called for success or failure to login respectively.
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("400x300")
    Label(login_screen, text="Please enter login information").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1,
           command=login_verify).pack()  # calls login_verify to parse user file

    """
    Button(login_screen,
           text="Exit Application",
           command=sys.exit(0)).pack()  # Button to exit app
    """
    
    main_screen.withdraw()


# Verifies user login credentials against current list.
def login_verify():
    global username1
    global firstName
    global lastName
    global email

    pList = []
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
    
        
    ##sql = "SELECT userName, passWord FROM USER WHERE userName = %s AND passWord = %s VALUES (%s, %s)"

    ##val = (username1, password1)

    ##db_cursor.execute(sql, val)
    #result = db_cursor.fetchall()
    
    #if result == None:
        #user_not_found()
    #else:
        #importFile()

    #for row in result:
        #print(row)
        #print("\n")


    list_of_files = os.listdir()
    if username1 in list_of_files:  # if username is found
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        email = file1.read().splitlines()
        if password1 in verify:  # if password is found
             # logSuccess()                               # Calls function with verification
            # new_window(logSuccess)                     # Class call for valid entry
            importFile()  # Call importFile for option for file destination

        else:
            password_not_recognised()  # calls password_not_recognised

    else:
        user_not_found()  # calls user_not_found

   
    pList = verify              # Copy file data into list to be used for data designations
    email = pList[3]
    firstName = pList[6]
    lastName = pList[7]
    print(email)
    print(firstName)
    print(lastName)


# Login Success.
# Maintains most functionality to see user appropriate data.
class logSuccess:
    def __init__(self, window):

        self.window = window

        global patientFname
        global patientLname
        global x
        global y

        highThreshold = 0
        lowThreshold = 0
        impactThreshold = 0
        highthreshCounter = 0
        lowthreshCounter = 0
        impactCounter = 0
        threshTot = 0
        seconds = 0
        totalCount = 0
        Counter = 0
        xCounter = 0
        secCounter = 0
        index = 0
        intIndex = 0
        jerkCalc = 0
        yTotal = 0
        rofD = 0
        foP = 0
        j = 0

        size = 0.3          # Pie Chart size
        yVal = 800

        patientFname = "John"
        patientLname = "Doe"

        # window = Toplevel(main_screen)

        delete_importFile()  # Clean up import screen
     
        menubar = Menu(window)
        window.config(menu=menubar)
        window.geometry("1700x1500")  # Set overall size of screen

        fileMenu = Menu(menubar)  # Sets drop down menu just exit is implemented right now
        fileMenu.add_command(label="Exit", command=window.quit)
        menubar.add_cascade(label="Menu", menu=fileMenu)

        tabControl = ttk.Notebook(window)

        splitView = ttk.Frame(tabControl)
        patientView = ttk.Frame(tabControl)
        analysisView = ttk.Frame(tabControl)
        multiView = ttk.Frame(tabControl)

        tabControl.add(splitView, text='Split View')
        tabControl.add(patientView, text='Patient View')
        tabControl.add(analysisView, text='Analysis View')
        tabControl.add(multiView, text='Multiple Plot View')
        tabControl.grid(sticky=NW)
       
        cmap = plt.get_cmap("tab20c")
        outer_colors = cmap(np.arange(3) * 4)  # Random color generated for pie charts
        inner_colors = cmap([1, 2, 5, 6, 9, 10])  # Not being used but could at more depth for more data

        y = []  # x and y lists used to fill file data
        x = []
        yXa = []
        xXa = []       # List for setting x index labels
    
        plt_list = []

        with open(filename, 'r') as csvfile:  # Set file designation
            plots = csv.reader(csvfile)
            for row in plots:
                y.append(int(row[0]))  # Using data points as y-axis points
                x.append(Counter)
                if row:
                    Counter += 1  # Counting rows in text file and using them for x-axis
   
        
        for i in y:  # Number of impacts under set threshold
            if i < lowThreshold:
                lowthreshCounter+= 1
                continue

        for i in y:  # Number of impacts over set threshold
            if i > highThreshold:
                highthreshCounter+= 1
                continue


        for i in y:  # Number of impacts over ZERO
            if i > impactThreshold:
                impactCounter += 1
                continue

        for i in x:  # Number of impacts
            totalCount += 1

        for i in y:
            yTotal = i + yTotal
        

        """
        index = Counter / 8                 # Counter = total data pts. / 8 is the number of x axis ticks
        intIndex = (int(index))             # Turn double calc result back to a int
        
        for i in x:                            # For loop for setting x-axis tick labels
            if i % intIndex == 0:               # Every calculated index 
                xMod.append(int(i / 250))       # append to list and turned into an int

        second = totalCount / 250
        

        yXa.append(0)                   # X Axis algorithm for MultiView & Quad Plot View
        while j < (len(y)):
            j += 1
            if j % 250 == 0:
                yXa.append(y[j])
                #yCounter += 1


        for i in x:
            if i % 250 == 0:
                minMod = i / 250
                xXa.append(minMod)
                xCounter += 1
        """

        highthreshCalc = highthreshCounter / Counter  # % Calc
        lowthreshCalc = lowthreshCounter / Counter # % Calc
        threshTot = lowthreshCounter+lowthreshCounter

        avgNewtons = (round(yTotal / totalCount, 4))            # Average Newton Calc


        seconds = totalCount / 250

        print("Total Above: ", highthreshCounter)  # Output to make sure everything is right
        print("Total Below: ", lowthreshCounter)  # Output to make sure everything is right
        print("Total Impacts: ", impactCounter)
        print("Total Points: ", Counter)
        print("High Threshold %: ", highthreshCalc)
        print("Low Threshold %: ", lowthreshCalc)
        print("Total Thresh %: ", threshTot)
        print("Impact Counter: ", impactCounter)
        print("Total Count: ", totalCount)
        print("Y sum: ", yTotal)
        print("Avg Newtons: ", avgNewtons)      # Rounding action!
        print("Seconds: ", seconds)

        #assert 0

        vals = np.array([[10., 10.], [highthreshCounter, highthreshCounter]])  # Setting pie chart %
        vals3 = np.array([[10., 10.], [lowthreshCounter, lowthreshCounter]])  # Setting pie chart %
        vals2 = np.array([[50., 50.], [10., 10.]])  #

        sizesB = [highthreshCalc, lowthreshCalc, (threshTot)]  # Setting pie b (Threshold) chart labels
        labelsB = 'Above Upper', 'Below Lower', 'Ideal Force'

        sizesC = [20, 20, 60]  # Setting pie c (Impact) chart labels
        labelsC = 'Above Upper', 'Below Lower', 'Ideal Force'

      

        def setFunc():

            global line_1
            global line_2
            global line_3
            global line_4
            global highthreshCounter
            global lowthreshCounter

            Counter = 0  # Set vals back to Zero
            highthreshCounter = 0
            lowthreshCounter = 0
            impactCounter = 0
            totalCount = 0

            y = []
          
            highThreshold = simpledialog.askinteger(" ", "Enter upper value: ")  # FINALLY !!!
            lowThreshold = simpledialog.askinteger(" ", "Enter lower value: ")  # FINALLY !!!
            
            print("In replot....")

            with open(filename, 'r') as csvfile:  # Re-set file designation
                plots = csv.reader(csvfile)
                for row in plots:
                    y.append(int(row[0]))  # Using data points as y-axis points
                    x.append(Counter)
                    if row:
                        Counter += 1  # Counting rows in text file and using them for x-axis

            for i in y:  # Number of impacts under set threshold
                if i < lowThreshold:
                    lowthreshCounter += 1
                    continue

            for i in y:  # Number of impacts over set threshold
                if i > highThreshold:
                    highthreshCounter += 1
                    continue

            for i in y:  # Number of impacts over ZERO
                if i > impactThreshold:
                    impactCounter += 1
                    continue

            for i in x:  # Number of impacts
                totalCount += 1
                continue
                            

            highthreshCalc = highthreshCounter / Counter  # % Calc
            lowthreshCalc = lowthreshCounter / Counter  # % Calc
            threshTot = 1 - (highthreshCalc + lowthreshCalc)
            #threshTot = 1 - highthreshCalc

            print("In setFunc.......")  # Now IN Function
            print("Total Above: ", highthreshCounter)  # Output to make sure everything is right
            print("Total Below: ", lowthreshCounter)  # Output to make sure everything is right
            print("Total Impacts: ", impactCounter)
            print("Total Points: ", Counter)
            print("High Threshold %: ", highthreshCalc)
            print("Low Threshold %: ", lowthreshCalc)
            print("Total Thresh #: ", threshTot)
            print("Impact Counter: ", impactCounter)
            print("Total Count: ", totalCount)
            #print("Seconds total: ", second)
            print(highThreshold)

            vals = np.array([[10., 10.], [highthreshCounter, highthreshCounter]])  # Setting pie chart %
            vals3 = np.array([[100., 100.], [lowthreshCounter, lowthreshCounter]])  # Setting pie chart %
            vals2 = np.array([[50., 50.], [10., 10.], [100., 100.]])  #

            #sizesB = [highthreshCalc, lowthreshCalc, (impactCounter - threshTot)]  # Setting pie b (Threshold) chart labels
            sizesB = [highthreshCalc, lowthreshCalc, (threshTot)]  # Setting pie b (Threshold) chart labels
            labelsB = 'Above Upper', 'Below Lower', 'Ideal Force'

            sizesC = [20, 20, 60]  # Setting pie c (Impact) chart labels
            labelsC = 'Above Upper', 'Below Lower', 'Ideal Force'

            #plt.ion()

            fig4 = plt.figure(figsize=(4, 3), dpi=95)  # dpi zooms out and in with a change of value
            fig5 = plt.figure(figsize=(4, 3), dpi=95)  # dpi zooms out and in with a change of value

            rePlot = fig4.add_subplot(1, 1, 1)  # Pie chart for client
            rePlot.set_title("Activity Peaks", fontsize=12) 
            rePlot.pie(sizesB, labels=labelsB, autopct='%1.1f%%', colors=outer_colors,
                       # startangle sets starting point of % divisions
                       radius=1.2, shadow=True, startangle=180,  # colors are random right now calling outer_colors
                       wedgeprops=dict(width=size, edgecolor='w'),
                       textprops={'fontsize': 11})
            

            rePlotPV = fig5.add_subplot(1, 1, 1)  # Pie chart for client
            rePlotPV.set_title("Activity Peaks", fontsize=12)
            rePlotPV.pie(sizesB, labels=labelsB, autopct='%1.1f%%', colors=outer_colors,
                         radius=1.2, shadow=True, startangle=180,  # colors are random right now calling outer_colors
                         wedgeprops=dict(width=size, edgecolor='w'),
                         textprops={'fontsize': 11})
            

            canvasRP = FigureCanvasTkAgg(fig4, master=splitView)
            # canvasRP.draw()
            canvasRP.get_tk_widget().grid(row=0, column=0, rowspan=4, padx=10,
                                          pady=150)  # Setting position of Pie chart threshold

            canvasPV = FigureCanvasTkAgg(fig5, master=patientView)
            # canvasPV.draw()
            canvasPV.get_tk_widget().grid(row=4, column=5, rowspan=4, padx=50,
                                          pady=150)  # Setting position of Pie chart threshold

            R3 = Label(splitView,
                   borderwidth=10,
                   width=15,
                   relief="flat",
                   bg="mint cream",
                   text=highthreshCounter)  # One way to display a calculated value

            R4 = Label(splitView,
                   borderwidth=10,
                   width=15,
                   relief="flat",
                   bg="mint cream",
                   text=lowthreshCounter)

            A3 = Label(analysisView,
                   borderwidth=10,
                   width=15,
                   relief="flat",
                   bg="mint cream",
                   text=highthreshCounter)  # One way to display a calculated value

            A4 = Label(analysisView,
                   borderwidth=10,
                   width=15,
                   relief="flat",
                   bg="mint cream",
                   text=lowthreshCounter)

            

            R3.grid(row=0, column=5, pady=2)
            R4.grid(row=1, column=5, pady=2)

            A3.grid(row=4, column=5, pady=2)        # High thresh counter
            A4.grid(row=5, column=5, pady=2)        # Low thresh counter

            plt.ion()

            # threshold = simpledialog.askinteger("Theshold Value ", "Enter new value: ")  # FINALLY !!!
            if line_1:  # Checks to see if theres something in list, if so then pop it and remove line
                line = line_1.pop(0)
                line.remove()

            if not line_1:  # Checks empty list, and if true, plots the graph.
                line_1 = a.plot([0., Counter], [highThreshold, highThreshold], "k--")

            if line_2:  # For Analysis View
                line = line_2.pop(0)
                line.remove()

            if not line_2:
                line_2 = av.plot([0., Counter], [highThreshold, highThreshold], "k--")

            # threshold = simpledialog.askinteger("Threshold Value ", "Enter new value: ")  # FINALLY !!!
            if line_3:  # Checks to see if theres something in list, if so then pop it and remove line
                line = line_3.pop(0)
                line.remove()

            if not line_3:  # Checks empty list, and if true, plots the graph.
                line_3 = a.plot([0., Counter], [lowThreshold, lowThreshold], "k--")

            if line_4:  # For Analysis View
                line = line_4.pop(0)
                line.remove()

            if not line_4:
                line_4 = av.plot([0., Counter], [lowThreshold, lowThreshold], "k--")

           

            plt.ioff()  # Trapping updated threshold inbetween ion() & ioff() so only threshold get drawn

        def setThreshLine():
            global line_1
            global line_2
            global line_3
            global line_4

            line_1 = a.plot([0., Counter], [highThreshold, highThreshold], "k--")  # plots threshold line, assigns to list
            line_2 = av.plot([0., Counter], [highThreshold, highThreshold], "k--")  # plots threshold line, to Analysis View
            line_3 = a.plot([0., Counter], [lowThreshold, lowThreshold], "k--")  # plots threshold line, assigns to list
            line_4 = av.plot([0., Counter], [lowThreshold, lowThreshold], "k--")  # plots threshold line, to Analysis View
            

        def onpick(event):
            thisline = event.artist
            xdata = thisline.get_xdata()
            ydata = thisline.get_ydata()
            ind = event.ind
            points = tuple(zip(xdata[ind], ydata[ind]))
            #print('onpick points:', points)
            print(xdata[ind])
            print(ydata[ind])

            foP = ydata[ind]

            A6 = Label(analysisView,
                    borderwidth=10,
                    width=15,
                    relief="flat",
                    bg="mint cream",
                    text=foP)

            A6.grid(row=3, column=5, pady=2)


        #*********************************************************

        def multPlot():

            xMV = []
            yMV = []
            xS = []
            yS = []
            x1 = []
            y1 = []
            x2 = []
            y2 = []
            x3 = []
            y3 = []
            x4 = []
            y4 = []
        
            Counter = 0
            jM = 0

            with open(filename, 'r') as csvfile:  # Re-set file designation
                plots = csv.reader(csvfile)
                for row in plots:
                    yMV.append(int(row[0]))  # Using data points as y-axis points
                    xMV.append(Counter)
                    if row:
                        Counter += 1  # Counting rows in text file and using them for x-axis

            yS.append(0)                   # X Axis algorithm for MultiView & Quad Plot View
            while jM < (len(yMV)):
                jM += 1
                if jM % 250 == 0:
                    yS.append(yMV[jM])
                    #yCounter += 1


            for i in xMV:
                if i % 250 == 0:
                    minModM = i / 250
                    xS.append(minModM)
                    #xCounter += 1

            s1 = simpledialog.askinteger(" ", "Enter Graph 1 start value: ")  
            f1 = simpledialog.askinteger(" ", "Enter Graph 1 end value: ")
            s2 = simpledialog.askinteger(" ", "Enter Graph 2 start value: ")  
            f2 = simpledialog.askinteger(" ", "Enter Graph 2 end value: ") 
            s3 = simpledialog.askinteger(" ", "Enter Graph 3 start value: ")  
            f3 = simpledialog.askinteger(" ", "Enter Graph 3 end value: ")
            s4 = simpledialog.askinteger(" ", "Enter Graph 4 start value: ")  
            f4 = simpledialog.askinteger(" ", "Enter Graph 4 end value: ")
            
            s1Mult = s1 
            f1Mult = f1 
            s2Mult = s2 
            f2Mult = f2 
            s3Mult = s3 
            f3Mult = f3 
            s4Mult = s4 
            f4Mult = f4 
           
            x1 = (xS[s1Mult:f1Mult])         # List slicing!!
            y1 = (yS[s1Mult:f1Mult]) 
            x2 = (xS[s2Mult:f2Mult])         
            y2 = (yS[s2Mult:f2Mult])
            x3 = (xS[s3Mult:f3Mult])         
            y3 = (yS[s3Mult:f3Mult])
            x4 = (xS[s4Mult:f4Mult])         
            y4 = (yS[s4Mult:f4Mult])

            figMV = plt.figure(constrained_layout=True)
            figMV.set_figheight(5)
            figMV.set_figwidth(5)

            specMV = gridspec.GridSpec(ncols=2, nrows=2, figure=figMV,
                                        width_ratios=[8, 8], wspace=0.5,
                                        hspace=0.5, height_ratios=[8, 8])

            ax1 = figMV.add_subplot(specMV[0])
            ax2 = figMV.add_subplot(specMV[1])
            ax3 = figMV.add_subplot(specMV[2])
            ax4 = figMV.add_subplot(specMV[3])
            
            ax1.plot(x1, y1, color='darkorange')
            ax2.plot(x2, y2, color='forestgreen')
            ax3.plot(x3, y3, color='darkmagenta')
            ax4.plot(x4, y4, color='royalblue')

                            
            canvasMV = FigureCanvasTkAgg(figMV, master=multiView)
            canvasMV.draw()
            canvasMV.get_tk_widget().grid(row=2, column=0, rowspan=5, padx=10,
                                         pady=10)
            
  
        def primSec(): 

            global fileone
            
            secCounter = 0
            Counter = 0
            j1 = 0
            j2 = 0

            x1 = []
            x2 = []
            y1 = []
            y2 = []
            x1A = []
            y1A = []
            x2A = []
            y2A = []

            fileone = filedialog.askopenfilename(initialdir = "/",
                                                    title = "Select a File",
                                                    filetypes = (("Text files","*.txt*"),("all files","*.*")))
          
            if os.stat(fileone).st_size == 0:  # If file is not null open main class else no go!
               print('File is empty')

            else:
               print('File is not empty')
               print(fileone)

            with open(fileone, 'r') as csvfile:  # Set file designation
                plots1 = csv.reader(csvfile)
                for row in plots1:
                    y1.append(int(row[0]))  # Using data points as y-axis points
                    x1.append(Counter)
                    if row:
                        Counter += 1  # Counting rows in text file and using them for x-axis
          
                     
            y1A.append(0)
            while j1 < (len(y1)):
                j1 += 1
                if j1 % 250 == 0:
                    y1A.append(y1[j1])
                    
            for i in x1:
                if i % 250 == 0:
                    minMod1 = i / 250
                    x1A.append(minMod1)
        
            a.plot(x1A, y1A, color="r")
            ax.plot(x1A, y1A, color="r")
            ax1.plot(x1A, y1A, color="r")   
            ax2.plot(x1A, y1A, color="r") 
            ax3.plot(x1A, y1A, color="r")
            ax4.plot(x1A, y1A, color="r")  
            #a.plot(x2A, y2A, color="g")
            #av.plot(x1, y1, color="r") 
            #av.plot(x2, y2, color="b")
                 
            canvas1b = FigureCanvasTkAgg(fig1, master=splitView)
            splitView.cursor = Cursor(a, useblit=True, color='red', linewidth=2)  # Used for Analysis graph cursor
            canvas1b.draw()
            canvas1b.get_tk_widget().grid(row=1, column=3, rowspan=4, padx=10,
                                                 pady=150)
            """
            canvas1 = FigureCanvasTkAgg(figAV, master=analysisView)
            analysisView.cursor = Cursor(av, useblit=True, color='red', linewidth=2)
            canvas1.draw()
            canvas1.get_tk_widget().grid(row=1, column=3, rowspan=4, padx=10,
                                         pady=10)
            """

            canvasMVS = FigureCanvasTkAgg(figMVS, master=multiView)
            #multiView.cursor = Cursor(figMV, useblit=True, color='red', linewidth=2)
            canvasMVS.draw()
            canvasMVS.get_tk_widget().grid(row=2, column=4, rowspan=2, padx=10,
                                         pady=10)

            canvasMV = FigureCanvasTkAgg(figMV, master=multiView)
            #multiView.cursor = Cursor(figMV, useblit=True, color='red', linewidth=2)
            canvasMV.draw()
            canvasMV.get_tk_widget().grid(row=2, column=0, rowspan=2, padx=10,
                                         pady=10)
            # Setting positions of Analysis graph
            #lineA1, = av.plot(x1, y1,'o',picker=0.01)  # 5 points tolerance         # For Force @ a point click event
            #lineA2, = av.plot(x2, y2,'o',picker=0.01)  # 5 points tolerance         # For Force @ a point click event

            toolbarFrame = Frame(master=splitView)
            toolbarFrame.grid(row=4, column=3)
            toolbar = NavigationToolbar2Tk(canvas1b, toolbarFrame)
            """
            toolbarFrame = Frame(master=analysisView)
            toolbarFrame.grid(row=0, column=3)
            toolbar = NavigationToolbar2Tk(canvas1, toolbarFrame)
            """

        def setPrim():

            importFile()
        
        def setJerk():

            lineX = []
            lineY = []
            xJ1 = []
            yJ1 = []
            x2 = []
            y2 = []

            lineCounter = 0

            with open(filename, 'r') as csvfile:  # Re-set file designation
                plots = csv.reader(csvfile)
                for row in plots:
                    lineY.append(int(row[0]))  # Using data points as y-axis points
                    lineX.append(lineCounter)
                    if row:
                        lineCounter += 1  # Counting rows in text file and using them for x-axis

            start = simpledialog.askinteger(" ", "Enter start value: ")  
            end = simpledialog.askinteger(" ", "Enter end value: ")

            xJ1 = (lineX[start:end])         # List slicing!!
            yJ1 = (lineY[start:end])


            startCalc = lineX[start] / 250
            endCalc = lineX[end] / 250

            timeSec = endCalc - startCalc
            yDiff = lineY[end] - lineY[start]

            jrkCalc = yDiff / timeSec
            rofCalc = lineY[end] / timeSec
            
            print("Y start: ", lineY[start])
            print("Y end: ", lineY[end]) 
            print(startCalc)
            print(endCalc)
            print("In sec: ", timeSec)
            print("Y diff: ", yDiff)
            print("Jerk: ", (round (jrkCalc, 3)))
            print("ROF: ", (round (rofCalc, 3)))



            arrJX = np.array(xJ1)     # Convert list into array for slope line CALC
            arrJY = np.array(yJ1)

            res = stats.linregress(xJ1, yJ1)       # Calc performed on sub-array

            figAVJ = plt.figure(figsize=(4, 3), dpi=85)

            avj = figAVJ.add_subplot(1, 1, 1)
    
            avj.plot(arrJX, arrJY, 'o', label="Jerk:%r "%(round(res.slope,4)))
            avj.plot(arrJX, res.intercept + res.slope*arrJX, 'r', label='fitted line')
            avj.legend()
            
            avj.set_title('Jerk', fontsize=15)

            canvasAVJ = FigureCanvasTkAgg(figAVJ, master=analysisView)
            canvasAVJ.draw()
            canvasAVJ.get_tk_widget().grid(row=1, column=0, rowspan=1, padx=20,
                                         pady=10)
        def setROF():

            lineXR = []
            lineYR = []
            xR1 = []
            yR1 = []
            x2 = []
            y2 = []

            lineCounterROF = 0

            with open(filename, 'r') as csvfile:  # Re-set file designation
                plots = csv.reader(csvfile)
                for row in plots:
                    lineYR.append(int(row[0]))  # Using data points as y-axis points
                    lineXR.append(lineCounterROF)
                    if row:
                        lineCounterROF += 1  # Counting rows in text file and using them for x-axis

            startR = simpledialog.askinteger(" ", "Enter start value: ")  
            endR = simpledialog.askinteger(" ", "Enter end value: ")

            xR1 = (lineXR[startR:endR])         # List slicing!!
            yR1 = (lineYR[startR:endR]) 

            arrRX = np.array(xR1)     # Convert list into array for slope line CALC
            arrRY = np.array(yR1)

            resROF = stats.linregress(xR1, yR1)       # Calc performed on sub-array

            figAVR = plt.figure(figsize=(4, 3), dpi=85)

            avr = figAVR.add_subplot(1, 1, 1)
    
            avr.plot(arrRX, arrRY, 'o', label="Rate of Force:%r "%(round(resROF.slope,4)))
            avr.plot(arrRX, resROF.intercept + resROF.slope*arrRX, 'r', label='fitted line')
            avr.legend()
            
            avr.set_title('Rate of Force', fontsize=15)

            canvasAVR = FigureCanvasTkAgg(figAVR, master=analysisView)
            canvasAVR.draw()
            canvasAVR.get_tk_widget().grid(row=3, column=0, rowspan=1, padx=20,
                                         pady=10)



            
       # Split View ***************************************       

        #patient_username_info = username.get()
        #patient_username_info = username.get()
        #file = open(patient_username_info, "r")  # creates file with a user name and password
        #first = read(patient_fname_info)
        #file.write(lname_info + "\n")

        l1 = Label(splitView,
                   text="Above Threshold: ",
                   font="bold")
    
        l2 = Label(splitView,
                    relief="flat",
                    bg="mint cream",
                    text= "Name:  %s %s\nEmail: %s"%(firstName, lastName, email),
                    font="bold")
                    

        l3 = tk.Button(splitView,
                   text="Set Secondary Data",
                   font="bold",
                   command=primSec)
        
        l4 = tk.Button(splitView,
                   text="Set Primary Data",
                   font="bold",
                   command=setPrim)
        
        l5 = Label(splitView,
                   text="Total Activity: ",
                   font="bold")

        R2 = Label(splitView,
                   text="Analysis Tools",
                   font="bold")

        l6 = Label(splitView,
                   text="Below Threshold: ",
                   font="bold")

   
        R3 = Label(splitView,
                   borderwidth=10,
                   width=15,
                   relief="flat",
                   bg="mint cream",
                   text=highthreshCounter)  # One way to display a calculated value

        R4 = Label(splitView,
                   borderwidth=10,
                   width=15,
                   relief="flat",
                   bg="mint cream",
                   text=lowthreshCounter)

        R5 = Label(splitView,
                   relief="flat",
                   bg="mint cream",
                   text="Email: %s"%email)

        R6 = Label(splitView,
                   borderwidth=10,
                   width=15,
                   relief="flat",
                   bg="mint cream",
                   text=impactCounter)

        setThreshold = tk.Button(splitView,
                                 text="Set Thresholds",
                                 bg="mint cream",
                                 command=setFunc)  # command calls any function you want (setFunc, clear.....) !
  
        l1.grid(row=0, column=4, pady=2)
        l2.grid(row=0, column=0, pady=2)
        l3.grid(row=1, column=3, pady=2)
        l4.grid(row=0, column=3, pady=2)
        l5.grid(row=3, column=4, pady=2)
        l6.grid(row=1, column=4, pady=2)

        R3.grid(row=0, column=5, pady=2)
        R4.grid(row=1, column=5, pady=2)
        #R5.grid(row=1, column=0, pady=2)
        R6.grid(row=3, column=5, pady=2)


        # ******* Analysis View ************************************

        """
        jerkCalc = 0
        rofD = 0
        foP = 0
        """

        A1 = Label(analysisView,
                    text="Points Above Threshold: ",
                    font="bold")

   
        A2 = Label(analysisView,
                    text="Points Below Threshold: ",
                    font="bold")
  
        A3 = Label(analysisView,
                   borderwidth=10,
                   width=15,
                   relief="flat",
                   bg="mint cream",
                   text=highthreshCounter)  # One way to display a calculated value

        A4 = Label(analysisView,
                   borderwidth=10,
                   width=15,
                   relief="flat",
                   bg="mint cream",
                   text=lowthreshCounter)
  
        setThresholdAV = tk.Button(analysisView,
                                   text="Re-set Thresholds",
                                   bg="mint cream",
                                   command=setFunc)  # command calls any function you want (setFunc, clear

        setJerkAV = tk.Button(analysisView,
                           text="Set Jerk Range",
                           bg="mint cream",
                           command=setJerk)

        setROFAV = tk.Button(analysisView,
                           text="Set Rate of Force Range",
                           bg="mint cream",
                           command=setROF)
  
        A5 = Label(analysisView,
                    text="Force at point: ",
                    font="bold")

        A6 = Label(analysisView,
                    borderwidth=10,
                    width=15,
                    relief="flat",
                    bg="mint cream",
                    text=foP)
        
        A7 = Label(analysisView,
                    text="Patient Notes",
                    font="bold")             #creates the header for Patient notes

        A8 = Text(analysisView,
                    relief="flat",
                    bg="mint cream",
                    height=15,
                    width=45)                 #creates the text box for patient notes

          

        A1.grid(row=4, column=4, pady=2)        # Points above text
        A2.grid(row=5, column=4, pady=2)        # Points Below text
        A3.grid(row=4, column=5, pady=2)        # High thresh counter
        A4.grid(row=5, column=5, pady=2)        # Low thresh counter
        A5.grid(row=3, column=4, pady=2)       # Force at a point
        A6.grid(row=3, column=5, pady=2)       # foP
        A7.grid(row=0, column=4, pady=2)       # Patient notes
        A8.grid(row=1, column=4, pady=2)       # Text box
        
        setThresholdAV.grid(row=4, column=3, pady=5)
        setJerkAV.grid(row=0, column=0, pady=5)
        setROFAV.grid(row=2, column=0, pady=5)

        # Patient View ***********************************************************

        p1 = Label(patientView,
                   borderwidth=10,
                   width=15,
                   relief="flat",
                   bg="mint cream",
                   text="Impacts\n%r"%impactCounter,
                   font="bold")

        p2 = Label(patientView,
                   borderwidth=10,
                   width=15,
                   relief="flat",
                   bg="mint cream",
                   text="Time period:\n%r"%seconds,
                   font="bold")

        p3 = Label(patientView,
                   borderwidth=10,
                   width=15,
                   relief="flat",
                   bg="mint cream",
                   text="Average Newtons:\n%r"%avgNewtons,
                   font="bold")

        p4 = Label(patientView,
                   borderwidth=10,
                   width=15,
                   relief="flat",
                   bg="mint cream",
                   text="Total Datapoints\n%r"%totalCount,
                   font="bold")

        p1.grid(row=6, column=3)
        p2.grid(row=7, column=3)
        p3.grid(row=8, column=2)
        p4.grid(row=8, column=4)

        # Multi View **************************************


        m1 = Label(multiView,
                    text="Multiple Plot View ",
                    font="bold")

        m2 = Label(multiView,
                    text=" ",
                    font="bold")

        setPlot = tk.Button(multiView,
                    text="Set Plots",
                    bg="mint cream",
                    command=multPlot)  # command calls any function you want (setFunc, clear.....) !

        m1.grid(row=0, column=3)
        m2.grid(row=0, column=0)
        setPlot.grid(row=1, column=0, pady=5)
        setThreshold.grid(row=4, column=5, pady=5)

        # Graph Setup   **********************************************************

  
        fig1 = plt.figure(figsize=(7, 6), dpi=90)  # Instances of individual figures for alignment
        figAV = plt.figure(figsize=(7, 6), dpi=90)  # Analysis View fig
        figAVJ = plt.figure(figsize=(4, 3), dpi=85)
        figAVR = plt.figure(figsize=(4, 3), dpi=85)
        figMVS = plt.figure(figsize=(6, 6))  # Multiple Plot View

        figMV = plt.figure(constrained_layout=True)
        figMV.set_figheight(5)
        figMV.set_figwidth(5)

        fig2 = plt.figure(figsize=(4, 3), dpi=95)  # figsize sets overall size of each figure
        fig3 = plt.figure(figsize=(4, 3), dpi=95)  # dpi zooms out and in with a change of value

        specMVS = figMVS.add_subplot(1, 1, 1)
        specMV = gridspec.GridSpec(ncols=2, nrows=2, figure=figMV,
                        width_ratios=[8, 8], wspace=0.5,
                        hspace=0.5, height_ratios=[8, 8])

  
        a = fig1.add_subplot(1, 1, 1)  # Analysis View Graph plot
        av = figAV.add_subplot(1, 1, 1)  # Analysis View Graph plot
        ax = figMVS.add_subplot(1, 1, 1)  # Mulit View Bottom
        avj = figAVJ.add_subplot(1, 1, 1)   # Jerk Graph
        avr = figAVR.add_subplot(1, 1, 1)    # Rate of Force Graph     
               
        ax1 = figMV.add_subplot(specMV[0])          # Quad Multi-View plots
        ax2 = figMV.add_subplot(specMV[1])
        ax3 = figMV.add_subplot(specMV[2])
        ax4 = figMV.add_subplot(specMV[3])
        #ax5 = figMV.add_subplot(specMV[4, :])
        """
        ax1.set_xticklabels(xMod)
        ax2.set_xticklabels(xMod)
        ax3.set_xticklabels(xMod)
        ax4.set_xticklabels(xMod)
        """
        ax1.plot(xXa, yXa, color='darkorange')
        ax2.plot(xXa, yXa, color='forestgreen')
        ax3.plot(xXa, yXa, color='darkmagenta')
        ax4.plot(xXa, yXa, color='royalblue')

        ax.plot(x, y)
        avj.plot(x, y)
        avr.plot(x, y)
        a.plot(x, y)
        av.plot(x, y)

        line, = av.plot(x, y,'o',picker=0.01)  # 5 points tolerance         # For Force @ a point click event

        # a.plot([0., Counter], [highThreshold, highThreshold], "k--")            # Plotting threshold designation
        setThreshLine()
        a.set_xlabel('Time(seconds)', fontsize=15)  # Set X axis title
        a.set_ylabel('Force in Newtons', fontsize=15)  # Set Y axis title
        av.set_xlabel('Data Points', fontsize=15)  # Set X axis title
        av.set_ylabel('Force in Newtons', fontsize=15)  # Set Y axis title
        av.set_title("Data Analysis", fontsize=15)
        ax.set_xlabel('Time(seconds)', fontsize=15)  # Set X axis title
        ax.set_ylabel('Force in Newtons', fontsize=15)  # Set Y axis title
        avj.set_title('Jerk', fontsize=15)
        avr.set_title('Rate of Force', fontsize=15)
    
        #a.set_xticklabels(xMod)
        a.set_yticks(
            [0, 250, 500, 750, 1000, 1250, 1500, 1750, 2000])  # Just using this right now but will most likely change

        #av.set_xticklabels(xMod)
        av.set_yticks(
            [0, 250, 500, 750, 1000, 1250, 1500, 1750, 2000])  # Just using this right now but will most likely change

        #ax.set_xticklabels(xMod)
        ax.set_yticks(
            [0, 250, 500, 750, 1000, 1250, 1500, 1750, 2000])  # Just using this right now but will most likely change
     
        b = fig2.add_subplot(1, 1, 1)  # Pie chart for client
        b.set_title("Activity Peaks", fontsize=12)
        b.pie(sizesB, labels=labelsB, autopct='%1.1f%%', colors=outer_colors,
              # startangle sets starting point of % divisions
              radius=1.2, shadow=True, startangle=180,  # colors are random right now calling outer_colors
              wedgeprops=dict(width=size, edgecolor='w'),
              textprops={'fontsize': 11})

        c = fig3.add_subplot(1, 1, 1)
        c.set_title("Total Recorded Impacts", fontsize=12)
        c.pie(sizesC, labels=labelsC, autopct='%1.1f%%', colors=outer_colors,
              radius=1.2, shadow=True, startangle=180,
              wedgeprops=dict(width=size, edgecolor='w'),
              textprops={'fontsize': 11})

        # End pie chart code block for verification.
        # Instances of figs included into a single Canvas

        canvas1 = FigureCanvasTkAgg(figAV, master=analysisView)
        analysisView.cursor = Cursor(av, useblit=True, color='red', linewidth=2)
        canvas1.draw()
        canvas1.get_tk_widget().grid(row=0, column=3, rowspan=4, padx=10,
                                     pady=10)

        canvasAVJ = FigureCanvasTkAgg(figAVJ, master=analysisView)
        canvasAVJ.draw()
        canvasAVJ.get_tk_widget().grid(row=1, column=0, rowspan=1, padx=20,
                                     pady=10)

        canvasAVR = FigureCanvasTkAgg(figAVR, master=analysisView)
        canvasAVR.draw()
        canvasAVR.get_tk_widget().grid(row=3, column=0, rowspan=1, padx=20,
                                     pady=10)
        # Setting positions of Analysis graph

        figAV.canvas.mpl_connect('pick_event', onpick)


        canvas1b = FigureCanvasTkAgg(fig1, master=splitView)
        splitView.cursor = Cursor(a, useblit=True, color='red', linewidth=2)  # Used for Analysis graph cursor
        canvas1b.draw()
        canvas1b.get_tk_widget().grid(row=1, column=3, rowspan=4, padx=10,
                                      pady=150)

        canvas2 = FigureCanvasTkAgg(fig2, master=splitView)
        canvas2.draw()
        canvas2.get_tk_widget().grid(row=0, column=0, rowspan=4, padx=10,
                                     pady=150)  # Setting position of Pie chart threshold

        canvas2b = FigureCanvasTkAgg(fig3, master=patientView)
        canvas2b.draw()
        canvas2b.get_tk_widget().grid(row=4, column=1, rowspan=4, padx=50,
                                      pady=150)  # Setting position of Pie chart threshold

        canvas3 = FigureCanvasTkAgg(fig3, master=splitView)
        canvas3.draw()
        canvas3.get_tk_widget().grid(row=3, column=0, rowspan=4, padx=10,
                                     pady=150)  # Setting posision of Pie chart Impacts

        canvas3b = FigureCanvasTkAgg(fig2, master=patientView)
        canvas3b.draw()
        canvas3b.get_tk_widget().grid(row=4, column=5, rowspan=4, padx=50,
                                      pady=150)  # Setting position of Pie chart Impacts

        canvasMV = FigureCanvasTkAgg(figMV, master=multiView)
        #multiView.cursor = Cursor(figMV, useblit=True, color='red', linewidth=2)
        canvasMV.draw()
        canvasMV.get_tk_widget().grid(row=2, column=0, rowspan=2, padx=10,
                                     pady=10)

        canvasMVS = FigureCanvasTkAgg(figMVS, master=multiView)
        #multiView.cursor = Cursor(figMV, useblit=True, color='red', linewidth=2)
        canvasMVS.draw()
        canvasMVS.get_tk_widget().grid(row=2, column=4, rowspan=2, padx=10,
                                     pady=10)

        # navigational toolbar setup & pos
        toolbarFrame = Frame(master=splitView)
        toolbarFrame.grid(row=4, column=3)
        toolbar = NavigationToolbar2Tk(canvas1b, toolbarFrame)

        toolbarFrame = Frame(master=analysisView)
        toolbarFrame.grid(row=0, column=3)
        toolbar = NavigationToolbar2Tk(canvas1, toolbarFrame)

        """ 
        toolbarFrame = Frame(master=multiView)
        toolbarFrame.grid(row=7, column=3)
        toolbar = NavigationToolbar2Tk(canvasMV, toolbarFrame)
        """


# Failed login attempt.
# Clears user input and informs user of failed login.
def password_not_recognised():
    global password_not_recog_screen

    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()  # Destroys screen


# User not found.
# Clears user input and informs user of failed login.
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()


# -------------------- User Login ---------- End ----------


# ---------- Start ---------- User Registration --------------------
# This method displays a registration screen for the user.
# registration for doctor.
def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title(" ")
    register_screen.geometry("300x420")

    global username  # Globals for patient database
    global password
    global username_entry
    global password_entry

    global email
    global phonenumber
    global fname
    global lname
    global doctorID
    global website

    global email_entry
    global phonenumber_entry
    global fname_entry
    global lname_entry
    global doctorID_entry
    global website_entry

    email = StringVar()
    phonenumber = StringVar()
    fname = StringVar()
    lname = StringVar()
    doctorID = StringVar()
    website = StringVar()

    username = StringVar()
    password = StringVar()

    Label(register_screen, text="Fill in all Fields to Register", bg="#42e9f5").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()

    # email text and enter box
    email_lable = Label(register_screen, text="Email * ")
    email_lable.pack()
    email_entry = Entry(register_screen, textvariable=email)
    email_entry.pack()

    phonenumber_lable = Label(register_screen, text="Phone Number * ")
    phonenumber_lable.pack()
    phonenumber_entry = Entry(register_screen, textvariable=phonenumber)
    phonenumber_entry.pack()

    website_lable = Label(register_screen, text="website * ")
    website_lable.pack()
    website_entry = Entry(register_screen, textvariable=website)
    website_entry.pack()

    fname_lable = Label(register_screen, text="First name * ")
    fname_lable.pack()
    fname_entry = Entry(register_screen, textvariable=fname)
    fname_entry.pack()
    

    lname_lable = Label(register_screen, text="Last name * ")
    lname_lable.pack()
    lname_entry = Entry(register_screen, textvariable=lname)
    lname_entry.pack()

    doctorID_lable = Label(register_screen, text="DoctorID(if Doctor) * ")
    doctorID_lable.pack()
    doctorID_entry = Entry(register_screen, textvariable=doctorID)
    doctorID_entry.pack()

    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="#42e9f5",
           command=register_Doctor).pack()  # calls register_Doctor

    Button(register_screen,
           text="Exit Application")
           #command=sys.exit(0)).pack()  # Button to exit app

# This method collects the Doctor's info. Then it saves the user's info into a File.
def register_Doctor():
    username_info = username.get()
    password_info = password.get()
    email_info = email.get()
    phonenumber_info = phonenumber.get()
    fname_info = fname.get()
    lname_info = lname.get()
    doctorID_info = doctorID.get()
    website_info = website.get()

    sql = "insert into TEST (user, num) values (%s, %s)"
    val = ('hello', int(18))
    
    if (email.get() != "") and (fname.get() != "") and (lname.get() != "") and (phonenumber.get() != "") and (username.get() != "") and (password.get() != ""):
        
        Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
        file = open(username_info, "w")  # creates file with a user name and password
        file.write("userID" + "\n")  # need to get a method to create unique user IDs
        file.write(username_info + "\n")
        file.write(password_info + "\n")
        file.write(email_info + "\n")
        file.write(phonenumber_info + "\n")
        file.write(website_info + "\n")
        file.write(fname_info + "\n")
        file.write(lname_info + "\n")
        file.write(doctorID_info + "\n")
        file.write("TRUE")  # true here being for doctor type.
        file.close()

        username_entry.delete(0, END)
        password_entry.delete(0, END)
        email_entry.delete(0, END)
        phonenumber_entry.delete(0, END)
        website_entry.delete(0, END)
        fname_entry.delete(0, END)
        lname_entry.delete(0, END)
        doctorID_entry.delete(0, END)

    else:
        Label(register_screen, text="Registration Error", fg="red", font=("calibri", 11)).pack()
      

    # sql = "insert into TEST (user, num) values (%(users)s, %(number)s)"
    # val = {
    #   'users': 'hello',
    #    'number': 18,
    #    }
    #db_cursor.execute(sql, val)
    #cnx.commit()

    ##sql = "INSERT INTO DOCTOR (docID, licNum, phone, website) VALUES (%s, %s, %s, %s)"

    ##val = (ID_info, doctorID_info, phonenumber_info, website_info)

    ##db_cursor.execute(sql, val)

    ##sql = "INSERT INTO USER (ID, userName, passWord, email, userType, first_Name, last_Name) VALUES (%s, %s, %s, %s, %s, %s, %s)"

    ##val = (ID_info, username_info, password_info, email_info, userType_info(TRUE), fname_info, lname_info)

    ##db_cursor.execute(sql, val)

    ##db_connection.commit()

  

    # ----------------------------------------------separator between doctors registration and patient registration------------------


def registerPatient():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Patient Register")
    register_screen.geometry("300x420")

    global patient_username  # Globals for patient database
    global patient_password
    global patient_username_entry
    global patient_password_entry

    global patient_email
    global patient_fname
    global patient_lname

    global patient_email_entry
    global patient_fname_entry
    global patient_lname_entry

    patient_email = StringVar()
    patient_fname = StringVar()
    patient_lname = StringVar()

    patient_username = StringVar()
    patient_password = StringVar()

    Label(register_screen, text="Register a Patient", bg="#42e9f5").pack()
    Label(register_screen, text="").pack()

    patient_username_lable = Label(register_screen, text="Username * ")
    patient_username_lable.pack()
    patient_username_entry = Entry(register_screen, textvariable=username)
    patient_username_entry.pack()
    patient_password_lable = Label(register_screen, text="Password * ")
    patient_password_lable.pack()
    patient_password_entry = Entry(register_screen, textvariable=password, show='*')
    patient_password_entry.pack()

    # email text and enter box
    patient_email_lable = Label(register_screen, text="Email * ")
    patient_email_lable.pack()
    patient_email_entry = Entry(register_screen, textvariable=patient_email)
    patient_email_entry.pack()

    patient_fname_lable = Label(register_screen, text="First name * ")
    patient_fname_lable.pack()
    patient_fname_entry = Entry(register_screen, textvariable=patient_fname)
    patient_fname_entry.pack()

    patient_lname_lable = Label(register_screen, text="Last name * ")
    patient_lname_lable.pack()
    patient_lname_entry = Entry(register_screen, textvariable=patient_lname)
    patient_lname_entry.pack()

    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="#42e9f5",
           command=register_Patient).pack()  # calls register_Patient

    # This method collects the Patients's info. Then it saves the patient's info into a File.


def register_Patient():
    global patient_fname_info
    global patient_lname_info

    patient_username_info = username.get()
    patient_password_info = password.get()
    patient_email_info = email.get()
    patient_fname_info = fname.get()
    patient_lname_info = lname.get()

    ##sql = "INSERT INTO PATIENT (patID, bio, goals, lowThreshold, highThreshold) VALUES (%s, %s, %s, %s, %s)"

    ##val = (ID_info, bio_info(NULL), goals_info(NULL), lowThreshold_info(NULL), highThreshold_info(NULL))

    ##db_cursor.execute(sql, val)

    ##sql = "INSERT INTO USER (ID, userName, passWord, email, userType, first_Name, last_Name) VALUES (%s, %s, %s, %s, %s, %s, %s)"

    ##val = (ID_info, username_info, password_info, email_info, userType_info(FALSE), fname_info, lname_info)

    ##db_cursor.execute(sql, val)

    ##db_connection.commit()

    file = open(patient_username_info, "w")  # creates file with a user name and password

    file.write("userID" + "\n")  # need to get a method to create unique user IDs

    file.write(patient_username_info + "\n")
    file.write(patient_password_info + "\n")
    file.write(patient_email_info + "\n")
    file.write(patient_fname_info + "\n")
    file.write(patient_lname_info + "\n")
    file.write("FALSE")  # false here being for being the patient type.
    file.close()

    
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    email_entry.delete(0, END)
    fname_entry.delete(0, END)
    lname_entry.delete(0, END)
    

    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()


# -------------------- User Registration ---------- End ----------


# -------------------- Patient Select ---------- Start ----------


def patientSelection():
    global patientSelect
    global patientFname
    global patientLname

    master = Tk()

    # create the label
    l1 = Label(master, text="Height")
    l2 = Label(master, text="Patient selection")

    # Grid
    l1.grid(row=0, column=0, sticky=W, pady=2)
    l2.grid(row=0, column=0, sticky=W, pady=2)

    patientFname = "Sarah"
    patientLname = "Doe"

    # sql stuff for fetching info from the DB

    # referenceLOGIN stuff - Should be elsewhere
    # mydb = mysql.connector.connect(
    # host="dbName??",
    #  user="userName",
    #   password="myPass"

    # )

    # DB select from Monitors table where login ID matches the Doc's ID
    # mycursor = mydb.cursor()

    # sql = "SELECT patientID FROM monitors WHERE docID = %s"
    # myVal = ("loginID")

    # mycursor.execute(sql, myVal)

    # myresult = mycursor.fetchall()

    # for x in myresult
    # myTable(x) = myresult(x)


# -------------------- Patient Select ------------- End ----------


# ---------- Start ---------- File Exploration  --------------------
# Allows user to browse through local files for data.
def browseFiles():
    global filename
    # delete_importFile()         # Clean up import screen
    """
    filename = HexToDec(filedialog.askopenfilename(initialdir="/", title="Select a File", # Passes file to the
                                                   # HexToDec class. Returns filepath of modified file
                                                  filetypes=(("Text files", "*.txt*"),  # Only pulls txt files
                                                              ("all files", "*.*"))))
    """
    filename = filedialog.askopenfilename(initialdir = "/",
                                            title = "Select a File",
                                         filetypes = (("Text files",
                                                          "*.txt*"),
                                                       ("all files",
                                                            "*.*")))
                                                                                                                 
    fileExplorer.configure(text="File Opened: " + "" + filename)
    

    #assert filename != "", "Filename valdidation is functioning"

    if os.stat(filename).st_size == 0:  # If file is not null open main class else no go!
        print('File is empty')


    else:
        print('File is not empty')
        print(filename)

        new_window(logSuccess)  # Calls main class here!!!!!



# Allows user to search and import data from external service.
def importFile():
    global importFile_screen
    global fileExplorer

    delete_login()  # Clean up login screen
    importFile_screen = tk.Tk()

    importFile_screen.title('File Explorer')  # Window Title
    importFile_screen.geometry("350x300")
    importFile_screen.config(background="white")  # Set window background color
    fileExplorer = Label(importFile_screen,
                         text="File Explorer ",
                         width=50, height=4,
                         fg="blue")

    buttonExplore = Button(importFile_screen,
                           text="Browse Files",
                           command=browseFiles)  # Command call for browseFile function

    buttonExit = Button(importFile_screen,
                        text="Exit",
                        command=delete_importFile)          # Exits out of program

    fileExplorer.grid(column=0, row=1)  # Using grid layout
    buttonExplore.grid(column=0, row=2)
    buttonExit.grid(column=0, row=3)



# -------------------- File Exploration ---------- End ----------


# ---------- Start ---------- Remove Pop Ups From Display --------------------

def delete_login_success():
    login_success_screen.destroy()  # destroy instances of function when called


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()


def delete_importFile():
    importFile_screen.destroy()


def delete_login():
    login_screen.destroy()




# -------------------- Remove Pop Ups From Display ---------- End ----------

# This line starts the program by calling the beginning function.
main_account_screen()
