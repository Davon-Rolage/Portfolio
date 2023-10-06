from create_number import create_number
from format_number import format_number
import os


user_dct = {
    1: '1',
    2: '2',
    3: '3',
}

lang = {
    'en': {
        'user_request': '''1) Create N telephone numbers
2) Format existing numbers
3) Create N unformatted telephone numbers\n''',
        'choose_option': 'Choose option 1, 2, or 3: ',
        'enter_amount': 'Amount of telephone numbers to create: ',
        'enter_amount_error': 'Please, type a number greater than 0: ',
        'enter_file_name': 'Enter file name (or leave empty): ',
        'chosen_name': f'Chosen file name ->',
        'enter_location_path': 'Enter a full path to a file with unformatted telephone numbers (or leave empty):\n',
        'enter_location_path_error': 'Please, enter a valid path (or leave empty):\n',
        'enter_saving_path': 'Enter saving path (or leave empty):\n',
        'enter_saving_path_error': 'Please, enter a valid path (or leave empty):\n',
        'file_is_saved': f'The file has been successfully saved at:\n',
    },
    'ru': {
        'user_request': '''1) Создать N номеров
2) Форматировать имеющиеся номера телефона
3) Создать N "сырых" номеров\n''',
        'choose_option': 'Выберите 1, 2 или 3: ',
        'enter_amount': 'Введите желаемое количество номеров: ',
        'enter_amount_error': 'Введите целое число больше 0: ',
        'enter_file_name': 'Введите желаемое имя файла (или оставьте пустым): ',
        'chosen_name': f'Имя файла ->',
        'enter_location_path': 'Введите путь к файлу с неформатированными номерами телефона (или оставьте пустым):\n',
        'enter_location_path_error': 'Введите корректный путь к файлу (или оставьте пустым):\n',
        'enter_saving_path': 'Введите директорию сохранения файла (или оставьте пустым):\n',
        'enter_saving_path_error': 'Введите корректный путь сохранения файла (или оставьте пустым):\n',
        'file_is_saved': f'Файл успешно сохранен по пути:\n',
    },
}

user_lang = input('Language ru/en: ')
if user_lang.lower() not in ['ru', 'russian', 'r', 'рус', 'русский', 'р']:
    user_lang = 'en'
else:
    user_lang = 'ru'

messages = lang[user_lang]

user_request = input(messages['user_request'])

while True:
    try:
        # Get key of the 'user_dct' dictionary by the value of user's input
        option = list(user_dct.keys())[list(user_dct.values()).index(user_request)]
        break
    except:
        user_request = input(messages['choose_option'])

if option in [1, 3]:
    amount = input(messages['enter_amount'])
    # Check whether user's input is an integer
    while True:
        try:
            amount = int(amount)
            if int(amount) > 0:
                break
            else:
                raise ValueError
        except ValueError:
            amount = input(messages['enter_amount_error'])

    fin_lst = []
    for _ in range(amount):
        n = create_number()
        # Format the telephone number if user chose option 1
        if option == 1:
            n = format_number(n)
        # Append the number to the final list of telephone numbers
        fin_lst.append(n+'\n')

    file_name = input(messages['enter_file_name'])
    if file_name == '' and option == 1:
        file_name = 'created_numbers.txt'

    elif file_name == '' and option == 3:
        file_name = 'raw_numbers.txt'

    print(messages['chosen_name'], file_name)

    message = messages['enter_saving_path']
    default_file_destination = os.getcwd()
    while True:
        file_destination = input(message)
        if file_destination == '':
            file_destination = default_file_destination
            break
        elif os.path.isfile(file_destination):
            break
        else:
            message = messages['enter_saving_path_error']

    file_destination += '\\' + file_name

    with open(file_destination, 'w') as f:
        f.writelines(fin_lst)
    print(messages['file_is_saved'] + file_destination)

# If chosen option is 2 (format telephone numbers)
else:
    default_path = os.getcwd() + '\\example.txt'
    f_lst = []
    message = messages['enter_location_path']
    # Check whether user path is available for reading
    while True:
        try:
            user_input = input(message)
            file_location = default_path if user_input == '' else user_input
            open(file_location)
            print("File location: ", file_location)
            break

        except Exception as err:
            # If error is raised, print the error message and ask for file's path again
            print(err)
            message = messages['enter_location_path_error']

    with open(file_location, 'r') as f:
        txt_string = ''.join(f.readlines())
        lines = txt_string.split()

    for number in lines:
        f_lst.append(format_number(number)+'\n')

    file_name = input(messages['enter_file_name'])
    file_name = 'formatted_numbers.txt' if file_name == '' else file_name
    print(messages['chosen_name'], file_name)

    default_file_destination = os.getcwd() + file_name
    file_destination = input(messages['enter_saving_path'])
    file_destination = default_file_destination if file_destination == '' else file_destination
    with open(file_destination, 'w', encoding='utf-8') as f:
        f.writelines(f_lst)
    print(messages['file_is_saved'] + file_destination)

# Open the created file
os.startfile(file_destination)
