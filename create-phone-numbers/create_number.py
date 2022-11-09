import random as r
from format_number import format_number


def create_number():
    prefixes = [
        '+7',
        '7',
        '8',
    ]
    lst = [str(r.randint(0, 9)) for _ in range(10)]
    string = ''.join(lst)
    return f'{r.choice(prefixes)}{string}'


if __name__ == '__main__':
    user_input = input('Введите желаемое количество номеров: ')
    wrong_input = True
    while wrong_input:
        try:
            user_input = int(user_input)
            if user_input > 0:
                wrong_input = False
            else:
                user_input = input('Введите число больше 0: ')
        except ValueError:
            user_input = input('Введите число больше 0: ')

    user_choice = input('Форматировать номера? y\\n\n')
    user_choice = 'y' if not user_choice == 'n' else user_choice
    print(f'Выбранный режим -> {"форматирование" if user_choice == "y" else "без форматирования"}')

    for _ in range(user_input):
        n = create_number()
        if user_choice == 'y':
            n = format_number(n)
        print(n)
