def format_number(num_string):
    template = '+7 {}{}{} {}{}{}-{}{}-{}{}'
    raw_string = ''.join(char for char in num_string if char.isdigit())
    if len(raw_string) != 11:
        return f'{num_string} error'

    significant_digits = raw_string[-10:]
    return template.format(*significant_digits)


if __name__ == '__main__':
    with open('example.txt', 'r') as f:
        lines = f.readlines()
        lines = list(map(lambda x: x.strip(), lines))
    for num in lines:
        print(format_number(num))
        