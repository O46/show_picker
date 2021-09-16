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
        # self.shows = ["Aggretsuko", "Bobobo", "The Boys S2", "Mob Psycho 100 2"]
        return open(os.path.join(location, target_file)).read().splitlines()
    except IOError:
        print("File \"" + str(os.path.join(location, target_file)) + "\" not found.")
        sys.exit(0)


class ShowPicker:
    def __init__(self):
        self.shows = load_file("resources", "shows.txt")
        self.colors = load_file("resources", "colors.txt")

        '''try:
            self.colors = ["Teal", "Burgandy",  "Glaucous", "Orange", "Cosmic Latte", "Amaranth", "Chartreuse", "Coquelicot", "Celadon"]
            self.colors = open(os.path.join("resources", "colors.txt")).readlines()
        except:
            print("File \"" + str(os.path.join("resources", "colors.txt")) + "\" not found.")
            sys.exit(0)'''


    def runner(self):
        while True:
            random.shuffle(self.shows)
            random.shuffle(self.colors)
            picked = input("Pick a color: \n\t" + "\n\t".join(self.colors[:len(self.shows)]) + "\n").strip().capitalize()
            if picked in self.colors[:len(self.shows)]:
                print("Your show is: " + self.shows[self.colors.index(picked)] + "\n" * 5)
            else:
                input("Your selection, " + picked + ", was not found in the color list. Press enter to continue." + "\n" * 5)


if __name__ == "__main__":
    # sp_cls = show_picker()
    ShowPicker().runner()

# Pick a color:
#	Glaucous
#	Amaranth
#	Chartreuse
#	Cosmic Latte
