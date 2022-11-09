import sys
import os

import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk, filedialog
import re


class Ui_MainWindow():
    def __init__(self, master):
        self.user_lang = 'rus'
        self.lang_interface()

        self.frm_open_file = tk.Frame(master, width=100)
        self.frm_main = tk.Frame(master)
        self.frm_lang = tk.Frame(self.frm_main)
        self.frm_report = tk.Frame(master)

        self.frm_open_file.grid(
            row=1, column=1, columnspan=2, sticky='nw', padx=10, pady=10)
        self.frm_lang.grid(row=5, column=1, sticky='ne', pady=20)
        self.frm_main.grid(row=2, column=1, sticky='nw', padx=10)
        self.frm_report.grid(row=2, column=2, sticky='nswe')

        self.btn_open = tk.Button(
            self.frm_open_file,
            text=self.messages['btn_open'],
            anchor='w',
            bg='#FFFACD',
            command=self.open_file
        )
        self.lbl_open = tk.Label(
            self.frm_open_file, text='', anchor='w', padx=10)

        self.btn_proceed = tk.Button(self.frm_main, text=self.messages['btn_proceed'], height=2,
                                     width=16, background='#00ff7f', command=self.proceed)
        self.btn_save = tk.Button(
            self.frm_main, text=self.messages['btn_save'], height=2, width=14, command=self.save_file)
        self.btn_open_report = tk.Button(
            self.frm_main, text=self.messages['btn_open_report'], pady=3, command=self.open_report)

        self.lbl_preview = tk.Label(
            self.frm_report, text=self.messages['lbl_preview'])
        self.my_tree = ttk.Treeview(self.frm_report)

        self.btn_rus = tk.Button(
            self.frm_lang, width=8, text='Русский', command=lambda: self.apply_lang('rus'))
        self.btn_eng = tk.Button(
            self.frm_lang, width=8, text='English', command=lambda: self.apply_lang('eng'))

        self.btn_exit = tk.Button(
            self.frm_lang, width=7, text=self.messages['btn_exit'], command=sys.exit)

        self.btn_open.grid(row=1, column=1)
        self.lbl_open.grid(row=1, column=2)
        self.btn_proceed.grid(row=1, column=1)
        self.btn_save.grid(row=2, column=1, pady=15)
        self.btn_open_report.grid(row=3, column=1)

        self.lbl_preview.grid(row=1, column=1, sticky='w')
        self.btn_rus.grid(row=1, column=1, padx=3, pady=10)
        self.btn_eng.grid(row=1, column=2)
        self.btn_exit.grid(row=2, column=1, pady=7, sticky='w', padx=3)

        self.apply_lang(self.user_lang)
        self.filepath = self.file_destination = None

        self.frm_ideas = tk.Frame(master)
        self.lbl_ideas = tk.Label(
            self.frm_ideas,
            justify='left',
            text='''            ***New Features***
        1. Add regular expression to phone numbers
        2. Make new column adjacent to old phone numbers
        3. Get rid of the second-row-checking bug
        4. Align all buttons and make width equal for all languages
        5. Add \'Reset Report\' button'''
        )
        self.frm_ideas.grid(row=9, column=1, columnspan=2, sticky='nw')
        self.lbl_ideas.grid(row=1, column=1)

    def open_file(self) -> str:
        self.filepath = filedialog.askopenfilename(
            filetypes=(
                ('All Files', '*.*'),
                ('Excel Files', '*.xlsx'),
                ('Text files', '*.txt'),
            )
        )
        if not self.filepath:
            return

        self.file_extension = self.filepath.rpartition('.')[-1]
        self.lbl_open['text'] = self.filepath
        self.clear_tree()
        self.get_contents()

    def get_contents(self):
        if self.file_extension == 'txt':
            self.df = pd.read_csv(self.filepath, sep=' ', header=None)

        elif self.file_extension == 'xlsx':
            self.df = pd.read_excel(self.filepath)

        self.make_tree()

    def make_tree(self):
        self.my_tree['column'] = list(self.df.columns)
        self.my_tree['show'] = 'headings'

        for column in self.my_tree['column']:
            self.my_tree.heading(column, text=column)

        df_rows = self.df.to_numpy().tolist()
        for row in df_rows:
            self.my_tree.insert('', 'end', values=row)

        self.my_tree.grid(row=2, column=1)

    def proceed(self):
        if self.lbl_open['text'] == '':
            return
        num_column = None
        for i in range(len(self.df.columns)):
            result = self.format_number(self.df.iloc[1, i])
            is_result = re.search('[0-9] [0-9]{3} * [0-9]', result)
            if is_result:
                num_column = i
                break
        else:
            no_phone_column_error = self.messages['no_phone_column_error']
            tk.messagebox.showerror(
                title=self.messages['no_phone_column_error_title'], message=no_phone_column_error)
            return

        fin = [self.format_number(num) for num in self.df.iloc[:, num_column]]
        self.df[self.messages['new_numbers_column_title']] = fin
        self.clear_tree()
        self.make_tree()

    def format_number(self, string) -> str:
        string = str(string)
        number = ''
        try:
            for char in string:
                if char.isdigit():
                    number += char
        except Exception:
            raise Exception

        if len(number) != 11:
            return f'{string} {self.messages["phone_error"]}'

        return '{} {}{}{} {}{}{} {}{} {}{}'.format(*number)

    def clear_tree(self):
        self.my_tree.delete(*self.my_tree.get_children())

    def save_file(self):
        if self.lbl_open['text'] == '':
            return

        self.file_destination = filedialog.asksaveasfilename(
            defaultextension='xlsx',
            initialfile=self.messages['default_file_name'],
            filetypes=(
                ('xlsx files', '*.xlsx'),
                ('Text files', '*.txt'),
            )
        )
        if not self.file_destination:
            return

        self.saved_file_extension = self.file_destination.rpartition('.')[-1]
        if self.saved_file_extension == 'xlsx':
            self.df.to_excel(self.file_destination, index=False)

        elif self.saved_file_extension == 'txt':
            self.df.to_csv(self.file_destination, sep=' ', index=False)

        root.title(f'{self.messages["saved_at"]} {self.file_destination}')

    def open_report(self):
        if not self.file_destination:
            return

        print(self.file_destination)
        os.startfile(self.file_destination)

    def lang_interface(self):
        self.lang_dct = {
            'eng': {
                'window_title': 'Phone Number Formatting',
                'btn_open': 'Open file',
                'btn_proceed': 'Format Numbers',
                'btn_save': 'Save file',
                'btn_open_report': 'Open Report',
                'lbl_preview': 'Preview',
                'no_phone_column_error': "Couldn't find a column with phone numbers!",
                'no_phone_column_error_title': 'No phone numbers to format',
                'new_numbers_column_title': 'New Numbers',
                'phone_error': 'error',
                'default_file_name': 'new_numbers',
                'saved_at': 'Saved at:',
                'btn_exit': 'Exit'
            },
            'rus': {
                'window_title': 'Форматирование номеров телефона',
                'btn_open': 'Открыть',
                'btn_proceed': 'Форматировать',
                'btn_save': 'Сохранить файл',
                'btn_open_report': 'Открыть отчёт',
                'lbl_preview': 'Предварительный просмотр',
                'no_phone_column_error': "Не удалось найти колонки с номерами телефона!",
                'no_phone_column_error_title': 'Нет телефона для форматирования',
                'new_numbers_column_title': 'Новые номера телефона',
                'phone_error': 'ошибка',
                'default_file_name': 'новые_номера_телефона',
                'saved_at': 'Сохранено в:',
                'btn_exit': 'Выйти'
            }
        }
        self.messages = self.lang_dct[self.user_lang]

    def apply_lang(self, user_lang):
        self.messages = self.lang_dct[user_lang]

        root.title(self.messages['window_title'])
        self.btn_open['text'] = self.messages['btn_open']
        self.btn_proceed['text'] = self.messages['btn_proceed']
        self.btn_save['text'] = self.messages['btn_save']
        self.btn_open_report['text'] = self.messages['btn_open_report']
        self.lbl_preview['text'] = self.messages['lbl_preview']
        self.btn_exit['text'] = self.messages['btn_exit']


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('800x480')
    MainWindow = Ui_MainWindow(root)
    root.mainloop()
