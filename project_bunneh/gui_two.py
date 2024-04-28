import tkinter as tk

def gui_two():
    g2 = tk.Tk()
    g2.title("Second Gui Page")
    g2.geometry("400x800")

    # Define custom colors
    background_color = "#271454"
    button_color = "#BD54AA"
    text_color = "#FFFFFF"

    # Configure the mw window background color
    g2.configure(bg=background_color)

    # Create a label with custom text color
    label = tk.Label(g2, text="Custom Tkinter Example", fg=text_color, bg=background_color)
    label.pack(pady=10)

    # Create a button with custom background color
    button = tk.Button(g2, text="Click Me", bg=button_color)
    button.pack(pady=10)

    g2.mainloop()