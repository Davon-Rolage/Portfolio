import tkinter as tk
import tkinter.font as font


class Table:
    def __init__(self, root):
        for i in range(total_rows):
            for j in range(total_columns):
                self.l = tk.Label(root, font=('Arial', 11), width=22)
                self.l.grid(row=i, column=j)
                self.l['text'] = lst[i][j]

def calculate_tax():
    tax_rate_dct = {
        12_451: .19,
        20_201: .24,
        35_201: .3,
        60_001: .37,
        float('inf'): .45
    }
    try:
        income = float(entry_income.get())
    except ValueError:
        lbl_tax_rate['text'] = 'Enter a valid number'
        lbl_tax_value['text'] = ''
        lbl_net_income['text'] = ''
        return

    for tax_rate in tax_rate_dct:
        if 0 <= income < tax_rate:
            tax_rate = tax_rate_dct[tax_rate]
            lbl_tax_rate['text'] = f'{tax_rate*100}%'
            break

    tax_value = tax_rate * income
    lbl_tax_value['text'] = f'{tax_value:>10,.2f}€'
    net_income = income - tax_value
    lbl_net_income['text'] = f'{net_income:>10,.2f}€'


root = tk.Tk()
root.title('Simple Tax Calculator (Spain)')
root.geometry('600x400')

window_height = 400
window_width = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = int((screen_width/2) - (window_width/2))
y_coordinate = int((screen_height/2) - (window_height/2))

root.geometry("{}x{}+{}+{}".format(window_width,
              window_height, x_coordinate, y_coordinate))

myFont = font.Font(size=14)

frm_main = tk.Frame(root)
frm_tax_table = tk.Frame(root)
frm_main.grid(row=1, column=1, padx=80)
frm_tax_table.grid(row=2, column=1, pady=30)

lst = [
    ('Taxable income band €', 'National income tax rates'),
    ('0 to 12,450', '19%'),
    ('12,451 to 20,200', '24%'),
    ('20,201 to 35,200', '30%'),
    ('35,201 to 60,000', '37%'),
    ('60,001 +', '45%')
]

total_rows = len(lst)
total_columns = len(lst[0])
table = Table(frm_tax_table)

lbl_income = tk.Label(frm_main, text='Gross income: €', font=myFont)
entry_income = tk.Entry(frm_main, font=myFont)
lbl_tax_rate_txt = tk.Label(frm_main, text='Tax rate (Spain):   ', font=myFont)
lbl_tax_rate = tk.Label(frm_main, text='', font=myFont)
btn_calculate_tax = tk.Button(
    frm_main,
    text='Calculate Tax',
    bg='#00ff7f',
    font=myFont,
    command=calculate_tax
)
lbl_tax_value_txt = tk.Label(frm_main, text='Tax:', font=myFont)
lbl_tax_value = tk.Label(frm_main, text='', font=myFont)
lbl_net_income_txt = tk.Label(frm_main, text='Net income:', font=myFont)
lbl_net_income = tk.Label(frm_main, text='', font=myFont)

lbl_income.grid(row=1, column=1)
entry_income.grid(row=1, column=2)
lbl_tax_rate_txt.grid(row=2, column=1, sticky='e')
lbl_tax_rate.grid(row=2, column=2, sticky='w')
btn_calculate_tax.grid(row=3, column=1, columnspan=2, pady=10)
lbl_tax_value_txt.grid(row=5, column=1, sticky='e')
lbl_tax_value.grid(row=5, column=2, sticky='w')
lbl_net_income_txt.grid(row=4, column=1, sticky='e')
lbl_net_income.grid(row=4, column=2, sticky='w')

root.mainloop()
