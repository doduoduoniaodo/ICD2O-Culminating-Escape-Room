from tkinter import *
import tkinter.messagebox
from PIL import Image, ImageTk
from countdown import global_timer

# create main window
window1 = Tk()
window1.title('Escape Room Game')
window1.geometry('800x500')
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




#----------------------Room 1-----------------------
def Room1Submit():
    a1 = entry1.get()
    if a1 == '110011':
        timerObject.detachLabel(room1timer)
        room1.destroy()
        Room_2()
    else:
        tryagain1 = Label(room1, text='Try Again...')
        tryagain1.pack()

def Room_1():
    global entry1, room1, room1timer

    room1 = Toplevel()
    room1.title('The Entrance')
    
    timerObject.startTimer()
    room1timer = Label(room1)
    room1timer.pack()
    timerObject.attachLabel(room1timer)
    
    topframe = Frame(room1)
    middleframe = Frame(room1)
    bottomframe = Frame(room1)
    topframe.pack()
    middleframe.pack()
    bottomframe.pack()
    
    q1 = Label(topframe, text='''You enter the palace and you want to go deeper.
You soon find there is a huge door and a digital lock on it. You look closer and see a hint next to it. \
“Binary number of the place you at”''')
    q1.pack()
    
    entry1 = Entry(middleframe, justify='center')
    entry1.pack()
    
    submit1 = Button(bottomframe, text='Submit', command=Room1Submit)
    submit1.pack()



#----------------------Room 2-----------------------
def Room2Submit():
    a2 = entry2.get()
    if a2 == '111101':
        Room_3()
    else:
        tryagain2 = Label(room2, text='Try Again...')
        tryagain2.pack()
    
def Room_2():
    global room2, entry2
    
    room2 = Toplevel()
    room2.title('The Meeting Room')

    room2timer = Label(room2)
    room2timer.pack()
    timerObject.attachLabel(room2timer)

    topframe = Frame(room2)
    middleframe = Frame(room2)
    bottomframe = Frame(room2)
    topframe.pack()
    middleframe.pack()
    bottomframe.pack()
    
    q2 = Label(topframe, text='''You enter the meeting room and your find a bigger door. 
There are no hints beside the digital lock. Fortunately, you find a notepad on the desk and there are some words… 
“Tell me the date of the first human space flight! In binary!”''')
    q2.pack()
    
    entry2 = Entry(middleframe, justify='center')
    entry2.pack()
    
    submit2 = Button(bottomframe, text='Submit', command=Room2Submit)
    submit2.pack()



#----------------------Room 3-----------------------
def Room3Submit():
    if upordown.get() == 1:
        Room_4()
    else:
        Room_1()

def Room_3():
    global upordown
    
    room3 = Toplevel()

    room3timer = Label(room3)
    room3timer.pack()
    timerObject.attachLabel(room3timer)

    topframe = Frame(room3)
    middleframe = Frame(room3)
    bottomframe = Frame(room3)
    topframe.pack()
    middleframe.pack()
    bottomframe.pack()
    
    q3 = Label(topframe, text='''You come to the atrium. 
You realize that this palace is way larger than you thought. You have a long way to go… 
There is an elevator. It can’t select floors. You can decide whether to go up or down. ''')
    q3.pack()
    
    upordown = IntVar()
    
    radiobutton3_1 = Radiobutton(middleframe, text='Up', variable=upordown, value=1)
    radiobutton3_2 = Radiobutton(middleframe, text='Down', variable=upordown, value=2)
    radiobutton3_1.pack()
    radiobutton3_2.pack()
    
    submit3 = Button(bottomframe, text='Submit', command=Room3Submit)
    submit3.pack()



#----------------------Room 4-----------------------
def Room4Submit():
    a4 = entry4.get()
    if a4 == '':
        Room_5()
    else:
        tryagain4 = Label(room4, text='Try Again...')
        tryagain4.pack()

def Room_4():
    global room4, entry4
    
    room4 = Toplevel()
    room4.title('The Machine Room')

    room4timer = Label(room4)
    room4timer.pack()
    timerObject.attachLabel(room4timer)
    
    topframe = Frame(room4)
    middleframe = Frame(room4)
    bottomframe = Frame(room4)
    topframe.pack()
    middleframe.pack()
    bottomframe.pack()
    
    q4 = Label(topframe, text='''''')
    q4.pack()
    
    entry4 = Entry(middleframe, justify='center')
    entry4.pack()
    
    submit4 = Button(bottomframe, text='Submit', command=Room4Submit)
    submit4.pack()


#----------------------Room 5-----------------------
def Room5Submit():
    a5 = c_or_unc.get()
    if a5 == 1:
        Room_6A()
    else:
        Room_6B()

def Room_5():
    global c_or_unc
    
    room5 = Toplevel()

    room5timer = Label(room5)
    room5timer.pack()
    timerObject.attachLabel(room5timer)

    topframe = Frame(room5)
    middleframe = Frame(room5)
    bottomframe = Frame(room5)
    topframe.pack()
    middleframe.pack()
    bottomframe.pack()
    
    q5 = Label(topframe, text='''You exit the machine room, now here is a narrow corridor. 
At the end, there are two doors. There are signs on each door. 
“Certainty” and “Uncertainty”. Which one would you choose?''')
    q5.pack()
    
    c_or_unc = IntVar()
    
    radiobutton5_1 = Radiobutton(middleframe, text='Certainty', variable=c_or_unc, value=1)
    radiobutton5_2 = Radiobutton(middleframe, text='Uncertainty', variable=c_or_unc, value=2)
    radiobutton5_1.pack()
    radiobutton5_2.pack()
    
    submit5 = Button(bottomframe, text='Submit', command=Room5Submit)
    submit5.pack()
    

#----------------------Room 6-----------------------
def Room_6A():
    room6a = Toplevel()
    room6a.title('The Lab')

    room6atimer = Label(room6a)
    room6atimer.pack()
    timerObject.attachLabel(room6atimer)


#----------------------Room 7-----------------------
def Room_6B():
    room6b = Toplevel()
    room6b.title('The Unknown')
    
    room6btimer = Label(room6b)
    room6btimer.pack()
    timerObject.attachLabel(room6btimer)


#----------------------Trap-----------------------
def Trap():
    trapwindow = Toplevel()
    

#----------------------Room 7-----------------------
def Room_7():
    room7 = Toplevel()

    room7timer = Label(room7)
    room7timer.pack()
    timerObject.attachLabel(room7timer)


#----------------------Room 8-----------------------
def Room_8():
    room8 = Toplevel()

    room8timer = Label(room8)
    room8timer.pack()
    timerObject.attachLabel(room8timer)


#----------------------Success-----------------------
def Success():
    successwindow = Toplevel()


#----------------------Failed-----------------------
def Failed():
    failedwindow = Toplevel()


#--------------------------------------
timerObject = global_timer(1800, Failed)

timer = Label(window1, text='30:00', font=('',15), bg='#98a2af', fg='red')
timer.pack()

timerObject.attachLabel(timer)


startbutton = Button(middleframe, text='Start!', command=Room_1)
startbutton.pack()
#startimage = ImageTk.PhotoImage(Image.open('1.jpg').resize((100, 100), Image.NEAREST))
#startimagelabel = Label(bottomframe, image=startimage)
#startimagelabel.pack()
  
window1.mainloop()