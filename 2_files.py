"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    with open('referat.txt', 'r', encoding='utf-8') as f:
        new_string = f.read()
        print(f'Длинна строки: {len(new_string)} символа(ов)')
        words = new_string.split()
        print(f'Количество слов в тексте: {len(words)}')
        modified_string = new_string.replace('.','!')

    with open('referat2.txt', 'a', encoding='utf-8') as f:
        f.write(modified_string)

if __name__ == "__main__":
    main()
