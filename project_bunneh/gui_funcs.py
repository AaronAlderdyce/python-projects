import os
import customtkinter as ctk
# from race import Race
# from job import Job
# from stats import Stats, DerivedStats
# from skills import Skills

def new_char_window():
    char_window = ctk.CTk()
    char_window.title("Character Creation")
    char_window.geometry("800x800")

    # Frame for Char Creation
    char_frame = ctk.CTkFrame(char_window)
    char_frame.pack(expand=True,fill="both")

    # Add buttons and widgets for char creation
    label = ctk.CTkLabel(char_frame,text="Create Your Character:")
    label.pack()

    button1 = ctk.CTkButton(char_window, text="Gender",)
    button1.pack(pady=5,padx=5)
    button2 = ctk.CTkButton(char_window, text="Race",)
    button2.pack(pady=5,padx=5)
    button3 = ctk.CTkButton(char_window, text="Job",)
    button3.pack(pady=5,padx=5)
    button4 = ctk.CTkButton(char_window, text="Stats",)
    button4.pack(pady=5,padx=5)
    button5 = ctk.CTkButton(char_window, text="Skills",)
    button5.pack(pady=5,padx=5)
    button6 = ctk.CTkButton(char_window, text="Back", command=char_window.destroy)
    button6.pack(pady=5,padx=5)

    # Keeping window open
    char_window.mainloop()