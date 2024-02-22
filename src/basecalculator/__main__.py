import argparse

from . import *


def create_parser():
    """
    Создание парсера.
    :return: Парсер для командной строки
    """

    # Создание парсера
    new_parser = argparse.ArgumentParser(
        prog='coolcalc',
        description='Калькулятор поддерживает два режима работы:\n'
                    '- консольный\n'
                    '- графический',
        epilog='(C) Dimasneas, 2024',
        add_help=False,
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser_params = new_parser.add_argument_group("Параметры")
    parser_params.add_argument('--help', '-h', action='help', help='Справка')

    # Создаём подпарсер
    subparser = new_parser.add_subparsers(
        dest='mode',
        title='Команды',
        description='Команды которые должны быть в качестве первого параметра %(prog)s'
    )

    # Подпарсер для ввода с консоли
    console_parser = subparser.add_parser(
        'expr',
        add_help=False,
        help='Запуск в консольном режиме',
        description=
        '''
В этом режиме для расчёта выражения его нужно указать рядом в кавычках.
Калькулятор поддерживает следующие функции:
    log(expr) - десятичный логарифм от выражения, пример 'log(10)' // 1
    ln(expr) - натуральный логарифм от выражения, пример 'ln(2)' // 0.9...
    sqrt(expr) - квадратный корень из выражения, пример 'sqrt(4)'  // 2
    ^ - возведение в степень пример '2^5' // 32
    abs(expr) - модуль выражения, пример abs(-12) // 12
    factorial(expr) или  expr! - факториал выражения, пример 4! // 24.
    Перевод в системы счисления:
        bin - двоичная,
        ter - троичная,
        qua - четверичная,
        fiv - пятеричная,
        six - шестиричная,
        sep - семиричная,
        oct - восмеричная,
        dec - десятичная.
    Пример использования bin5+2 // = bin7 = 111
        ''',
        formatter_class=argparse.RawTextHelpFormatter
    )

    console_parser.add_argument('expression', help='Выражение указанное в кавычках для вычисления')
    console_params = console_parser.add_argument_group('Консольные параметры')
    console_params.add_argument('--help', '-h', action='help', help='Справка')
    console_params.add_argument(
        '--lang', '-l',
        choices=LANGUAGES,
        default='en',
        nargs='?',
        help='Язык приложения(en/ru)'
    )

    # Подпарсер для запуска графического приложения
    graph_parser = subparser.add_parser(
        'graph',
        add_help=False,
        help='Запуск в графическом режиме',
        description='В этом режиме для расчёта выражения его нужно ввести в открывшееся окно'
    )

    graph_params = graph_parser.add_argument_group(title='Графические параметры')
    graph_params.add_argument('--help', '-h', action='help', help='Справка')
    graph_params.add_argument('-e', '--expand', action='store_true', help='Запуск в расширенном режиме')
    graph_params.add_argument('-b', '--basic', action='store_true', help='Запуск в базовом режиме(по умолчанию)')
    graph_params.add_argument(
        '-t', '--theme',
        choices=THEMES,
        default='dark',
        nargs='?',
        help='Тема приложения(dark/light/kids)'
    )
    graph_params.add_argument(
        '--lang', '-l',
        choices=LANGUAGES,
        default='en',
        nargs='?',
        help='Язык приложения(en/ru)'
    )
    return new_parser


if __name__ == '__main__':

    parser = create_parser()
    args = parser.parse_args()
    app_lang = args.lang

    if args.mode == 'expr':
        app_lang = args.lang
        expr = args.expression
        translate(app_lang)
        print(calculate(expr))
    elif args.mode == 'graph':
        theme = args.theme
        app_lang = args.lang
        app = App(app_lang, theme)
        if args.expand:
            app.change_mode()
        app.mainloop()
    else:
        parser.print_help()


