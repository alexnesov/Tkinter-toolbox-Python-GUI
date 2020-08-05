# Python Program to make a scrollable frame 
# using Tkinter 
   
from tkinter import *
   
class ScrollBar: 
      
    # constructor 
    def __init__(self): 
          
        # create root window 
        root = Tk() 
   
        # create a horizontal scrollbar by 
        # setting orient to horizontal 
        h = Scrollbar(root, orient = 'horizontal') 
   
        # attach Scrollbar to root window at  
        # the bootom 
        h.pack(side = BOTTOM, fill = X) 
   
        # create a vertical scrollbar-no need 
        # to write orient as it is by 
        # default vertical 
        v = Scrollbar(root) 
   
        # attach Scrollbar to root window on  
        # the side 
        v.pack(side = RIGHT, fill = Y) 
           
   
        # create a Text widget with 15 chars 
        # width and 15 lines height 
        # here xscrollcomannd is used to attach Text 
        # widget to the horizontal scrollbar 
        # here yscrollcomannd is used to attach Text 
        # widget to the vertical scrollbar 
        t = Text(root, width = 15, height = 15, wrap = NONE, 
                 xscrollcommand = h.set,  
                 yscrollcommand = v.set) 
   
        # insert some text into the text widget 
        for i in range(20): 
            t.insert(END,"this is some text\n") 
   
        # attach Text widget to root window at top 
        t.pack(side=TOP, fill=X) 
   
        # here command represents the method to 
        # be executed xview is executed on 
        # object 't' Here t may represent any 
        # widget 
        h.config(command=t.xview) 
   
        # here command represents the method to 
        # be executed yview is executed on 
        # object 't' Here t may represent any 
        # widget 
        v.config(command=t.yview) 
   
        # the root window handles the mouse 
        # click event 
        root.mainloop() 
  
# create an object to Scrollbar class 
s = ScrollBar() 

#==============================

import sys
import random
import matplotlib
import matplotlib.pyplot as plt

from PyQt5.QtWidgets import (
                        QWidget,
                        QApplication,
                        QMainWindow,
                        QVBoxLayout,
                        QScrollArea,
                    )

from matplotlib.backends.backend_qt5agg import (
                        FigureCanvasQTAgg as FigCanvas,
                        NavigationToolbar2QT as NabToolbar,
                    )

# Make sure that we are using QT5
matplotlib.use('Qt5Agg')

# create a figure and some subplots
FIG, AXES = plt.subplots(ncols=4, nrows=5, figsize=(16,16))

for AX in AXES.flatten():
    random_array = [random.randint(1, 30) for i in range(10)]
    AX.plot(random_array)

def main():
    app = QApplication(sys.argv)
    window = MyApp(FIG)
    sys.exit(app.exec_())

class MyApp(QWidget):
    def __init__(self, fig):
        super().__init__()
        self.title = 'VERTICAL, HORIZONTAL SCROLLABLE WINDOW : HERE!'
        self.posXY = (700, 40)
        self.windowSize = (1200, 800)
        self.fig = fig
        self.initUI()

    def initUI(self):
        QMainWindow().setCentralWidget(QWidget())

        self.setLayout(QVBoxLayout())
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.layout().setSpacing(0)

        canvas = FigCanvas(self.fig)
        canvas.draw()

        scroll = QScrollArea(self)
        scroll.setWidget(canvas)

        nav = NabToolbar(canvas, self)
        self.layout().addWidget(nav)
        self.layout().addWidget(scroll)

        self.show_basic()

    def show_basic(self):
        self.setWindowTitle(self.title)
        self.setGeometry(*self.posXY, *self.windowSize)
        self.show()


if __name__ == '__main__':
    main()


#=================


import math
import sys

from tkinter import Tk, Button, Frame, Canvas, Scrollbar
import tkinter.constants as Tkconstants

from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pprint

frame = None
canvas = None

def printBboxes(label=""):
  global canvas, mplCanvas, interior, interior_id, cwid
  print("  "+label,
    "canvas.bbox:", canvas.bbox(Tkconstants.ALL),
    "mplCanvas.bbox:", mplCanvas.bbox(Tkconstants.ALL))

def addScrollingFigure(figure, frame):
  global canvas, mplCanvas, interior, interior_id, cwid
  # set up a canvas with scrollbars
  canvas = Canvas(frame)
  canvas.grid(row=1, column=1, sticky=Tkconstants.NSEW)

  xScrollbar = Scrollbar(frame, orient=Tkconstants.HORIZONTAL)
  yScrollbar = Scrollbar(frame)

  xScrollbar.grid(row=2, column=1, sticky=Tkconstants.EW)
  yScrollbar.grid(row=1, column=2, sticky=Tkconstants.NS)

  canvas.config(xscrollcommand=xScrollbar.set)
  xScrollbar.config(command=canvas.xview)
  canvas.config(yscrollcommand=yScrollbar.set)
  yScrollbar.config(command=canvas.yview)

  # plug in the figure
  figAgg = FigureCanvasTkAgg(figure, canvas)
  mplCanvas = figAgg.get_tk_widget()
  #mplCanvas.grid(sticky=Tkconstants.NSEW)

  # and connect figure with scrolling region
  cwid = canvas.create_window(0, 0, window=mplCanvas, anchor=Tkconstants.NW)
  printBboxes("Init")
  canvas.config(scrollregion=canvas.bbox(Tkconstants.ALL),width=200,height=200)

# def changeSize(figure, factor):
#   global canvas, mplCanvas, interior, interior_id, frame, cwid
#   oldSize = figure.get_size_inches()
#   print("old size is", oldSize)
#   figure.set_size_inches([factor * s for s in oldSize])
#   wi,hi = [i*figure.dpi for i in figure.get_size_inches()]
#   print("new size is", figure.get_size_inches())
#   print("new size pixels: ", wi,hi)
#   mplCanvas.config(width=wi, height=hi) ; printBboxes("A")
#   #mplCanvas.grid(sticky=Tkconstants.NSEW)
#   canvas.itemconfigure(cwid, width=wi, height=hi) ; printBboxes("B")
#   canvas.config(scrollregion=canvas.bbox(Tkconstants.ALL),width=200,height=200)
#   figure.canvas.draw() ; printBboxes("C")
#   print()

if __name__ == "__main__":
  root = Tk()
#   root.rowconfigure(1, weight=1)
#   root.columnconfigure(1, weight=1)

  frame = Frame(root)
  frame.grid(column=1, row=1, sticky=Tkconstants.NSEW)
  frame.rowconfigure(1, weight=1)
  frame.columnconfigure(1, weight=1)

  figure = plt.figure(dpi=150, figsize=(4, 4))
  plt.plot(range(10), [math.sin(x) for x in range(10)])

  addScrollingFigure(figure, frame)

#   buttonFrame = Frame(root)
#   buttonFrame.grid(row=1, column=2, sticky=Tkconstants.NS)
#   biggerButton = Button(buttonFrame, text="larger",
#                         command=lambda : changeSize(figure, 1.5))
#   biggerButton.grid(column=1, row=1)
#   smallerButton = Button(buttonFrame, text="smaller",
#                          command=lambda : changeSize(figure, .5))
#   smallerButton.grid(column=1, row=2)

  root.mainloop()

#=============


from tkinter import * 

from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from matplotlib.figure import Figure

class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        # self.configure(width=400, height=400)


        # f = Figure(figsize=(6, 5), dpi=100)
        # a = f.add_subplot(111)
        # t = arange(0.0, 3.0, 0.01)
        # s = sin(2*pi*t)
        # a.plot(t, s)

        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().grid(row=0, column=0)

        vbar=Scrollbar(self, orient = VERTICAL)
        vbar.grid(row=0, column=1)       
        hbar=Scrollbar(self, orient=HORIZONTAL)
        hbar.grid(row=1, column=0)


        canvas.get_tk_widget().config(xscrollcommand=hbar.set, yscrollcommand = vbar.set)

        hbar.config(command=canvas.get_tk_widget().xview)
        vbar.config(command=canvas.get_tk_widget().yview)



if __name__ == "__main__":
    app = App()
    app.geometry("400x400+51+51")
    app.title("Test")
    app.mainloop()


 #======================



import tkinter as tk  # python 3
# import Tkinter as tk  # python 2

class Example(tk.Frame):
    def __init__(self, root):

        tk.Frame.__init__(self, root)
        self.canvas = tk.Canvas(root, borderwidth=0, background="#ffffff")
        self.frame = tk.Frame(self.canvas, background="#ffffff")
        self.vsb = tk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((4,4), window=self.frame, anchor="nw", 
                                  tags="self.frame")

        self.frame.bind("<Configure>", self.onFrameConfigure)

        self.populate()

    def populate(self):
        '''Put in some fake data'''
        for row in range(100):
            tk.Label(self.frame, text="%s" % row, width=3, borderwidth="1", 
                     relief="solid").grid(row=row, column=0)
            t="this is the second column for row %s" %row
            tk.Label(self.frame, text=t).grid(row=row, column=1)

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

if __name__ == "__main__":
    root=tk.Tk()
    Example(root).pack(side="top", fill="both", expand=True)
    root.mainloop()


#===============
import tkinter as tk
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
 
class tkintertool:
    def __init__(self,master):
        self.clicks= 0 
        self.master = master
         
        master.geometry("2000x1000")
         
        self.myframe = tk.Frame(master,relief=tk.GROOVE,width=500,height=300,bd=1,background="blue")
        self.myframe.grid(row=0,column=0)
 
        self.canvas=tk.Canvas(self.myframe,background="green")
        self.frame=tk.Frame(self.canvas,background="red")
         
        button = tk.Button(master,text='click',command=lambda: self.data())
         
        myscrollbar=tk.Scrollbar(self.myframe,orient="vertical",command=self.canvas.yview)
        myscrollbarx=tk.Scrollbar(self.myframe,orient="horizontal",command=self.canvas.xview)
        self.canvas.configure(yscrollcommand=myscrollbar.set,xscrollcommand=myscrollbarx.set)
 
        myscrollbar.pack(side="right",fill="y")
        myscrollbarx.pack(side="bottom",fill="x")
        button.grid(row=2,column=0)
        self.canvas.pack(side="left")
        self.canvas.create_window((0,0),window=self.frame,anchor='nw')
        self.frame.bind("<Configure>",self.myfunction())
        size = (self.frame.winfo_reqwidth(), self.frame.winfo_reqheight())
        print(size)
    def data(self):
        self.clicks+=1
        self.frame.bind("<Configure>",self.myfunction())
        shape = np.random.randint(0,(3),[5,5])
        lon = np.arange(5)
        lat = np.arange(5)
        fig = Figure(figsize=(4,4))
        ax = fig.add_subplot(111)
        c = ax.pcolor(lon,lat,shape)
        fig.colorbar(c,ax=ax,fraction=0.046,pad=0.04)
        canvas = FigureCanvasTkAgg(fig,self.frame)
        canvas.get_tk_widget().grid(row=0,column=(self.clicks))
    #    self.canvas.config(scrollregion='0 0 %s %s' % size)
 
    def myfunction(self):
        self.canvas.configure(scrollregion=(0,0,288*(self.clicks),288),width=500,height=300)
         
root = tk.Tk()
my_gui = tkintertool(root)
root.mainloop()