import rus_alphabet
import random as r
import string as s
import os

ALPHABET = s.ascii_letters + rus_alphabet.rus_letters
STUPIDITY_THRESHOLD = 5
DEFAULT = 5
counter = 0


def make_palindrome(length):
    lst = ''.join([r.choice(ALPHABET) for _ in range(length // 2)])
    lst += lst[::-1]
    if length % 2 == 1:
        lst = lst[:len(lst) // 2] + r.choice(ALPHABET) + lst[len(lst) // 2:]
    return lst


def make_some_palindromes(length=5, amount=5):
    global counter
    array = [make_palindrome(length) for u in range(amount)]
    fin = []
    # for k, pal in enumerate(array, start=1):
    #     fin.append(f'{k}. {pal}\n')
    # if counter == 5:
    #     fin.append(f'Take a cookie from the shelf. You IQ is -{amount}')
    # return fin
    return '\n'.join(array)


def get_user_input(question):
    answer = input(messages[question])
    return answer


def ask_user(command):
    global STUPIDITY_THRESHOLD
    global counter
    wrong_answer = True

    while wrong_answer:
        try:
            return int(get_user_input(command))
        except ValueError as e:
            if counter == STUPIDITY_THRESHOLD:
                print(f"____\nI'm done with you, get outta here. Chosen {command} -> {DEFAULT}")
                return DEFAULT
            else:
                counter += 1
            print(f'Wrong input. Try again {counter}/{DEFAULT}')


if __name__ == '__main__':
    lang = {
        'eng': {
            'mode': 'Write or Append? (w / a)\n',
            'chosen_mode': 'Chosen mode ->',
            'name_of_file': "What is the name of the file: ",
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
            'name_of_file': 'Придумайте имя файла: ',
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
    save_path = r'C:\Users\boroda\Desktop'
    name_of_file = input(messages['name_of_file'])
    name_of_file = 'foobar' if name_of_file == '' else name_of_file
    print(messages['chosen_name'], name_of_file)
    complete_name = os.path.join(save_path, name_of_file + ".txt")

    with open(complete_name, mode) as f:

        lines = make_some_palindromes(
            ask_user('length'),
            ask_user('amount')
        )
        f.writelines(lines)

    print(f'{messages["file_path"]}{complete_name}')
    os.startfile(complete_name)
