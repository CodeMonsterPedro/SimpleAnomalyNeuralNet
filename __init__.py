import sys
import random
import pandas as pd
import numpy as np
from sklearn import metrics
from datetime import date
from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog, QListWidgetItem, QTableWidgetItem
from UIs.mainwindow import Ui_MainWindow
from StatDialog import StatDialog
from myRow import MyRow
import tensorflow as tf
from tensorflow import keras

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


'''


class Base(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._NetBuild = []
        self._NetTree = []
        self._values = []
        self._labels = []
        self._dataSet = []
        self._train_values = []
        self._train_labels = []
        self._test_values = []
        self._test_labels = []
        self._predictions = []
        self._method = []
        self._metric = []
        self._loss = 'sparse_categorical_crossentropy'
        self._optimizer = 'adam'
        self._statDialog = StatDialog()
        self._scoreResult = 0
        self._metricResult = 0
        self._isStatSaved = False
        self._isFileParsed = False
        self._classMetricLabels = ('accuracy', 'balanced_accuracy', 'average_precision', 'neg_brier_score', 'f1', 'precision', 'precision', 'recall', 'jaccard')
        self.ui.cb_method.addItems(('Сверточная', 'Перцептрон', 'Рекуррентная'))
        self.ui.cb_method.currentIndexChanged.connect(self._setMethod)
        self.ui.cb_metric.addItems(self._classMetricLabels)
        self.ui.cb_metric.currentIndexChanged.connect(self._setMetric)
        self.ui.btn_setFile.clicked.connect(self._parseFile)
        self.ui.btn_start.clicked.connect(self._startTraining)
        self.ui.btn_stat.clicked.connect(self._showStatistic)
        self.ui.btn_addlayout.clicked.connect(self._addNewLayout)
        self.ui.btn_dellayout.clicked.connect(self._delLayout)
        self.ui.btn_setNeuralnet.clicked.connect(self._importNet)
        self.ui.ln_id.textChanged.connect(self._idChanged)

    def _startTraining(self):
        self._isStatSaved = False
        print('start train')
        if self._isFileParsed:
            self._train_values, self._train_labels, self._test_values, self._test_labels = train_test_split(self._dataSet, self._labels, test_size=0.15, random_state=42)
        self._method.fit(self._train_values, self._train_labels, epochs=10)
        test_loss, test_acc = model.evaluate(self._test_values,  self._test_labels, verbose=2)
        print('stop train')
        self._predictions = self._method.predict(self._test_values)
        print(self._predictions)
        self._scoreResult = self._method.score(self._test_values, self._test_labels)
        print(self._scoreResult)
        self._metricResult = self._metric(self._test_labels, self._predictions)
        print(self._metricResult)
        #self._statDialog.setData(self._train_values, self._train_labels, self._test_values, self._test_labels, self._predictions)
        #self._statDialog.show()
        #if not self._isStatSaved:
        #    self._statDialog.save()
        #    self._isStatSaved = True
        #self._makeFile()

    def _setMethod(self):
        for i in range(self.ui.tbw_net_tree.rowCount(), -1, -1):
            self.ui.tbw_net_tree.removeRow(i)
        self._NetTree = []
        self._method = keras.Sequential()
        self._method.add(keras.layers.Input(shape=(len(self._dataSet[0]),)))
        if self.ui.cb_method.currentIndex() == 0:
            self._method.add(keras.layers.Conv2D(32, (3,3), padding='same', activation='relu', input_shape=(28,28,1)))
            self._method.add(keras.layers.MaxPooling2D((2,2), strides=2))
        elif self.ui.cb_method.currentIndex() == 1:
            for row in self._NetTree:
                self._method.add(keras.layers.Dense(row[1], activation='relu'))
        elif self.ui.cb_method.currentIndex() == 2:
            self._method = KNeighborsClassifier(n_neighbors=5)
        self._method.add(keras.layers.Dense(1, activation='softmax'))
        self._method.compile(optimizer='adam', loss='binary_crossentropy', metrics=self._metric)

# -------------------------------

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
        self.ui.cb_parametr1.addItems(list(self._dataSet.columns))
        self.ui.cb_parametr2.addItems(list(self._dataSet.columns))
        self._isFileParsed = True

    def _setMetric(self):
        if self.ui.cb_metric.currentIndex() >= 0 and self.ui.cb_metric.currentIndex() <= 7:
            self._metric = self._metric.append(self._classMetricLabels[self.ui.cb_metric.currentIndex()])

    def _addNewLayout(self):
        l = [len(self._NetTree), self.ui.spb_neirons.value()]
        self._NetTree.append(l)
        self._updateTreeTable()

    def _delLayout(self):
        self._NetTree.pop(int(self.ui.ln_id.text()))
        self._updateTreeTable()

    def _importNet(self):
        pass

    def _idChanged(self):
        num = int(self.ui.ln_id.text())
        if num >= len(self._NetTree):
            self.ui.ln_id.setText(len(self._NetTree) - 1)

    def _updateTreeTable(self):
        for i in range(self.ui.tbw_net_tree.rowCount(), -1, -1):
            self.ui.tbw_net_tree.removeRow(i)
        i = 0
        j = 0
        self.ui.tbw_data.setColumnCount(len(self._NetTree[0]))
        for row in self._NetTree:
            self.ui.tbw_net_tree.insertRow(i)
            for item in row:
                if item == np.nan:
                    continue
                else:
                    self.ui.tbw_net_tree.setItem(i, j, QTableWidgetItem(str(item)))
                j += 1
            j = 0
            i += 1

    def _showStatistic(self):
        self._statDialog.show()
        if not self._isStatSaved:
            self._statDialog.save()
            self._isStatSaved = True

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
        html = '<h1>Data info</h1><table border="1" width="90%"><thead><tr><th width="20%">train_values</th><th  width="20%">train_labels</th><th width="20%">test_values</th><th width="20%">test_labels</th><th width="20%">self._predictions</th></tr></thead><tbody>'
        sum = 0
        for i in range(len(self._train_values)):
            if i >= len(self._test_values):
                html += '<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>'.format(self._train_values[i], self._train_labels[i], 0, 0, 0)
            else:
                html += '<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>'.format(self._train_values[i], self._train_labels[i], self._test_values[i], self._test_labels[i], self._predictions[i])
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
