class LangInterface():
    def __init__(self, user_lang='eng'):
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
            lang_dct = {
                'eng': {
                    'window_title': 'Personal Income Tax Calculator',
                    'lbl_choose_country': 'Choose country:',
                    'country_not_found_error': 'Choose country from the list',
                    'lbl_income': 'Annual gross income:',
                    'decimal_separator': 'dec. sep:',
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
                    'decimal_separator': 'десят. разд.:',
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
                    'decimal_separator': 'sep. dec:',
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
                    'decimal_separator': '',
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
            self.messages = lang_dct[user_lang]
