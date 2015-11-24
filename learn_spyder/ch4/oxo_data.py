# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 13:50:51 2015

@author: Nick

oxo_data is the data module for a tic-tac-toe (or OXO) game.

It saves and restores a game board. The functions are:
    save_game(game) -> None
    restore_game() -> game

Note that no limits are placed on the size of the data.

The game implementation is responsible for validating all data in and out.
"""

import os.path
game_file = ".oxogame.dat"

def __getPath():
    """getPath -> string
    Returns a valid path for data file.
    Tries to use the users home folder, defaults to cwd    
    """
    
    try:
        game_path = os.environ["HOMEPATH"] or os.environ["HOME"]
        if not os.path.exists(game_path):
            game_path = os.getcwd()
            
    except (KeyError, TypeError):
        game_path = os.getcwd()
        return game_path
        
def save_game(game):
    """save_game(game)->None
    
    saves a game object in the data file in the user's home folder.
    No checking is done on the input, which is expected to be a list of
    characters
    """
    
    path = os.path.join(__getPath(), game_file)
    with open(path, 'w') as gf:
        gamestr = ''.join(game)
        gf.write(gamestr)
        
def restore_game():
    """restore_game() -> game
    
    Restores a game from the data file.
    The game object is a list of characters    
    """
    
    path = os.path.join(__getPath(), game_file)
    with open(path) as gf:
        gamestr = gf.read()
        return list(gamestr)

def test():
    print("Path = ", __getPath())
    save_game(list("XO XO OX"))
    print(restore_game())

if __name__ == "__main__": 
    test()
    
