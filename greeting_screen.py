import tkinter as tki


class GreetingScreen:
    def __init__(self, root):
        # self.start_game = False
        self.__root = root
        self.set_img()
        self.label = tki.Label(self.__root, text=" WELCOME TO THE BOGGLE GAME ", bg="white", fg="blue",
                               font=("New Times Roman", 15))
        self.label.pack()
        self.button = tki.Button(self.__root, text="         START         ", bg="white", fg="blue",
                                 font=("New Times Roman", 20), command=self.start)
        self.button.pack()

    def set_img(self):
        """ sets image on greeting screen"""
        self.__img = tki.PhotoImage(file="start.png")
        label_img = tki.Label(self.__root, image=self.__img, height=500, width=625)
        label_img.place(x=0, y=0)

    def start(self):
        """ this function is called when user press the start button"""
        start_game = True
        self.__root.destroy()
        return start_game
