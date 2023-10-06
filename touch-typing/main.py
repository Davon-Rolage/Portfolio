import random as r


ALPHABET = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

def make_word():
    global ALPHABET
    length = r.randint(2, 6)
    return ''.join([r.choice(ALPHABET) for _ in range(length)])


def make_sentence():
    amount = r.randint(3, 10)
    sent = ' '.join([make_word() for _ in range(amount)])
    return sent


def check_input(user_input, sent):
    message = 'Поздравляем! Всё введено верно.'

    wrong_input = True
    while wrong_input:
        if user_input == sent:
            print(message)
            wrong_input = False
        else:
            print(sent)
            message = 'Попробуй еще раз:\n'
            user_input = input(message)


if __name__ == '__main__':
    wish = True
    while wish:
        sentence = make_sentence()
        print(sentence)
        user_sent = input('Повторите предложение:\n')
        check_input(user_sent, sentence)

        wish = input('Хотите ещё? да\\нет\n')
        wish = True if wish == 'да' else False

