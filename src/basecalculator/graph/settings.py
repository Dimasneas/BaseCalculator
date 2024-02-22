import gettext
import json
import os

from ..settings import settings_translate as global_translate

_ = gettext.gettext


def settings_translate(new_lang: str):
    """
    Установка языка фраз консольного и графического приложения.
    :param new_lang: новый язык для приложения.
    """
    global _
    lang = gettext.translation(domain='settings', localedir=LOCALE_DIR, languages=[new_lang])
    _ = lang.gettext
    global_translate(new_lang)


ROOT_DIR = os.path.dirname(__file__)

LOCALE_DIR = os.path.join(ROOT_DIR, '..', 'data', 'locales')

ICON = os.path.join(ROOT_DIR, 'data', 'icon.ico')

WIDTH = 400
HEIGHT = 550

TOP_WIDTH = 520
TOP_HEIGHT = 650


def languages() -> dict:
    """
    Названия языков на текущем языке.
    """
    return {
        "en": _("English"),
        "ru": _("Русский"),
    }


def themes() -> dict:
    """
    Темы на текущем языке.
    """
    return {
        "dark": _("Dark"),
        "light": _("Light"),
        "kids": _("Kids"),
    }


def get_theme(theme: str) -> dict:
    """
    Получение параметров темы из JSON файла.
    :param theme: тема для получения параметров.
    :return: Параметры темы.
    """
    with open(os.path.join(ROOT_DIR, 'data', 'themes', f'{theme}.json'), 'r', encoding='utf8') as json_file:
        return json.load(json_file)
