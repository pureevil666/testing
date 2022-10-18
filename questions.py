class Question:
    question_dict = {}
    question_list = []

    def create_ask(self, ask):
        self.ask = str(ask)
        self.question_dict[ask] = ()

    def create_answer(self, answer, validity=False):
        self.answer = answer
        self.validity = validity
        self.para = [self.answer, self.validity]
        self.question_dict[self.ask] += (self.para,)

    def show_test_block(self):
        print(f'Вопрос: {self.ask}')
        print("Ответы: ")
        for el in self.question_dict[self.ask]:
            print(el)

    @staticmethod
    def show_question_list():
        for el in Question.question_dict:
            print(f"\nВопрос: {el}")
            for answer in Question.question_dict[el]:
                print(f"    {answer[0]} - {answer[1]} ")

    @staticmethod
    def create_questions_list():
        for key in Question.question_dict:
            Question.question_list.append(key)


question1 = Question()
question1.create_ask("Как называется группа файлов, которая хранится отдельной группой и имеет собственное имя ?")
question1.create_answer("Байт")
question1.create_answer("Каталог", True)
question1.create_answer("Диск")

question2 = Question()
question2.create_ask("Архитектура компьютера — это:")
question2.create_answer("Техническое описание деталей устройств компьютера")
question2.create_answer("Описание программного обеспечения для работы компьютера")
question2.create_answer("Описание устройства и принципов работы компьютера, достаточное для понимания пользователя",
                        True)

question3 = Question()
question3.create_ask("Внешняя память необходима для")
question3.create_answer("Для хранения часто изменяющейся информации в процессе решения задачи")
question3.create_answer("Для долговременного хранения информации после выключения компьютера", True)
question3.create_answer("Для постоянного хранения информации о работе компьютера")

question4 = Question()
question4.create_ask("Файлом называется")
question4.create_answer("Программа на языке программирования для решения задачи")
question4.create_answer("Поименованная область на диске или другом машинном носителе", True)
question4.create_answer("Набор данных для решения задачи")

question5 = Question()
question5.create_ask("Алгоритм — это")
question5.create_answer("Некоторые истинные высказывания, которые должны "
                        "быть направлены на достижение поставленной цели")
question5.create_answer("Отражение предметного мира с помощью знаков и сигналов, "
                        "предназначенное для конкретного исполнителя")
question5.create_answer("Понятное и точное предписание исполнителю совершить последовательность действий, "
                        "направленных на решение поставленной задачи или цели", True)

question6 = Question()
question6.create_ask("Какие программные продукты можно использовать для выполнения следующих типовых файловых операций "
                     "(создания папок, копирования файлов и папок; перемещения файлов и папок; удаления файлов)")
question6.create_answer("Проводник", True)
question6.create_answer("WinRar")
question6.create_answer("WinZip")

question7 = Question()
question7.create_ask("Полное имя файла состоит из")
question7.create_answer("Собственного имени и расширения")
question7.create_answer("Имени логического диска, пути каталогов, имени файла", True)
question7.create_answer("Имени каталога и имени файл")

question8 = Question()
question8.create_ask("Буфер обмена служит для")
question8.create_answer("Хранения информации, которая подлежит удалению")
question8.create_answer("Перемещения информации")
question8.create_answer("Хранения информации об объектах, которые подлежат перемещению или копированию", True)

question9 = Question()
question9.create_ask("Оперативная память служит для")
question9.create_answer("Постоянного хранения программ и данных")
question9.create_answer("Временного хранения программ и данных", True)
question9.create_answer("Для записи программ и данных на носители")

question10 = Question()
question10.create_ask("Информационная система")
question10.create_answer("Взаимосвязанная совокупность средств, методов и персонала, "
                         "используемых для хранения, обработки и выдачи информации в интересах поставленной цели", True)
question10.create_answer("Совокупности единой системы классификации и кодирования информации, унифицированных "
                         "систем документации, схем информационных потоков предприятия")
question10.create_answer("Комплекса технических средств, ПК, устройства сбора, накопления, обработки, "
                         "передачи и вывода информации, материалов и т. д")

question11 = Question()
question11.create_ask("Информационная технология – это")
question11.create_answer("Процесс обработки и передачи информации для получения информационного продукта")
question11.create_answer("Процесс, использующий совокупность средств и методов сбора, обработки и "
                         "передачи первичной информации для получения информационного продукта", True)
question11.create_answer("Процесс принятия решения об использовании информации для получения информационного продукта")

question12 = Question()
question12.create_ask("Что такое операционная система (ОС)?")
question12.create_answer("Программа, обеспечивающая сервис работы при настройке или проверке аппаратной части ПК")
question12.create_answer("Программный комплекс, являющийся посредником между ПК и пользователем", True)
question12.create_answer("Программный комплекс для решения конкретной прикладной задачи")
