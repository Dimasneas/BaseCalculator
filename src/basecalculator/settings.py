import gettext
import os

# Перевод файла

_ = gettext.gettext


def settings_translate(new_lang: str):
    """
    Установка языка фраз консольного и графического приложения.
    :param new_lang: новый язык для приложения.
    """
    global _
    lang = gettext.translation(domain='settings', localedir=LOCALE_DIR, languages=[new_lang])
    _ = lang.gettext


# Общие настройки

ROOT_DIR = os.path.dirname(__file__)
""" Директория расположения файлов пакета"""

LOCALE_DIR = os.path.join(ROOT_DIR, 'data', 'locales')
"""Расположение файлов перевода"""

LANGUAGES = ["en", "ru"]
THEMES = ["dark", "light", "kids"]


def error_text() -> dict:
    """
    Ошибки на текущем языке.
    """
    return {
        "syntax": _('Wrong input'),
        "overflow": _('Too big answer'),
        "zero_division": _('Zero division'),
        "value": _('Too much nesting'),
    }
