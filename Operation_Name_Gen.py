#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide.QtCore import *
from PySide.QtGui import *
import Gen_UI, random, sys

class MainDialog(QDialog, Gen_UI.Ui_Dialog):

    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)
        self.connect(self.genButton, SIGNAL("clicked()"), self.generateOpName)

    def generateOpName(self):
        new_noun = self.selectNoun()
        new_verb = self.selectVerb()

        self.plainTextEdit.setPlainText(
            "[+] Welcome to Operation " + new_verb + " " + new_noun + "!" +
            "\n\n[+] Or, alternatively:" +
            "\n\n[+] Welcome to Operation " + new_noun + " " + new_verb + "!"
        )

    def selectNoun(self):
        nounArr = open("conv.data.noun", "r").read().splitlines()
        op_noun = nounArr[random.randint (0, len(nounArr))].title()
        return op_noun

    def selectVerb(self):
        verbArr = open("conv.data.verb", "r").read().splitlines()
        op_verb = verbArr[random.randint (0, len(verbArr))].title()
        return op_verb

app = QApplication(sys.argv)
form = MainDialog()
form.show()
app.exec_()

