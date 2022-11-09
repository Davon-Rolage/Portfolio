import os

import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk, filedialog
import re


root = tk.Tk()
root.geometry('800x480')


class Ui_MainWindow():
    def __init__(self, master):
        self.frm_open_file = tk.Frame(master)
        self.frm_main = tk.Frame(master)
        self.frm_report = tk.Frame(master)

        self.frm_open_file.grid(
            row=1, column=1, columnspan=2, sticky='nw', padx=10, pady=10)
        self.frm_main.grid(row=2, column=1, sticky='nw', padx=10)
        self.frm_report.grid(row=2, column=2, sticky='nswe')

        self.btn_open = tk.Button(
            self.frm_open_file, text='Open file', anchor='w', command=self.open_file)
        self.lbl_open = tk.Label(self.frm_open_file, text='', anchor='w')
        self.btn_proceed = tk.Button(self.frm_main, text='Proceed', height=2,
                                     width=15, background='#00ff7f', command=self.proceed)
        self.btn_save = tk.Button(
            self.frm_main, text='Save File', height=2, width=12, command=self.save_file)
        self.btn_open_report = tk.Button(
            self.frm_main, text='Open Report', pady=3, command=self.open_report)

        self.lbl_preview = tk.Label(self.frm_report, text='Preview')
        self.my_tree = ttk.Treeview(self.frm_report)

        self.btn_open.grid(row=1, column=1)
        self.lbl_open.grid(row=1, column=2)
        self.btn_proceed.grid(row=1, column=1)
        self.btn_save.grid(row=2, column=1, pady=15)
        self.btn_open_report.grid(row=3, column=1)

        self.lbl_preview.grid(row=1, column=1, sticky='w')

        self.filepath = self.file_destination = None

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
            message = "Couldn't find a column with phone numbers!"
            error_message = tk.messagebox.showerror(
                title="No phone numbers to format", message=message)
            return

        fin = [self.format_number(num) for num in self.df.iloc[:, num_column]]
        self.df['New Numbers'] = fin
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
            return f'{string} error'

        return '{} {}{}{} {}{}{} {}{} {}{}'.format(*number)

    def clear_tree(self):
        self.my_tree.delete(*self.my_tree.get_children())

    def save_file(self):
        if self.lbl_open['text'] == '':
            return
        self.file_destination = filedialog.asksaveasfilename(
            defaultextension='xlsx',
            initialfile='new_numbers',
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

        root.title(f'Saved at: {self.file_destination}')

    def open_report(self):
        if self.lbl_open['text'] == '':
            return
        
        print(self.file_destination)
        os.startfile(self.file_destination)

    # def lang_interface(self, user_lang):
    #     lang = {
    #         'eng': {
                
    #         },
    #         'rus': {

    #         }
    #     }


if __name__ == '__main__':
    MainWindow = Ui_MainWindow(root)
    root.mainloop()
