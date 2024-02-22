from tkinter import *

from ..calc import NUM_SYS, MATH_SIGNS, MATH_FUNCTIONS, MATH_ACTIONS, sqrt_sign, calculate


BUTTONS = [  # основные кнопки
    "(", ")", "C", "Del",
    "%", "^", sqrt_sign, "/",
    "7", "8", "9", "*",
    "4", "5", "6", "-",
    "1", "2", "3", "+",
    "+-", '0', '.', '=',
]

EXP_BUTTONS = [  # дополнительные клавиши
    'log', 'ln',
    '!', 'abs',
    'dec', 'bin',
    'oct', 'ter',
    'qua', 'fiv',
    'six', 'sep',
]


class Calculator(Frame):
    """
    Графическое представление калькулятора.
    """
    def __init__(self, master: Tk):
        """
        Конструктор класса.
        :param master: родительское окно
        """
        super(Calculator, self).__init__(master)
        # Объекты
        self.entry = None
        self.f_lbl = None
        self.res_lbl = None
        self.buttons = []
        self.exp_buttons = []
        self.mode = 'basic'

        self.build()

    def build(self):
        """
        Постройка интерфейса калькулятора
        """
        row = 0
        column = 0

        # Создание виджетов ввода-вывода
        self.res_lbl = Label(self, anchor=S)
        self.entry = Entry(self,
                           justify=RIGHT,
                           borderwidth=0,
                           state='normal',
                           readonlybackground="#000",
                           foreground="#fff",
                           highlightthickness=0,
                           )

        # Обработка событий клавиатуры
        self.entry.bind('<Delete>', lambda e: self.action('C'))
        self.entry.bind('<Return>', lambda e: self.action('='))
        self.entry.bind('<KeyRelease>', lambda _: self.update())
        self.entry.focus_set()

        # Размещение полей ввода-вывода в окне
        self.entry.grid(row=row, column=column, columnspan=4, sticky=N + E + S + W, padx=2, pady=2)
        row += 1
        self.res_lbl.grid(row=row, column=column, columnspan=4, sticky=E, padx=2, pady=2)
        row += 1

        # Создание кнопок и назначение им команд
        for bt in BUTTONS + EXP_BUTTONS:
            button = Button(self, text=bt, command=lambda x=bt: self.action(x))
            button.grid(column=column, row=row, sticky=N + E + S + W, padx=2, pady=2)
            if bt in BUTTONS:
                self.buttons.append(button)
            else:
                self.exp_buttons.append(button)
            column += 1

            if 3 < column < 5:
                column = 0
                row += 1
            elif column > 6:
                column = 5
                row += 1
            if row > 7:
                column = 5
                row = 2

        # Размещение кнопок
        for r in range(2, 8):
            self.rowconfigure(index=r, weight=1)
        for c in range(7):
            self.columnconfigure(index=c, weight=10)
        self.columnconfigure(index=4, weight=1)
        self.basic()

    def basic(self):
        """
        Отображает "обычный" вид калькулятора
        """
        self.mode = 'basic'
        self.entry.grid_configure(columnspan=4)
        self.res_lbl.grid_configure(columnspan=4)
        for bt in self.exp_buttons:
            bt.grid_remove()

    def expend(self):
        """
        Отображает "расширенный" вид калькулятора
        """
        self.mode = 'change_mode'
        self.entry.grid_configure(columnspan=7)
        self.res_lbl.grid_configure(columnspan=7)
        for bt in self.exp_buttons:
            bt.grid()

    def set_theme(self, params: dict):
        """
        Устанавливает тему для кнопок и полей калькулятора

        :param params: параметры темы.
        """
        theme = params['calculator']

        bg = params['app']['bg']
        fg = params['app']['fg']
        self.configure(bg=bg)
        theme_font = theme['labels']['font']

        self.entry.configure(
            font=theme_font,
            bg=bg,
            fg=fg
        )
        self.res_lbl.configure(
            font=theme_font,
            bg=bg,
            fg=fg)
        for bt in self.buttons + self.exp_buttons:
            if bt['text'] in theme['custom']:
                bg = theme['custom'][bt['text']]['bg']
                fg = theme['custom'][bt['text']]['fg']
            elif bt['text'].isdigit():
                bg = theme['numbers']['bg']
                fg = theme['numbers']['fg']
            elif bt['text'] in NUM_SYS:
                bg = theme['num_sys']['bg']
                fg = theme['num_sys']['fg']
            elif bt['text'] in EXP_BUTTONS:
                bg = theme['ex_actions']['bg']
                fg = theme['ex_actions']['fg']
            else:
                bg = theme['actions']['bg']
                fg = theme['actions']['fg']
            bt['bg'] = bg
            bt['fg'] = fg
            bt['font'] = theme['font']

    def action(self, command: str):
        """
        Выполняет действия в соответствие с командами

        :param command: команда
        """
        # Удаляем весь текст
        if command == "C":
            self.entry.delete(0, END)

        # Стираем один символ
        elif command == "Del":
            self.entry.delete(self.entry.index(END) - 1)

        # Возвращаем вычисленное выражение
        elif command == "=" or command == "Return" or command == 'dec':
            formula = self.entry.get()
            if formula:
                self.entry.delete(0, END)
                self.entry.insert(0, str(calculate(formula)))

        elif command == "+-":
            formula = ""
            if self.entry.get():
                if self.entry.get()[-1] not in MATH_SIGNS + ["("]:
                    formula = '*'
            formula += "(-"
            self.entry.insert(INSERT, formula)

        elif command in NUM_SYS:
            formula = command + self.entry.get()
            if formula:
                self.entry.delete(0, END)
                self.entry.insert(0, str(calculate(formula)))

        else:
            self.entry.insert(INSERT, command)

        self.update()

    def update(self):
        """
        Обновляет метку результата
        """
        self.entry.focus_set()
        formula = self.entry.get()

        # Узнаём есть ли в формуле математические выражения
        is_sign = False
        for sign in MATH_SIGNS + MATH_ACTIONS + MATH_FUNCTIONS:
            if sign in formula:
                is_sign = True
                break
        res = ""

        if is_sign:
            if formula[-1] not in MATH_SIGNS:
                res = calculate(formula)

        self.res_lbl.configure(text=res)
