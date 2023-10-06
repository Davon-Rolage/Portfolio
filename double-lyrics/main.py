import os

from googletrans import Translator

from timer import Timer


def main():
    translator = Translator()
    with Timer(text='Elapsed time: {:0.2f} seconds'):
        # english = 'en', russian = 'ru', georgian = 'ka', spanish = 'es', french = 'fr', german = 'de'
        final_lang = 'en'
        source_file = os.getcwd() + '\\original_text.txt'

        with open(source_file, encoding='utf-8') as f:
            source_lines = f.readlines()
            source_lines = [line for line in source_lines if line.strip()]
        
        source_lines = list(map(lambda x: x.strip(), source_lines))

        fin = ''
        num_source_lines = len(source_lines)
        for i, source_line in enumerate(source_lines, start=1):
            trans_line = translator.translate(source_line, dest=final_lang)
            print(f'Processed {i}/{num_source_lines} lines', end='\r')
            fin += f"{source_line}\n{trans_line.text}\n\n"

        title = 'result'
        
        # Check the title for invalid characters and remove them
        for char in r'\/:*?"<>|':
            if char in title:
                title = ''.join(list(filter(lambda ch: ch != char, title)))

        file_destination = f"{os.getcwd()}\\{title}.txt"

        with open(file_destination, 'w', encoding='utf-8') as f:
            for line in fin:
                f.write(line)

        print(f'The file is saved at:\n{file_destination}')
        os.startfile(file_destination)

if __name__ == '__main__':
    main()
