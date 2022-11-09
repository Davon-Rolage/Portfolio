# Make a comprehension list using chr() function in Unicode range of Russian letters
letters = ''.join([chr(i) for i in range(1072, 1104)])

# Add a tricky letter ё ('yo') to the list (Unicode code for ё is 1105)
letters_with_yo = letters[:6] + chr(ord('ё')) + letters[6:]

rus_lowercase = letters_with_yo
rus_uppercase = letters_with_yo.upper()
rus_letters = rus_lowercase + rus_uppercase
