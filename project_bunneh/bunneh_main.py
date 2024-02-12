import os, random
# from race import Race
# from job import Job
# from stats import Stats, DerivedStats
# from skills import Skills
import customtkinter as ctk
from bunneh_GUI import gui_main

def draw_menu():
    print("&##############################################################################&")

gender = ["male", "female"]
inventory = []
equipment = []
coords = []

# draw_menu()
# user = input("Hello, adventurer. You must be quite confused at where you are right now. Well, that doesn't matter right now. Tell me your name:\n > ")

# gender_user = input(f"Ah, well {user}, my eyes fail to recognize some of your most basic features... are you a {gender[0]} or a {gender[1]}??\n > ")

# if gender_user == gender[0]:
#     print(f"Ah, a {gender[0]}. I can see it now. Thank you for humoring an old fart like myself.")
# else:
#     print(f"Ah, a {gender[1]}. I can see it now. Thank you for humoring an old fart like myself.")

draw_window()