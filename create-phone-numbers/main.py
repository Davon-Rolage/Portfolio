from create_number import create_number
from format_number import format_number
import getpass
import os


user_dct = {
    1: '1',
    2: '2',
    3: '3',
}

lang = {
    'eng': {
        'user_request': '''1) Create N telephone numbers
2) Format existing numbers
3) Create N unformatted telephone numbers\n''',
        'choose_option': 'Choose option 1, 2, or 3: ',
        'enter_amount': 'Amount of telephone numbers to create: ',
        'enter_amount_error': 'Please, type a number greater than 0: ',
        'enter_file_name': 'Name of the file: ',
        'chosen_name': f'Chosen file name ->',
        'enter_location_path': 'Enter a file path with unformatted telephone numbers:\n',
        'enter_location_path_error': 'Please, enter a valid path:\n',
        'enter_saving_path': 'Enter saving path or leave empty:\n',
        'enter_saving_path_error': 'Please, enter a valid path or leave empty:\n',
        'file_is_saved': f'The file has been successfully saved at:\n',
    },
    'rus': {
        'user_request': '''1) Создать N номеров
2) Форматировать имеющиеся номера телефона
3) Создать N "сырых" номеров\n''',
        'choose_option': 'Выберите 1, 2 или 3: ',
        'enter_amount': 'Введите желаемое количество номеров: ',
        'enter_amount_error': 'Введите целое число больше 0: ',
        'enter_file_name': 'Введите желаемое имя файла: ',
        'chosen_name': f'Имя файла ->',
        'enter_location_path': 'Введите путь к файлу с неформатированными номерами телефона:\n',
        'enter_location_path_error': 'Введите корректный путь к файлу:\n',
        'enter_saving_path': 'Введите директорию сохранения файла или оставьте пустым:\n',
        'enter_saving_path_error': 'Введите корректный путь сохранения файла или оставьте пустым:\n',
        'file_is_saved': f'Файл успешно сохранен по пути:\n',
    },
}

user_lang = input('Language rus/eng: ')
if user_lang.lower() not in ['rus', 'russian', 'r', 'рус', 'русский', 'р']:
    user_lang = 'eng'
else:
    user_lang = 'rus'

messages = lang[user_lang]

user_request = input(messages['user_request'])

wrong_input = True
while wrong_input:
    try:
        # Get key of the 'user_dct' dictionary by the value of user's input
        option = list(user_dct.keys())[list(user_dct.values()).index(user_request)]
        wrong_input = False
    except:
        user_request = input(messages['choose_option'])

if option in [1, 3]:
    amount = input(messages['enter_amount'])
    wrong_input = True
    # Check whether user's input is an integer
    while wrong_input:
        try:
            amount = int(amount)
            if int(amount) > 0:
                wrong_input = False
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
        file_name = 'created_numbers'

    elif file_name == '' and option == 3:
        file_name = 'raw_numbers'

    print(messages['chosen_name'], file_name)

    wrong_input = True
    message = messages['enter_saving_path']
    while wrong_input:
        file_destination = input(message)
        # If user's input for file destination is empty, then file destination is the user's desktop
        if file_destination == '':
            file_destination = rf'C:\Users\{getpass.getuser()}\Desktop'
            wrong_input = False

        # Check whether user's path is available
        else:
            try:
                open(file_destination)
                wrong_input = False
            except Exception as err:
                # If error is raised, print the error message and ask for file's destination again
                print(err)
                message = messages['enter_saving_path_error']

    complete_name = os.path.join(rf'{file_destination}\{file_name}.txt')

    # Save the file to the user's path
    with open(complete_name, 'w') as f:
        f.writelines(fin_lst)
    print(messages['file_is_saved'] + complete_name)

else:
    f_lst = []
    message = messages['enter_location_path']
    wrong_input = True
    # Check whether user's path is available for reading
    while wrong_input:
        try:
            file_location = input(message)
            open(file_location)
            wrong_input = False
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
    # If user's input is empty, then assign  value 'formatted_numbers' to the 'file_name' variable
    file_name = 'formatted_numbers' if file_name == '' else file_name
    print(messages['chosen_name'], file_name)

    file_destination = input(messages['enter_saving_path'])
    # If user's input for file destination is empty, then file destination is the user's desktop
    file_destination = rf"C:\Users\{getpass.getuser()}\Desktop" if file_destination == '' else file_destination
    complete_name = os.path.join(f'{file_destination}\{file_name}.txt')
    with open(complete_name, 'w') as f:
        f.writelines(f_lst)
    print(messages['file_is_saved'] + complete_name)

# Open the file using 'startfile' function of 'os' module
os.startfile(complete_name)
