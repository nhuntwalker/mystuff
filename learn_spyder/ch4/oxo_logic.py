# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 14:09:38 2015

@author: Nick

This is the main logic for a tic-tac-toe game.

It is not optimized for a quality game, it simply generates random moves
and checks the results of a move for a winning line.

Exposed functions are:
    new_game()
    save_game()
    restore_game()
    user_move()
    computer_move()
"""

import os, random
import oxo_data
def new_game():
    """ Returns a new list of nine spaces"""
    return list(" "*9)

def save_game(game):
    """ Saves the current state of the game"""
    oxo_data.save_game(game)
    
def restore_game():
    """ 
    Tries to restore the game. If the game cannot be restored,
    it returns a blank gameboard
    """
    try:
        game = oxo_data.restore_game()
        if len(game) == 9:
            return game
        else:
            return new_game()
    except IOError:
        return new_game()
        
def _generate_move(game):
    """
    Generates a random move from the computer onto an empty space
    """
    options = [ii for ii in range(len(game)) if game[ii] == " "]
    return random.choice(options)

def _is_winning_move(game):
    """
    
    """
    wins = ((0,1,2),(3,4,5),(6,7,8),
            (0,4,8),(2,4,6),(0,3,6),
            (1,4,7),(2,5,8))    
    
    for a,b,c in wins:
        chars = game[a] + game[b] + game[c]
        if (chars == "XXX") or (chars=="OOO"):
            return True
            
    return False

def user_move(game, cell):
    if game[cell] != ' ':
        raise ValueError("Invalid Cell")
    else:
        game[cell] = "X"
    
    if _is_winning_move(game):
        return "X"
    else:
        return ""
        
def computer_move(game):
    cell = _generate_move(game)
    if cell == -1:
        return "D"
    game[cell] = "O"
    
    if _is_winning_move(game):
        return "O"
    else:
        return ""
        
def test():
    result = ""
    game = new_game() # 9 empty cells
    
    while not result:
        print(game)
        try:
            result = user_move(game, _generate_move(game))
        except ValueError:
            print("Oops, that shouldn't happen")
        if not result:
            result = computer_move(game)
            if not result:
                continue
        
        elif result == "D":
            print("it's a draw")
        
    else:
        print("Winner is: ", result)
        print(game)

if __name__ == "__main__":
    test()