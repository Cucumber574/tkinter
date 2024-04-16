import tkinter

'''
вопрос:  Label
Ответы: Button
Счет: кол-во правильных ответов
'''

question = [
    {
        'текст вопроса': 'Какой из этих типов данных измеяются',
        'варианты ответов': ['Tuple', 'list', 'str', 'int'], 
        'индекс правильного ответа': 1
    },
    {
        'текст вопроса': 'Какой оператор умножает числа',
        'варианты ответов': ['+', '**', 'X', '*'], 
        'индекс правильного ответа': 3
    }
]

class App:
    '''Приложение'''
    def __init__(self) -> None:
        self.window = tkinter.Tk()
        self.window.option_add('*Font', ('Consolas', 20))
        self.width = self.window.winfo_screenwidth()
        self.height = self.window.winfo_screenheight()
        self.window.geometry(f'{self.width}x{self.height}')
        self.make_widgets()
        self.positon_widget()
        self.start()
        self.window.mainloop()

    def make_widgets(self) -> None:
        '''Создает экземпляра виджетов'''
        self.label_question_text = tkinter.Label(self.window)
        self.label_answer_text_1 = tkinter.Label(self.window)
        self.label_answer_text_2 = tkinter.Label(self.window)
        self.label_answer_text_3 = tkinter.Label(self.window)
        self.label_answer_text_4 = tkinter.Label(self.window)
        self.button_answer_1 = tkinter.Button(
            self.window, text='1', command=lambda: self.on_click(1)
            )
        self.button_answer_2 = tkinter.Button(
            self.window, text='2', command=lambda: self.on_click(2)
            )
        self.button_answer_3 = tkinter.Button(
            self.window, text='3', command=lambda: self.on_click(3)
            )
        self.button_answer_4 = tkinter.Button(
            self.window, text='4', command=lambda: self.on_click(4)
            )

    def positon_widget(self) -> None:
        '''Позиционрует виджеты в окне'''
        self.label_question_text.pack()
        self.label_answer_text_1.pack()
        self.label_answer_text_2.pack()
        self.label_answer_text_3.pack()
        self.label_answer_text_4.pack()
        self.button_answer_1.pack()
        self.button_answer_2.pack()
        self.button_answer_3.pack()
        self.button_answer_4.pack()

    def start(self) -> None:
        self.question_number = 0
        self.label_question_text['text'] = question[self.question_number][
            'текст вопроса'
            ]
        self.button_answer_1.pack['text'] = '1. ' + question[
            self.question_number]['варианты ответов'][0]
        self.button_answer_2.pack['text'] = '2. ' + question[
            self.question_number]['варианты ответов'][1]
        self.button_answer_3.pack['text'] = '3. ' + question[
            self.question_number]['варианты ответов'][2]
        self.button_answer_4.pack['text'] = '4. ' + question[
            self.question_number]['варианты ответов'][3]

    def on_click(self, button_number: int) -> None:
        print('нажата', button_number)
        #ТУДУ: Сравнить номер кнопки с индексом правильного ответа

App()