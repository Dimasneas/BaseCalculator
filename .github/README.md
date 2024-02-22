# BaseCalculator: Graphing and Command-Line Calculator / BaseCalculator: Графический и Командный Калькулятор

BaseCalculator is a versatile Python calculator package that provides both a command-line interface for simple arithmetic calculations and a graphing calculator feature. It supports two languages, English and Russian, and two modes of operation: basic and advanced.

BaseCalculator - это многофункциональный пакет калькулятора на Python, который предоставляет как командный интерфейс для простых арифметических вычислений, так и графический калькулятор. Он поддерживает два языка: английский и русский, а также два режима работы: базовый и расширенный.

## Features / Возможности
 -Command-Line Calculator: Execute simple arithmetic operations from the command line. / Командный Калькулятор: Выполняйте простые арифметические операции из командной строки.
 -Graphing Calculator: Visualize mathematical functions in a graphical interface. / Графический Калькулятор: Визуализируйте математические функции в графическом интерфейсе.
 -Language Support: Available in both English and Russian. / Поддержка Языков: Доступно как на английском, так и на русском языках.
 -Basic and Advanced Modes: Choose between basic arithmetic operations and extended mathematical functions. / Режимы Работы: Выбирайте между базовыми арифметическими операциями и расширенными математическими функциями.
 -Number System Conversion: Convert integer results into binary, octal, decimal, or hexadecimal formats. / Конвертация в Систему Счисления: Преобразуйте целочисленные результаты в двоичную, восьмеричную, десятичную или шестнадцатеричную системы счисления.
 -Usage / Использование
 -Command-Line Interface / Командный Интерфейс
 -To use the command-line calculator, simply call the package without any arguments: / Для использования командного калькулятора просто вызовите пакет без аргументов:

 ```console
 py -m basecalculator graph
 ```

If arguments are provided, the calculator returns the result of the expression: / Если предоставлены аргументы, калькулятор возвращает результат выражения:

 ```console
 py -m basecalculator expr '5+5'
 10
 ```

## Graphing Calculator / Графический Калькулятор
When launched with arguments graph, the graphing calculator starts: / При запуске без аргументов начинает работу графический калькулятор:

 ```console
 py -m basecalculator graph
 ```
|                      English                      |                      Русский                      |
|:-------------------------------------------------:|:-------------------------------------------------:|
| ![en_photo](https://i.postimg.cc/J0bQFDgQ/en.png) | ![ru_photo](https://i.postimg.cc/5yc3pqP0/ru.png) |

## Language Selection / Выбор Языка
You can select the language by passing the appropriate argument (en for English, ru for Russian): / Вы можете выбрать язык, передав соответствующий аргумент (en для английского, ru для русского):
Default: en / По умолчанию: en 
 ```console
 py -m basecalculator expr --lang ru
 ```

## Mode Selection / Выбор Режима
Choose between basic and advanced modes by specifying the mode (basic or advanced): / Выберите между базовым и расширенным режимами, указав режим (basic или advanced):

```
py -m basecalculator graph --expend
```  
##Supported Functions / Поддерживаемые Функции
###Basic Mode / Базовый Режим
 - Addition (+) / Сложение (+)
 - Subtraction (-) / Вычитание (-)
 - Multiplication () / Умножение ()
 - Division (/) / Деление (/)
 - Square Root (sqrt) / Квадратный Корень (sqrt)
 - Modulo (%) / Остаток от Деления (%)
 - Exponentiation (^) / Возведение в Степень (^)
###Advanced Mode / Расширенный Режим
In addition to the basic functions: / Помимо базовых функций:
 - Logarithm (log) / Логарифм (log)
 - Natural Logarithm (ln) / Натуральный Логарифм (ln)
 - Absolute Value (abs) / Абсолютное Значение (abs)
 - Factorial (!) / Факториал (!)
 - Number System Conversion / Конвертация в Систему Счисления
To convert the result to a different number system, prefix the number system's abbreviation to the expression: / Чтобы преобразовать результат в другую систему счисления, добавьте префикс сокращенного названия системы счисления перед выражением:

 - Binary (bin) / Двоичная (bin)
 - Base 3 (ter) / Троичная (ter)
 - Base 4 (qua) / Четверичная (qua)
 - Base 5 (fiv) / Пятеричная (five)
 - Base 6 (six) / Шестеричная (six)
 - Base 7 (sep) / Семеричная (sep)
 - Octal (oct) / Восьмиричная (sep)
 - Base 10 (dec) / Десятичная (sep)
```console
 py -m basecalculator expr bin10+5
```

##Installation / Установка
Install BaseCalculator using pip: / Установите BaseCalculator с помощью pip:

bash
Copy code
```console
 py -m pip install -i https://test.pypi.org/simple/ basecalculator
```

License / Лицензия
This project is licensed under the MIT License - see the [LICENSE](../LICENSE.txt) file for details. / Этот проект лицензирован под лицензией MIT - см. файл [LICENSE](../LICENSE.txt) для получения дополнительной информации.