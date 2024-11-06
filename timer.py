import tkinter as tki


class Timer:
    def __init__(self, parent, func):
        self.parent = parent
        self.sec = 180
        self.label = tki.Label(self.parent, font=('arial', 9), text=str(self.sec // 60) + ":" + str(self.sec % 60),
                               height=2, width=10, fg="blue", bg="white")
        self.label.pack()
        self.to_cancel = self.parent.after(1000, self.clock_loop)
        self.func = func


    def clock_loop(self):
        if self.sec > 0:
            self.sec -= 1
            self.label['text'] = str(self.sec // 60) + ":" + str(self.sec % 60)
            self.parent.after(1000, self.clock_loop)
        else:
            self.func()
