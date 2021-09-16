# simple script for me 'n amanda to pick / track our shows
# TODO:
#   add menu to pick what we want to do
#   add DB-esque functionality, allow adding to shows / colors via command
#   add episode tracking
#   add distinction between movies / shows
#   add pick from either


import random
import os
import sys


def load_file(location, target_file):
    try:
        return open(os.path.join(location, target_file)).read().splitlines()
    except IOError:
        print("File \"" + str(os.path.join(location, target_file)) + "\" not found.")
        sys.exit(0)


class ShowPicker:
    def __init__(self):
        self.shows = load_file("resources", "shows.txt")
        self.colors = load_file("resources", "colors.txt")

    def runner(self):
        while True:
            random.shuffle(self.shows)
            random.shuffle(self.colors)
            picked = input("Pick a color: \n\t" + "\n\t".join(self.colors[:len(self.shows)]) + "\n").strip().capitalize()
            print(picked)
            if picked in self.colors[:len(self.shows)]:
                input("Your show is " + self.shows[self.colors.index(picked)] + ".\nPress enter to continue.")
            elif picked == "Exit":
                break
            else:
                input("Your selection, " + picked + ", was not found in the color list.\nPress enter to continue.")
            print("\n" * 100)

    def menu(self):
        while True:
            menu_choice = input("[1]\tPick a show\n[2]\tAdd a show\n[3]\tDelete a show\n[4]\tExit\n").strip()
            try:
                menu_choice = int(menu_choice)
                print(menu_choice)
                if menu_choice == 1:
                    self.runner()
                elif menu_choice == 2:
                    print("Not implemented yet.")
                elif menu_choice == 3:
                    print("Not implemented yet.")
                elif menu_choice == 4:
                    sys.exit(0)
                else:
                    print("Please choose one of the listed options.")
            except SystemExit:
                sys.exit(0)


if __name__ == "__main__":
    ShowPicker().menu()
