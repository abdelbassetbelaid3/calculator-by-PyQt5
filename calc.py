

from PyQt5 import QtCore, QtGui, QtWidgets 




class Ui_MainWindow(object):

    # setup UI  

    def setupUi(self, MainWindow):

        # set size window
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(311, 469)


        
        # function of button 

        def clear_button():
            self.lineEdit.clear()
        def del_button():
            string = str(self.lineEdit.text())  
            self.lineEdit.clear()        
            self.lineEdit.insert(string[:-1])    

        def clicked_button(button):
            self.lineEdit.insert(str(button))

        def result():
            string = self.lineEdit.text()
            string = string.replace("^","**")
            x = float(eval(string)) 
            self.label_1.setText(str(x))






        



        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # add buttons to UI

        #### numbers buttons

        self.Button_0 = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: clicked_button(0))
        self.Button_0.setGeometry(QtCore.QRect(70, 410, 50, 50))
        self.Button_0.setObjectName("Button_0")



        self.Button_1 = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: clicked_button(1))
        self.Button_1.setGeometry(QtCore.QRect(10, 350, 50, 50))
        self.Button_1.setObjectName("Button_1")



        self.Button_2 = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: clicked_button(2))
        self.Button_2.setGeometry(QtCore.QRect(70, 350, 50, 50))
        self.Button_2.setObjectName("Button_2")



        self.Button_3 = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: clicked_button(3))
        self.Button_3.setGeometry(QtCore.QRect(130, 350, 50, 50))
        self.Button_3.setObjectName("Button_3")



        self.Button_4 = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: clicked_button(4))
        self.Button_4.setGeometry(QtCore.QRect(10, 290, 50, 50))
        self.Button_4.setObjectName("Button_4")



        self.Button_5 = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: clicked_button(5))
        self.Button_5.setGeometry(QtCore.QRect(70, 290, 50, 50))
        self.Button_5.setObjectName("Button_5")



        self.Button_6 = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: clicked_button(6))
        self.Button_6.setGeometry(QtCore.QRect(130, 290, 50, 50))
        self.Button_6.setObjectName("Button_6")



        self.Button_7 = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: clicked_button(7))
        self.Button_7.setGeometry(QtCore.QRect(10, 230, 50, 50))
        self.Button_7.setObjectName("Button_7")



        self.Button_8 = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: clicked_button(8))
        self.Button_8.setGeometry(QtCore.QRect(70, 230, 50, 50))
        self.Button_8.setObjectName("Button_8")



        self.Button_9 = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: clicked_button(9))
        self.Button_9.setGeometry(QtCore.QRect(130, 230, 50, 50))
        self.Button_9.setObjectName("Button_9")



        # operators buttons

        self.Button_pow = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: clicked_button("^"))
        self.Button_pow.setGeometry(QtCore.QRect(190, 170, 50, 50))
        self.Button_pow.setObjectName("Button_pow")



        self.Button_sqrt = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: clicked_button("^0.5"))
        self.Button_sqrt.setGeometry(QtCore.QRect(250, 170, 50, 50))
        self.Button_sqrt.setObjectName("Button_sqrt")



        self.Button_precentage = QtWidgets.QPushButton(self.centralwidget)
        self.Button_precentage.setGeometry(QtCore.QRect(10, 170, 50, 50))
        self.Button_precentage.setObjectName("Button_precentage")



        self.Button_open_brackets = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: clicked_button("("))
        self.Button_open_brackets.setGeometry(QtCore.QRect(70, 170, 50, 50))
        self.Button_open_brackets.setObjectName("Button_open_brackets")



        self.Button_close_brackets = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: clicked_button(")"))
        self.Button_close_brackets.setGeometry(QtCore.QRect(130, 170, 50, 50))
        self.Button_close_brackets.setObjectName("Button_close_brackets")



        self.Button_delete = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: del_button())
        self.Button_delete.setGeometry(QtCore.QRect(190, 230, 50, 50))
        self.Button_delete.setObjectName("Button_delete")



        self.Button_negate = QtWidgets.QPushButton(self.centralwidget)
        self.Button_negate.setGeometry(QtCore.QRect(10, 410, 50, 50))
        self.Button_negate.setObjectName("Button_negate")



        self.Button_multiple = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: clicked_button("*"))
        self.Button_multiple.setGeometry(QtCore.QRect(190, 290, 50, 50))
        self.Button_multiple.setObjectName("Button_multiple")



        self.Button_point = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: clicked_button("."))
        self.Button_point.setGeometry(QtCore.QRect(130, 410, 50, 50))
        self.Button_point.setObjectName("Button_point")



        self.Button_equal = QtWidgets.QPushButton(self.centralwidget,clicked =lambda: result())
        self.Button_equal.setGeometry(QtCore.QRect(250, 410, 50, 50))
        self.Button_equal.setObjectName("pushButton_25")



        self.Button_plus = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: clicked_button("+"))
        self.Button_plus.setGeometry(QtCore.QRect(190, 350, 50, 50))
        self.Button_plus.setObjectName("Button_plus")



        self.Button_ans = QtWidgets.QPushButton(self.centralwidget)
        self.Button_ans.setGeometry(QtCore.QRect(190, 410, 50, 50))
        self.Button_ans.setObjectName("Button_ans")



        self.Button_divide = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: clicked_button("/"))
        self.Button_divide.setGeometry(QtCore.QRect(250, 290, 50, 50))
        self.Button_divide.setObjectName("Button_divide")



        self.Button_minus = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: clicked_button("-"))
        self.Button_minus.setGeometry(QtCore.QRect(250, 350, 50, 50))
        self.Button_minus.setObjectName("Button_minus")



        self.Button_clear = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: clear_button())
        self.Button_clear.setGeometry(QtCore.QRect(250, 230, 50, 50))
        self.Button_clear.setObjectName("Button_clear")

        # resualt screen

        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(10, 90, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_1.setFont(font)
        self.label_1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_1.setObjectName("label_1")


        # type screen
              
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 291, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")


        # menu bar
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 311, 31))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)





        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # translate UI 

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowIcon(QtGui.QIcon('\\calculator-by-PyQt5\\logo.png'))
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.Button_pow.setText(_translate("MainWindow", "^"))
        self.Button_sqrt.setText(_translate("MainWindow", "^0.5"))
        self.Button_precentage.setText(_translate("MainWindow", "%"))
        self.Button_7.setText(_translate("MainWindow", "7"))
        self.Button_8.setText(_translate("MainWindow", "8"))
        self.Button_open_brackets.setText(_translate("MainWindow", "("))
        self.Button_close_brackets.setText(_translate("MainWindow", ")"))
        self.Button_9.setText(_translate("MainWindow", "9"))
        self.Button_delete.setText(_translate("MainWindow", "del"))
        self.Button_4.setText(_translate("MainWindow", "4"))
        self.Button_1.setText(_translate("MainWindow", "1"))
        self.Button_negate.setText(_translate("MainWindow", "+/-"))
        self.Button_5.setText(_translate("MainWindow", "5"))
        self.Button_2.setText(_translate("MainWindow", "2"))
        self.Button_0.setText(_translate("MainWindow", "0"))
        self.Button_6.setText(_translate("MainWindow", "6"))
        self.Button_3.setText(_translate("MainWindow", "3"))
        self.Button_multiple.setText(_translate("MainWindow", "x"))
        self.Button_point.setText(_translate("MainWindow", "."))
        self.Button_clear.setText(_translate("MainWindow", "Clear"))
        self.Button_plus.setText(_translate("MainWindow", "+"))
        self.Button_ans.setText(_translate("MainWindow", "ans"))
        self.Button_divide.setText(_translate("MainWindow", "/"))
        self.Button_minus.setText(_translate("MainWindow", "-"))
        self.Button_equal.setText(_translate("MainWindow", "="))
        self.label_1.setText(_translate("MainWindow", "00000000000000000"))
        


# driver code

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
