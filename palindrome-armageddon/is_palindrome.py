import main

p_lst = ['abba', 'hey', 'wassaw', 'boy', 'cow', 'portrop', 'a', 'alkjasdo', 'alallala', 'britneyentirb']


def is_palindrome(word):
    return word == word[::-1]


def is_list_palindrome(lst):
    pals = list(map(lambda x: is_palindrome(x), lst))
    dct = dict(zip(lst, pals))
    for k, v in dct.items():
        print(f'{k} is {v}')
    return '______Done______'


with open(r'C:\Users\boroda\Desktop\foobar.txt', 'r') as f:
    lines = f.readlines()
    lines = list(map(lambda x: x.strip(), lines))
    print(is_list_palindrome(lines))

# print(is_list_palindrome(p_lst))
