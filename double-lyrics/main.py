# To install Google Translator module, use `pip install googletrans==4.0.0-rc1` in the Terminal window

from googletrans import Translator
from timer import Timer

translator = Translator()


def main():
    # Start the Timer using context manager
    with Timer(text='Elapsed time: {:0.2f} seconds'):
        
        # Choose the desired output language (line 13) and the source file location (line 14)
        # english = 'en', russian = 'ru', georgian = 'ka', spanish = 'es', french = 'fr', german = 'de'
        final_lang = 'ru'
        source_file = r'C:\Downloads\მონატრებიხარ ფიქრებს.txt'

        with open(source_file, encoding='utf8') as f:
            source_lines = f.readlines()
        
        # Get rid of the '\n' characters at the strings' end
        source_lines = list(map(lambda x: x.strip(), source_lines))

        fin = ''
        for source_line in source_lines:
            if not source_line == '':
                # Use .translate method to translate source_line into your desired language
                trans_line = translator.translate(source_line, dest=final_lang)
                fin += source_line + '\n'
                fin += trans_line.text + '\n\n'

        title = translator.translate(source_lines[0], dest=final_lang).text
        
        # Check the title for invalid characters and remove them
        for char in r'\/:*?"<>|':
            if char in title:
                title = ''.join(list(filter(lambda ch: ch != char, title)))

        # Choose the desired file destination. {title} takes the first translated line as a title
        file_destination = rf'C:\Downloads\{title}.txt'

        with open(file_destination, 'w+', encoding='utf8') as f:
            for line in fin:
                f.write(line)

        print(f'The file is saved at: {file_destination}')

if __name__ == '__main__':
    main()
