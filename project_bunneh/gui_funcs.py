import tkinter as tk



def open_main_window():
    mw = tk.Tk()
    mw.title("Project Bunneh: Way of the Rabbit's Foot")
    mw.geometry("800x800")



    # Define custom colors
    background_color = "#336699"
    button_color = "#FFA500"
    text_color = "#FFFFFF"

    # Configure the mw window background color
    mw.configure(bg=background_color)

    # Create a label with custom text color
    label = tk.Label(mw, text="Custom Tkinter Example", fg=text_color, bg=background_color)
    label.pack(pady=10)

    # Create a button with custom background color
    button = tk.Button(mw, text="Click Me", bg=button_color)
    button.pack(pady=10)








    mw.mainloop()