# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 15:04:35 2015

@author: Nick

CLI User Interface for Tic-Tac_Toe game.

Use as the main program, no reusable functions
"""

import oxo_logic

menu = ["Start New Game",
        "Resume Saved Game",
        "Display Help",
        "Quit"]

def get_menu_choice(a_menu):
    """
    get_menu_choice(a_menu) -> int

    takes a list of strings as input,
    displays as a nubered menu and loops until user selects a valid number    
    """
    
    if not a_menu:
        raise ValueError("No menu content")
    
    while True:
        print("\n\n")
        for ii, item in enumerate(a_menu, start=1):
            print(ii, "\t", item)
        try:
            choice = int(input("\nChoose a menu option: "))
            if 1 <= choice <= len(a_menu):
                return choice
            else:
                print ("Choose a number between 1 and ", len(a_menu))

        except ValueError:
            print("Choose the number of a menu option")

def start_game():
    return oxo_logic.new_game()
    
def resume_game():
    return oxo_logic.restore_game()
    
def display_help():
    print("""
    Start new game: starts a new game of tic-tac-toe.
    
    Resume saved game: restores the last saved game and commences play
    
    Display help: shows this page
    
    Quit: quits the application
    """)
    
def quit():
    print("Goodbye...")
    raise SystemExit

def execute_choice(choice):
    """
    execute_choice(int) -> None

    Execute whichever option the user selected.
    If the choice produces a valid game, then play the game until it
    completes.    
    """
    dispatch =[start_game, resume_game, display_help, quit]
    game = dispatch[choice-1]()
    if game:
        # play game here
        pass

def print_game(game):
    display = """
    1 | 2 | 3 {} | {} | {}
    _________ ____________
    4 | 5 | 6 {} | {} | {}
    _________ ____________
    7 | 8 | 9 {} | {} | {}
    """
    print(display.format(*game))

def play_game(game):
    result = ""
    while not result:
        print_game(game)
        choice = raw_input("Cell[1-9 or q to quit]: ")

        if choice.lower()[0] == "q":
            save = raw_input("Save game before quitting?[y/n] ")
            if save.lower()[0] == "y":
                oxo_logic.save_game(game)
            quit()
        else:                
            try:
                cell = int(choice)-1
                if not (0 <= cell <= 8): #check range
                    raise ValueError
            except ValueError:
                print("Choose a number between 1 and 9 or 'q' to quit ")
                continue

            try:
                result = oxo_logic.user_move(game, cell)
            except ValueError:
                print("Choose an empty cell ")
                continue
            
            if not result:
                result = oxo_logic.computer_move(game)
                if not result:
                    continue
                elif result == "D":
                    print_game(game)
                    print("Its a draw")
            else:
                print_game(game)
                print("Winner is ", result, "\n")
        

def main():
    while True:
        choice = get_menu_choice(menu)
        execute_choice(choice)
    
if __name__ == "__main__":
    game = start_game()
    play_game(game)