import customtkinter as ctk

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

    # Keeping window open
    char_window.mainloop()