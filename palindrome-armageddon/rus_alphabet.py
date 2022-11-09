# Сделаем список букв русского алфавита с помощью символов Юникода, используя функцию chr()
# Make a comprehension list using chr() function in Unicode range of Russian letters
letters = ''.join([chr(i) for i in range(1072, 1104)])

# Добавим в список букву ё, которая в символах Юникода стоит после буквы "я" (с кодом 1105)
# Add a tricky letter ё ('yo') to the list (Unicode code for ё is 1105)
letters_with_yo = letters[:6] + chr(ord('ё')) + letters[6:]

rus_lowercase = letters_with_yo
rus_uppercase = letters_with_yo.upper()
rus_letters = rus_lowercase + rus_uppercase

# rus_lowercase — строчные буквы русского алфавита
# rus_uppercase — заглавные буквы
# rus_letters — и строчные и заглавные буквы
