from tkinter import *
from tkinter.ttk import *
from questions import Question as Q

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
test_subject = "Тест по информатике 9 класс"
number = 1


def create_frame():
    global ask_frame, number
    for number in range(number, len(Q.question_dict) + 1):
        ask_frame = LabelFrame(main_frame, text=f'Вопрос {number} из {len(Q.question_dict)}')
        ask_frame.pack()
        ask = Label(ask_frame, text=Q.question_list[number - 1])
        ask.pack(pady=10, padx=10, anchor='w', )

        count = 0
        radio_value = IntVar()
        radio_value.set(0)

        for answer in Q.question_dict[Q.question_list[number - 1]]:
            text = answer[0]
            slice_index = 70
            if len(text) >= slice_index:
                text = word_wrap(text, slice_index)
            Radiobutton(ask_frame, text=text, variable=radio_value, value=count).pack(anchor='w', padx=10)
            count += 1
        button = Button(ask_frame, text='Далее', width=93, command=next_frame)
        button.pack()
        number += 1
        break


def word_wrap(text, slice_index):
    out_value = True
    index = slice_index
    new_text = ''
    print(text)
    print(index)
    while out_value:
        print(index)
        try:
            if text[index] == ' ':
                new_text = text[0:index]
                new_text += '\n' + text[index+1:]
                out_value = False
            else:
                index += 1
        except IndexError:
            return text
    return new_text


def next_frame():
    ask_frame.destroy()
    create_frame()


win = Tk()
win.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}+600+250')
win.resizable(False, False)
main_frame = Frame(win, width=WINDOW_WIDTH - 15, height=WINDOW_HEIGHT - 15)
main_frame.pack(padx=10, pady=10, )
main_label = Label(main_frame, text=test_subject, font=("Arial", 14))
main_label.pack()
ask_frame = LabelFrame(main_frame)
create_frame()

# Q.show_question_list()
# Q.show_test()
win.mainloop()
