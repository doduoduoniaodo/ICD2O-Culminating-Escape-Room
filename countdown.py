import time, threading
import tkinter.messagebox

class global_timer:
    labels = []
    isRunning = True
    isEnded = False
    exteralStop = False

    def __init__(self, t, endAction):
        self.t = t
        self.updateThread = threading.Thread(target=self.updateTimer,daemon=True)
        self.endAction = endAction

    def updateTimer(self):
        while self.t and not self.isEnded:
            while not self.isRunning:
                pass
            self.mins, self.secs = divmod(self.t, 60)
            for i in self.labels:
                i.config(text='{:02d}:{:02d}'.format(self.mins, self.secs))
            time.sleep(1)
            self.t -= 1
        if not self.exteralStop:
            tkinter.messagebox.showinfo('')
            self.endAction()

    def attachLabel(self, label):
        self.labels.append(label)

    def detachLabel(self, label):
        self.labels.remove(label)

    def startTimer(self):
        self.updateThread.start()

    def pause(self):
        self.isRunning = False

    def resume(self):
        self.isRunning = True

    def stop(self):
        self.isEnded = True
        self.exteralStop = True
