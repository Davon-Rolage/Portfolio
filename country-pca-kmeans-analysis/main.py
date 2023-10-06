from collections import Counter
from tkinter.filedialog import askopenfile, asksaveasfilename

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from kneed import KneeLocator
from PyQt5 import QtCore, QtGui, QtWidgets
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 770)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frm_filepath_lang = QtWidgets.QFrame(self.centralwidget)
        self.frm_filepath_lang.setGeometry(QtCore.QRect(10, 10, 961, 51))
        self.frm_filepath_lang.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_filepath_lang.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_filepath_lang.setObjectName("frm_filepath_lang")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frm_filepath_lang)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.btn_open = QtWidgets.QPushButton(self.frm_filepath_lang)
        self.btn_open.setMaximumSize(QtCore.QSize(95, 16777215))
        self.btn_open.setStyleSheet('background-color : #FFFACD')
        self.btn_open.clicked.connect(lambda: self.open_file())

        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_open.setFont(font)
        self.btn_open.setObjectName("btn_open")
        self.horizontalLayout.addWidget(self.btn_open)
        self.lbl_open = QtWidgets.QLabel(self.frm_filepath_lang)
        self.lbl_open.setEnabled(True)
        self.lbl_open.setMinimumSize(QtCore.QSize(300, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_open.setFont(font)
        self.lbl_open.setObjectName("lbl_open")

        self.horizontalLayout.addWidget(self.lbl_open)
        self.btn_rus = QtWidgets.QPushButton(self.frm_filepath_lang)
        self.btn_rus.setMaximumSize(QtCore.QSize(93, 16777215))
        self.btn_rus.setObjectName("btn_rus")
        self.btn_rus.clicked.connect(lambda: self.lang_interface('rus'))

        self.horizontalLayout.addWidget(self.btn_rus)
        self.btn_eng = QtWidgets.QPushButton(self.frm_filepath_lang)
        self.btn_eng.setMaximumSize(QtCore.QSize(93, 16777215))
        self.btn_eng.setObjectName("btn_eng")
        self.btn_eng.clicked.connect(lambda: self.lang_interface('eng'))

        self.horizontalLayout.addWidget(self.btn_eng)
        self.frm_calculations = QtWidgets.QFrame(self.centralwidget)
        self.frm_calculations.setGeometry(QtCore.QRect(10, 60, 321, 700))
        self.frm_calculations.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_calculations.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_calculations.setObjectName("frm_calculations")

        self.layoutWidget = QtWidgets.QWidget(self.frm_calculations)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 291, 110))
        self.layoutWidget.setObjectName("layoutWidget")
        self.layout_analysis_type = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.layout_analysis_type.setContentsMargins(0, 0, 0, 0)
        self.layout_analysis_type.setObjectName("layout_analysis_type")

        self.lbl_analysis_type = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_analysis_type.setFont(font)
        self.lbl_analysis_type.setObjectName("lbl_analysis_type")
        self.layout_analysis_type.addWidget(self.lbl_analysis_type)
        self.check_box_pca = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.check_box_pca.setFont(font)
        self.check_box_pca.setObjectName("check_box_pca")
        self.layout_analysis_type.addWidget(self.check_box_pca)
        self.check_box_kmeans = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.check_box_kmeans.setFont(font)
        self.check_box_kmeans.setObjectName("check_box_kmeans")
        self.layout_analysis_type.addWidget(self.check_box_kmeans)
        self.btn_proceed = QtWidgets.QPushButton(self.frm_calculations)
        self.btn_proceed.setStyleSheet('background-color : #00ff7f')

        self.btn_proceed.setGeometry(QtCore.QRect(10, 150, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_proceed.setFont(font)
        self.btn_proceed.setObjectName("btn_proceed")
        self.btn_proceed.clicked.connect(
            lambda: self.start_pca(self.dataframe))
        self.btn_proceed.clicked.connect(
            lambda: self.start_kmeans(self.pca_dataframe))

        self.btn_optimise_k = QtWidgets.QPushButton(self.frm_calculations)
        self.btn_optimise_k.setGeometry(QtCore.QRect(10, 210, 291, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btn_optimise_k.setFont(font)
        self.btn_optimise_k.setObjectName("btn_optimise_k")
        self.btn_optimise_k.clicked.connect(lambda: self.optimise_kmeans(data=self.pca_dataframe))
        
        self.lbl_status = QtWidgets.QLabel(self.frm_calculations)
        self.lbl_status.setGeometry(QtCore.QRect(10, 340, 291, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lbl_status.setFont(font)
        self.lbl_status.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_status.setObjectName("lbl_status")

        self.frm_k_counter = QtWidgets.QFrame(self.frm_calculations)
        self.frm_k_counter.setObjectName(u"frm_k_counter")
        self.frm_k_counter.setGeometry(QtCore.QRect(40, 250, 211, 91))
        self.layout_cluster_counter = QtWidgets.QGridLayout(self.frm_k_counter)
        self.layout_cluster_counter.setObjectName(u"layout_cluster_counter")
        self.layout_cluster_counter.setVerticalSpacing(0)
        self.lbl_k_clusters = QtWidgets.QLabel(self.frm_k_counter)
        self.lbl_k_clusters.setObjectName(u"lbl_k_clusters")

        self.frame_2 = QtWidgets.QFrame(self.frm_k_counter)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_decrease_1 = QtWidgets.QPushButton(self.frame_2)
        self.btn_decrease_1.setMaximumSize(QtCore.QSize(40, 16777215))
        self.btn_decrease_1.setObjectName("btn_decrease_1")
        self.btn_decrease_1.clicked.connect(lambda: self.decrease_1())
        self.horizontalLayout_3.addWidget(self.btn_decrease_1)
        self.lbl_k = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lbl_k.setFont(font)
        self.lbl_k.setObjectName("lbl_k")
        self.horizontalLayout_3.addWidget(
            self.lbl_k, 0, QtCore.Qt.AlignHCenter)
        self.btn_increase_1 = QtWidgets.QPushButton(self.frame_2)
        self.btn_increase_1.setMaximumSize(QtCore.QSize(40, 16777215))
        self.btn_increase_1.setObjectName("btn_increase_1")
        self.btn_increase_1.clicked.connect(lambda: self.increase_1())

        self.horizontalLayout_3.addWidget(self.btn_increase_1)
        self.btn_reset = QtWidgets.QPushButton(self.frame_2)
        self.btn_reset.setMaximumSize(QtCore.QSize(60, 16777215))
        self.btn_reset.setObjectName("btn_reset")
        self.btn_reset.clicked.connect(lambda: self.reset())

        self.horizontalLayout_3.addWidget(self.btn_reset)
        self.layout_cluster_counter.addWidget(self.frame_2, 1, 0, 1, 1)
        self.lbl_k_clusters = QtWidgets.QLabel(self.frm_k_counter)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lbl_k_clusters.setFont(font)
        self.lbl_k_clusters.setObjectName("lbl_k_clusters")
        self.layout_cluster_counter.addWidget(
            self.lbl_k_clusters, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.btn_show_plots = QtWidgets.QPushButton(self.frm_calculations)
        self.btn_show_plots.setGeometry(QtCore.QRect(60, 380, 190, 60))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_show_plots.setStyleSheet('background-color : #F0E68C')
        self.btn_show_plots.setFont(font)
        self.btn_show_plots.setObjectName("btn_show_plots")
        self.btn_show_plots.clicked.connect(
            lambda: self.make_plots(self.pca_dataframe))

        self.btn_clear = QtWidgets.QPushButton(self.frm_calculations)
        self.btn_clear.setGeometry(QtCore.QRect(20, 450, 100, 51))
        self.btn_clear.setObjectName("btn_clear")
        self.btn_clear.clicked.connect(
            lambda: self.clear())

        self.btn_revert = QtWidgets.QPushButton(self.frm_calculations)
        self.btn_revert.setGeometry(QtCore.QRect(180, 450, 100, 51))
        self.btn_revert.setObjectName("btn_revert")
        self.btn_revert.clicked.connect(
            lambda: self.revert())

        self.btn_save = QtWidgets.QPushButton(self.frm_calculations)
        self.btn_save.setGeometry(QtCore.QRect(20, 510, 120, 51))
        self.btn_save.setObjectName("btn_save")
        self.btn_save.clicked.connect(
            lambda: self.save_file())

        self.txt_report = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_report.setGeometry(QtCore.QRect(320, 60, 800, 600))
        self.txt_report.setObjectName("txt_report")
        self.frm_filepath_lang.raise_()
        self.txt_report.raise_()
        self.frm_calculations.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 801, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_open.setText(_translate("MainWindow", "Open"))
        self.lbl_open.setText(_translate("MainWindow", "Choose file path"))
        self.btn_rus.setText(_translate("MainWindow", "Русский"))
        self.btn_eng.setText(_translate("MainWindow", "English"))
        self.lbl_analysis_type.setText(
            _translate("MainWindow", "Type of Analysis"))
        self.check_box_pca.setText(_translate(
            "MainWindow", "Principal Component Analysis"))
        self.check_box_kmeans.setText(_translate(
            "MainWindow", "K Means Clusterisation"))
        self.btn_proceed.setText(_translate("MainWindow", "Make Calculations"))
        self.btn_optimise_k.setText(_translate(
            "MainWindow", "Find Optimal Number of Clusters"))
        self.lbl_status.setText(_translate("MainWindow", "..."))
        self.btn_decrease_1.setText(_translate("MainWindow", "-1"))
        self.lbl_k.setText(_translate("MainWindow", "2"))
        self.btn_increase_1.setText(_translate("MainWindow", "+1"))
        self.btn_reset.setText(_translate("MainWindow", "reset"))
        self.lbl_k_clusters.setText(_translate(
            "MainWindow", "Number of Clusters"))
        self.btn_show_plots.setText(_translate("MainWindow", "Show Plots"))
        self.btn_clear.setText(_translate("MainWindow", "Clear"))
        self.btn_revert.setText(_translate("MainWindow", "Revert"))
        self.btn_save.setText(_translate("MainWindow", "Save Report"))

        self.dataframe = None
        self.file_location = None
        self.user_lang = 'eng'

    def lang_interface(self, user_lang):
        lang = {
            'eng': {
                'btn_open': 'Open',
                'lbl_open': "Specify file's location",
                'lbl_analysis_type': 'Type of Analysis',
                'check_box_pca': "Principal Component Analysis",
                'check_box_kmeans': 'K Means Clusterisation',
                'btn_optimise_k': 'Find Optimal Number of Clusters',
                'lbl_k_clusters': 'Number of Clusters',
                'btn_reset': 'reset',
                'btn_proceed': 'Make Calculations',
                'btn_show_plots': 'Show Plots',
                'plot_title_kmeans': 'K Means of Countries Dataset',
                'btn_clear': 'Clear',
                'btn_revert': 'Revert',
                'btn_save': 'Save Report'
            },
            'rus': {
                'btn_open': 'Открыть',
                'lbl_open': 'Укажите путь к файлу',
                'lbl_analysis_type': 'Тип анализа',
                'check_box_pca': "Метод главных компонент",
                'check_box_kmeans': 'К средних кластеризация',
                'btn_optimise_k': 'Найти оптимальное число кластеров',
                'lbl_k_clusters': 'Число кластеров',
                'btn_reset': 'заново',
                'btn_proceed': 'Произвести вычисления',
                'btn_show_plots': 'Показать графики',
                'btn_clear': 'Очистить',
                'btn_revert': 'Вернуть',
                'btn_save': 'Сохранить отчёт'
            }
        }
        self.user_lang = user_lang
        self.messages = lang[self.user_lang]

        self.btn_open.setText(self.messages['btn_open'])
        self.lbl_open.setText(self.messages['lbl_open'])
        self.lbl_analysis_type.setText(self.messages['lbl_analysis_type'])
        self.check_box_pca.setText(self.messages['check_box_pca'])
        self.check_box_kmeans.setText(self.messages['check_box_kmeans'])
        self.btn_optimise_k.setText(self.messages['btn_optimise_k'])
        self.lbl_k_clusters.setText(self.messages['lbl_k_clusters'])
        self.btn_reset.setText(self.messages['btn_reset'])
        self.btn_proceed.setText(self.messages['btn_proceed'])
        self.btn_show_plots.setText(self.messages['btn_show_plots'])
        self.btn_clear.setText(self.messages['btn_clear'])
        self.btn_revert.setText(self.messages['btn_revert'])
        self.btn_save.setText(self.messages['btn_save'])

    def open_file(self):
        file_location = askopenfile(
            initialdir='D:/Downloads/',
            filetypes=[
                ('CSV Files', '*.csv'),
                ('All Files', '*.*')
            ]
        )
        if not file_location:
            return

        self.file_location = file_location.name
        self.dataframe = pd.read_csv(self.file_location, encoding='utf-8')
        self.index_column = list(self.dataframe[self.dataframe.columns[1]])
        self.dataframe.drop(self.dataframe.columns[0], axis=1, inplace=True)
        self.dataframe.set_index(self.dataframe.columns[0], inplace=True)
        
        self.lbl_open.setText(self.file_location)

    def increase_1(self):
        k = int(self.lbl_k.text())
        if k < 10:
            self.lbl_k.setText(str(k+1))

    def decrease_1(self):
        k = int(self.lbl_k.text())
        if k > 1:
            self.lbl_k.setText(str(k-1))

    def reset(self):
        self.lbl_k.setText('2')

    def clear(self):
        self.txt_report.clear()

    def revert(self):
        self.txt_report.setText(self.report_backup)

    def save_file(self):
        file_destination = asksaveasfilename(
            initialdir='D:/Downloads',
            initialfile='Analysis_Report',
            defaultextension='.txt',
            filetypes=[
                ('Text Files', '*.txt'),
                ('All Files', '*.*'),
            ]
        )
        if not file_destination:
            return

        self.file_destination = file_destination
        with open(self.file_destination, mode='w', encoding='utf8') as output_file:
            text = self.txt_report.toPlainText()
            output_file.write(text)

        MainWindow.setWindowTitle(
            f'PCA and K means analysis - {self.file_destination}')

    def start_pca(self, dataframe):
        df = dataframe
        outliers_by_personal_remittances = df[
            df['Personal remittances: receipts and payments, USD millions'] > 20000
        ]
        outliers_by_foreign_investment = df[
            df['Foreign direct investment, USD millions'] > 50000
        ]
        min_trade_balance = df['Trade balance, USD millions'].min()
        min_trade_balance = df.loc[
            df['Trade balance, USD millions'] < -200_000
        ]
        high_trade_balance = df[df['Trade balance, USD millions'] > 50000]
        
        outliers_lst = list(set([*list(outliers_by_personal_remittances.index),
                                 *list(outliers_by_foreign_investment.index),
                                 *list(min_trade_balance.index),
                                 *list(high_trade_balance.index),
                                 ]))
        df.drop(outliers_by_personal_remittances.index,
                errors='ignore', inplace=True)
        df.drop(outliers_by_foreign_investment.index,
                errors='ignore', inplace=True)
        df.drop(min_trade_balance.index, errors='ignore', inplace=True)
        df.drop(high_trade_balance.index, errors='ignore', inplace=True)
        self.index_column = [v for v in self.index_column if v not in outliers_lst]
        self.dataframe = df

        x = df.values
        x = StandardScaler().fit_transform(x)

        pca = PCA(n_components=2)
        principalComponent_countries = pca.fit_transform(x)

        pca_coefficients = pd.DataFrame(
            pca.components_,
            columns=[f'x{i}' for i in range(1, self.dataframe.shape[1]+1)],
            index=['PC-1', 'PC-2']
        )
        print(round(pca_coefficients, 3))

        if self.user_lang == 'eng':
            column_names = ['principal component 1', 'principal component 2']
        else:
            column_names = ['главная компонента 1', 'главная компонента 2']

        self.pca_dataframe = pd.DataFrame(
            data=principalComponent_countries,
            columns=column_names
        )
        self.pca_dataframe['ECONOMY, 2019'] = self.index_column
        self.pca_dataframe.set_index('ECONOMY, 2019', inplace=True)    
        
        expl_variance_ratio = pca.explained_variance_ratio_.round(3)
        total_evr = expl_variance_ratio.sum()
        eigen_values = pca.explained_variance_.round(2)

        if self.user_lang == 'eng':
            self.report_pca = f'''PCA analysis:
Explained variance ratio per principal component: {expl_variance_ratio}
Total variance explained: {total_evr*100:.1f}%
Eigenvalues are: {eigen_values}
__________'''
        else:
            self.report_pca = f'''Метод главных компонент:
Доля объяснённой дисперсии главных компонент: {expl_variance_ratio}
Общий процент объяснённой дисперсии: {total_evr*100:.1f}%
Собственные значения вектора: {eigen_values}
__________'''

        self.txt_report.setText(self.report_pca)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txt_report.setFont(font)

    def make_plots(self, dataframe):
        fig, (ax1, ax2) = plt.subplots(ncols=2, nrows=1, figsize=(15, 7))
        plt.xticks(fontsize=10)
        plt.yticks(fontsize=12)
        centers = np.array(self.kmeans.cluster_centers_)
        plt.title('Title')
        if self.user_lang == 'eng':
            ax1.set_title(
                'Principal Component Analysis of Countries Dataset', fontsize=14)
            ax1.set_xlabel('Principal Component 1', fontsize=12)
            ax1.set_ylabel('Principal Component 2', fontsize=12)
            ax1.scatter(
                x=dataframe['principal component 1'],
                y=dataframe['principal component 2']
            )
        else:
            ax1.set_title('Метод главных компонент для стран', fontsize=14)
            ax1.set_xlabel('Главная компонента 1', fontsize=12)
            ax1.set_ylabel('Главная компонента 2', fontsize=12)
            ax1.scatter(
                x=dataframe['главная компонента 1'],
                y=dataframe['главная компонента 2']
            )

        if self.user_lang == 'eng':
            ax2.set_title(
                'K Means Clustering of Countries Dataset', fontsize=14)
            ax2.set_xlabel('Principal Component 1', fontsize=12)
            ax2.set_ylabel('Principal Component 2', fontsize=12)
            ax2.scatter(
                x=dataframe['principal component 1'],
                y=dataframe['principal component 2'],
                c=self.kmeans.labels_
            )
            ax2.scatter(centers[:, 0], centers[:, 1], marker='x', color='r')
        else:
            ax2.set_title('Метод К средних для стран', fontsize=14)
            ax2.set_xlabel('Главная компонента 1', fontsize=12)
            ax2.set_ylabel('Главная компонента 2', fontsize=12)
            ax2.scatter(
                x=dataframe['главная компонента 1'],
                y=dataframe['главная компонента 2'],
                c=self.kmeans.labels_
            )
            ax2.scatter(centers[:, 0], centers[:, 1], marker='x', color='r')

        ax2.text(2.5, 2, f'k = {self.lbl_k.text()}', size=16)
        plt.show()

    def optimise_kmeans(self, data):
        means = []
        inertias = []
        max_k = 10

        for k in range(1, max_k):
            kmeans = KMeans(n_clusters=k)
            kmeans.fit(data)

            means.append(k)
            inertias.append(kmeans.inertia_)

        fig = plt.subplots(figsize=(10, 5))
        plt.plot(means, inertias, 'o-')
        plt.xlabel('Number of Clusters')
        plt.ylabel('Inertia')

        kn = KneeLocator(means, inertias, curve='convex',
                         direction='decreasing')
        print(kn.knee)

        plt.plot(means, inertias, 'bx-')
        plt.vlines(kn.knee, plt.ylim()[0], plt.ylim()[1], linestyles='dashed')
        plt.show()

    def start_kmeans(self, dataframe):
        k = int(self.lbl_k.text())
        kmeans = KMeans(n_clusters=k)
        kmeans.fit(dataframe)
        self.kmeans = kmeans
        self.lbl_status.setText(f'k = {k}')
        dct = dict(zip(self.index_column, self.kmeans.labels_))
        if self.user_lang == 'eng':
            self.txt_report.append(f'''K Means Clusterisation:
The lowest SSE value is {round(self.kmeans.inertia_, 3)}
Final locations of the centroid:
{self.kmeans.cluster_centers_.round(1)}
The number of iterations required to converge: {self.kmeans.n_iter_}
''')
        else:
            self.txt_report.append(f'''Кластеризация методом К средних:
Наименьшее значение ошибки: {round(self.kmeans.inertia_, 3)}
Центры кластеров:
{self.kmeans.cluster_centers_.round(1)}
Число проведенных итераций для сходимости кластеров: {self.kmeans.n_iter_}
''')

        self.txt_report.append(f'{dct!r}')
        counter = Counter(self.kmeans.labels_)
        counter = sorted(counter.items())
        self.txt_report.append(f'\n{counter}')

        self.report_backup = self.txt_report.toPlainText()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
