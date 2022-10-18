from tkinter import *
from tkinter.ttk import *

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
test_subject = "Тест по информатике 9 класс"



def create_main_window():
    win = Tk()
    win.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}+600+250')
    win.resizable(False, False)
    main_frame = Frame(win, width=WINDOW_WIDTH-15, height=WINDOW_HEIGHT-15)
    main_frame.pack(padx=10, pady=10,)
    main_label = Label(main_frame, text=test_subject, font=("Arial", 14))
    main_label.pack()
    # create_frame()

    win.mainloop()


def create_frame():
    pass

create_main_window()

