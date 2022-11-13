import tkinter as tk
import tkinter.font as font
from tkinter import ttk
from tkinter import messagebox


class Ui_MainWindow():
    def __init__(self, root):
        self.user_lang = 'eng'
        self.lang_interface()

        # Center the window upon opening
        window_height = 400
        window_width = 700
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x_coordinate = int((screen_width/2) - (window_width/2)) - 70
        y_coordinate = int((screen_height/2) - (window_height/2)) - 50
        root.geometry(
            "{}x{}+{}+{}".format(
                window_width,
                window_height,
                x_coordinate,
                y_coordinate
            )
        )

        menubar = tk.Menu(root)
        root.config(menu=menubar)
        menubar.add_cascade(
            label="What's new",
            command=self.show_new_features,
        )
        menubar.add_cascade(
            label='To be added',
            command=self.to_be_added
        )
        menubar.add_cascade(
            label='Changelog',
            command=self.changelog
        )

        self.font = font.Font(size=11)

        self.frm_main_upper = tk.Frame(root)
        self.frm_button = tk.Frame(root)
        self.frm_lang = tk.Frame(root)
        self.frm_tax_table = tk.Frame(root)

        self.frm_main_upper.grid(row=1, column=1)
        self.frm_button.grid(row=2, column=1, columnspan=2)
        self.frm_lang.grid(row=1, column=2, sticky='ne', padx=75, pady=30)
        self.frm_tax_table.grid(row=3, column=1, columnspan=2, pady=15)

        self.updated = tk.Label(root, text='last updated on Nov 13 2022', font=('Arial', 8))
        self.updated.place(x=500, y=5)

        self.lbl_choose_country = tk.Label(
            self.frm_main_upper,
            text=self.messages['lbl_choose_country'],
            font=self.font
        )
        self.lbl_income = tk.Label(
            self.frm_main_upper,
            text=self.messages['lbl_income'],
            font=self.font,
            width=30,
        )
        self.entry_income = tk.Entry(self.frm_main_upper, font=self.font, width=15)
        self.lbl_tax_rate_txt = tk.Label(
            self.frm_main_upper,
            text=self.messages['lbl_tax_rate_txt'],
            font=self.font
        )
        self.lbl_tax_rate = tk.Label(
            self.frm_main_upper, text='')
        self.btn_calculate_tax = tk.Button(
            self.frm_button,
            text=self.messages['btn_calculate_tax'],
            width=20,
            height=2,
            bg='#00ff7f',
            font=self.font,
            command=self.calculate_tax
        )
        self.lbl_tax_value_txt = tk.Label(
            self.frm_main_upper,
            text=self.messages['lbl_tax_value_txt'],
            font=self.font
        )
        self.lbl_tax_value = tk.Label(self.frm_main_upper, text='', font=self.font)
        self.lbl_net_income_txt = tk.Label(
            self.frm_main_upper,
            text=self.messages['lbl_net_income_txt'],
            font=self.font
        )
        self.lbl_net_income = tk.Label(self.frm_main_upper, text='', font=self.font)

        self.btn_eng = tk.Button(
            self.frm_lang, text='English', width=10, command=lambda: self.apply_lang('eng'))
        self.btn_rus = tk.Button(
            self.frm_lang, text='Русский', width=10, command=lambda: self.apply_lang('rus'))
        self.btn_esp = tk.Button(
            self.frm_lang, text='Español', width=10, command=lambda: self.apply_lang('esp'))
        
        self.btn_eng.grid(row=1, column=1)
        self.btn_rus.grid(row=2, column=1, pady=2)
        self.btn_esp.grid(row=3, column=1, pady=2)

        self.lbl_choose_country.grid(row=1, column=1, sticky='e')
        self.lbl_income.grid(row=2, column=1)
        self.lbl_income.config(anchor='e')
        self.entry_income.grid(row=2, column=2, sticky='w')
        self.lbl_tax_rate_txt.grid(row=3, column=1, sticky='e')
        self.lbl_tax_rate.grid(row=3, column=2, sticky='w')
        self.btn_calculate_tax.grid(
            row=4, column=1, columnspan=2, sticky='e')
        self.lbl_tax_value_txt.grid(row=6, column=1, sticky='e')
        self.lbl_tax_value.grid(row=6, column=2, sticky='w')
        self.lbl_net_income_txt.grid(row=5, column=1, sticky='e')
        self.lbl_net_income.grid(row=5, column=2, sticky='w')

        self.initialMenuText = tk.StringVar()
        self.initialMenuText.set(self.messages['country_lst'][0])
        self.apply_lang(self.user_lang)

    def lang_interface(self):
        self.country_abbr = {
            'Spain': ('esp', '€'),
            'France': ('fr', '€'),
            'Germany': ('de', '€'),
            'United Kingdom': ('uk', '£'),
            'USA': ('usa', '$'),
            'Brazil': ('br', 'R$'),
            'Russia': ('rus', '₽'),
            'India': ('in', '₹'),
            'China': ('cn', '¥'),
            'South Africa': ('sa', 'R')
        }
        self.lang_dct = {
            'eng': {
                'window_title': 'Personal Income Tax Calculator',
                'lbl_choose_country': 'Choose country:',
                'country_not_found_error': 'Choose country from the list',
                'lbl_income': 'Annual gross income:',
                'lbl_tax_rate_txt': 'Tax rate:',
                'lbl_tax_rate_error': 'Enter a valid number',
                'btn_calculate_tax': 'Calculate Tax',
                'lbl_tax_value_txt': 'Tax:',
                'lbl_net_income_txt': 'Net income:',
                'taxable_income_band': 'Taxable income band ',
                'income_tax_rates': 'National income tax rates',
                'single_tax': 'Single tax',
                'excess_over': 'of the excess over',
                'country_abbr': self.country_abbr,
                'country_lst': [
                    'Spain',
                    'France',
                    'Germany',
                    'United Kingdom',
                    'USA',
                    'Brazil',
                    'Russia',
                    'India',
                    'China',
                    'South Africa',
                ],
            },
            'rus': {
                'window_title': 'Калькулятор подоходного налога',
                'lbl_choose_country': 'Выберите страну:',
                'country_not_found_error': 'Выберите страну из списка',
                'lbl_income': 'Налогооблагаемый доход (за год):',
                'lbl_tax_rate_txt': 'Налоговая ставка:',
                'lbl_tax_rate_error': 'Введите корректное число',
                'btn_calculate_tax': 'Рассчитать налог',
                'lbl_tax_value_txt': 'НДФЛ:',
                'lbl_net_income_txt': 'Чистый доход:',
                'taxable_income_band': 'Налогооблагаемый доход, ',
                'income_tax_rates': 'Ставки подоходного налога',
                'single_tax': 'Единый налог',
                'excess_over': 'от суммы свыше',
                'country_abbr': self.country_abbr,
                'country_lst': [
                    'Испания',
                    'Франция',
                    'Германия',
                    'Великобритания',
                    'США',
                    'Бразилия',
                    'Россия',
                    'Индия',
                    'Китай',
                    'ЮАР',
                ],
            },
            'esp': {
                'window_title': 'Calculadora de IRPF (Impuesto sobre la renta de las personas físicas)',
                'lbl_choose_country': 'Elige país:',
                'country_not_found_error': 'Por favor, elija un país de la lista',
                'lbl_income': 'Ingresos anuales brutos:',
                'lbl_tax_rate_txt': 'Tasa de impuesto:',
                'lbl_tax_rate_error': 'Ingrese un número válido',
                'btn_calculate_tax': 'Calcular impuestos',
                'lbl_tax_value_txt': 'Impuesto:',
                'lbl_net_income_txt': 'Ganancia neta:',
                'taxable_income_band': 'Banda de renta imponible ',
                'income_tax_rates': 'Tasas de IRPF',
                'single_tax': 'Impuesto único',
                'excess_over': 'del exceso sobre',
                'country_abbr': self.country_abbr,
                'country_lst': [
                    'España',
                    'Francia',
                    'Alemania',
                    'Reino Unido',
                    'EE.UU',
                    'Brasil',
                    'Rusia',
                    'India',
                    'China',
                    'Sudáfrica',
                ],
            },
            'lang_template': {
                'window_title': '',
                'lbl_choose_country': '',
                'country_not_found_error': '',
                'lbl_income': '',
                'lbl_tax_rate_txt': '',
                'lbl_tax_rate_error': '',
                'btn_calculate_tax': '',
                'lbl_tax_value_txt': '',
                'lbl_net_income_txt': '',
                'taxable_income_band': '',
                'income_tax_rates': '',
                'single_tax': '',
                'excess_over': '',
                'country_abbr': self.country_abbr,
                'country_lst': [],
            }
        }
        self.messages = self.lang_dct[self.user_lang]

    def apply_lang(self, user_lang):
        self.messages = self.lang_dct[user_lang]

        root.title(self.messages['window_title'])
        self.lbl_choose_country['text'] = self.messages['lbl_choose_country']
        self.country_lst = self.messages['country_lst']

        self.lbl_income['text'] = self.messages['lbl_income']
        self.lbl_tax_rate_txt['text'] = self.messages['lbl_tax_rate_txt']
        self.btn_calculate_tax['text'] = self.messages['btn_calculate_tax']
        self.lbl_tax_value_txt['text'] = self.messages['lbl_tax_value_txt']
        self.lbl_net_income_txt['text'] = self.messages['lbl_net_income_txt']

        self.dropdown_menu = ttk.Combobox(
            self.frm_main_upper,
            font=self.font,
            value=self.country_lst
        )
        self.dropdown_menu.current(0)
        self.dropdown_menu.grid(row=1, column=2, sticky='w')

    def make_table(self, root):
        # Clear the table before making another table
        for widget in root.winfo_children():
            widget.destroy()

        for i in range(self.rows_count):
            for j in range(self.column_count):
                self.l = tk.Label(root, font=('Arial', 10))
                self.l['text'] = self.tax_table[i][j]
                self.l.config(width=len(self.l['text']))
                self.l.grid(row=i, column=j)


    def get_tax_table(self):
        self.tax_table_dct = {
            self.country_abbr['Spain']: [
                (self.messages['taxable_income_band'] + '€', self.messages['income_tax_rates']),
                ('1 – 12,450', '19%'),
                ('12,451 – 20,200', '24%'),
                ('20,201 – 35,200', '30%'),
                ('35,201 – 60,000', '37%'),
                ('60,001 +', '45%')
            ],
            self.country_abbr['France']: [
                (self.messages['taxable_income_band'] + '€', self.messages['income_tax_rates']),
                ('1 – 10,064', '0%'),
                ('10,065 – 25,659', '11%'),
                ('25,660 – 73,369', '30%'),
                ('73,370 – 157,806', '41%'),
                ('157,807 +', '45%')
            ],
            self.country_abbr['Germany']: [
                (self.messages['taxable_income_band'] + '€', self.messages['income_tax_rates']),
                ('0 – 9,984', '0%'),
                ('9,985 – 14,926', '14%'),
                ('14,927 – 58,596', '24%'),
                ('58,597 – 277,825', '42%'),
                ('277,826 +', '45%')
            ],
            self.country_abbr['United Kingdom']: [
                (self.messages['taxable_income_band'] +
                 '£', self.messages['income_tax_rates']),
                ('0 – 12,570', '0%'),
                ('12,571 – 14,667', '19%'),
                ('14,668 – 25,296', '20%'),
                ('25,297 – 43,662', '21%'),
                ('43,663 – 150,000', '41%'),
                ('150,001 +', '46%')
            ],
            self.country_abbr['USA']: [
                (self.messages['taxable_income_band'] + '$', self.messages['income_tax_rates']),
                ('0 – 10,275', '10%'),
                ('10,276 – 41,775', f"$1,027.50 + 12% {self.messages['excess_over']} $10,275"),
                ('41,776 – 89,075', f"$4,807.50 + 22% {self.messages['excess_over']} $41,775"),
                ('89,076 – 170,050', f"$15,213.50 + 24% {self.messages['excess_over']} $89,075"),
                ('170,051 – 215,950',
                 f"$34,647.50 + 32% {self.messages['excess_over']} $170,050"),
                ('215,951 – 539,900', f"$49,335.50 + 35% {self.messages['excess_over']} $215,950"),
                ('539,901 +', f"$162,718 + 37% {self.messages['excess_over']} $539,900")
            ],
            self.country_abbr['Brazil']: [
                (self.messages['taxable_income_band'] +'R$', self.messages['income_tax_rates']),
                (self.messages['single_tax'], '27.5%')
            ],
            self.country_abbr['Russia']: [
                (self.messages['taxable_income_band'] +
                 '₽', self.messages['income_tax_rates']),
                ('0 – 5,000,000', '13%'),
                ('5,000,001 +', '15%')
            ],
            self.country_abbr['India']: [
                (self.messages['taxable_income_band'] +
                 '₹', self.messages['income_tax_rates']),
                ('0 - 250,000', '0%'),
                ('250,001 – 500,000', '5%'),
                ('500,001 – 750,000', '10%'),
                ('750,001 – 1,000,000', '15%'),
                ('1,000,000 – 1,250,000', '20%'),
                ('1,250,001 – 1,500,000', '25%'),
                ('1,500,001 +', '30%')
            ],
            self.country_abbr['China']: [
                (self.messages['taxable_income_band'] +
                 '¥', self.messages['income_tax_rates']),
                ('0 – 36,000', '3%'),
                ('36,001 – 144,000', '10%'),
                ('144,001 – 300,000', '20%'),
                ('300,001 – 420,000', '25%'),
                ('420,001 – 660,000', '30%'),
                ('660,001 – 960,000', '35%'),
                ('960,001 +', '45%')
            ],
            self.country_abbr['South Africa']: [
                (self.messages['taxable_income_band'] +
                 'R', self.messages['income_tax_rates']),
                ('1 – 226,000', '18%'),
                ('226,001 – 353,100', f"40,680 + 26% {self.messages['excess_over']} 226,000"),
                ('353,101 – 488,700', f"73,726 + 31% {self.messages['excess_over']} 353,100"),
                ('488,701 – 641,400', f"115,762 + 36% {self.messages['excess_over']} 488,700"),
                ('641,401 – 817,600', f"170,734 + 39% {self.messages['excess_over']} 641,400"),
                ('817,601 – 1,731,600', f"239,452 + 41% {self.messages['excess_over']} 817,600"),
                ('1,731,601 +', f"614,192 + 45% {self.messages['excess_over']} 1,731,600")
            ],
        }
        self.tax_table = self.tax_table_dct[self.chosen_country]
        self.rows_count = len(self.tax_table)
        self.column_count = 2
        self.tax_table_object = self.make_table(self.frm_tax_table)

    def get_tax_rate(self):
        tax_table = self.tax_table[1:]
        lower_bounds_raw = [v[0].split(' – ')[0].strip() for v in tax_table]
        lower_bounds = []
        for bound in lower_bounds_raw:
            digit = ''
            for char in bound:
                if char.isdigit():
                    digit += char
            lower_bounds.append(digit)
        lower_bounds = list(map(lambda x: int(x), lower_bounds))

        tax_lst = [v[1] for v in tax_table]
        tax_lst = list(map(lambda x: x.rstrip('%'), tax_lst))
        tax_lst = [int(x)/100 for x in tax_lst]
        tax_rate_dct = {k: v for k, v in zip(lower_bounds, tax_lst)}
        
        for income, tax_rate in tax_rate_dct.items():
            if self.income >= income:
                self.tax_rate = tax_rate
                self.lbl_tax_rate['text'] = f'{tax_rate*100:.0f}%'        

    def calculate_tax(self):
        self.lbl_net_income['text'] = self.lbl_tax_value['text'] = ''

        chosen_country = self.dropdown_menu.get()
        try:
            country_id = self.messages['country_lst'].index(chosen_country)
        except ValueError:
            self.lbl_tax_rate.config(fg='red', font=('Times New Roman', 10), width=24, anchor='w')
            self.lbl_tax_rate['text'] = self.messages['country_not_found_error']

        self.chosen_country = list(self.country_abbr.values())[country_id]
        self.get_tax_table()

        try:
            self.income = float(self.entry_income.get())
        except ValueError:
            self.lbl_tax_rate['text'] = self.messages['lbl_tax_rate_error']
            self.lbl_tax_rate.config(fg='red', font=('Times New Roman', 10), width=22, anchor='w')
            self.lbl_tax_value['text'] = self.lbl_net_income['text'] = ''
            return

        self.get_tax_rate()
        self.lbl_tax_rate.config(font=self.font, fg='black', anchor='w')
        currency_symbol = self.chosen_country[1]

        tax_value = self.tax_rate * self.income
        net_income = self.income - tax_value

        lbl_net_income = f'{net_income:,.2f} {currency_symbol}'
        lbl_tax_value = f'{tax_value:,.2f} {currency_symbol}'

        # Right align tax value and net income
        length_tax_value = len(lbl_tax_value)
        delta = len(lbl_net_income) - len(lbl_tax_value)
        if delta:
            if delta == 1:
                lbl_tax_value = f'{tax_value:>{length_tax_value},.2f} {currency_symbol}'
            else:
                lbl_tax_value = f'{tax_value:>{length_tax_value+1},.2f} {currency_symbol}'

        self.lbl_net_income['text'] = lbl_net_income
        self.lbl_tax_value['text'] = lbl_tax_value

    def show_new_features(self):
        message = '''1) Added several countries
2) Added countries' taxe rates and currencies
3) Now supports English, Russian and Spanish
4) Added menubar'''
        messagebox.showinfo(title='Last update on Nov 13 2022', message=message)

    def to_be_added(self):
        message = '''            Future features:

1) Calculating taxes of USA and South Africa
2) Get rid of the 'Calculate Tax' button dislocation upon clicking
3) Support any user's thousands separator (12.005 or 12,005 or 12 005)
4) Converting from local currency to another
5) Support more languages
6) Support report saving
7) Add more options to menubar (Save, changelog)'''
        messagebox.showinfo(title='Features to be added', message=message)

    def changelog(self):
        message = '''Nobody here but us chickens!'''
        messagebox.showinfo(title='Changelog', message=message)


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Income Tax Calculator')
    MainWindow = Ui_MainWindow(root)
    root.mainloop()
