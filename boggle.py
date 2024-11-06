from ex12_utils import *
from screen import *
from greeting_screen import *


class Boggle:
    MSGS = {"Wrong Guess": "wrong word or invalid path. try again",
            "Right Guess": "You chose a correct word. You're so smart!",
            "End Game": "Time is up. Game over. Would you like to play again?",
            "Found this word already": "You have already chosen a path with this word. Sorry, try again!",
            "Can't get a hint yet!": "You have to first earn at least one point."}

    def __init__(self, word_filename):
        self.__word_list = get_words(word_filename)
        self.__path = []  # list of coordinates of path of chosen letters
        self.__right_words = []  # list of correct words user has found (to be displayed on a label..?)
        self.__score = 0
        self.__play_again = True
        self.__path = []
        self.run_game()
        self.__end_turn = False

    def play_screen(self):
        """ initializes game screen"""
        self.__root = tki.Tk()
        self.__root.wm_title("Boggle")
        self.__root.geometry("600x400")
        self.__root.resizable(0, 0)
        self.__board = randomize_board()
        self.__screen = Screen(self.__root, self.__board, self.play_again_msg)
        self.set_commands()
        self.__root.mainloop()

    def end_turn(self):
        """The command for the button which finishes the turn.
        if the chosen letters are a valid word, the word is added to the list on the board and the score is updated."""
        word = self.__screen.buttons.current_str
        self.__screen.buttons.current_str = ""  # reset the chosen letters label
        self.__screen.buttons.display_label.configure(text=self.__screen.buttons.current_str)
        self.__path = self.__screen.buttons.get_letters_path()  # updates the list of coords to pressed coords
        if self.__path:
            path_value = is_valid_path(self.__board, self.__path, self.__word_list)  # checks validity
            if not path_value:
                self.__screen.show_message("Wrong Guess", self.MSGS["Wrong Guess"])
            else:
                if path_value in self.__right_words:  # already chosen this word
                    self.__screen.show_message("Found this word already", self.MSGS["Found this word already"])
                else:
                    self.correct_word(word)
        self.__screen.buttons.letters_path = []  # reset coords path

    def correct_word(self, word):
        """this function is called when user chooses a correct word.
        it displays a message to the user, adds the correct word to the list of correct words and updates the score"""
        self.__screen.show_message("Right Guess", self.MSGS["Right Guess"])
        self.__right_words.append(word)
        self.update_score()
        self.__screen.list_text += word + '\n'
        self.__screen.text_list_label.configure(text=self.__screen.list_text)

    def set_commands(self):
        """ sets commands for buttons"""
        self.__screen.buttons.enter_button['command'] = self.end_turn
        self.__screen.buttons.hint_button['command'] = self.hints
        
    def play_again_msg(self):
        """ defines message box at end of game"""
        if tkinter.messagebox.askyesno("End Game", self.MSGS["End Game"]):  # response is "yes"-> True
            self.__root.destroy()
            self.play_screen()
        else:
            self.__root.destroy()

    def update_score(self):
        """ updates score value and sets updated value on screen"""
        n = len(self.__path)
        self.__score += n ** 2
        self.__screen.set_score(self.__score)

    def hints(self):
        """ this function is called when user presses the hint button. it displays a word hint on the screen"""
        hint_lst = []
        if self.__score == 0:
            self.__screen.show_message("Can't get a hint yet!", self.MSGS["Can't get a hint yet!"])
        else:
            self.__score -= 1
            self.__screen.set_score(self.__score)
            for word in self.__word_list:
                if word not in self.__right_words:
                    hint_lst = max_score_paths(self.__board, [word])
                    if hint_lst:
                        break
            for path in hint_lst:
                letters_of_path = coords_to_word(board_coords(self.__board), path)
                if letters_of_path not in self.__right_words:
                    self.__screen.list_hints += letters_of_path + "\n"
                    self.__screen.hint_label.configure(text=self.__screen.list_hints)
                    break

    def greeting_window(self):
        """ this function initializes greeting window at start of game"""
        root = tki.Tk()
        root.wm_title("WELCOME TO BOGGLE")
        root.geometry("620x500")
        root.resizable(0, 0)
        GreetingScreen(root)
        root.mainloop()

    def run_game(self):
        """ this function runs the boggle game"""
        self.greeting_window()
        self.play_screen()


if __name__ == "__main__":
    game = Boggle("boggle_dict.txt")
