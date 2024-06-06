import time, threading

class global_timer:
    labels = []
    def __init__(self, t):
        self.t = t
        self.updateThread = threading.Thread(target=self.updateTimer,daemon=True)

    def updateTimer(self):
        while self.t:
            self.mins, self.secs = divmod(self.t, 60)
            for i in self.labels:
                i.config(text='{:02d}:{:02d}'.format(self.mins, self.secs))
            time.sleep(1)
            self.t -= 1

    def attachLabel(self, label):
        self.labels.append(label)

    def startTimer(self):
        self.updateThread.start()
