from user_lang import LangInterface

import tkinter as tk
import tkinter.font as font
from tkinter import ttk
from tkinter import messagebox
import pendulum


class Ui_MainWindow():
    def __init__(self, root):

        DEBUG = False
        self.update_date = 'last updated on Nov 15, 2022'

        self.user_lang = 'eng'
        self.messages = LangInterface(self.user_lang).messages

        # Center the window upon opening
        window_height = 400
        window_width = 650
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
        self.frm_separator = tk.Frame(root)
        self.frm_button = tk.Frame(root)
        self.frm_lang = tk.Frame(root)
        self.frm_tax_table = tk.Frame(root)

        self.frm_main_upper.grid(row=1, column=1)
        self.frm_separator.place(relx=.55, rely=.058)
        self.frm_button.place(relx=.33, rely=.35)
        self.frm_lang.place(relx=.77, rely=.02)
        self.frm_tax_table.place(relx=.19, rely=.52)

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
        self.entry_income = tk.Entry(self.frm_main_upper, font=self.font, width=14)

        self.lbl_sep = tk.Label(
            self.frm_separator, 
            text=self.messages['decimal_separator'], 
            width=10
        )
        self.lbl_sep.config(width=12)
        self.dropdown_sep = ttk.Combobox(
            self.frm_separator,
            value=['.', ','],
            width=1
        )
        self.dropdown_sep.current(0)
        self.dropdown_sep.config(font=4)
        self.lbl_sep.grid(row=2, column=3, sticky='e')
        self.dropdown_sep.grid(row=2, column=4, sticky='w')

        self.lbl_tax_rate_txt = tk.Label(
            self.frm_main_upper,
            text=self.messages['lbl_tax_rate_txt'],
            font=self.font
        )

        self.lbl_tax_rate = tk.Label(self.frm_main_upper, text='')
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
        self.btn_calculate_tax.grid(row=1, column=1)
        self.btn_calculate_tax.config(anchor='center')
        self.lbl_tax_value_txt.grid(row=6, column=1, sticky='e')
        self.lbl_tax_value.grid(row=6, column=2, sticky='w')
        self.lbl_net_income_txt.grid(row=5, column=1, sticky='e')
        self.lbl_net_income.grid(row=5, column=2, sticky='w')

        self.initialMenuText = tk.StringVar()
        self.initialMenuText.set(self.messages['country_lst'][0])
        self.apply_lang(self.user_lang)

        if DEBUG:
            self.now = pendulum.now().to_formatted_date_string()

            self.frm_debug = tk.Frame(root)
            self.frm_debug.place(x=.01, y=.01)

            self.lbl_config_on = tk.Label(
                self.frm_debug, text="DEBUG IS ON", bg='yellow')
            self.lbl_config_on.grid(row=1, column=1, sticky='w')

            self.lbl_update_date = tk.Label(
                self.frm_debug,
                text=f'{self.update_date}\n\ncurrent date: {self.now}',
                font=('Arial', 8),
                bg='yellow'
            )
            self.lbl_update_date.grid(row=3, column=1, columnspan=2)

    def apply_lang(self, user_lang):
        self.messages = LangInterface(user_lang).messages

        root.title(self.messages['window_title'])
        self.lbl_choose_country['text'] = self.messages['lbl_choose_country']
        self.country_lst = self.messages['country_lst']

        self.lbl_income['text'] = self.messages['lbl_income']
        self.lbl_sep['text'] = self.messages['decimal_separator']
        self.lbl_tax_rate_txt['text'] = self.messages['lbl_tax_rate_txt']
        self.btn_calculate_tax['text'] = self.messages['btn_calculate_tax']
        self.lbl_tax_value_txt['text'] = self.messages['lbl_tax_value_txt']
        self.lbl_net_income_txt['text'] = self.messages['lbl_net_income_txt']

        self.lbl_sep.config(anchor='e')

        self.dropdown_menu = ttk.Combobox(
            self.frm_main_upper,
            font=self.font,
            value=self.country_lst,
            width=14
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
                (self.messages['taxable_income_band']+'€', self.messages['income_tax_rates']),
                ('0 – 12,450', '19%'),
                ('12,451 – 20,200', '24%'),
                ('20,201 – 35,200', '30%'),
                ('35,201 – 60,000', '37%'),
                ('60,001 +', '45%')
            ],
            self.country_abbr['France']: [
                (self.messages['taxable_income_band']+'€', self.messages['income_tax_rates']),
                ('0 – 10,064', '0%'),
                ('10,065 – 25,659', '11%'),
                ('25,660 – 73,369', '30%'),
                ('73,370 – 157,806', '41%'),
                ('157,807 +', '45%')
            ],
            self.country_abbr['Germany']: [
                (self.messages['taxable_income_band']+'€', self.messages['income_tax_rates']),
                ('0 – 9,984', '0%'),
                ('9,985 – 14,926', '14%'),
                ('14,927 – 58,596', '24%'),
                ('58,597 – 277,825', '42%'),
                ('277,826 +', '45%')
            ],
            self.country_abbr['United Kingdom']: [
                (self.messages['taxable_income_band']+'£', self.messages['income_tax_rates']),
                ('0 – 12,570', '0%'),
                ('12,571 – 14,667', '19%'),
                ('14,668 – 25,296', '20%'),
                ('25,297 – 43,662', '21%'),
                ('43,663 – 150,000', '41%'),
                ('150,001 +', '46%')
            ],
            self.country_abbr['USA']: [
                (self.messages['taxable_income_band']+'$', self.messages['income_tax_rates']),
                ('0 – 10,275', '10%'),
                ('10,276 – 41,775', f"$1,027.50 + 12% {self.messages['excess_over']} $10,275"),
                ('41,776 – 89,075', f"$4,807.50 + 22% {self.messages['excess_over']} $41,775"),
                ('89,076 – 170,050', f"$15,213.50 + 24% {self.messages['excess_over']} $89,075"),
                ('170,051 – 215,950', f"$34,647.50 + 32% {self.messages['excess_over']} $170,050"),
                ('215,951 – 539,900', f"$49,335.50 + 35% {self.messages['excess_over']} $215,950"),
                ('539,901 +', f"$162,718 + 37% {self.messages['excess_over']} $539,900")
            ],
            self.country_abbr['Brazil']: [
                (self.messages['taxable_income_band']+'R$', self.messages['income_tax_rates']),
                (self.messages['single_tax'], '27.5%')
            ],
            self.country_abbr['Russia']: [
                (self.messages['taxable_income_band']+'₽', self.messages['income_tax_rates']),
                ('0 – 5,000,000', '13%'),
                ('5,000,001 +', '15%')
            ],
            self.country_abbr['India']: [
                (self.messages['taxable_income_band']+'₹', self.messages['income_tax_rates']),
                ('0 - 250,000', '0%'),
                ('250,001 – 500,000', '5%'),
                ('500,001 – 750,000', '10%'),
                ('750,001 – 1,000,000', '15%'),
                ('1,000,000 – 1,250,000', '20%'),
                ('1,250,001 – 1,500,000', '25%'),
                ('1,500,001 +', '30%')
            ],
            self.country_abbr['China']: [
                (self.messages['taxable_income_band']+'¥', self.messages['income_tax_rates']),
                ('0 – 36,000', '3%'),
                ('36,001 – 144,000', '10%'),
                ('144,001 – 300,000', '20%'),
                ('300,001 – 420,000', '25%'),
                ('420,001 – 660,000', '30%'),
                ('660,001 – 960,000', '35%'),
                ('960,001 +', '45%')
            ],
            self.country_abbr['South Africa']: [
                (self.messages['taxable_income_band']+'R', self.messages['income_tax_rates']),
                ('0 – 226,000', '18%'),
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

        # If tax is single, lower bound is set to 0, else convert all lower bounds to integers.
        self.lower_bounds = [0] if lower_bounds == [''] else list(map(lambda x: int(x), lower_bounds))

        if self.chosen_country[0] in ['usa', 'sa']:
            self.get_complex_tax()

        else:
            tax_lst = [v[1] for v in tax_table]
            tax_lst = list(map(lambda x: x.rstrip('%'), tax_lst))
            tax_lst = [float(x)/100 for x in tax_lst]

            tax_rate_dct = {k: v for k, v in zip(self.lower_bounds, tax_lst)}

            for income, tax_rate in tax_rate_dct.items():
                if self.income >= income:
                    self.tax_rate = tax_rate
                    self.lbl_tax_rate['text'] = f'{tax_rate*100:.1f}%'

    def get_complex_tax(self):
        tax_table = self.tax_table[1:]
        tax_table = [tax_table[i][1] for i in range(len(tax_table))]

        min_tax_lst_raw = list(map(lambda x: x.split(' + ')[0], tax_table))
        min_tax_lst = []
        for tax in min_tax_lst_raw:
            digit = ''
            for char in tax:
                if char.isdigit() or char == '.':
                    digit += char
            min_tax_lst.append(float(digit))

        tax_lst = []
        for tax in tax_table:
            try:
                tax = tax.split('+')[1].strip()
            except IndexError:
                pass
            tax = tax.split('%')[0]
            tax = float(tax) / 100
            tax_lst.append(tax)

            tax_rate_dct = {k: v for k, v in zip(self.lower_bounds, tax_lst)}
            for i, (lower_bound, tax_rate) in enumerate(tax_rate_dct.items()):
                if self.income >= lower_bound:
                    self.taxable_income = self.income - lower_bound
                    self.minimal_tax = min_tax_lst[i]
                    self.tax_rate = tax_rate
                    self.lbl_tax_rate['text'] = f'{tax_rate*100:.1f}%'

    def calculate_tax(self):
        self.minimal_tax = 0

        self.lbl_net_income['text'] = self.lbl_tax_value['text'] = ''
        chosen_country = self.dropdown_menu.get()
        try:
            self.country_abbr = LangInterface().country_abbr
            country_id = self.messages['country_lst'].index(chosen_country)
        except ValueError:
            self.lbl_tax_rate.config(fg='red', font=(
                'Times New Roman', 10), width=24, anchor='w')
            self.lbl_tax_rate['text'] = self.messages['country_not_found_error']
        
        self.chosen_country = list(self.country_abbr.values())[country_id]
        self.get_tax_table()
        try:
            self.income = ''
            sep = self.dropdown_sep.get()
            for char in self.entry_income.get():
                if char.isdigit() or char == sep:
                    self.income += char
                elif char in [',', '.', ' ']:
                    pass
                else:
                    raise ValueError
            self.income = self.income.replace(sep, '.')
            self.income = float(self.income)
            self.taxable_income = self.income

        except ValueError:
            self.lbl_tax_rate['text'] = self.messages['lbl_tax_rate_error']
            self.lbl_tax_rate.config(
                fg='red', width=22, anchor='w',
                font=('Times New Roman', 10)
            )
            self.lbl_tax_value['text'] = self.lbl_net_income['text'] = ''
            return

        self.get_tax_rate()
        self.lbl_tax_rate.config(font=self.font, fg='black', anchor='w')
        currency_symbol = self.chosen_country[1]

        tax_value = self.tax_rate * self.taxable_income + self.minimal_tax
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
        update_date = self.update_date
        message = '''1) Now calculates taxes for the USA and South Africa
2) Button doesn't dislocate upon clicking
3) User can specify decimal separator
4) Added DEBUG state'''
        messagebox.showinfo(
            title=update_date, message=message)

    def to_be_added(self):
        message = '''- Converting from local currency to another
- Full translation of language interface
- Support more languages
- Tax report saving
'''
        messagebox.showinfo(title='Features to be added', message=message)

    def changelog(self):
        log_window = tk.Tk()
        log_window.title('Changelog')
        log_window.geometry('600x500')
        txt_changelog = tk.Text(log_window)

        with open('changelog.txt', 'r') as f:
            log = f.read()        
        
        txt_changelog.insert('1.0', log)
        txt_changelog.pack(expand=True, fill=tk.BOTH)
        txt_changelog.config(state=tk.DISABLED)


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Income Tax Calculator')
    MainWindow = Ui_MainWindow(root)
    root.mainloop()
