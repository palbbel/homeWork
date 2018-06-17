import sys
from urllib.request import urlopen

from lxml import etree
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, Qt, pyqtSlot
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QWidget, QDoubleSpinBox, QPushButton, QVBoxLayout



class Course(QObject):
    CBR_URL = 'http://www.cbr.ru/scripts/XML_daily.asp'


    def get(self):
        with urlopen(self.CBR_URL) as r:
            tree = etree.parse(r)
            value = tree.xpath('*[@ID="R01235"]/Value')[0].text
            return float(value.replace(',', '.'))


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._initUi()
        self._initSignals()
        self._initLayouts()


    def _initUi(self):
        self.setWindowTitle('Конвертер валют')

        self.srcLabel = QLabel('Сумма в рублях', self)
        self.resultLabel = QLabel('Сумма в долларах', self)

        self.srcAmountEdit = QDoubleSpinBox(self)
        self.srcAmountEdit.setMaximum(999999999)
        self.resultAmountEdit = QDoubleSpinBox(self)
        self.resultAmountEdit.setMaximum(999999999)

        self.convertBtn = QPushButton('Перевести', self)
        self.convertBtn.setEnabled(False)



    def _initSignals(self):
        self.srcAmountEdit.valueChanged.connect(self.controlValue)
        self.resultAmountEdit.valueChanged.connect(self.controlValue)

        self.convertBtn.clicked.connect(self.onClickConvertBtn)
        self.convertBtn.setAutoDefault(True)


        # def keyPressEvent(self, e):
        #
        #     self.convertBtn.keyPressEvent(e)
        #     if self.convertBtn.key() == Qt.Key_Return:
        #         self.onClickConvertBtn()


    def _initLayouts(self):
        w = QWidget(self)

        self.mainLayout = QVBoxLayout(w)

        self.mainLayout.addWidget(self.srcLabel)
        self.mainLayout.addWidget(self.srcAmountEdit)
        self.mainLayout.addWidget(self.resultLabel)
        self.mainLayout.addWidget(self.resultAmountEdit)
        self.mainLayout.addWidget(self.convertBtn)

        self.setCentralWidget(w)



    @QtCore.pyqtSlot()
    def onClickConvertBtn(self):
        # sender = self.sender()
        if self.srcAmountEdit != 0:
            value = self.srcAmountEdit.value()
            if value:
                self.resultAmountEdit.setValue(value / Course().get())
        if self.resultAmountEdit != 0:
            value = self.resultAmountEdit.value()
            if value:
                self.srcAmountEdit.setValue(value * Course().get())
        #value = self.srcAmountEdit.value()

        #if value:
            #self.resultAmountEdit.setValue(value / Course().get())



    def controlValue(self):
        if (self.srcAmountEdit.value() == 0 and self.resultAmountEdit.value() == 0)\
                or (self.srcAmountEdit.value() != 0 and self.resultAmountEdit.value() != 0)\
                or (self.srcAmountEdit.value() == None or self.resultAmountEdit.value() == None):
            self.convertBtn.setEnabled(False)
        else:
            self.convertBtn.setEnabled(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    converter = MainWindow()
    converter.show()

    sys.exit(app.exec_())

