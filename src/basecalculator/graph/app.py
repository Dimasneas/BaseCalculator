import gettext
from tkinter import Tk, BOTH, Menu, END, Event

from .graph_calc import Calculator
from .pages import InfoPage, about_text, help_text, pages_translate
from .settings import WIDTH, HEIGHT, themes, languages, settings_translate, get_theme, LOCALE_DIR, ICON

# Перевод файла

_ = gettext.gettext


def app_translate(new_lang: str):
    """
    Установка языка главной части приложения.
    :param new_lang: новый язык для приложения.
    """
    global _
    lang = gettext.translation(domain='app', localedir=LOCALE_DIR, languages=[new_lang])
    _ = lang.gettext


class App(Tk):
    """
    Основное окно приложения.
    """
    def __init__(self, lang: str, theme: str):
        """
        Конструктор класса.
        :param lang: язык приложения.
        :param theme: тема графического калькулятора.
        """
        super().__init__()
        self.theme = theme
        self.mode = 'basic'

        self.iconbitmap(ICON)

        x = self.winfo_screenwidth() // 2 - WIDTH // 2
        y = self.winfo_screenheight() // 2 - HEIGHT // 2

        self.geometry(f"{WIDTH}x{HEIGHT}+{x}+{y}")
        self.resizable(False, False)

        self.calc = Calculator(self)
        self.calc.pack(pady=10, padx=10, fill=BOTH, expand=True)

        self.main_menu = Menu(self)
        self.view_menu = Menu(self.main_menu, tearoff=0)

        self.create_menu()
        self.set_new_lang(lang)
        self.set_theme(self.theme)

    def create_menu(self):
        """
        Создание меню приложения.
        """
        self.main_menu = Menu(self)
        self.view_menu = Menu(self.main_menu, tearoff=0)

        self.title(_("Calculator"))

        file_menu = Menu(self.main_menu, tearoff=0)
        """ Меню "Файл" """
        theme_menu = Menu(self.main_menu, tearoff=0)
        """ Подменю темы """
        lang_menu = Menu(self.main_menu, tearoff=0)
        """ подменю языков """
        about_menu = Menu(self.main_menu, tearoff=0)
        """ Меню "О программе" """

        # Файл
        file_menu.add_command(
            label=_('Copy'),
            command=lambda: self.calc.entry.event_generate("<<Copy>>"),
            accelerator='Ctrl+C'
        )
        file_menu.add_command(
            label=_('Paste'),
            command=lambda: self.calc.entry.event_generate("<<Paste>>"),
            accelerator='Ctrl+V',
        )

        # Вид
        self.view_menu.add_command(
            label=_('Expand'),
            command=self.change_mode,
            accelerator='Ctrl+E',
            )

        self.view_menu.add_separator()
        # Темы
        for theme in themes():
            theme_menu.add_command(
                label=themes()[theme],
                command=lambda t=theme: self.set_theme(t)
            )

        self.view_menu.add_cascade(label=_('Themes'), menu=theme_menu)
        self.view_menu.add_separator()
        # Языки
        for lang in languages():
            lang_menu.add_command(
                label=languages()[lang],
                command=lambda l=lang: self.set_new_lang(l)
            )

        self.view_menu.add_cascade(label=_('Language'), menu=lang_menu)

        # О программе
        about_menu.add_command(label=_('Help'), command=self.menu_help, accelerator='Ctrl+H')
        about_menu.add_command(label=_('About'), command=self.about, accelerator='Ctrl+I')
        self.bind_all("<Key>", self.hot_keys)
        # Добавление списков меню
        self.main_menu.add_cascade(label=_('File'), menu=file_menu)
        self.main_menu.add_cascade(label=_('View'), menu=self.view_menu)
        self.main_menu.add_cascade(label=_('About'), menu=about_menu)
        self.config(menu=self.main_menu)

    def change_mode(self):
        """
        Смена режимов приложения.
        """
        if self.mode == 'basic':
            self.view_menu.entryconfig(0, label=_("Basic"))
            self.geometry(f"{int(1.5 * WIDTH + 10)}x{HEIGHT}")
            self.mode = 'change_mode'
            self.calc.expend()
        elif self.mode == 'change_mode':
            self.view_menu.entryconfig(0, label=_("Expand"))
            self.geometry(f"{WIDTH}x{HEIGHT}")
            self.mode = 'basic'
            self.calc.basic()

    def set_theme(self, theme: str):
        """
        Установка темы основного окна приложения.
        :param theme: тема.
        """
        new_theme = get_theme(theme)
        self.calc.set_theme(new_theme)
        self['bg'] = new_theme['app']['bg']
        self.set_menu_color(self.main_menu, new_theme['menu'])
        self.theme = theme

    def set_menu_color(self, menu: Menu, color: dict):
        """
        Смена цвета меню и подменю.
        :param menu: меню.
        :param color: цвета.
        """
        menu.config(background=color['bg'],
                    foreground=color['fg'],
                    activebackground=color['abg'],
                    activeforeground=color['afg']
                    )
        for item in menu.winfo_children():
            if isinstance(item, Menu):
                self.set_menu_color(item, color)

    def set_new_lang(self, lang: str):
        """
        Смена языка основного окна.
        :param lang: новый язык.
        """
        self.main_menu.delete(0, END)
        settings_translate(lang)
        app_translate(lang)
        pages_translate(lang)
        self.create_menu()

    def menu_help(self):
        """
        Создание окна "Справка".
        """
        theme = get_theme(self.theme)
        page = InfoPage(self, help_text(), theme['settings'])
        page.mainloop()

    def about(self):
        """
        Создание окна "О программе".
        """
        theme = get_theme(self.theme)
        page = InfoPage(self, about_text(), theme['settings'])
        page.mainloop()

    def hot_keys(self, e: Event):
        """
        Обработка "горячих" клавиш.
        :param e: событие клавиатуры.
        """
        if e.keycode == 67 and e.state == 12:  # ctrl+c
            self.calc.entry.event_generate("<<Copy>>")
        elif e.keycode == 86 and e.state == 12:  # ctrl+v
            self.calc.entry.event_generate("<<Paste>>")
        elif e.keycode == 72 and e.state == 12:  # ctrl+h
            self.menu_help()
        elif e.keycode == 73 and e.state == 12:  # ctrl+i
            self.about()
        elif e.keycode == 69 and e.state == 12:  # ctrl+e
            self.change_mode()
