import customtkinter as ctk
from gui_funcs import new_char_window


def draw_window():
    # Main window attributes
    window = ctk.CTk()
    window.title("Project Bunneh")
    window.geometry("400x800")


    # Frame for Main Menu
    main_menu_frame = ctk.CTkFrame(window)
    main_menu_frame.pack(expand=True,fill="both")

    label = ctk.CTkLabel(main_menu_frame,text="""Press New Game to start a fresh new game.\nPress Load Game to continue.\nPress Tutorial if you need help with terms.\nPress Credits if you want to see who worked on this project.\nPress Quit Game to exit the game.""")
    label.pack(expand=True,fill="both",)

    button1 = ctk.CTkButton(main_menu_frame, text="New Game",command=new_char_window,)
    button1.pack(expand=True,fill="both", pady=5,padx=5)
    button2 = ctk.CTkButton(main_menu_frame, text="Load Game",)
    button2.pack(expand=True,fill="both", pady=5,padx=5)
    button3 = ctk.CTkButton(main_menu_frame, text="Tutorial",)
    button3.pack(expand=True,fill="both", pady=5,padx=5)
    button4 = ctk.CTkButton(main_menu_frame, text="Credits",)
    button4.pack(expand=True,fill="both", pady=5,padx=5)
    button5 = ctk.CTkButton(main_menu_frame, text="Quit Game",command=window.destroy,)
    button5.pack(expand=True,fill="both", pady=5,padx=5)

    # Keeping window open
    window.mainloop()




draw_window()