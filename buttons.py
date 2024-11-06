import tkinter as tki
from boggle_board_randomizer import *


class Buttons:

    def __init__(self, parent, board):
        self.__parent = parent
        self.board = board
        self.grid_buttons = []  # saves board grid  buttons
        self.letters_path = []  # coordinates of letters path
        self.current_str = ''

    def init_board(self, parent):
        """
        initializes letter buttons on board at start of game
        """
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                b = tki.Button(parent, text=str(self.board[i][j]), fg='blue', bg='white',
                               font=("Courier", 30), command=self.letter_event(i, j))
                self.grid_buttons.append(b)
                b.grid(row=i, column=j, sticky="ew")

    def letter_event(self, i, j):
        def letter_press():
            """ this function is called when a letter is pressed.
                it adds the letter coordinates to a list,
                adds the chosen letter to a string and updates the label with the new string"""
            self.letters_path.append((i, j))
            self.current_str += str(self.board[i][j])
            self.display_label.configure(text=self.current_str)
        return letter_press

    def get_letters_path(self):
        """ this function returns a list of coordinates representing the letter path"""
        return self.letters_path

    def display_label(self, parent):
        """ initializes the display label"""
        self.current_str = ""
        self.display_label = tki.Label(parent, text=self.current_str, font=("Arial", 20), bg="yellow")
        self.display_label.place(x=80, y=360)

    def enter_button(self, parent):
        """ initializes enter button"""
        self.enter_button = tki.Button(parent, text="   FINISHED  " + "\n" + "YOUR" + "\n" + "TURN?" + "\n" + "\n"
                                                    + "click here", fg='yellow', bg='blue',
                                       font=("New Times Roman", 10))
        self.enter_button.place(x=398, y=295)

    def hint_button(self, parent):
        """ initializes the hint button"""
        self.hint_button = tki.Button(parent, text="HINT" + "\n" + "  click here   ",
                                      fg='blue', bg='yellow', font=("New Times Roman", 10))  # add command

        self.hint_button.place(x=398, y=140)
