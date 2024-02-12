import customtkinter as ctk


def draw_window():
    # Main window attributes
    window = ctk.CTk()
    window.title("Project Bunneh")
    window.geometry("400x800")

    # Frame for Main Menu
    main_menu_frame = ctk.CTkFrame(window)
    main_menu_frame.pack(expand=True,fill="both")

    button1 = ctk.CTkButton(window, text="New Game",)
    button1.pack(expand=True,fill="both", pady=1)
    button2 = ctk.CTkButton(window, text="Load Game",)
    button2.pack(expand=True,fill="both", pady=1)
    button3 = ctk.CTkButton(window, text="Tutorial",)
    button3.pack(expand=True,fill="both", pady=1)
    button4 = ctk.CTkButton(window, text="Credits",)
    button4.pack(expand=True,fill="both", pady=1)
    button5 = ctk.CTkButton(window, text="Quit Game",)
    button5.pack(expand=True,fill="both", pady=1)

















    # Keeping window open
    window.mainloop()




draw_window()