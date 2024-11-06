from boggle_board_randomizer import *


def is_valid_path(board, path, words):
    """
    this function checks if path is valid and returns word if word from path is in the word list.
     Otherwise returns None
    :param board: game board of letters
    :param path: list of coordinates representing path on board
    :param words: list of words
    :return: word (str) or None
    """
    board_dict = board_coords(board)
    if check_path_coords(path):
        word = coords_to_word(board_dict, path)
        if word in words:
            return word
    return None


def get_words(filename):
    """
    this function extracts a list of words from file and returns them in a list
    :param filename: name of file user extracts words from
    :return: list of words
    """
    with open(filename, 'r') as words_file:
        word_lst = []
        for line in words_file:
            word = line.rstrip()
            word_lst.append(word)
    return word_lst


def check_path_coords(path):
    """
    this function checks that the path is valid and that each letter from board is only used once in a word
    :param path: list of tuples representing coordinates on the board
    :return: True of False
    """
    if len(set(path)) != len(path):
        return False
    for i in range(len(path) - 1):
        (x, y) = path[i]
        moves = possible_moves(path[i])
        if x > BOARD_SIZE - 1 or x < 0 or y > BOARD_SIZE - 1 or y < 0:
            return False
        if path[i + 1] not in moves:
            return False
    return True


def board_coords(board):
    """
    this function returns a dictionary of coordinates and letters from the board
    :return: dictionary of coordinates and letters
    """
    # board = randomize_board()
    board_dict = {}
    row = col = 0
    for lst in board:
        for letter in lst:
            board_dict[(row, col)] = letter
            col += 1
        row += 1
        col = 0
    return board_dict


def coords_to_word(board_dict, path):
    """
    this function converts coordinates of spot on board to letters
    :param board_dict: dictionary of coordinates and letters from board
    :param path: list of coordinates representing path on board
    :return: word (str)
    """
    word = ""
    for coordinate in path:
        if coordinate in board_dict:
            word += board_dict[coordinate]
    return word


def find_length_n_paths(n, board, words):
    """
    this function returns all possible n- length paths containing a word from word list.
    :param n: int
    :param board: list of lists containing game board letters
    :param words: word list
    :return: list of possible paths
    """
    paths_list = []
    for word in words:
        if len(word) >= n:
            spot_lst = find_spot(board, word, 0)
            for spot in spot_lst:
                find_length_n_paths_helper(n, board, word, [spot], paths_list, len(board_coords(board)[spot]))
    return paths_list


def find_length_n_paths_helper(n, board, word, path, paths_list, i):
    """ helper function for finding n length word paths"""
    if len(path) == n and check_path_coords(path) and i == len(word):
        paths_list.append(path)
        return path
    moves = possible_moves(path[-1])
    new_spots = find_spot(board, word, i)[:]
    for spot in new_spots:
        if spot in moves:
            new_path = path[:]
            find_length_n_paths_helper(n, board, word, new_path + [spot], paths_list,
                                       i + len(board_coords(board)[spot]))


def possible_moves(coord):
    """
    this function receives a coordinate and returns all possible moves
    :param coord: tuple
    :return: list of coordinates
    """
    (x, y) = coord
    return [(x - 1, y - 1), (x - 1, y), (x - 1, y + 1), (x, y - 1),
            (x, y + 1), (x + 1, y - 1), (x + 1, y), (x + 1, y + 1)]


def find_spot(board, word, i):
    """
    this function finds coordinates on board of letter in word at according index (i)
    :param i: index of letter in word
    :param board: list of lists with letters from board
    :param word: word from word list
    :return: list of coordinates
    """
    spots = []
    for (key, value) in board_coords(board).items():
        if word[i:].startswith(value):
            spots.append(key)
    return spots


def contains_n_list(n, list_of_lists):
    """Checks if the list of lists contains a list in length of n."""
    for lst in list_of_lists:
        if len(lst) == n:
            return lst


def find_length_n_words_helper(board, word, path, paths_list, max_list, i, bool):
    """ helper function for finding n length word paths"""
    if bool:  # max function is calling
        if contains_n_list(len(word), paths_list) and contains_n_list(len(word), paths_list) not in max_list:
            max_list.append(contains_n_list(len(word), paths_list))
            return

    if i == len(word) and check_path_coords(path):
        paths_list.append(path)
        return path

    moves = possible_moves(path[-1])
    for spot in moves:  # all possible coords in eight directions
        if spot in list(board_coords(board).keys()):  # checks if the coord is in the board limit
            relevant_spots = find_spot(board, word, i)[:]  # coords in board with the relevant letter\letters
            if spot in relevant_spots:
                new_path = path[:]
                new_i = i + len(board_coords(board)[spot])
                find_length_n_words_helper(board, word, new_path + [spot], paths_list, max_list, new_i, bool)


def find_length_n_words(n, board, words):
    """ this function finds all n length word paths and returns a list of these paths"""
    paths_list = []
    for word in words:
        if len(word) == n:
            spot_lst = find_spot(board, word, 0)  # all spots in board containing the first letter\letters
            for spot in spot_lst:
                find_length_n_words_helper(board, word, [spot], paths_list, [],
                                           len(coords_to_word(board_coords(board), [spot])), False)
    return paths_list


def max_length_list(paths):
    """Return the list from the list of lists which length is the highest"""
    current_len = 0
    current = paths[0]
    for path in paths[1:]:
        current_len = len(current)
        if len(path) > current_len:
            current = path
    return current


def max_score_paths(board, words):
    """ this function finds the paths for words from the word list that give the highest score
    :param board: game board of letters
    :param words: list of words
    :return: list of possible paths on board
    """
    max_scr_paths = []
    for word in list(set(words)):
        spot_lst = find_spot(board, word, 0)  # all spots in board containing the first letter\letters
        for spot in spot_lst:
            paths = []
            old_list = max_scr_paths[:]
            find_length_n_words_helper(board, word, [spot], paths, max_scr_paths,
                                       len(coords_to_word(board_coords(board), [spot])), True)
            if old_list == max_scr_paths:  # max_scr_paths did not change, no list in length of len(word)
                if paths:  # paths is not empty
                    max_scr_paths.append(max_length_list(paths))
    return max_scr_paths
