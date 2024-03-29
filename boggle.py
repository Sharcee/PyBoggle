"""
Name: Simon Aizpurua
FSUID: saa13b
Course: CIS4930
Date: 1/29/17
"""
import random
import enchant

def DFS(word, board):
    """

    :param word: Word to search for in a Boggle Board
    :param board: Board generated by 16 dice
    :return: bool
    """
    start = [(x,y) for x in range(4) for y in range(4) if board[x+y*4] == word[0]]
    for (x,y) in start:
        if search_adj(word, 1, board, x, y, [(x, y)]):
            return True
    return False

def search_adj(word, pos, board, x, y, vis):
    """

    :param word: word we're looking for
    :param pos: position in the word to search for
    :param board: the generated board
    :param x: column
    :param y: row
    :param vis: node already visited
    :return: bool
    """
    if pos >= len(word):
        return True
    for dx in [-1, 0, 1]: # check row
        for dy in [-1, 0, 1]: #check col
            if 0 <= dx + x < 4 and 0 <= dy + y < 4:
                if board[(dx + x) + (dy + y) * 4] == word[pos]:
                    if ((dx + x), (dy + y)) not in vis:
                        if search_adj(word, pos+1, board, dx+x, dy+y, vis+[(dx+x, dy+y)]):
                            return True
    return False

def wordChecker():
    # First checking if the word is valid to be scored
    if len(word) >= 3:
        if dict.check(word): # checks if the word is even a word
            length = len(word)
            if length == 3 or length == 4: # checking how long the word is to score for points
                points = 1
            elif length == 5:
                points = 2
            elif length == 6:
                points = 3
            elif length == 7:
                points = 5
            elif length >= 8:
                points = 11
            print("Valid word! Worth: %s points" %points)
            scoredWords.append(word)
            return points
        else: # not an actual word
            print("Invalid Word.")
            points = 0
            return points
    else: # word is not valid
        print("Please input a word longer then 2 characters.")
        points = 0
        return points


def generateBoard():
    # Defines a list for the board, and then the choice list
    # using a 2d list to define all possible letters on all sides of the dice
    board = []
    dice = [
                ['A', 'E', 'A', 'N', 'E', 'G'],
                ['A', 'H', 'S', 'P', 'C', 'O'],
                ['A', 'S', 'P', 'F', 'F', 'K'],
                ['O', 'B', 'J', 'O', 'A', 'B'],
                ['I', 'O', 'T', 'M', 'U', 'C'],
                ['R', 'Y', 'V', 'D', 'E', 'L'],
                ['L', 'R', 'E', 'I', 'X', 'D'],
                ['E', 'I', 'U', 'N', 'E', 'S'],
                ['W', 'N', 'G', 'E', 'E', 'H'],
                ['L', 'N', 'H', 'N', 'R', 'Z'],
                ['T', 'S', 'T', 'I', 'Y', 'D'],
                ['O', 'W', 'T', 'O', 'A', 'T'],
                ['E', 'R', 'T', 'T', 'Y', 'L'],
                ['T', 'O', 'E', 'S', 'S', 'S'],
                ['T', 'E', 'R', 'W', 'H', 'V'],
                ['N', 'U', 'I', 'H', 'M', 'Qu']
                ]
    for i in range (0,16,1): # generating a roll for each die to place on the board
        choice = random.choice(dice[i])
        board.append(choice)
    return board

def printBoard():
    """
    Prints the generated board for the player to see
    :return: void
    """
    print (" %s %s %s %s " %(board [0], board [1], board [2], board [3]))
    print (" %s %s %s %s " %(board [4], board [5], board [6], board [7]))
    print (" %s %s %s %s " %(board [8], board [9], board [10], board [11]))
    print (" %s %s %s %s " %(board [12], board [13], board [14], board [15]))


if __name__ == '__main__':
    dict = enchant.Dict("en_US") # getting the dictionary ready to use
    board = generateBoard() # assigns "board" to the generated board
    printBoard() # shows the board to the player

    totalPoints = 0 # sets points to 0
    scoredWords = [] # list to store all scored words so they cannot be used again
    while True: # infinite loop for now to play the game
        word = input("Input the word you would like to check for - type only X to exit\n")
        word.upper() # changes the word to all uppercase, allows for easier use in the program
        if word == "X" or word == "x": # exit function, also shows total points
            print("You got a total of: %d points!" %totalPoints)
            exit(0)
        else: # plays the game
            if DFS(word.upper(), board):
                if any(word in s for s in scoredWords):
                    print("Word has already been scored! Try another one.")
                else:
                    points = wordChecker()
                    totalPoints = points + totalPoints
            else:
                print("Word: %s was not found on the grid." %word)