from tkinter import *
from tkinter.ttk import *

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
test_subject = "Тест по информатике 9 класс"


class Question:
    question_list = {}

    def create_ask(self, ask):
        self.ask = str(ask)
        self.question_list[ask] = ()

    def create_answer(self, answer, validity=False):
        self.answer = answer
        self.validity = validity
        self.para = [self.answer, self.validity]
        self.question_list[self.ask] += (self.para,)

    def show_test_block(self):
        print(f'Вопрос: {self.ask}')
        print("Ответы: ")
        for el in self.question_list[self.ask]:
            print(el)


def create_main_window():
    win = Tk()
    win.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}+600+250')
    win.resizable(False, False)
    main_frame = Frame(win, width=WINDOW_WIDTH - 15, height=WINDOW_HEIGHT - 15)
    main_frame.pack(padx=10, pady=10, )
    main_label = Label(main_frame, text=test_subject, font=("Arial", 14))
    main_label.pack()
    # create_frame()

    win.mainloop()


def create_frame():
    pass


create_main_window()
