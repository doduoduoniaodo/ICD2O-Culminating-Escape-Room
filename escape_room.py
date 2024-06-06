from tkinter import *
import tkinter.messagebox
from PIL import Image, ImageTk
from countdown import global_timer

# create main window
window1 = Tk()
window1.title('Escape Room Game')
window1.geometry('400x500')
window1.config(background='#98a2af')

# create a menubar for user to quit the program
menubar = Menu(window1)
quitmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Quit', menu=quitmenu)
quitmenu.add_command(label='Quit', command=exit)
window1.config(menu = menubar)

quitlabel = Label(window1, text='👆Quit the program', font=('Consolas', 8), bg='#98a2af')
quitlabel.pack(anchor='nw')


# create three frame
topframe = Frame(window1, relief=GROOVE, borderwidth=5, bg='#98a2af')
middleframe = Frame(window1, relief=RAISED, borderwidth=5, bg='#98a2af')
bottomframe = Frame(window1, borderwidth=20, bg='#98a2af')
topframe.pack()
middleframe.pack()
bottomframe.pack()

# create the instruction label
instruction1 = Label(topframe, text='''You are a rookie agent at Sector 51. 
Your task is to retrieve a powerful artifact named “Quantum Nexus” which can manipulate reality. 
The only intelligence is that artifact is now in at an abandoned palace in the Nevade Desert. 
Now, you are in the palace and there are labyrinthine corridors. 
You need to navigate through these corridors and solve puzzles to reach the “Quantum Nexus”. 
Secure the Quantum Nexus and don't let it fall into the wrong hands!''', font=('consolas', 10))
instruction1.pack()

timerObject = global_timer(1800)

timer = Label(window1, text='30:00', font=('',15), bg='#98a2af', fg='red')
timer.pack()

timerObject.attachLabel(timer)

def Room_1():
    room1 = Toplevel()
    timerObject.startTimer()
    room1timer = Label(room1)
    room1timer.pack()
    timerObject.attachLabel(room1timer)
    
    
def Room_2():
    room2 = Toplevel()
    timerObject.startTimer()
    room2timer = Label(room2)
    room2timer.pack()
    timerObject.attachLabel(room2timer)
    
def Room_3():
    room3 = Toplevel()
    timerObject.startTimer()
    room3timer = Label(room3)
    room3timer.pack()
    timerObject.attachLabel(room3timer)
    
def Room_4():
    room4 = Toplevel()
    timerObject.startTimer()
    room4timer = Label(room4)
    room4timer.pack()
    timerObject.attachLabel(room4timer)
    
def Room_5():
    room5 = Toplevel()
    timerObject.startTimer()
    room5timer = Label(room5)
    room5timer.pack()
    timerObject.attachLabel(room5timer)
    
def Room_6A():
    room6a = Toplevel()
    timerObject.startTimer()
    room6atimer = Label(room6a)
    room6atimer.pack()
    timerObject.attachLabel(room6atimer)
    
def Room_6B():
    room6b = Toplevel()
    timerObject.startTimer()
    room6btimer = Label(room6b)
    room6btimer.pack()
    timerObject.attachLabel(room6btimer)
    
def Trap():
    trapwindow = Toplevel()
    
    
def Room_7():
    room7 = Toplevel()
    timerObject.startTimer()
    room7timer = Label(room7)
    room7timer.pack()
    timerObject.attachLabel(room7timer)
    
def Room_8():
    room8 = Toplevel()
    timerObject.startTimer()
    room8timer = Label(room8)
    room8timer.pack()
    timerObject.attachLabel(room8timer)
    
def Success():
    successwindow = Toplevel()
    
def Failed():
    failedwindow = Toplevel()
  
  
startbutton = Button(middleframe, text='Start!', command=Room_1)
startbutton.pack()
#startimage = ImageTk.PhotoImage(Image.open('1.jpg').resize((100, 100), Image.NEAREST))
#startimagelabel = Label(bottomframe, image=startimage)
#startimagelabel.pack()
  
window1.mainloop()