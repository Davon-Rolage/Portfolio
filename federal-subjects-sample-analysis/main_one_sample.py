import os
import pandas as pd
import secrets as s
import tkinter as tk
from math import sqrt
from tkinter.filedialog import askopenfilename, asksaveasfilename


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


class Figure:
    # Figure = Показатель
    def __init__(self, name, rus_name, size, sample_names, average, general_average,
                 standard_deviation, mrg_error, confidence_interval, is_in_confidence_interval):
        self.name = name
        self.rus_name = rus_name
        self.size = size
        self.sample_names = sample_names
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


def open_file():
    global FILE_LOCATION
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
    FILE_LOCATION = filepath


def save_file():
    global FILE_DESTINATION
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
    FILE_DESTINATION = filepath


def clear():
    lbl_open['text'] = "Specify file's location"
    txt_report.delete('1.0', tk.END)


def open_report():
    global FILE_DESTINATION
    os.startfile(FILE_DESTINATION)


def make_calculations():
    global FILE_LOCATION
    global FILE_DESTINATION
    df = pd.read_csv(FILE_LOCATION, encoding='utf8', delimiter=';')
    old_columns = df.columns
    new_columns = ['Субъект', 'Доходы', 'Расходы', 'Мужчины', 'Женщины']
    for i in range(len(old_columns)):
        df.rename(inplace=True, columns={df.columns[i]: new_columns[i]})

    df['Женщины'] = df['Женщины'].apply(lambda x: float(x.split(',', 1)[0]))
    df['Субъект'] = df['Субъект'].apply(lambda x: x.split(',')[1].strip())

    df['Население'] = df['Мужчины'] + df['Женщины']

    # random sampling size = размер случайной выборки
    rand_sampling_size = s.choice(list(range(40, 60)))
    # sample subject indices = индексы выборки, состоящей из 85 субъектов РФ
    sample_subject_indices = set()

    while len(sample_subject_indices) < rand_sampling_size:
        sample_subject_indices.add(s.choice(list(range(len(df['Субъект'])))))

    sample_subject_indices = list(sample_subject_indices)
    sample_subject_count = len(sample_subject_indices)

    rand_subjects = [df.iloc[i]['Субъект'] for i in sample_subject_indices]

    # Must specify column's name (Мужчины, Женщины или Население)
    average_population = round(df['Население'].mean(numeric_only=True), 3)
    average_income = round(df['Доходы'].mean(numeric_only=True), 3)
    average_consumption = round(df['Расходы'].mean(numeric_only=True), 3)

    average_sample_population = round(df.iloc[sample_subject_indices]['Население'].mean(numeric_only=True), 3)
    average_sample_income = round(df.iloc[sample_subject_indices]['Доходы'].mean(numeric_only=True), 3)
    average_sample_consumption = round(df.iloc[sample_subject_indices]['Расходы'].mean(numeric_only=True), 3)

    sample_income_deviation = df['Доходы'].apply(lambda x: (x - average_sample_income) ** 2)
    sample_income_std = sqrt(sum(sample_income_deviation) / sample_subject_count)
    sample_consumption_deviation = df['Расходы'].apply(lambda x: (x - average_sample_consumption) ** 2)
    sample_consumption_std = sqrt(sum(sample_consumption_deviation / sample_subject_count))

    sample_population_deviation = df['Население'].apply(lambda x: (x - average_sample_population) ** 2)
    sample_population_std = sqrt(sum(sample_population_deviation / sample_subject_count))

    alpha = 0.05
    t = 2
    income_marginal_error = marginal_error(sample_subject_count, sample_income_std, t)
    consumption_marginal_error = marginal_error(sample_subject_count, sample_consumption_std, t)
    population_marginal_error = marginal_error(sample_subject_count, sample_population_std, t)

    income_conf_interval = get_conf_interval(
        average_sample_income,
        income_marginal_error,
        'average income'
    )
    consumption_conf_interval = get_conf_interval(
        average_sample_consumption,
        consumption_marginal_error,
        'average consumption'
    )
    population_conf_interval = get_conf_interval(
        average_sample_population,
        population_marginal_error,
        'average population'
    )

    income = Figure(
        name='consumer income in RUB',
        rus_name='Среднедушевые денежные доходы населения, руб./мес.',
        size=rand_sampling_size,
        sample_names=rand_subjects,
        average=average_sample_income,
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
        size=rand_sampling_size,
        sample_names=rand_subjects,
        average=average_sample_consumption,
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
        size=rand_sampling_size,
        sample_names=rand_subjects,
        average=average_sample_population,
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

    report = f'''Level of confidence is set at {(1 - alpha) * 100}%. t-value = {t}

{income_report}
{consumption_report}
{population_report}
Random subjects - {rand_subjects}
'''
    txt_report.delete('1.0', tk.END)
    txt_report.insert(tk.END, report)


global FILE_LOCATION
global FILE_DESTINATION

window = tk.Tk()
window.title('Расчет доверительных интервалов')
window.geometry('1000x700')

frm_open_button = tk.Frame(window)
frm_buttons = tk.Frame(window)
frm_report = tk.Frame(window)

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
btn_exit = tk.Button(
    frm_buttons,
    text='Exit Program',
    width=10,
    height=2,
    command=exit
)
btn_open_report = tk.Button(
    frm_buttons,
    text='Open The Report',
    width=18,
    height=3,
    command=open_report
)

txt_report = tk.Text(frm_report, width=100, height=45)

frm_open_button.pack(fill=tk.X)
frm_buttons.pack(side=tk.LEFT)
frm_report.pack()

btn_open.grid(row=0, column=0, padx=10, pady=10)
lbl_open.grid(row=0, column=1)
txt_report.grid(row=0, column=0, padx=10)
btn_proceed.grid(row=0, column=0, padx=10, pady=10)
btn_save.grid(row=1, column=0, pady=10)
btn_clear.grid(row=2, column=0, pady=10)
btn_exit.grid(row=3, column=0)
btn_open_report.grid(row=4, column=0, padx=10, pady=15)

window.mainloop()
