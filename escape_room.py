from tkinter import *
import tkinter.messagebox
from PIL import Image, ImageTk
from pygame import mixer
from countdown import global_timer

# create main window
window1 = Tk()
window1.title('Escape Room Game')
window1.geometry('800x450')
window1.config(background='#98a2af')

# initialise the pygame
mixer.init()

# play the background music
mixer.music.load("Background_music.mp3")
mixer.music.set_volume(0.4)
mixer.music.play(loops=8)

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
topframe.pack()
middleframe.pack()

# create the instruction label
instruction1 = Label(topframe, text='''You are a rookie agent at Sector 51. 
Your task is to retrieve a powerful artifact named “Quantum Nexus” which can manipulate reality. 
The only intelligence is that artifact is now in at an abandoned palace in the Nevade Desert. \n
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

def Room1Clue():
    tkinter.messagebox.showinfo('Clue', 'You are at Sector 51')

def Room_1():
    global entry1, room1, room1timer, entranceimage

    room1 = Toplevel()
    room1.title('The Entrance')
    
    clue1 = Button(room1, text='Clue', command=Room1Clue)
    clue1.pack(anchor='ne')
    
    try:
        timerObject.startTimer()
    except RuntimeError:
        pass
    room1timer = Label(room1, fg='red')
    room1timer.pack()
    timerObject.attachLabel(room1timer)
    
    middleframe = Frame(room1)
    middleframe.pack()
    
    q1 = Label(middleframe, text='''You enter the palace and you want to go deeper.
You soon find there is a huge door and a digital lock on it. You look closer and see a hint next to it.
“Binary number of the place you at”''')
    q1.pack()
    
    entry1 = Entry(middleframe, justify='center')
    entry1.pack()
    
    submit1 = Button(middleframe, text='Submit', command=Room1Submit)
    submit1.pack()
    
    entranceimage = ImageTk.PhotoImage(Image.open('images/Entrance.jpg'))
    entranceimagelabel = Label(room1, image=entranceimage)
    entranceimagelabel.pack()
    
    



#----------------------Room 2-----------------------
def Room2Submit():
    a2 = entry2.get()
    if a2 == '111101':
        timerObject.detachLabel(room2timer)
        room2.destroy()
        Room_3()
    else:
        tryagain2 = Label(room2, text='Try Again...')
        tryagain2.pack()

def Room2Clue():
    tkinter.messagebox.showinfo('Clue', '1 9 6 1')

def Room_2():
    global room2, entry2, meetingroomimage, room2timer
    
    room2 = Toplevel()
    room2.title('The Meeting Room')
    
    clue2 = Button(room2, text='Clue', command=Room2Clue)
    clue2.pack(anchor='ne')
    
    room2timer = Label(room2, fg='red')
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
“Tell me the date of the first human space flight! In binary! (19xx)”''')
    q2.pack()
    
    entry2 = Entry(middleframe, justify='center')
    entry2.pack()
    
    submit2 = Button(bottomframe, text='Submit', command=Room2Submit)
    submit2.pack()
    
    meetingroomimage = ImageTk.PhotoImage(Image.open('images/Meeting_Room.jpg').resize((600, 338), Image.NEAREST))
    meetingroomimagelabel = Label(room2, image=meetingroomimage)
    meetingroomimagelabel.pack()



#----------------------Room 3-----------------------
def Room3Submit():
    if upordown.get() == 1:
        timerObject.detachLabel(room3timer)
        room3.destroy()
        Room_4()
    else:
        timerObject.detachLabel(room3timer)
        room3.destroy()
        Room_1()

def Room_3():
    global upordown, atriumimage, room3timer, room3
    
    room3 = Toplevel()
    room3.title('The Atrium')
    room3.attributes('-topmost', 'true')

    room3timer = Label(room3, fg='red')
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
    
    atriumimage = ImageTk.PhotoImage(Image.open('images/Atrium.jpg').resize((600, 338), Image.NEAREST))
    atriumimagelabel = Label(room3, image=atriumimage)
    atriumimagelabel.pack()



#----------------------Room 4-----------------------
def Room4Submit():
    a4 = entry4.get()
    if a4 == '':
        timerObject.detachLabel(room4timer)
        room4.destroy()
        Room_5()
    else:
        tryagain4 = Label(room4, text='Try Again...')
        tryagain4.pack()

def Room4Clue():
    tkinter.messagebox.showinfo('Clue', '')

def Room_4():
    global room4, entry4, machineroomimage, room4timer
    
    room4 = Toplevel()
    room4.title('The Machine Room')
    
    clue4 = Button(room4, text='Clue', command=Room4Clue)
    clue4.pack(anchor='ne')

    room4timer = Label(room4, fg='red')
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
    
    machineroomimage = ImageTk.PhotoImage(Image.open('images/Machine_Room.jpg'))
    machineroomimagelabel = Label(room4, image=machineroomimage)
    machineroomimagelabel.pack()



#----------------------Room 5-----------------------
def Room5Submit():
    a5 = c_or_unc.get()
    if a5 == 1:
        timerObject.detachLabel(room5timer)
        room5.destroy()
        Room_6A()
    else:
        timerObject.detachLabel(room5timer)
        room5.destroy()
        Room_6B()

def Room_5():
    global c_or_unc, narrowcorridormimage, room5, room5timer
    
    room5 = Toplevel()
    room5.title('The Narrow Corridor')
    room5.attributes('-topmost', 'true')

    room5timer = Label(room5, fg='red')
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
    
    narrowcorridormimage = ImageTk.PhotoImage(Image.open('images/Narrow_Corridor.jpg'))
    narrowcorridorimagelabel = Label(room5, image=narrowcorridormimage)
    narrowcorridorimagelabel.pack()
    


#----------------------Room 6A-----------------------
def Room6aSubmit():
    a6a = entry6a.get()
    if a6a == '':
        timerObject.detachLabel(room6atimer)
        room6a.destroy()
        Room_7()
    else:
        timerObject.detachLabel(room6atimer)
        room6a.destroy()
        Trap()

def Room6aClue():
    tkinter.messagebox.showinfo('Clue', '')

def Room_6A():
    global entry6a, room6a, room6atimer
    
    room6a = Toplevel()
    room6a.title('The Lab')

    clue6a = Button(room6a, text='Clue', command=Room6aClue)
    clue6a.pack(anchor='ne')
    
    room6atimer = Label(room6a, fg='red')
    room6atimer.pack()
    timerObject.attachLabel(room6atimer)
    
    topframe = Frame(room6a)
    middleframe = Frame(room6a)
    bottomframe = Frame(room6a)
    topframe.pack()
    middleframe.pack()
    bottomframe.pack()
    
    q6a = Label(topframe, text='''''')
    q6a.pack()
    
    entry6a = Entry(middleframe, justify='center')
    entry6a.pack()
    
    submit6a = Button(bottomframe, text='Submit', command=Room6aSubmit)
    submit6a.pack()
    
    


#----------------------Room 6B-----------------------
def Room6bSubmit():
    sudoku_grid_9x9 = []
    for i in entry6b:
        temp = []
        for j in i:
            temp.append(j.get().strip())
        sudoku_grid_9x9.append(temp)
    
    # input validation
    for i in range(9):
        for j in range(9):
            if sudoku_grid_9x9[i][j].isdigit() == False or int(sudoku_grid_9x9[i][j]) > 9 or int(sudoku_grid_9x9[i][j]) < 1:
                tkinter.messagebox.showerror('Invalid input', 'Please enter valid values')
                return
    
    
    # Check if each row has no repeated number
    for x in range(9):
        temp = set()
        for y in range(9):
            temp.add(sudoku_grid_9x9[y][x])
        if len(temp) != 9:
            tryagain6b = Label(room4, text='Try Again...')
            tryagain6b.pack()
            return
    
    # Check if each column has no repeated numbe
    for x in range(9):
        temp = set(sudoku_grid_9x9[x])
        if len(temp) != 9:
            tryagain6b = Label(room4, text='Try Again...')
            tryagain6b.pack()
            return
    
    # Check if each smaller 3x3 square has no repeated number
    for x in range(0, 7, 3):
        for y in range(0, 7, 3):
            temp = set()
            temp.add(sudoku_grid_9x9[x][y])
            temp.add(sudoku_grid_9x9[x][y+1])
            temp.add(sudoku_grid_9x9[x][y+2])
            
            temp.add(sudoku_grid_9x9[x+1][y])
            temp.add(sudoku_grid_9x9[x+1][y+1])
            temp.add(sudoku_grid_9x9[x+1][y+2])
            
            temp.add(sudoku_grid_9x9[x+2][y])
            temp.add(sudoku_grid_9x9[x+2][y+1])
            temp.add(sudoku_grid_9x9[x+2][y+2])
            
            if len(temp) != 9:
                tryagain6b = Label(room4, text='Try Again...')
                tryagain6b.pack()
                return
    
    # if the user answer correctly, call Correct() function
    timerObject.detachLabel(room6btimer)
    room6b.destroy()
    Room_7()        
    return
    

def Room_6B():
    global entry6b, unknownimage, room6b, room6btimer
    
    room6b = Toplevel()
    room6b.title('The Unknown')
    room6b.attributes('-topmost', 'true')
    
    room6btimer = Label(room6b, fg='red')
    room6btimer.pack()
    timerObject.attachLabel(room6btimer)

    q6b = Label(room6b, text='''Good, everyone likes uncertainty. You are in an unknown room. 
There is a magic cube! It is a design diagram. Each side is 3x3 and there are numbers on it. 
Combined 9 sides become a 9x9 grid. You notice that this may be a sudoku puzzle. 
Objective: Fill a 9 x 9 grid with digits so that each column, each row, and each of the six 3 x 3 subgrids that compose the grid contains all of the digits from 1 to 6. 
There may be a lot of possible solutions. Come up with one of any of them.''')
    q6b.pack()
    
    sudokuframe = Frame(room6b)
    sudokuframe.pack()
    
    board = [[0, 5, 0, 4, 0, 9, 6, 0, 0], 
        [8, 2, 0, 3, 1, 7, 0, 5, 0], 
        [1, 4, 9, 6, 5, 8, 0, 0, 0], 
        [2, 8, 5, 1, 3, 4, 9, 7, 6],
        [6, 9, 1, 8, 0, 0, 5, 4, 3],
        [3, 0, 4, 9, 6, 5, 1, 0, 8],
        [0, 3, 0, 0, 9, 0, 0, 0 ,4],
        [4, 1, 2, 0, 8, 6, 3, 9, 0],
        [9, 6, 7, 0, 4, 3, 0, 1, 5]]
    
    canvas = Canvas(sudokuframe, width=225, height=225)
    canvas.pack(side='left')
    
    for i in range(9):
        for j in range(9):
            x = 25 * j
            y = 25 * i
            if i % 3 == 0:
                canvas.create_line(x, y, x + 225, y, width=2)
            if j % 3 == 0:
                canvas.create_line(x, y, x, y + 225, width=2)
            canvas.create_rectangle(x, y, x + 25, y + 25)
            if board[i][j] != 0:
                canvas.create_text(x + 12.5, y + 12.5, text=str(board[i][j]))

    canvas.create_line(4, 4, 225, 4, width=2)
    canvas.create_line(4, 4, 4, 225, width=2)
    canvas.create_line(225, 0, 225, 225, width=2)
    canvas.create_line(0, 225, 225, 225, width=2)
    
    entry6b = []
    for i in range(9):
        tempframe = Frame(sudokuframe)
        tempframe.pack()
        temp = []
        for j in range(9):
            entry = Entry(tempframe, width=3, justify='center')
            entry.pack(side=LEFT)
            temp.append(entry)
        entry6b.append(temp)
    
    submit6b = Button(room6b, text='Submit', command=Room6bSubmit)
    submit6b.pack()
    
    unknownimage = ImageTk.PhotoImage(Image.open('images/Unknown.jpg').resize((512, 288), Image.NEAREST))
    unknownimagelabel = Label(room6b, image=unknownimage)
    unknownimagelabel.pack()
    


#----------------------Trap-----------------------
def Trap():
    global trapimage
    trapwindow = Toplevel()
    trapwindow.title('Trap')
    
    qtrap = Label(trapwindow, text='''That’s not correct! 
You’ve fallen into a trap! The room fills with an alien gas, and your vision fades. You’ve failed…''')
    qtrap.pack()

    trapimage = ImageTk.PhotoImage(Image.open('images/Trap.jpg'))
    trapimagelabel = Label(trapwindow, image=trapimage)
    trapimagelabel.pack()
    
    Failed()


#----------------------Room 7-----------------------
def Room7Submit():
    a7 = entry7.get()
    if a7 == '1729':
        timerObject.detachLabel(room7timer)
        room7.destroy()
        Room_8()
    else:
        tryagain7 = Label(room7, text='Try Again...')
        tryagain7.pack()

def Room7Clue():
    tkinter.messagebox.showinfo('Clue', '12^3 + 1^3 = 10^3 + 9^3 = ?')

def Room_7():
    global room7, entry7, room7timer, controlroomimage
    room7 = Toplevel()
    room7.title('The Control Room')

    clue7 = Button(room7, text='Clue', command=Room7Clue)
    clue7.pack(anchor='ne')
    
    room7timer = Label(room7, fg='red')
    room7timer.pack()
    timerObject.attachLabel(room7timer)
    
    topframe = Frame(room7)
    middleframe = Frame(room7)
    bottomframe = Frame(room7)
    topframe.pack()
    middleframe.pack()
    bottomframe.pack()
    
    q7 = Label(topframe, text='''You are standing in front of the control room. Unfortunately, it is also locked. 
There is a riddle on the digital lock: “What is the smallest positive integer that can be expressed as the sum of two cubes in two different ways?”''')
    q7.pack()
    
    entry7 = Entry(middleframe, justify='center')
    entry7.pack()
    
    submit7 = Button(bottomframe, text='Submit', command=Room7Submit)
    submit7.pack()
    
    controlroomimage = ImageTk.PhotoImage(Image.open('images/Control_Room.jpg').resize((653, 306), Image.NEAREST))
    controlroomimagelabel = Label(room7, image=controlroomimage)
    controlroomimagelabel.pack()



#----------------------Room 8-----------------------
def Room8Submit():
    a8 = entry8.get()
    if a8 == '16':
        timerObject.detachLabel(room8timer)
        room8.destroy()
        Success()
    else:
        timerObject.detachLabel(room8timer)
        room8.destroy()
        Failed()

def Room_8():
    global room8, entry8, room8timer, quantumnnexusimage
    room8 = Toplevel()
    room8.title('The Quantum Nexus')

    room8timer = Label(room8, fg='red')
    room8timer.pack()
    timerObject.attachLabel(room8timer)
    
    topframe = Frame(room8)
    middleframe = Frame(room8)
    bottomframe = Frame(room8)
    topframe.pack()
    middleframe.pack()
    bottomframe.pack()
    
    q8 = Label(topframe, text='''You finally reach the control room. But you find that the “Quantum Nexus” is not in here! 
You are nearly going to give up. But the curiosity leads you to press down the red button on the desks. 
Suddenly, a well-protected box rose from the floor. There is a lock. The huge monitor suddenly turns on and shows the hint. 

def solve(x):
    if x < 10:
        return solve(x * 2)
    return x
print(solve(2))

What is the output? 
''')
    q8.pack()
    
    entry8 = Entry(middleframe, justify='center')
    entry8.pack()
    
    submit8 = Button(bottomframe, text='Submit', command=Room8Submit)
    submit8.pack()

    quantumnnexusimage = ImageTk.PhotoImage(Image.open('images/Quantum_Nexus.jpg'))
    quantumnnexusimagelabel = Label(room8, image=quantumnnexusimage)
    quantumnnexusimagelabel.pack()
    


#----------------------Success-----------------------
def Success():
    global successimage
    successwindow = Toplevel()
    timerObject.stop()
    
    successlabel = Label(successwindow, text='''After solving the final puzzle, you open the box. 
The "Quantum Nexus" is in it! You input the passcode sequence. 
After that, its light dims. The energy it emits becomes stabilized, and it goes dormant. 
You’ve done it! You’ve secured the Quantum Nexus and saved Earth from a reality-twist catastrophe.''')
    successlabel.pack()

    quitbutton = Button(successwindow, text='Exit the Program', command=exit)
    quitbutton.pack()
    
    successimage = ImageTk.PhotoImage(Image.open('images/Success.jpg').resize((600, 400), Image.NEAREST))
    successimagelabel = Label(successwindow, image=successimage)
    successimagelabel.pack()
    


#----------------------Failed-----------------------
def Failed():
    global failedimage
    failedwindow = Toplevel()
    timerObject.stop()
    
    failedlabel = Label(failedwindow, text='''Despite your best efforts, the puzzles are too challenging. 
You are considered an enemy and are locked up here forever. The “Quantum Nexus” falls into the wrong hands finally. 
Reality begins to warp and twist around you as the Nexus is activated. The world as you know it changes, and not for the better.''')
    failedlabel.pack()
    
    quitbutton = Button(failedwindow, text='Exit the Program', command=exit)
    quitbutton.pack()
    
    failedimage = ImageTk.PhotoImage(Image.open('images/Failed.jpg').resize((600, 340), Image.NEAREST))
    failedimagelabel = Label(failedwindow, image=failedimage)
    failedimagelabel.pack()
       


#---------------------------------------------------
timerObject = global_timer(1800, Failed)

timer = Label(window1, text='30:00', font=('',15), bg='#98a2af', fg='red')
timer.pack()

timerObject.attachLabel(timer)


startbutton = Button(middleframe, text='Start!', command=Room_1)
startbutton.pack()
startimage = ImageTk.PhotoImage(Image.open('images/Desert.jpg').resize((300, 200), Image.NEAREST))
startimagelabel = Label(window1, image=startimage)
startimagelabel.pack()
  
window1.mainloop()