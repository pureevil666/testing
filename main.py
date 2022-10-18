from tkinter import *
from tkinter.ttk import *
from questions import *
from questions import Question as Q

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
test_subject = "Тест по информатике 9 класс"
Q.create_questions_list()


def create_frame():
    for number in range(1, len(Q.question_dict) + 1):
        ask_frame = LabelFrame(main_frame, text=f'Вопрос {number} из {len(Q.question_dict)}')
        ask_frame.pack()
        ask = Label(ask_frame, text=Q.question_list[number - 1])
        ask.pack(pady=10, padx=10)

        count = 0
        radio_value = IntVar()
        radio_value.set(0)

        for answer in Q.question_dict[Q.question_list[number - 1]]:
            Radiobutton(ask_frame, text=answer[0], variable=radio_value, value=count).pack(anchor='w', padx=10)
            count += 1

        break


win = Tk()
win.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}+600+250')
win.resizable(False, False)
main_frame = Frame(win, width=WINDOW_WIDTH - 15, height=WINDOW_HEIGHT - 15)
main_frame.pack(padx=10, pady=10, )
main_label = Label(main_frame, text=test_subject, font=("Arial", 14))
main_label.pack()
create_frame()

Q.show_question_list()
win.mainloop()
