from PySide2.QtWidgets import QWidget, QHBoxLayout, QCheckBox


class MyRow(QWidget):
    def __init__(self, text, parent=None):
        super(MyRow, self).__init__(parent)
        self.row = QHBoxLayout()
        self.cb = QCheckBox(text)
        self.row.addWidget(self.cb)
        self.setLayout(self.row)

    def isChecked(self):
        return self.cb.isChecked()

    def getText(self):
        return self.cb.text()
