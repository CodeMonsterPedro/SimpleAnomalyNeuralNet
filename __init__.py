import sys
import random
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from datetime import date
from fpdf import FPDF, HTMLMixin
from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog, QListWidgetItem, QTableWidgetItem
from UIs.mainwindow import Ui_MainWindow
from StatDialog import StatDialog
from myRow import MyRow

class MyFPDF(FPDF, HTMLMixin):
    pass
'''

2. Выбрать 3-4 разных типа моделей искусственной нейронной сети (сверточная, рекурсивная, перцептрон,…..)
3. Разработать программное приложение, желательно на Django|Flask (но можно и десктоп), с поддержкой функционала, схожего с тем, 
что вы делали по ИДЗ в прошлом году (ввод данных, настройка гиперпараметров,….), добавив возможность визуализации модели нейросети 
в виде графа/картинки, сохранение модели в формате *.h5 (или другом, pickle например), загрузки ее в интерфейс (значения гиперпараметров 
должны разумеется сохраняться при этом).
4. Предусмотреть в интерфейсе возможности импорта/ввода нового набора/файла данных для использования на нем полученной модели и 
вывода результата его анализа/обработки нейросетью (т.е. допустим, для эмоционального окраса речи, например, должно быть предусмотрено 
поле ввода предложения, кнопка анализ, по нажатию на которую введенные данные пользователем обработаются моделью ИНС и выходное значение, 
например, это будет тип эмоции: раздраженность, нейтральность, позитивизм, будет выведено в виде текста.
5. Составить пояснительную записку по примеру, что выслал. Т.е. 35 страниц на 2 главы, 1-я до 10 страниц на анализ проблематики, 
сферы решения задачи, 2-я от 20 страниц, где описать проект, привести скрины и таблицы/графики работы нейросети, ошибка, точность 
и т.д. Обязательно сравнить 2-3 разные модели, показав, какая из них лучше/хуже решает задачу.
6. Уникальность 70% по етхт.



Тематика машинного обучения (МО). Требуется реализовать веб-приложение сравнения возможностей разных алгоритмов МО (минимум 3) 
на примере решения задачи классификации или регрессии. Библиотеки skilearn, numpy, pandas, matplotlib.
Требуемый функционал:
1. Поддержка возможности загрузки входных данных из файла формата csv.**
2. Отображение импортированных данных в таблице с возможностями редактирования и сортировки**
3. Расчет и вывод в другой таблице статистических показателей данных (по примеру, как это выводится в дедукторе или рапидмайнере)
, среднее, медиана, мода, максимум, минимум…!**
4. Возможность выбора нужного алгоритма МО и его конфигурации (выбор параметров алгоритма, у каждого есть свои входные, так называемые, гиперпараметры)**
5. Возможность выбора метрики оценки качества модели (например, MSE, подробнее тут https://habr.com/ru/company/ods/blog/328372/)**
6. Возможность разбития импортированной выборки на входную и тестовую.**
7. Возможность запуска алгоритма и построения графика его ошибки + выдачи данных в текстовом виде !
(в файл или текстовое поле) (7 и 8 - После окончания работы алгоритма появляется диалог который все показывает + генерит файл отчет)
8. Возможность сохранения полученных данных в виде отчета в файл, хотя бы текстовый.!

'''


class Base(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._hiperNames = []
        self._X = []
        self._y = []
        self._dataSet = []
        self._train_X = []
        self._train_y = []
        self._test_X = []
        self._test_y = []
        self._predictions = []
        self._method = []
        self._metric = []
        self._statDialog = StatDialog()
        self._scoreResult = 0
        self._metricResult = 0
        self._isSplit = True
        self._isStatSaved = False
        self._isFileParsed = False
        self._classMetricLabels = ('accuracy', 'balanced_accuracy', 'average_precision', 'neg_brier_score', 'f1', 'precision', 'precision', 'recall', 'jaccard')
        self._regressionMetricLabels = ('explained_variance', 'max_error', 'neg_mean_absolute_error', 'neg_mean_squared_error', 'neg_median_absolute_error', 'r2', 'neg_mean_poisson_deviance', 'neg_mean_gamma_deviance')
        self.ui.cb_method.addItems(('Linear regression', 'Logistic regression', 'K-nearest neighbors'))
        self.ui.cb_method.currentIndexChanged.connect(self._setMethod)
        self.ui.cb_metric.addItems(self._regressionMetricLabels)
        self.ui.cb_metric.currentIndexChanged.connect(self._setMetric)
        self.ui.cb_parametr1.currentIndexChanged.connect(self._setParametr1)
        self.ui.cb_parametr2.currentIndexChanged.connect(self._setParametr2)
        self.ui.lw_parametrs.itemChanged.connect(self._updateHiperparamets)
        self.ui.chb_twice.stateChanged.connect(self._updateTwiceData)
        self.ui.spb_k_count.editingFinished.connect(self._setK)
        self.ui.btn_setFile.clicked.connect(self._parseFile)
        self.ui.btn_start.clicked.connect(self._startTraining)
        self.ui.btn_stat.clicked.connect(self._showStatistic)

    def _startTraining(self):
        self._isStatSaved = False
        print('start train')
        self._train_X, self._test_X, self._train_y, self._test_y = train_test_split(self._X, self._y, test_size=0.25, random_state=42)
        self._method.fit(self._train_X, self._train_y)
        self._predictions = self._method.predict(self._test_X)
        print(self._predictions)
        print('stop train')
        self._scoreResult = self._method.score(self._test_X, self._test_y)
        print(self._scoreResult)
        self._metricResult = self._metric(self._test_y, self._predictions)
        print(self._metricResult)
        self._statDialog.setData(self._train_X, self._train_y, self._test_X, self._test_y, self._predictions)
        self._statDialog.show()
        if not self._isStatSaved:
            self._statDialog.save()
            self._isStatSaved = True
        self._makeFile()


    def _updateTwiceData(self):
        if self.ui.chb_twice.isChecked():
            self._isSplit = True
        else:
            self._isSplit = False

    def _setMethod(self):
        if self.ui.cb_method.currentIndex() == 0:
            self._method = LinearRegression()
            self.ui.cb_metric.clear()
            self.ui.cb_metric.addItems(self._regressionMetricLabels)
            self._metric = []
        elif self.ui.cb_method.currentIndex() == 1:
            self._method = LogisticRegression()
            self.ui.cb_metric.clear()
            self.ui.cb_metric.addItems(self._classMetricLabels)
            self._metric = []
        elif self.ui.cb_method.currentIndex() == 2:
            self._method = KNeighborsClassifier(n_neighbors=5)
            self.ui.cb_metric.clear()
            self.ui.cb_metric.addItems(self._classMetricLabels)
            self._metric = []

    def _showStatistic(self):
        self._statDialog.show()
        if not self._isStatSaved:
            self._statDialog.save()
            self._isStatSaved = True


# -------------------------------
    def _setParametr1(self):
        if self._isFileParsed:
            if not isinstance(self._y, list):
                self._X = self._dataSet[self.ui.cb_parametr1.currentText()]
                self._X = self._X.values
                self._X = self._X.reshape(-1, 1)
                print(self._X)
            else:
                self._X = self._dataSet[self.ui.cb_parametr1.currentText()]
                self._X = self._X.values
                self._X = self._X.reshape(-1, 1)
                print(self._X)

    def _setParametr2(self):
        if self._isFileParsed:
            if not isinstance(self._X, list):
                self._y = self._dataSet[self.ui.cb_parametr2.currentText()]
                self._y = self._y.values
                print(self._y)
            else:
                self._y = self._dataSet[self.ui.cb_parametr2.currentText()]
                self._y = self._y.values
                print(self._y)

    def _updateHiperparamets(self):
        self._hiperNames = []
        for i in range(self.ui.lw_parametrs.count()):
            item = self.ui.lw_parametrs.item(i)
            element = self.ui.lw_parametrs.itemWidget(item)
            if isinstance(element, MyRow) and element.isChecked():
                self._hiperNames.append(element.getText())
        print(self._hiperNames)

    def _parseFile(self):
        fileInfo = QFileDialog.getOpenFileName()
        fileName = fileInfo[0].split('.')
        result = 0
        if fileName[-1] == 'csv':
            result = pd.read_csv(fileInfo[0], error_bad_lines=False)
        else:
            result = pd.read_excel(fileInfo[0], error_bad_lines=False)
        self._dataSet = result
        self._dataSet = self._dataSet.fillna(0)
        self._fillTable()
        self._setHiperparametrs(self._dataSet.columns)
        self.ui.cb_parametr1.addItems(list(self._dataSet.columns))
        self.ui.cb_parametr2.addItems(list(self._dataSet.columns))
        self._isFileParsed = True


    def _setMetric(self):
        if self.ui.cb_method.currentIndex() == 0:
            if self.ui.cb_metric.currentIndex() == 0:
                self._metric = metrics.explained_variance_score
            elif self.ui.cb_metric.currentIndex() == 1:
                self._metric = metrics.max_error
            elif self.ui.cb_metric.currentIndex() == 2:
                self._metric = metrics.mean_absolute_error
            elif self.ui.cb_metric.currentIndex() == 3:
                self._metric = metrics.mean_squared_error
            elif self.ui.cb_metric.currentIndex() == 4:
                self._metric = metrics.median_absolute_error
            elif self.ui.cb_metric.currentIndex() == 5:
                self._metric = metrics.r2_score
            elif self.ui.cb_metric.currentIndex() == 6:
                self._metric = metrics.mean_poisson_deviance
            elif self.ui.cb_metric.currentIndex() == 7:
                self._metric = metrics.mean_gamma_deviance
        else:
            if self.ui.cb_metric.currentIndex() == 0:
                self._metric = metrics.accuracy_score
            elif self.ui.cb_metric.currentIndex() == 1:
                self._metric = metrics.balanced_accuracy_score
            elif self.ui.cb_metric.currentIndex() == 2:
                self._metric = metrics.average_precision_score
            elif self.ui.cb_metric.currentIndex() == 3:
                self._metric = metrics.brier_score_loss
            elif self.ui.cb_metric.currentIndex() == 4:
                self._metric = metrics.f1_score
            elif self.ui.cb_metric.currentIndex() == 5:
                self._metric = metrics.precision_score
            elif self.ui.cb_metric.currentIndex() == 6:
                self._metric = metrics.recall_score
            elif self.ui.cb_metric.currentIndex() == 7:
                self._metric = metrics.jaccard_score
                
    def _setK(self):
        self._method = self._method = KNeighborsClassifier(n_neighbors=int(self.ui.spb_k_count.value()))

    def _setHiperparametrs(self, names):
        for name in names:
            item = QListWidgetItem(self.ui.lw_parametrs)
            self.ui.lw_parametrs.addItem(item)
            row = MyRow(name)
            item.setSizeHint(row.minimumSizeHint())
            self.ui.lw_parametrs.setItemWidget(item, row)

    def _fillTable(self):
        for i in range(self.ui.tbw_data.rowCount(), -1, -1):
            self.ui.tbw_data.removeRow(i)
        i = 0
        j = 0
        self.ui.tbw_data.setColumnCount(len(list(self._dataSet.columns)))
        self.ui.tbw_data.setHorizontalHeaderLabels(list(self._dataSet.columns))
        tmp = self._dataSet.values
        for record in self._dataSet.values:
            self.ui.tbw_data.insertRow(i)
            for item in record:
                if item == np.nan:
                    continue
                else:
                    self.ui.tbw_data.setItem(i, j, QTableWidgetItem(str(item)))
                j += 1
            j = 0
            i += 1

    def _makeFile(self):
        pdf = MyFPDF()
        pdf.add_page()
        html = '<h1>Data info</h1><table border="1" width="90%"><thead><tr><th width="20%">train_X</th><th  width="20%">train_y</th><th width="20%">test_X</th><th width="20%">test_y</th><th width="20%">self._predictions</th></tr></thead><tbody>'
        sum = 0
        for i in range(len(self._train_X)):
            if i >= len(self._test_X):
                html += '<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>'.format(self._train_X[i], self._train_y[i], 0, 0, 0)
            else:
                html += '<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>'.format(self._train_X[i], self._train_y[i], self._test_X[i], self._test_y[i], self._predictions[i])
        html += '<tr><td colspan=4 >score answer </td><td>{}</td></tr>'.format(self._scoreResult)
        html += '<tr><td colspan=4 >Metric answer </td><td>{}</td></tr>'.format(self._metricResult)
        html += '</tbody></table>'
        pdf.write_html(html)
        d = date.today()
        t = d.timetuple()
        pdf.output('data_{}-{}-{}.pdf'.format(t.tm_hour, t.tm_min, t.tm_sec))


if __name__ == "__main__":
    app = QApplication([])
    window = Base()
    window.show()
    sys.exit(app.exec_())