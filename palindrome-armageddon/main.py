import rus_alphabet
import random as r
import string as s
import os


ALPHABET = s.ascii_letters + rus_alphabet.rus_letters
DEFAULT = 5


def make_palindrome(length):
    lst = ''.join([r.choice(ALPHABET) for _ in range(length // 2)])
    lst += lst[::-1]
    if length % 2 == 1:
        lst = lst[:len(lst) // 2] + r.choice(ALPHABET) + lst[len(lst) // 2:]
    return lst


def make_some_palindromes(length=5, amount=5):
    array = [make_palindrome(length) for _ in range(amount)]
    return '\n'.join(array)


def ask_user(command):
    while True:
        try:
            return int(input(messages[command]))

        except ValueError:
            return DEFAULT


if __name__ == '__main__':
    lang = {
        'eng': {
            'mode': 'Write or Append? (w / a)\n',
            'chosen_mode': 'Chosen mode ->',
            'file_name': "What is the name of the file: ",
            'chosen_name': 'Chosen name ->',
            'length': 'Length of the words: ',
            'chosen_length': 'Chosen length ->',
            'amount': 'Number of words: ',
            'chosen_amount': 'Chosen amount ->',
            'file_path': f'____________\nThe file has been successfully saved at:\n'
        },
        'rus': {
            'mode': 'Перезаписать или Дописать? (w / a)\n',
            'chosen_mode': 'Выбранный режим ->',
            'file_name': 'Придумайте имя файла: ',
            'chosen_name': 'Выбранное имя ->',
            'length': 'Какова длина слов: ',
            'chosen_length': 'Выбранная длина ->',
            'amount': 'Количество слов: ',
            'chosen_amount': 'Выбранное количество слов ->',
            'file_path': f'____________\nФайл был успешно сохранен по пути:\n'
        }
    }

    user_lang = input('Language rus/eng: ')
    if user_lang not in ['rus', 'russian', 'r', 'рус', 'русский', 'р']:
        user_lang = 'eng'
    else:
        user_lang = 'rus'

    messages = lang[user_lang]

    mode = input(messages['mode'])
    mode = 'a' if not mode == 'w' else mode
    print(messages['chosen_mode'], mode)
    save_path = os.getcwd()
    file_name = input(messages['file_name'])
    file_name = 'foobar' if file_name == '' else file_name
    print(messages['chosen_name'], file_name)
    
    complete_name = os.path.join(save_path, file_name + ".txt")
    with open(complete_name, mode, encoding='utf-8') as f:
        lines = make_some_palindromes(
            ask_user('length'),
            ask_user('amount')
        )
        f.writelines(lines)

    print(f'{messages["file_path"]}{complete_name}')
    os.startfile(complete_name)
