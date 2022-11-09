import os
import sys
import pandas as pd
import secrets as s
from math import sqrt
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import matplotlib.pyplot as plt
import seaborn as sns
from math import factorial
from time import time


class Figure:
    # Figure = Показатель
    def __init__(self, name, rus_name, size, average, general_average,
                 standard_deviation, mrg_error, confidence_interval, is_in_confidence_interval):
        self.name = name
        self.rus_name = rus_name
        self.size = size
        self.average = average
        self.general_average = general_average
        self.std = standard_deviation
        self.mrg_err = mrg_error
        self.conf_interval = ' <= '.join([str(char) for char in confidence_interval])
        self.is_in_conf_interval = is_in_confidence_interval

    def describe(self):
        # Capitalize the first letter of the English name + add Russian name
        return (f'''{self.name[0].upper() + self.name[1:]} ({self.rus_name})
Sample size: {self.size}
Sample average {self.name}: {self.average:.3f}
Standard deviation: {self.std:.3f}
Marginal error: {self.mrg_err:.3f}
Confidence interval: {self.conf_interval}

Statistical population mean value of {self.name}: {self.general_average:.2f}
--Check whether statistical population average corresponds with the confidence interval:
{self.is_in_conf_interval}
_____''')


def how_many_combinations(a, b):
    fin = factorial(b) / (factorial(a) * factorial(b - a))
    fin_text = f'''Number of possible samples of size n = {a} for N = {b} is:
{fin:,.0f}'''
    return fin_text


def marginal_error(n, std, t_value):
    # Расчет предельной ошибки.
    return t_value * sqrt(std ** 2 / n)


def get_conf_interval(mean_value, error, title='value'):
    # Построение доверительного интервала.
    lower_bound = mean_value - error
    upper_bound = mean_value + error
    return [round(lower_bound, 2), title, round(upper_bound, 2)]


def check_conf_interval(stat_population_mean, lower_bound, upper_bound, title='value'):
    # Проверка, входит ли генеральная средняя в доверительный интервал.
    # Statistical population mean = Средняя генеральной совокупности.
    if lower_bound <= stat_population_mean <= upper_bound:
        # print(f'Population mean for {title} is within the confidence interval!')
        message = f'{lower_bound:.1f} <= {stat_population_mean:.2f} <= {upper_bound:.2f} ({title})'
        return message

    # print(f'Unfortunately, population mean for {title} is not within the confidence interval:')
    if stat_population_mean < lower_bound:
        return f'__{stat_population_mean:.3f}__ < {lower_bound:.3f} < {upper_bound:.1f} ({title})'

    return f'{lower_bound:.1f} < {upper_bound:.3f} < __{stat_population_mean:.3f}__ ({title})'


def open_file():
    global file_location
    filepath = askopenfilename(
        filetypes=(
            ('CSV Files', '*.csv'),
            ('Text Files', '*.txt'),
            ('All Files', '*.*'),
        )
    )
    if not filepath:
        return
    lbl_open['text'] = filepath
    file_location = filepath


def save_file():
    global file_destination
    filepath = asksaveasfilename(
        defaultextension='.txt',
        filetypes=[
            ('Text Files', '*.txt'),
            ('All Files', '*.*'),
        ]
    )
    if not filepath:
        return
    with open(filepath, mode='w', encoding='utf8') as output_file:
        text = txt_report.get('1.0', tk.END)
        output_file.write(text)

    window.title(f'Расчет доверительных интервалов - {filepath}')
    file_destination = filepath


def decrease_1000():
    initial_size = int(lbl_size['text'])
    fin_size = initial_size - 1000
    if fin_size < 1:
        lbl_size['text'] = '1'
    else:
        lbl_size['text'] = fin_size


def decrease_100():
    initial_size = int(lbl_size['text'])
    fin_size = initial_size - 100
    if fin_size < 1:
        lbl_size['text'] = '1'
    else:
        lbl_size['text'] = fin_size


def increase_100():
    initial_size = int(lbl_size['text'])
    fin_size = initial_size + 100
    lbl_size['text'] = fin_size if fin_size <= 20000 else '20000'


def increase_1000():
    initial_size = int(lbl_size['text'])
    fin_size = initial_size + 1000
    lbl_size['text'] = fin_size if fin_size <= 20000 else '20000'


def reset_iterations():
    lbl_size['text'] = '1000'


def show_plots():
    global boot_population
    global boot_income
    global boot_consumption

    sns.set_style('darkgrid')
    fig, axes = plt.subplots(1, 3)

    ax1 = sns.histplot(boot_population, kde=True, ax=axes[0], legend=False)
    ax1.set_xlabel('Средняя численность населения')
    ax1.set_ylabel('Частота')

    ax2 = sns.histplot(boot_income, kde=True, ax=axes[1], legend=False)
    ax2.set_xlabel('Среднедушевые доходы населения')
    ax2.set_ylabel('Частота')

    ax3 = sns.histplot(boot_consumption, kde=True, ax=axes[2], legend=False)
    ax3.set_xlabel('Среднедушевые расходы населения')
    ax3.set_ylabel('Частота')

    plt.show()


def clear():
    lbl_open['text'] = "Specify file's location"
    txt_report.delete('1.0', tk.END)


def revert_changes():
    global report_backup
    txt_report.delete('1.0', tk.END)
    txt_report.insert(tk.END, report_backup)


def open_report():
    global file_destination
    os.startfile(file_destination)


def make_calculations():
    start_clock = time()
    global file_location
    global file_destination
    global boot_population
    global boot_income
    global boot_consumption
    global report_backup
    global iterations

    df = pd.read_csv(file_location, encoding='utf8', delimiter=';')
    old_columns = df.columns
    new_columns = ['Субъект', 'Доходы', 'Расходы', 'Мужчины', 'Женщины']
    for i in range(len(old_columns)):
        df.rename(inplace=True, columns={df.columns[i]: new_columns[i]})

    df['Женщины'] = df['Женщины'].apply(lambda x: float(x.split(',', 1)[0]))
    df['Субъект'] = df['Субъект'].apply(lambda x: x.split(',')[1].strip())

    df['Население'] = df['Мужчины'] + df['Женщины']

    # Must specify column's name (Мужчины, Женщины или Население)
    average_population = round(df['Население'].mean(numeric_only=True), 3)
    average_income = round(df['Доходы'].mean(numeric_only=True), 3)
    average_consumption = round(df['Расходы'].mean(numeric_only=True), 3)

    sample_size = s.choice(list(range(50, 60)))

    iterations = int(lbl_size.cget('text'))
    boot_population = []
    boot_income = []
    boot_consumption = []
    for i in range(iterations):
        sample = df.sample(n=sample_size)
        boot_population_mean = sample['Население'].mean(numeric_only=True)
        boot_population.append(boot_population_mean)

        boot_income_mean = sample['Доходы'].mean(numeric_only=True)
        boot_income.append(boot_income_mean)

        boot_consumption_mean = sample['Расходы'].mean(numeric_only=True)
        boot_consumption.append(boot_consumption_mean)

    boot_population = pd.DataFrame(boot_population)
    boot_income = pd.DataFrame(boot_income)
    boot_consumption = pd.DataFrame(boot_consumption)

    boot_population_mean = list(boot_population.mean())[0]
    boot_income_mean = list(boot_income.mean())[0]
    boot_consumption_mean = list(boot_consumption.mean())[0]

    sample_income_deviation = df['Доходы'].apply(lambda x: (x - boot_income_mean) ** 2)
    sample_income_std = sqrt(sum(sample_income_deviation) / sample_size)
    sample_consumption_deviation = df['Расходы'].apply(lambda x: (x - boot_consumption_mean) ** 2)
    sample_consumption_std = sqrt(sum(sample_consumption_deviation / sample_size))

    sample_population_deviation = df['Население'].apply(lambda x: (x - boot_population_mean) ** 2)
    sample_population_std = sqrt(sum(sample_population_deviation / sample_size))

    alpha = 0.05
    t = 2
    income_marginal_error = marginal_error(sample_size, sample_income_std, t)
    consumption_marginal_error = marginal_error(sample_size, sample_consumption_std, t)
    population_marginal_error = marginal_error(sample_size, sample_population_std, t)

    income_conf_interval = get_conf_interval(
        boot_income_mean,
        income_marginal_error,
        'average income'
    )
    consumption_conf_interval = get_conf_interval(
        boot_consumption_mean,
        consumption_marginal_error,
        'average consumption'
    )
    population_conf_interval = get_conf_interval(
        boot_population_mean,
        population_marginal_error,
        'average population'
    )

    income = Figure(
        name='consumer income in RUB',
        rus_name='Среднедушевые денежные доходы населения, руб./мес.',
        size=sample_size,
        average=boot_income_mean,
        general_average=average_income,
        standard_deviation=sample_income_std,
        mrg_error=income_marginal_error,
        confidence_interval=income_conf_interval,
        is_in_confidence_interval=check_conf_interval(
            average_income,
            income_conf_interval[0],
            income_conf_interval[2],
            'income'
        )
    )
    consumption = Figure(
        name='consumer spending in RUB',
        rus_name='Расходы на потребление, руб.',
        size=sample_size,
        average=boot_consumption_mean,
        general_average=average_consumption,
        standard_deviation=sample_consumption_std,
        mrg_error=consumption_marginal_error,
        confidence_interval=consumption_conf_interval,
        is_in_confidence_interval=check_conf_interval(
            average_consumption,
            consumption_conf_interval[0],
            consumption_conf_interval[2],
            'consumption'
        )
    )

    population = Figure(
        name='population in thousand persons',
        rus_name='Население, тыс. чел.',
        size=sample_size,
        average=boot_population_mean,
        general_average=average_population,
        standard_deviation=sample_population_std,
        mrg_error=population_marginal_error,
        confidence_interval=population_conf_interval,
        is_in_confidence_interval=check_conf_interval(
            average_population,
            population_conf_interval[0],
            population_conf_interval[2],
            'population'
        )
    )

    income_report = income.describe()
    consumption_report = consumption.describe()
    population_report = population.describe()
    end_clock = time()
    report = f'''It took {end_clock - start_clock:.2f} seconds to complete the report.
{how_many_combinations(sample_size, 85)}
Number of iterations i = {iterations} for sample size n = {sample_size}
Level of confidence is set at {(1 - alpha) * 100}%. t-value = {t}

{income_report}
{consumption_report}
{population_report}
'''
    report_backup = report
    txt_report.delete('1.0', tk.END)
    txt_report.insert(tk.END, report)


global file_location
global file_destination
global iterations
global boot_population
global boot_income
global boot_consumption
global report_backup

window = tk.Tk()
window.title('Расчет доверительных интервалов')
window.geometry('1000x700')

frm_open_button = tk.Frame(window)
frm_left_half = tk.Frame(window)
frm_right_half = tk.Frame(window)

frm_left_half.grid(row=1, column=0, sticky='nw')
frm_right_half.grid(row=1, column=1, sticky='e')

frm_size = tk.Frame(frm_left_half)
frm_buttons = tk.Frame(frm_left_half)
frm_report = tk.Frame(frm_right_half)

btn_open = tk.Button(
    frm_open_button,
    text='Open',
    width=15,
    height=2,
    bg='#FFFACD',
    command=open_file
)
lbl_open = tk.Label(frm_open_button, text="Specify file's location")
btn_proceed = tk.Button(
    frm_buttons,
    text='Make Calculations',
    width=15,
    height=3,
    command=make_calculations,
    bg='#00ff7f'
)
btn_plots = tk.Button(
    frm_buttons,
    text='Show Plots',
    width=15,
    height=3,
    command=show_plots,
    bg='#F0E68C'
)
btn_save = tk.Button(
    frm_buttons,
    text='Save Report',
    width=15,
    height=3,
    command=save_file
)
btn_clear = tk.Button(
    frm_buttons,
    text='Clear',
    width=10,
    height=2,
    command=clear
)
btn_revert = tk.Button(
    frm_buttons,
    text='Revert',
    width=10,
    height=2,
    command=revert_changes
)
btn_exit = tk.Button(
    frm_buttons,
    text='Exit Program',
    width=10,
    height=2,
    command=sys.exit
)
btn_open_report = tk.Button(
    frm_buttons,
    text='Open The Report',
    width=15,
    height=3,
    command=open_report
)

txt_report = tk.Text(frm_report, width=100, height=45)

frm_open_button.grid(row=0, column=0, columnspan=2, sticky='w')
frm_size.grid(row=1, column=0, padx=10, pady=10, sticky='w')
frm_buttons.grid(row=2, column=0, sticky='w')
frm_report.grid(row=1, column=1)


btn_open.grid(row=0, column=0, padx=10, pady=5)
lbl_open.grid(row=0, column=1)
txt_report.grid(row=0, column=0, padx=10)
btn_proceed.grid(row=0, column=0, padx=10)
btn_plots.grid(row=1, column=0, padx=10, pady=10)
btn_save.grid(row=2, column=0, pady=10)
btn_clear.grid(row=3, column=0, pady=2)
btn_revert.grid(row=4, column=0, pady=5)
btn_open_report.grid(row=5, column=0, padx=10, pady=10)
btn_exit.grid(row=6, column=0)

lbl_name_iterations = tk.Label(frm_size, text='iterations')
lbl_size = tk.Label(frm_size, text='1000')
btn_decrease_1000 = tk.Button(frm_size, text='-1000', command=decrease_1000)
btn_decrease_100 = tk.Button(frm_size, text='-100', command=decrease_100)
btn_increase_100 = tk.Button(frm_size, text='+100', command=increase_100)
btn_increase_1000 = tk.Button(frm_size, text='+1000', command=increase_1000)
btn_reset = tk.Button(frm_size, text='reset', command=reset_iterations)

lbl_name_iterations.grid(row=0, column=2)
btn_decrease_1000.grid(row=1, column=0)
btn_decrease_100.grid(row=1, column=1)
lbl_size.grid(row=1, column=2, padx=12)
btn_increase_100.grid(row=1, column=3)
btn_increase_1000.grid(row=1, column=4)
btn_reset.grid(row=1, column=5, padx=5)

window.mainloop()
