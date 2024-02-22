import gettext
import os
import platform
from tkinter import Toplevel, Frame, TOP, Label, LEFT, BOTH, Button, BOTTOM, Tk

from .settings import WIDTH, TOP_WIDTH, HEIGHT, TOP_HEIGHT, LOCALE_DIR

# Перевод файла

_ = gettext.gettext


def pages_translate(new_lang: str):
    """
    Установка языка дополнительных страниц приложения(О программе, Справка).
    :param new_lang: новый язык для приложения.
    """
    global _
    lang = gettext.translation(domain='pages', localedir=LOCALE_DIR, languages=[new_lang])
    _ = lang.gettext

# Содержание страниц


def about_text() -> dict:
    """
    Текст окна "О программе" на текущем языке.
    """
    return {
        "title": _('About'),
        "body": {
            "title": {
                "content": _('Calculator'),
                "font": 'Times 14',
            },
            "main": {
                "content": _(
                    'The calculator has two modes: simple and advanced.\n'
                    'In simple mode, the calculator can perform operations such as: arithmetic operations, sign change,'
                    ' percentages, squaring, square master.\n'
                    'In advanced mode, the calculator can perform such operations as: functions of a simple calculator,'
                    ' trigonometric functions, exponentiation, ogarithms (natural and decimal), modulus of a number, '
                    'factorial of a number, translation into number systems (2, 3, 4, 5, 6, 7, 8)\n'
                    'The calculator has several params for design, among which there is a kids. \n'
                    'You can also change the interface language to Russian.\n'
                    'The program was created and has an MIT license.\n'
                    'Creators:\n'
                    'Glushenkov Dmitrii Alekseevich'
                ),
                "font": 'Times 12',
            },
            "version": {
                "content": _('Operating system: ') + platform.platform(),
                "font": 'Times 12',
            },
            "user": {
                "content": _('Username: ') + os.getlogin(),
                "font": 'Times 12'
            },
        }
    }


def help_text() -> dict:
    """
    Текст окна "Справка" на текущем языке.
    """
    return {
        "title": _('Help'),
        "body": {
            "main": {
                "content": _(
                    'This window is designed to answer some questions about the application. \n\n'
                    'СALCULATOR\n\n'
                    'In this tab, you can copy or paste the values. To copy the item you need, select it with the left '
                    'mouse button, go to the "Calculator" tab and click "Copy". To insert the element you need, '
                    'select it with the left mouse button, go to the Calculator tab and click "Paste".\n\n'
                    'VIEW\n\n'
                    'To switch the calculator view, go to the "View" tab and select the mode you need. '
                    'If you want to find out how the modes differ from each other, go to the "About" tab and select '
                    '"About". To change the theme of the calculator, go to the "View" tab, then hover over the "View" '
                    'tab and select the topic you are interested in. You can also change the language to English in '
                    'this tab. Go to the "View" tab, then hover over the "Language" tab and select the language you '
                    'are interested in.\n\n'
                    'ABOUT\n\n'
                    'In this tab, you can read this manual in the Help tab. If you want to learn more about the '
                    'program, open the About tab.\n\n'
                    'Some functions:\n'
                    'ln(x) — natural logarithm\n'
                    'log(x) - logarithm\n'
                    'abs(x) — module\n'
                    'sqrt(x) — master\n'
                    'x^y — x power y \n'
                    'of x! — factorial(x)\n'
                ),
                "font": "Times 12",
            }
        }
    }

# Класс окна информации


class InfoPage(Toplevel):
    """
    Информационная страница - окно перекрывающее главное окно приложения.
    """
    def __init__(self, parent: Tk, info: dict, theme: dict):
        """
        Конструктор класса.

        :param parent: родительский элемент окна.
        :param info: информация выводимая в окне.
        :param theme: параметры текущей темы приложения.
        """
        super().__init__(parent)

        lbs = Frame(self)
        lbs.pack(side=TOP)

        main = info["body"]

        for part in main:
            body = Label(lbs,
                         text=main[part]['content'],
                         font=main[part]['font'],
                         anchor='w',
                         justify=LEFT,
                         wraplength=500,
                         bg=theme['bg'],
                         fg=theme['fg'])
            body.pack(fill=BOTH)

        btn = Frame(self, bg=theme['bg'])
        quite_btn = Button(btn,
                           text=_("Cancel"),
                           command=self.cancel,
                           bg=theme['btn']['bg'],
                           fg=theme['btn']['fg'],
                           )
        btn.pack(side=BOTTOM)
        quite_btn.pack(side=BOTTOM, pady=(0, 5))

        # подсчёт координат окна
        x = parent.winfo_rootx()
        y = parent.winfo_rooty()
        x += WIDTH / 2 - TOP_WIDTH / 2
        y += HEIGHT / 2 - TOP_HEIGHT / 2

        # задание параметров окна
        self['bg'] = theme['bg']
        self.title(info['title'])
        self.minsize(TOP_WIDTH, TOP_HEIGHT)
        self.geometry(f"+{int(x)}+{int(y)}")
        self.resizable(width=False, height=False)
        self.grab_set()

    def cancel(self):
        """
        Закрытие окна.
        """
        self.destroy()
