# russian-alphabet
The code adds strings of Russian letters in lowercase and uppercase.
It includes three variables *rus_lowercase*, *rus_uppercase*, and *rus_letters* similar to *ascii_letters* used in the *string* library.

There is a **join** method in addition to the **list comprehension** where russian letters are found using Unicode codes in range 1072-1104.

Variable *letters_with_yo* adds an additional character ***ё*** whose Unicode code is 1105. As you can see, the **slice** method is used to separate two parts of the alphabet where ё is to be located.

Lastly, *letters_with_yo* is assigned to the variable *rus_lowercase* and the method ***upper()*** is used to capitalise letters in the alphabet. Variable ***rus_letters*** contains all of the Russian letters, both lowercase and uppercase.
________
# русский-алфавит
Этот код добавляет строки русских букв в нижнем и верхнем регистрах.
Он включает в себя три переменные *rus_lowercase*, *rus_uppercase* и *rus_letters* похожие на метод ***ascii_letters*** библиотеки **string**.

В переменной *letters* используется метод *join*, а внутри инициализируется список, в котором с помощью функции ***chr()*** находятся символы по таблице Юникод в диапазоне 1072-1104. Здесь отсутствует буква ***ё***.

В переменной *letters_with_yo* строка с буквами делится на две части с помощью слайса (среза), чтобы добавить символ ***ё*** между ними.

Наконец, переменной rus_lowercase присваивается значение переменной *letters_with_yo*, переменной rus_uppercase — *letters_with_yo*, но с добавлением метода ***upper()***, чтобы озаглавить буквы; и переменная *rus_letters* включает в себя буквы и верхнего и нижнего регистров.
