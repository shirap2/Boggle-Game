import tkinter.messagebox
from buttons import *
from timer import *


class Screen:

    def __init__(self, root, board, func):
        self.__root = root
        self.__root.wm_title("Boggle")
        self.__board = board
        self.yellow_back_round()
        self.init_time(func)
        self._score_val = tki.StringVar()
        self.buttons = Buttons(root, self.__board)
        self.grid()
        self.list_text = ""
        self.list_hints = ""
        self.init_score()
        self.init_list()
        self.init_hint()
        self.buttons.enter_button(self.__root)
        self.buttons.display_label(self.__root)

    def grid(self):
        """ initializes grid on screen"""
        self.grid_frame = tki.Frame(self.__root)
        self.grid_frame.place(x=16, y=52)
        self.buttons.init_board(self.grid_frame)  # list of all buttons in grid

    def yellow_back_round(self):
        """ sets yellow background"""
        self.right_yellow = tki.Frame(self.__root, height=400, width=400, bg='yellow')
        self.right_yellow.place(x=270, y=0)
        self.up_yellow = tki.Frame(self.__root, height=50, width=300, bg='yellow')
        self.up_yellow.place(x=0, y=0)
        self.down_yellow = tki.Frame(self.__root, height=50, width=300, bg='yellow')
        self.down_yellow.place(x=0, y=350)

    def init_score(self):
        """ sets score display on screen"""
        self._score_val.set("0")
        score_title = tki.Label(self.__root, text="SCORE", bg="yellow", fg="blue", font=("New Times Roman", 10))
        score_title.place(x=410, y=20)
        score_frame = tki.Frame(self.__root, height=2, bd=1, relief=tki.SUNKEN)
        score_frame.place(x=398, y=50)
        score = tki.Label(score_frame, height=2, width=10, textvariable=self._score_val, fg="blue", bg="white")
        score.pack()

    def init_time(self, func):
        """" sets time display on screen"""
        time_title = tki.Label(self.__root, text="TIME", bg="yellow", fg="blue", font=("New Times Roman", 10))
        time_title.place(x=307, y=20)
        time_frame = tki.Frame(self.__root, height=2, bd=1, relief=tki.SUNKEN)
        time_frame.place(x=288, y=50)
        self.__time_label = Timer(time_frame, func)
        self.sec = self.__time_label.sec


    def init_list(self):
        """ initializes list of correctly guessed words on screen"""
        list_title = tki.Label(self.__root, text="FOUND WORDS", bg="yellow", fg="blue", font=("New Times Roman", 10))
        list_title.place(x=280, y=110)
        list_frame = tki.Frame(self.__root, height=250, width=90, bd=1, relief=tki.SUNKEN, bg='white')
        list_frame.place(x=288, y=140)
        self.text_list_label = tki.Label(list_frame, height=16, width=12, text=self.list_text, fg="blue", bg="white")
        self.text_list_label.pack()

    def init_hint(self):
        """ initializes hints on game screen"""
        self.buttons.hint_button(self.__root)
        self.__hint_frame = tki.Frame(self.__root, height=100, width=90, bd=1, relief=tki.SUNKEN, bg='white')
        self.__hint_frame.place(x=398, y=180)
        self.hint_label = tki.Label(self.__hint_frame, text=self.list_hints, bg="white",
                                fg="blue", height=10, width=11)
        self.hint_label.pack()

    def set_score(self, val):
        """
        Sets the current game score
        :param val: The game score
        :type val: int
        """
        self._score_val.set(str(val))

    def show_message(self, title, msg):
        """
        This is a method used to show messages in the game.
        :param title: The title of the message box.
        :param msg: The message to show in the message box.
        """
        tkinter.messagebox.showinfo(str(title), str(msg))




