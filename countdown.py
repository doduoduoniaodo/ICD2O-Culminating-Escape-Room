import time, threading
import tkinter.messagebox

class global_timer:
    labels = []
    isRunning = True
    isEnded = False
    exteralStop = False

    # initialize the timer
    def __init__(self, t, endAction):
        self.t = t
        self.updateThread = threading.Thread(target=self.updateTimer,daemon=True)
        self.endAction = endAction

    # countdown
    def updateTimer(self):
        while self.t and not self.isEnded:
            while not self.isRunning:
                pass
            self.mins, self.secs = divmod(self.t, 60)
            for i in self.labels:
                i.config(text='{:02d}:{:02d}'.format(self.mins, self.secs))
            time.sleep(1)
            self.t -= 1
        
        # when the time runs out, show a message box and call "Failed" function
        if not self.isEnded:
            tkinter.messagebox.showinfo('The Time Runs Out', 'The Time Runs Out...')
            self.endAction()
    
    # add existing labels to the list
    def attachLabel(self, label):
        self.labels.append(label)

    # remove nonexistent labels
    def detachLabel(self, label):
        self.labels.remove(label)

    # start the timer
    def startTimer(self):
        self.updateThread.start()

    # stop the timer
    def stop(self):
        self.isEnded = True
