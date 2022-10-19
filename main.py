from tkinter import *
from tkinter.ttk import *
from questions import Question as Q

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
test_subject = "Тест по информатике 9 класс"
number = 1
score = 0


def create_frame():
    global ask_frame, number
    for number in range(number, len(Q.question_dict) + 1):
        ask_frame = LabelFrame(main_frame, text=f'Вопрос {number} из {len(Q.question_dict)}')
        ask_frame.pack()
        ask_text = Q.question_list[number - 1]
        ask = Label(ask_frame, wraplength=550, text=ask_text)
        ask.pack(pady=10, padx=10, anchor='w', )
        radio_value = IntVar()
        radio_value.set(1)

        for i in range(1, 4):
            text = Q.get_answer_text(number, i)
            if len(text) > 70:
                text = word_wrap(text, 70)
            Radiobutton(ask_frame, text=text, variable=radio_value, value=i).pack(anchor='w', padx=5)

        button = Button(ask_frame, text='Далее', width=93, command=lambda: next_frame(radio_value.get()))
        button.pack(pady=10)

        number += 1
        break


def result():
    global result_frame
    ask_frame.destroy()
    result_frame = LabelFrame(main_frame)
    result_frame.pack()
    Label(result_frame, text=f'Ваш результат: {score} правильных ответов из {len(Q.question_dict)}',
          font=('Arial', 16), anchor='c').pack(pady=30, padx=50)
    Label(result_frame, text=f'Оценка: {round(score / len(Q.question_dict) * 5)}',
          font=('Arial', 16), anchor='c').pack(pady=10, padx=50)
    Button(result_frame, text="Пройти заново", width=93, command=lambda: restart()).pack(pady=10)


def restart():
    global result_frame, score, number, ask_frame
    result_frame.destroy()
    ask_frame.destroy()
    score = 0
    number = 1
    create_frame()


def word_wrap(text, slice_index):
    out_value = True
    index = slice_index
    new_text = ''
    while out_value:
        try:
            if text[index] == ' ':
                new_text = text[0:index] + '\n' + text[index + 1:]
                out_value = False
            else:
                index += 1
        except IndexError:
            return text
    return new_text


def check_answer(answer_number):
    global score
    if Q.get_answer_value(number - 1, answer_number):
        score += 1


def next_frame(checked_answer):
    check_answer(checked_answer)
    if number == len(Q.question_dict) + 1:
        result()
    else:
        ask_frame.destroy()
        create_frame()


win = Tk()
win.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}+600+250')
win.resizable(False, False)
main_frame = Frame(win, width=WINDOW_WIDTH - 15, height=WINDOW_HEIGHT - 15)
main_frame.pack(padx=10, pady=10, )
main_label = Label(main_frame, text=test_subject, font=("Arial", 14))
main_label.pack()
create_frame()
Q.show_test()
win.mainloop()
