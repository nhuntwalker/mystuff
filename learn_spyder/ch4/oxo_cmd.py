# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 16:14:19 2015

@author: Nick
"""

import cmd, oxo_ui, oxo_logic
import argparse as ap

class Oxo_cmd(cmd.Cmd):
    intro = "Enter a command: new, resume, quit. Type 'help' or '?' for help"
    prompt = "(oxo) "
    game = ""
    
    def do_new(self, arg):
        print("Starting new game")
        self.game = oxo_logic.new_game()
        oxo_ui.play_game(self.game)
    
    def do_resume(self, arg):
        print("Restoring previous game")
        self.game = oxo_logic.restore_game()
        oxo_ui.play_game(self.game)
        
    def do_quit(self, arg):
        print("Goodbye...")
        raise SystemExit
        
def main():
    p = ap.ArgumentParser(description="Play a game of Tic-Tac-Toe")
    grp = p.add_mutually_exclusive_group()
    grp.add_argument("-n", "--new", action="store_true", help="start new game")
    grp.add_argument("-r","--res",action="store_true",help="restore old game")
    args = p.parse_args()
    
    if args.new:
        execute_choice(1)
    elif args.res:
        execute_choice(2)
    else:
        while True:
            choice = get_menu_choice(menu)
            execute_choice(choice)
    
    game = Oxo_cmd().cmdloop()

if __name__ == "__main__":
    main()