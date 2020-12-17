from UIs.statDialog import Ui_Dialog
from PySide2.QtWidgets import QDialog, QTableWidgetItem, QTableWidget
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from datetime import date
from fpdf import FPDF, HTMLMixin

class MyFPDF(FPDF, HTMLMixin):
    pass

class StatDialog(QDialog):

    def __init__(self, train_X=[], train_y=[], test_X=[], test_y=[], predictions=[]):
        QDialog.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self._train_X = train_X
        self._train_y = train_y
        self._test_X = test_X
        self._test_y = test_y
        self._predictions = predictions
        self._stats = []
        self._targets = [self._train_X, self._train_y, self._test_X, self._test_y, self._predictions]
        self.ui.tbw_stat.setColumnCount(5)
        self.ui.tbw_data.setColumnCount(5)
        self.ui.tbw_stat.setHorizontalHeaderLabels(('train_X', 'train_y', 'test_X', 'test_y', 'predictions'))
        self.ui.tbw_data.setHorizontalHeaderLabels(('train_X', 'train_y', 'test_X', 'test_y', 'predictions'))
        self.ui.tbw_stat.setVerticalHeaderLabels(('Mean', 'Max', 'Min', 'Median', 'Moda'))

    def setData(self, train_X=[], train_y=[], test_X=[], test_y=[], predictions=[]):
        self._train_X = train_X
        self._train_y = train_y
        self._test_X = test_X
        self._test_y = test_y
        self._predictions = predictions
        self._targets = [self._train_X, self._train_y, self._test_X, self._test_y, self._predictions]
        self._update()

    def show(self):
        if not isinstance(self._train_X, list) and not isinstance(self._train_y, list) and not isinstance(self._test_X, list) and not isinstance(self._test_y, list) and not isinstance(self._predictions, list):
            self._showInfo()
        else:
            pass

    def save(self):
        if not isinstance(self._train_X, list) and not isinstance(self._train_y, list) and not isinstance(self._test_X, list) and not isinstance(self._test_y, list) and not isinstance(self._predictions, list):
            pdf = MyFPDF()
            pdf.add_page()
            html = '<h1>Data info</h1><table border="1" width="90%"><thead><tr><th width="20%">train_X</th><th  width="20%">train_y</th><th width="20%">test_X</th><th width="20%">test_y</th><th width="20%">self._predictions</th></tr></thead><tbody>'
            sum = 0
            for i in range(len(self._stats[0])):
                html += '<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>'.format(self._stats[0][i], self._stats[1][i], self._stats[2][i], self._stats[3][i], self._stats[4][i])
            html += '</tbody></table>'
            pdf.write_html(html)
            d = date.today()
            t = d.timetuple()
            pdf.output('stat_{}-{}-{}.pdf'.format(t.tm_hour, t.tm_min, t.tm_sec))
        else:
            return False

    def _update(self):
        if self.ui.tbw_data.rowCount() > 0:
            for i in range(self.ui.tbw_data.rowCount()):
                self.ui.tbw_data.removeRow(i)
        if self.ui.tbw_stat.rowCount() > 0:
            for i in range(self.ui.tbw_stat.rowCount()):
                self.ui.tbw_stat.removeRow(i)
        j = 0
        for i in range(len(self._targets[0])):
            self.ui.tbw_data.insertRow(i)
        for i in range(5):
            self.ui.tbw_stat.insertRow(i)
        for element in self._targets:
            print(element.dtype)
            l = []
            if not element.dtype == 'object':
                l.append(np.mean(element))
                l.append(np.max(element))
                l.append(np.min(element))
                l.append(np.median(element))
                l.append(stats.mode(element))
                self.ui.tbw_stat.setItem(0, j, QTableWidgetItem(str(np.mean(element))))
                self.ui.tbw_stat.setItem(1, j, QTableWidgetItem(str(np.max(element))))
                self.ui.tbw_stat.setItem(2, j, QTableWidgetItem(str(np.min(element))))
                self.ui.tbw_stat.setItem(3, j, QTableWidgetItem(str(np.median(element))))
                self.ui.tbw_stat.setItem(4, j, QTableWidgetItem(str(stats.mode(element))))
            else:
                l.append('-')
                l.append('-')
                l.append('-')
                l.append('-')
                l.append('-')
                self.ui.tbw_stat.setItem(0, j, QTableWidgetItem(str('-')))
                self.ui.tbw_stat.setItem(1, j, QTableWidgetItem(str('-')))
                self.ui.tbw_stat.setItem(2, j, QTableWidgetItem(str('-')))
                self.ui.tbw_stat.setItem(3, j, QTableWidgetItem(str('-')))
                self.ui.tbw_stat.setItem(4, j, QTableWidgetItem(str('-')))
            j += 1
            self._stats.append(l)
        i = 0
        j = 0
        for element in self._targets:
            for item in element:
                if item == np.nan:
                    continue
                else:
                    self.ui.tbw_data.setItem(i, j, QTableWidgetItem(str(item)))
                i += 1
            i = 0
            j += 1


    def _showInfo(self):
        plt.figure(figsize=(12, 6))
        plt.plot(self._test_X, self._predictions)     # regression line
        plt.plot(self._test_X, self._test_y, 'ro')   # scatter plot showing actual data
        plt.title('Actual vs Predicted')
        plt.xlabel('X')
        plt.ylabel('y')
        plt.show()
        self.exec_()
        if self.ui.tbw_data.rowCount() > 0:
            for i in range(self.ui.tbw_data.rowCount()):
                self.ui.tbw_data.removeRow(i)
        if self.ui.tbw_stat.rowCount() > 0:
            for i in range(self.ui.tbw_stat.rowCount()):
                self.ui.tbw_stat.removeRow(i)