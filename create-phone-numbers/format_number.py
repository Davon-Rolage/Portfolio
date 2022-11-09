def format_number(num_string):
    template = '+7 {}{}{} {}{}{}-{}{}-{}{}'
    raw_string = num_string.strip().lstrip('+')
    for char in raw_string:
        if char not in '0123456789':
            raw_string = raw_string.replace(char, '')
    if len(raw_string) != 11:
        return f'{num_string} ошибка'

    significant_digits = raw_string[-10:]
    return template.format(*significant_digits)

# Old version
# def format_number(num_string):
#     template = '+7 {}{}{} {}{}{}-{}{}-{}{}'
#     string = num_string.strip()
#     for char in string[::-1]:
#         if char not in '0123456789':
#             string = num_string.replace(char, '')
#     if len(string) < 11:
#         return f'{num_string} ошибка'
#     else:
#         significant_numbers = string[-10:]
#         if num_string[:2] == "+7":
#             if len(num_string) > 12:
#                 return f'{num_string} ошибка'
#             else:
#                 try:
#                     return template.format(*significant_numbers)
#                 except Exception as err:
#                     print(f'{num_string} - {err}')
#         elif num_string[0] in '78':
#             if len(string) > 11:
#                 return f'{num_string} ошибка'
#             else:
#                 try:
#                     return template.format(*significant_numbers)
#                 except Exception as err:
#                     print(f'{num_string} - {err}')
#         else:
#             if not len(string) == 10:
#                 return f'{num_string} ошибка'
#             else:
#                 try:
#                     return template.format(*significant_numbers)
#                 except Exception as err:
#                     print(f'{num_string} - {err}')


if __name__ == '__main__':
    # user_input = input('Введите номер телефона в любом формате:\n')
    # print(format_number(user_input))
    with open('example', 'r') as f:
        lines = f.readlines()
        lines = list(map(lambda x: x.strip(), lines))
    for num in lines:
        print(format_number(num))