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
mixer.music.play(loops=10)

# create a menubar for user to quit the program
menubar = Menu(window1)
quitmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Quit', menu=quitmenu)
quitmenu.add_command(label='Quit', command=exit)
window1.config(menu = menubar)

# create a label to show where to quit the program
quitlabel = Label(window1, text='👆Quit the program', font=('Consolas', 8), bg='#98a2af')
quitlabel.pack(anchor='nw')

# create a label to show DO NOT CLOSE ANY WINDOW BY CLICKING THE TOP-RIGHT “❌” BUTTON
warninglabel = Label(window1, text='***DO NOT CLOSE ANY WINDOW BY CLICKING THE TOP-RIGHT “❌” BUTTON***', 
                     fg='red')
warninglabel.pack()

# create three frame
topframe = Frame(window1, relief=GROOVE, borderwidth=5, bg='#98a2af')
middleframe = Frame(window1, relief=RAISED, borderwidth=5, bg='#98a2af')
topframe.pack()
middleframe.pack()

# create the intro label
intro1 = Label(topframe, text='''You are a rookie agent at Sector 51. 
Your task is to retrieve a powerful artifact named “Quantum Nexus” which can manipulate reality. 
The only intelligence is that artifact is now in at an abandoned palace in the Nevade Desert. \n
Now, you are in the palace and there are labyrinthine corridors. 
You need to navigate through these corridors and solve puzzles to reach the “Quantum Nexus”. 
Secure the Quantum Nexus and don't let it fall into the wrong hands!''', font=('consolas', 10))
intro1.pack()



#----------------------Room 1-----------------------
# define a function for checking the answer
def Room1Submit():
    # get the answer from the entry box
    a1 = entry1.get()
    
    # if the user answer correctly
    # continue to Room 2
    # otherwise, create a label of "Try Again"
    if a1 == '110011':
        timerObject.detachLabel(room1timer)
        room1.destroy()
        Room_2()
    else:
        tryagain1 = Label(room1, text='Try Again...', font=('consolas', 10), fg='red')
        tryagain1.pack()

# if the user clicks the clue button
# a pop-up message box contains the clue
def Room1Clue():
    tkinter.messagebox.showinfo('Clue', 'You are at Sector 51')

def Room_1():
    global entry1, room1, room1timer, entranceimage

    # create a Toplevel window for Room 1
    room1 = Toplevel()
    room1.title('The Entrance')
    room1.config(background='#d9d2c5')
    
    # create a clue button
    clue1 = Button(room1, text='Clue', command=Room1Clue, bg='#c5f2d9', font=('', 11))
    clue1.pack(anchor='ne')
    
    # start the timer
    try:
        timerObject.startTimer()
    except RuntimeError:
        pass
    room1timer = Label(room1, fg='red')
    room1timer.pack()
    timerObject.attachLabel(room1timer)
    
    # create a frame contains the riddle
    middleframe = Frame(room1, relief=GROOVE, borderwidth=5)
    middleframe.pack()
    
    # create a label for the riddle
    q1 = Label(middleframe, text='''You enter the palace and you want to go deeper.
You soon find there is a huge door and a digital lock on it. You look closer and see a hint next to it.
“The binary number of the place you at”''', font=('consolas', 11), bg='#c5d2d9')
    q1.pack()
    
    # create an entry box
    entry1 = Entry(room1, justify='center')
    entry1.pack()
    
    # create a submit button
    submit1 = Button(room1, text='Submit', command=Room1Submit)
    submit1.pack()
    
    # show an image    
    entranceimage = ImageTk.PhotoImage(Image.open('images/Entrance.jpg'))
    entranceimagelabel = Label(room1, image=entranceimage)
    entranceimagelabel.pack()
    
    

#----------------------Room 2-----------------------
def Room2Submit():
    # get the answer from the entry box
    a2 = entry2.get()
    
    # if the user answer correctly
    # continue to Room 3
    # otherwise, create a label of "Try Again"
    if a2 == '111101':
        timerObject.detachLabel(room2timer)
        room2.destroy()
        Room_3()
    else:
        tryagain2 = Label(room2, text='Try Again...', font=('consolas', 11), fg='red')
        tryagain2.pack()

# if the user clicks the clue button
# a pop-up message box contains the clue
def Room2Clue():
    tkinter.messagebox.showinfo('Clue', '1 9 6 1')

def Room_2():
    global room2, entry2, meetingroomimage, room2timer
    
    # create a window for Room 2
    room2 = Toplevel()
    room2.title('The Meeting Room')
    room2.config(background='#d9d2c5')
    
    # create a clue button
    clue2 = Button(room2, text='Clue', command=Room2Clue, bg='#c5f2d9', font=('', 11))
    clue2.pack(anchor='ne')
    
    # create a timer label
    room2timer = Label(room2, fg='red')
    room2timer.pack()
    timerObject.attachLabel(room2timer)

    # create three frames
    topframe = Frame(room2, relief=GROOVE, borderwidth=5)
    middleframe = Frame(room2)
    bottomframe = Frame(room2)
    topframe.pack()
    middleframe.pack()
    bottomframe.pack()
    
    # create a label for the riddle
    q2 = Label(topframe, text='''You enter the meeting room and your find a bigger door. 
There are no hints beside the digital lock. Fortunately, you find a notepad on the desk and there are some words… 
“Tell me the date of the first human space flight! In binary! (19xx)”''', 
font=('consolas', 11), bg='#c5d2d9')
    q2.pack()
    
    # create an entry box
    entry2 = Entry(middleframe, justify='center')
    entry2.pack()
    
    # create a submit button
    submit2 = Button(bottomframe, text='Submit', command=Room2Submit)
    submit2.pack()
    
    # show an image
    meetingroomimage = ImageTk.PhotoImage(Image.open('images/Meeting_Room.jpg').resize((600, 338), Image.NEAREST))
    meetingroomimagelabel = Label(room2, image=meetingroomimage)
    meetingroomimagelabel.pack()



#----------------------Room 3-----------------------
def Room3Submit():
    # get the answer from the entry box
    # choose "up" --> continue to Room 4
    # choose "down" --> back to Room 1
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
    
    # create a window for Room 3
    room3 = Toplevel()
    room3.title('The Atrium')
    room3.config(background='#d9d2c5')
    room3.attributes('-topmost', 'true')

    # create a timer label
    room3timer = Label(room3, fg='red')
    room3timer.pack()
    timerObject.attachLabel(room3timer)

    # create three frames
    topframe = Frame(room3, relief=GROOVE, borderwidth=5)
    middleframe = Frame(room3)
    bottomframe = Frame(room3)
    topframe.pack()
    middleframe.pack()
    bottomframe.pack()
    
    # create a label for the choice question
    q3 = Label(topframe, text='''You come to the atrium. 
You realize that this palace is way larger than you thought. You have a long way to go… 
There is an elevator. It can’t select floors. You can decide whether to go up or down.''', 
font=('consolas', 11), bg='#c5d2d9')
    q3.pack()
    
    # create an IntVar to store the user's choice
    upordown = IntVar()
    
    # create two radio buttons
    radiobutton3_1 = Radiobutton(middleframe, text='Up', variable=upordown, value=1)
    radiobutton3_2 = Radiobutton(middleframe, text='Down', variable=upordown, value=2)
    radiobutton3_1.pack()
    radiobutton3_2.pack()
    
    # create a submit button
    submit3 = Button(bottomframe, text='Submit', command=Room3Submit)
    submit3.pack()
    
    # show an image
    atriumimage = ImageTk.PhotoImage(Image.open('images/Atrium.jpg').resize((600, 338), Image.NEAREST))
    atriumimagelabel = Label(room3, image=atriumimage)
    atriumimagelabel.pack()



#----------------------Room 4-----------------------
def Room4Submit():
    # get the answer from the entry box
    a4 = entry4.get()
    
    # if the user answer correctly
    # continue to Room 5
    # otherwise, create a label of "Try Again"
    if a4 == '7.5':
        timerObject.detachLabel(room4timer)
        room4.destroy()
        Room_5()
    else:
        tryagain4 = Label(room4, text='Try Again...', font=('consolas', 10), fg='red')
        tryagain4.pack()

# if the user clicks the clue button
# a pop-up message box contains the clue
def Room4Clue():
    tkinter.messagebox.showinfo('Clue', 'The minute hand is at 90 degrees, and the hour hand is at 97.5 degrees')

def Room_4():
    global room4, entry4, clockimage, machineroomimage, room4timer
    
    # create a window for Room 4
    room4 = Toplevel()
    room4.title('The Machine Room')
    room4.config(background='#d9d2c5')
    
    # create a clue button
    clue4 = Button(room4, text='Clue', command=Room4Clue, bg='#c5f2d9', font=('', 11))
    clue4.pack(anchor='ne')

    # create a timer label
    room4timer = Label(room4, fg='red')
    room4timer.pack()
    timerObject.attachLabel(room4timer)
    
    # show an image (the clock shows 3:15)
    clockimage = ImageTk.PhotoImage(Image.open('images/3_15.png').resize((182, 182), Image.NEAREST))
    clockimagelabel = Label(room4, image=clockimage)
    clockimagelabel.pack()
    
    # create three frames
    topframe = Frame(room4, relief=GROOVE, borderwidth=5)
    middleframe = Frame(room4)
    bottomframe = Frame(room4)
    topframe.pack()
    middleframe.pack()
    bottomframe.pack()
    
    # create a label for the riddle
    q4 = Label(topframe, text='''You come to the machine room but you can’t see anything. 
You feel for the light switch on the wall and turn it on. There are some old computers on the desks. 
Beside the screen, there is a door. Again, no hints. You notice that there is a note on the desk. 
“The passcode is the angle between the hour and minute hands of the clock”''', 
font=('consolas', 11), bg='#c5d2d9')
    q4.pack()
    
    # create an entry box
    entry4 = Entry(middleframe, justify='center')
    entry4.pack()
    
    # create a submit button
    submit4 = Button(bottomframe, text='Submit', command=Room4Submit)
    submit4.pack()
    
    # create an image
    machineroomimage = ImageTk.PhotoImage(Image.open('images/Machine_Room.jpg'))
    machineroomimagelabel = Label(room4, image=machineroomimage)
    machineroomimagelabel.pack()



#----------------------Room 5-----------------------
def Room5Submit():
    # get the answer from the entry box
    a5 = c_or_unc.get()
    
    # choose "Certainty" --> continue to Room 6A
    # choose "Uncertainty" --> continue to Room 6B
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
    
    # create a window for Room 5
    room5 = Toplevel()
    room5.title('The Narrow Corridor')
    room5.config(background='#d9d2c5')
    room5.attributes('-topmost', 'true')

    # create a timer label
    room5timer = Label(room5, fg='red')
    room5timer.pack()
    timerObject.attachLabel(room5timer)

    # create three frames
    topframe = Frame(room5, relief=GROOVE, borderwidth=5)
    middleframe = Frame(room5)
    bottomframe = Frame(room5)
    topframe.pack()
    middleframe.pack()
    bottomframe.pack()
    
    # create a label of choice question
    q5 = Label(topframe, text='''You exit the machine room, now here is a narrow corridor. 
At the end, there are two doors. There are signs on each door. 
“Certainty” and “Uncertainty”. Which one would you choose?''', 
font=('consolas', 11), bg='#c5d2d9')
    q5.pack()
    
    # create an IntVar to store the user's choice
    c_or_unc = IntVar()
    
    # create two radio buttons
    radiobutton5_1 = Radiobutton(middleframe, text='Certainty', variable=c_or_unc, value=1)
    radiobutton5_2 = Radiobutton(middleframe, text='Uncertainty', variable=c_or_unc, value=2)
    radiobutton5_1.pack()
    radiobutton5_2.pack()
    
    # create a submit button
    submit5 = Button(bottomframe, text='Submit', command=Room5Submit)
    submit5.pack()
    
    # show an image
    narrowcorridormimage = ImageTk.PhotoImage(Image.open('images/Narrow_Corridor.jpg'))
    narrowcorridorimagelabel = Label(room5, image=narrowcorridormimage)
    narrowcorridorimagelabel.pack()
    


#----------------------Room 6A-----------------------
def Room6aSubmit():
    # get the answer from the entry box
    a6a = entry6a.get()
    
    # if the user answer correctly
    # continue to Room 7
    # otherwise, fall in to the trap
    if a6a == '36':
        timerObject.detachLabel(room6atimer)
        room6a.destroy()
        Room_7()
    else:
        timerObject.detachLabel(room6atimer)
        room6a.destroy()
        Trap()

# if the user clicks the clue button
# a pop-up message box contains the clue
def Room6aClue():
    tkinter.messagebox.showinfo('Clue', 'The answer in the centre of each triangle equals the difference between the top and left hand values, multiplied by the right hand value.')

def Room_6A():
    global entry6a, room6a, room6atimer, room6apuzzleimage, labimage
    
    # create a window for Room 6A
    room6a = Toplevel()
    room6a.title('The Lab')
    room6a.config(background='#d9d2c5')

    # create a clue button
    clue6a = Button(room6a, text='Clue', command=Room6aClue, bg='#c5f2d9', font=('', 11))
    clue6a.pack(anchor='ne')
    
    # create a timer label
    room6atimer = Label(room6a, fg='red')
    room6atimer.pack()
    timerObject.attachLabel(room6atimer)
    
    # create three frames
    topframe = Frame(room6a, relief=GROOVE, borderwidth=5, bg='#c5d2d9')
    middleframe = Frame(room6a)
    bottomframe = Frame(room6a)
    topframe.pack()
    middleframe.pack()
    bottomframe.pack()
    
    # create a label of puzzle
    q6a = Label(topframe, text='''Good, everyone likes certainty. Continue to move on! 
You are in the lab. You notice that here is the place where those people studied the “Quantum Nexus” in the past. 
There is a door that says “Do not enter”. But that is the only place you can go. Again, a digital lock. Again, no hints. 
You realize that the “Certainty” sign and an unsolved puzzle are on the board.''', 
font=('consolas', 11), bg='#c5d2d9')
    q6a.pack()
    
    # show the puzzle image
    room6apuzzleimage = ImageTk.PhotoImage(Image.open('images/room_6a_puzzle.png'))
    room6apuzzleimagelabel = Label(topframe, image=room6apuzzleimage)
    room6apuzzleimagelabel.pack()
    
    # create an entry box
    entry6a = Entry(middleframe, justify='center')
    entry6a.pack()
    
    # create a submit button
    submit6a = Button(bottomframe, text='Submit', command=Room6aSubmit)
    submit6a.pack()
    
    # show an image
    labimage = ImageTk.PhotoImage(Image.open('images/Lab.jpg').resize((512, 288), Image.NEAREST))
    labimagelabel = Label(room6a, image=labimage)
    labimagelabel.pack()
    
    


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
            tryagain6b = Label(room6b, text='Try Again...', font=('consolas', 10), fg='red')
            tryagain6b.pack()
            return
    
    # Check if each column has no repeated numbe
    for x in range(9):
        temp = set(sudoku_grid_9x9[x])
        if len(temp) != 9:
            tryagain6b = Label(room6b, text='Try Again...', font=('consolas', 10), fg='red')
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
                tryagain6b = Label(room6b, text='Try Again...', font=('consolas', 10), fg='red')
                tryagain6b.pack()
                return
    
    # if the user answer correctly, call Correct() function
    timerObject.detachLabel(room6btimer)
    room6b.destroy()
    Room_7()        
    return

# if the user clicks the clue button
# a pop-up message box contains the clue
def Room6bClue():
    for i in range(9):
        answer6b = Label(room6b, text=answer[i])
        answer6b.pack()

def Room_6B():
    global entry6b, unknownimage, room6b, room6btimer, answer
    
    # create a window for Room 6B
    room6b = Toplevel()
    room6b.title('The Unknown')
    room6b.config(background='#d9d2c5')
    
    # create a clue button
    clue6b = Button(room6b, text='Clue', command=Room6bClue, bg='#c5f2d9', font=('', 11))
    clue6b.pack(anchor='ne')
    
    # create a timer label
    room6btimer = Label(room6b, fg='red')
    room6btimer.pack()
    timerObject.attachLabel(room6btimer)

    # create three frames
    topframe = Frame(room6b, relief=GROOVE, borderwidth=5)
    topframe.pack()
    
    # create a label of the puzzle 
    q6b = Label(topframe, text='''Good, everyone likes uncertainty. You are in an unknown room. 
There is a magic cube! It is a design diagram. Each side is 3x3 and there are numbers on it. 
Combined 9 sides become a 9x9 grid. You notice that this may be a sudoku puzzle. 
Objective: Fill a 9 x 9 grid with digits so that each column, each row, and each of the six 3 x 3 subgrids 
that compose the grid contains all of the digits from 1 to 6. 
There may be a lot of possible solutions. Come up with one of any of them.''', 
font=('consolas', 11), bg='#c5d2d9')
    q6b.pack()
    
    # create a frame that contains the sudoku grid
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
    
    # Answer:
    answer = [[7, 5, 3, 4, 2, 9, 6, 8, 1], 
            [8, 2, 6, 3, 1, 7, 4, 5, 9], 
            [1, 4, 9, 6, 5, 8, 7, 3, 2], 
            [2, 8, 5, 1, 3, 4, 9, 7, 6],
            [6, 9, 1, 8, 7, 2, 5, 4, 3],
            [3, 7, 4, 9, 6, 5, 1, 2, 8],
            [5, 3, 8, 7, 9, 1, 2, 6 ,4],
            [4, 1, 2, 5, 8, 6, 3, 9, 7],
            [9, 6, 7, 2, 4, 3, 8, 1, 5]]
    
    # create a canva to show the sudoku grid
    canvas = Canvas(sudokuframe, width=225, height=225)
    canvas.pack(side='left')
    
    # draw the lines and show the numbers
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
    
    # create 9 by 9 entry boxes
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
    
    # create a submit button
    submit6b = Button(room6b, text='Submit', command=Room6bSubmit)
    submit6b.pack()
    
    # show an image
    unknownimage = ImageTk.PhotoImage(Image.open('images/Unknown.jpg').resize((512, 288), Image.NEAREST))
    unknownimagelabel = Label(room6b, image=unknownimage)
    unknownimagelabel.pack()
    


#----------------------Trap-----------------------
def Trap():
    global trapimage
    
    # create a window for Trap
    trapwindow = Toplevel()
    trapwindow.title('Trap')
    trapwindow.config(background='#d9d2c5')
    
    # create a frame
    topframe = Frame(trapwindow, relief=GROOVE, borderwidth=5)
    topframe.pack()
    
    # create a label for the plot
    qtrap = Label(topframe, text='''That’s not correct! 
You’ve fallen into a trap! The room fills with an alien gas, and your vision fades. You’ve failed…''', 
font=('consolas', 11), bg='#c5d2d9')
    qtrap.pack()

    # show an image of a trap
    trapimage = ImageTk.PhotoImage(Image.open('images/Trap.jpg'))
    trapimagelabel = Label(trapwindow, image=trapimage)
    trapimagelabel.pack()
    
    # call Failed function
    Failed()


#----------------------Room 7-----------------------
def Room7Submit():
    # get the answer from the entry box
    a7 = entry7.get()
    
    # if the user answer correctly
    # continue to Room 8
    # otherwise, create a label of "Try Again"
    if a7 == '1729':
        timerObject.detachLabel(room7timer)
        room7.destroy()
        Room_8()
    else:
        tryagain7 = Label(room7, text='Try Again...', font=('consolas', 10), fg='red')
        tryagain7.pack()

# if the user clicks the clue button
# a pop-up message box contains the clue
def Room7Clue():
    tkinter.messagebox.showinfo('Clue', '12^3 + 1^3 = 10^3 + 9^3 = ?')

def Room_7():
    global room7, entry7, room7timer, controlroomimage
    
    # create a window for Room 7
    room7 = Toplevel()
    room7.title('The Control Room')
    room7.config(background='#d9d2c5')

    # create a clue button
    clue7 = Button(room7, text='Clue', command=Room7Clue, bg='#c5f2d9', font=('', 11))
    clue7.pack(anchor='ne')
    
    # create a timer label
    room7timer = Label(room7, fg='red')
    room7timer.pack()
    timerObject.attachLabel(room7timer)
    
    # create three frames
    topframe = Frame(room7, relief=GROOVE, borderwidth=5)
    middleframe = Frame(room7)
    bottomframe = Frame(room7)
    topframe.pack()
    middleframe.pack()
    bottomframe.pack()
    
    # create a label of the riddle
    q7 = Label(topframe, text='''You are standing in front of the control room. Unfortunately, it is also locked. 
There is a riddle on the digital lock: “What is the smallest positive integer that can be expressed as the sum of two cubes in two different ways?”''',
font=('consolas', 11), bg='#c5d2d9')
    q7.pack()
    
    # create an entry box
    entry7 = Entry(middleframe, justify='center')
    entry7.pack()
    
    # create a submit button
    submit7 = Button(bottomframe, text='Submit', command=Room7Submit)
    submit7.pack()
    
    # show an image
    controlroomimage = ImageTk.PhotoImage(Image.open('images/Control_Room.jpg').resize((653, 306), Image.NEAREST))
    controlroomimagelabel = Label(room7, image=controlroomimage)
    controlroomimagelabel.pack()



#----------------------Room 8-----------------------
def Room8Submit():
    # get the answer from the entry box
    a8 = entry8.get()
    
    # if the user answer correctly
    # continue to success_window
    # otherwise, continue to failed_window
    if a8 == '16':
        timerObject.detachLabel(room8timer)
        room8.destroy()
        Success()
    else:
        timerObject.detachLabel(room8timer)
        room8.destroy()
        Failed()

def Room_8():
    global room8, entry8, room8timer, quantumnnexusimage, q8_2
    
    # create a window for Room 8
    room8 = Toplevel()
    room8.title('The Quantum Nexus')
    room8.config(background='#d9d2c5')

    # create a timer label
    room8timer = Label(room8, fg='red')
    room8timer.pack()
    timerObject.attachLabel(room8timer)
    
    # create three frames
    topframe = Frame(room8, bg='#c5d2d9', relief=GROOVE, borderwidth=5)
    middleframe = Frame(room8)
    bottomframe = Frame(room8)
    topframe.pack()
    middleframe.pack()
    bottomframe.pack()
    
    # create a label for the riddle
    q8_1 = Label(topframe, text='''You finally reach the control room. But you find that the “Quantum Nexus” is not in here! 
You are nearly going to give up. But the curiosity leads you to press down the red button on the desks. 
Suddenly, a well-protected box rose from the floor. There is a lock. The huge monitor suddenly turns on and shows the hint.''', 
font=('consolas', 11), bg='#c5d2d9')
    q8_1.pack()

    # show the riddle (an image)
    q8_2 = ImageTk.PhotoImage(Image.open('images/room_8_puzzle.png'))
    q8_2l = Label(topframe, image=q8_2)
    q8_2l.pack()

    # create a label for the riddle
    q8_3 = Label(topframe, text='''What is the output?''', font=('consolas', 11), bg='#c5d2d9')
    q8_3.pack()
    
    # create an entry box
    entry8 = Entry(middleframe, justify='center')
    entry8.pack()
    
    # create submit button
    submit8 = Button(bottomframe, text='Submit', command=Room8Submit)
    submit8.pack()

    # show an image
    quantumnnexusimage = ImageTk.PhotoImage(Image.open('images/Quantum_Nexus.jpg'))
    quantumnnexusimagelabel = Label(room8, image=quantumnnexusimage)
    quantumnnexusimagelabel.pack()
    


#----------------------Success-----------------------
def Success():
    global successimage
    
    # create a window
    successwindow = Toplevel()
    successwindow.title('Success')
    successwindow.config(background='#d9d2c5')
    
    # stop the timer
    timerObject.stop()
    
    # create a frame
    topframe = Frame(successwindow, relief=GROOVE, borderwidth=5)
    topframe.pack()
    
    # create a label for the plot
    successlabel = Label(topframe, text='''After solving the final puzzle, you open the box. 
The "Quantum Nexus" is in it! You input the passcode sequence. 
After that, its light dims. The energy it emits becomes stabilized, and it goes dormant. 
You’ve done it! You’ve secured the Quantum Nexus and saved Earth from a reality-twist catastrophe.''', 
font=('consolas', 11), bg='#c5d2d9')
    successlabel.pack()

    # create a button for user exiting the program
    quitbutton = Button(successwindow, text='Exit the Program', command=exit)
    quitbutton.pack()
    
    # show an image
    successimage = ImageTk.PhotoImage(Image.open('images/Success.jpg').resize((600, 400), Image.NEAREST))
    successimagelabel = Label(successwindow, image=successimage)
    successimagelabel.pack()
    


#----------------------Failed-----------------------
def Failed():
    global failedimage
    
    # create a window
    failedwindow = Toplevel()
    failedwindow.title('Failed')
    failedwindow.config(background='#d9d2c5')
    timerObject.stop()
    
    # create a frame
    topframe = Frame(failedwindow, relief=GROOVE, borderwidth=5)
    topframe.pack()
    
    # create a label for the plot
    failedlabel = Label(topframe, text='''Despite your best efforts, the puzzles are too challenging. 
You are considered an enemy and are locked up here forever. The “Quantum Nexus” falls into the wrong hands finally. 
Reality begins to warp and twist around you as the Nexus is activated. The world as you know it changes, and not for the better.''', 
font=('consolas', 11), bg='#c5d2d9')
    failedlabel.pack()
    
    # create a button for user exiting the program
    quitbutton = Button(failedwindow, text='Exit the Program', command=exit)
    quitbutton.pack()
    
    # show an image
    failedimage = ImageTk.PhotoImage(Image.open('images/Failed.jpg').resize((600, 340), Image.NEAREST))
    failedimagelabel = Label(failedwindow, image=failedimage)
    failedimagelabel.pack()
       


#---------------------------------------------------
# set the timer to 30 minutes
timerObject = global_timer(1800, Failed)
timer = Label(window1, text='30:00', font=('',15), bg='#98a2af', fg='red')
timer.pack()
timerObject.attachLabel(timer)

# create a start button
startbutton = Button(middleframe, text='Start!', command=Room_1)
startbutton.pack()

# create a image label at the main window (a desert)
startimage = ImageTk.PhotoImage(Image.open('images/Desert.jpg').resize((300, 200), Image.NEAREST))
startimagelabel = Label(window1, image=startimage)
startimagelabel.pack()

# keep running the window
window1.mainloop()