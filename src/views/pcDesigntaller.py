# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/views/pcDesigntaller.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1572, 834)
        MainWindow.setMouseTracking(False)
        MainWindow.setTabletTracking(False)
        MainWindow.setAcceptDrops(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setAutoFillBackground(True)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setEnabled(True)
        self.scrollArea.setMaximumSize(QtCore.QSize(1920, 1080))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1552, 814))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.textEditCodigoObjeto = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.textEditCodigoObjeto.setFrameShape(QtWidgets.QFrame.Box)
        self.textEditCodigoObjeto.setObjectName("textEditCodigoObjeto")
        self.gridLayout.addWidget(self.textEditCodigoObjeto, 3, 3, 4, 1)
        self.table_registros = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.table_registros.setMinimumSize(QtCore.QSize(356, 0))
        self.table_registros.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.table_registros.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table_registros.setObjectName("table_registros")
        self.table_registros.setColumnCount(2)
        self.table_registros.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.table_registros.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_registros.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_registros.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_registros.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_registros.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_registros.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_registros.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_registros.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_registros.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_registros.setItem(3, 0, item)
        self.table_registros.horizontalHeader().setDefaultSectionSize(170)
        self.gridLayout.addWidget(self.table_registros, 2, 1, 3, 2)
        self.button_enlazar_cargar = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.button_enlazar_cargar.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.button_enlazar_cargar.setObjectName("button_enlazar_cargar")
        self.gridLayout.addWidget(self.button_enlazar_cargar, 2, 3, 1, 1)
        self.textEditConsola = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.textEditConsola.setFrameShape(QtWidgets.QFrame.Box)
        self.textEditConsola.setObjectName("textEditConsola")
        self.gridLayout.addWidget(self.textEditConsola, 8, 2, 4, 3)
        self.button_ensamblar = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.button_ensamblar.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.button_ensamblar.setObjectName("button_ensamblar")
        self.gridLayout.addWidget(self.button_ensamblar, 1, 4, 1, 1)
        self.button_ultima_instruccion = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.button_ultima_instruccion.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.button_ultima_instruccion.setObjectName("button_ultima_instruccion")
        self.gridLayout.addWidget(self.button_ultima_instruccion, 11, 1, 1, 1)
        self.table_alu = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.table_alu.setMinimumSize(QtCore.QSize(356, 0))
        self.table_alu.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.table_alu.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table_alu.setObjectName("table_alu")
        self.table_alu.setColumnCount(2)
        self.table_alu.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.table_alu.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_alu.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_alu.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_alu.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_alu.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_alu.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_alu.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_alu.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_alu.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_alu.setItem(3, 0, item)
        self.table_alu.horizontalHeader().setDefaultSectionSize(170)
        self.gridLayout.addWidget(self.table_alu, 6, 1, 1, 2)
        self.button_compilar = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.button_compilar.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.button_compilar.setObjectName("button_compilar")
        self.gridLayout.addWidget(self.button_compilar, 1, 5, 1, 1)
        self.label_ram = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_ram.setMouseTracking(True)
        self.label_ram.setToolTip("")
        self.label_ram.setObjectName("label_ram")
        self.gridLayout.addWidget(self.label_ram, 0, 0, 1, 1)
        self.label_codigo_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_codigo_2.setMouseTracking(True)
        self.label_codigo_2.setToolTip("")
        self.label_codigo_2.setObjectName("label_codigo_2")
        self.gridLayout.addWidget(self.label_codigo_2, 0, 3, 1, 1)
        self.label_codigo = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_codigo.setMouseTracking(True)
        self.label_codigo.setToolTip("")
        self.label_codigo.setObjectName("label_codigo")
        self.gridLayout.addWidget(self.label_codigo, 0, 4, 1, 1)
        self.label_alu = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_alu.setObjectName("label_alu")
        self.gridLayout.addWidget(self.label_alu, 5, 1, 1, 1)
        self.button_siguiente_instruccion = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.button_siguiente_instruccion.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.button_siguiente_instruccion.setAutoDefault(False)
        self.button_siguiente_instruccion.setDefault(False)
        self.button_siguiente_instruccion.setFlat(False)
        self.button_siguiente_instruccion.setObjectName("button_siguiente_instruccion")
        self.gridLayout.addWidget(self.button_siguiente_instruccion, 10, 1, 1, 1)
        self.label_registros = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_registros.setMouseTracking(True)
        self.label_registros.setToolTip("")
        self.label_registros.setObjectName("label_registros")
        self.gridLayout.addWidget(self.label_registros, 0, 1, 1, 1)
        self.label_unidad_control = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_unidad_control.setObjectName("label_unidad_control")
        self.gridLayout.addWidget(self.label_unidad_control, 7, 1, 1, 1)
        self.button_reiniciar = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.button_reiniciar.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.button_reiniciar.setObjectName("button_reiniciar")
        self.gridLayout.addWidget(self.button_reiniciar, 9, 1, 1, 1)
        self.textEditCodigoFuente = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.textEditCodigoFuente.setFrameShape(QtWidgets.QFrame.Box)
        self.textEditCodigoFuente.setObjectName("textEditCodigoFuente")
        self.gridLayout.addWidget(self.textEditCodigoFuente, 2, 5, 5, 1)
        self.table_unidad_control = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.table_unidad_control.setMinimumSize(QtCore.QSize(288, 0))
        self.table_unidad_control.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.table_unidad_control.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.table_unidad_control.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table_unidad_control.setObjectName("table_unidad_control")
        self.table_unidad_control.setColumnCount(1)
        self.table_unidad_control.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.table_unidad_control.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_unidad_control.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_unidad_control.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_unidad_control.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_unidad_control.setItem(1, 0, item)
        self.table_unidad_control.horizontalHeader().setDefaultSectionSize(165)
        self.gridLayout.addWidget(self.table_unidad_control, 8, 1, 1, 1)
        self.label_codigo_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_codigo_3.setMouseTracking(True)
        self.label_codigo_3.setToolTip("")
        self.label_codigo_3.setObjectName("label_codigo_3")
        self.gridLayout.addWidget(self.label_codigo_3, 0, 5, 1, 1)
        self.textEditCodigoASM = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.textEditCodigoASM.setFrameShape(QtWidgets.QFrame.Box)
        self.textEditCodigoASM.setObjectName("textEditCodigoASM")
        self.gridLayout.addWidget(self.textEditCodigoASM, 2, 4, 5, 1)
        self.spinBox_pos_enlazar = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_pos_enlazar.setMaximum(1024)
        self.spinBox_pos_enlazar.setObjectName("spinBox_pos_enlazar")
        self.gridLayout.addWidget(self.spinBox_pos_enlazar, 1, 3, 1, 1)
        self.table_ram = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.table_ram.setEnabled(True)
        self.table_ram.setMinimumSize(QtCore.QSize(288, 0))
        self.table_ram.setAccessibleName("")
        self.table_ram.setAccessibleDescription("")
        self.table_ram.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.table_ram.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.table_ram.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.table_ram.setLineWidth(1)
        self.table_ram.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table_ram.setShowGrid(True)
        self.table_ram.setWordWrap(False)
        self.table_ram.setCornerButtonEnabled(False)
        self.table_ram.setRowCount(1024)
        self.table_ram.setObjectName("table_ram")
        self.table_ram.setColumnCount(1)
        item = QtWidgets.QTableWidgetItem()
        item.setText("Valor Binario")
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.table_ram.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_ram.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_ram.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_ram.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_ram.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_ram.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_ram.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_ram.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_ram.setItem(7, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_ram.setItem(8, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_ram.setItem(9, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_ram.setItem(10, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_ram.setItem(11, 0, item)
        self.table_ram.horizontalHeader().setCascadingSectionResizes(False)
        self.table_ram.horizontalHeader().setDefaultSectionSize(210)
        self.gridLayout.addWidget(self.table_ram, 2, 0, 10, 1)
        self.textEditInput = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.textEditInput.setObjectName("textEditInput")
        self.gridLayout.addWidget(self.textEditInput, 8, 5, 4, 1)
        self.label_codigo_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_codigo_4.setMouseTracking(True)
        self.label_codigo_4.setToolTip("")
        self.label_codigo_4.setObjectName("label_codigo_4")
        self.gridLayout.addWidget(self.label_codigo_4, 7, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 7, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 7, 5, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textEditCodigoObjeto.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        item = self.table_registros.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "A"))
        item = self.table_registros.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "B"))
        item = self.table_registros.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "C"))
        item = self.table_registros.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "D"))
        item = self.table_registros.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "BINARIO"))
        item = self.table_registros.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "DECIMAL"))
        __sortingEnabled = self.table_registros.isSortingEnabled()
        self.table_registros.setSortingEnabled(False)
        self.table_registros.setSortingEnabled(__sortingEnabled)
        self.button_enlazar_cargar.setText(_translate("MainWindow", "Enlazar Cargar"))
        self.textEditConsola.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.button_ensamblar.setText(_translate("MainWindow", "Ensamblar"))
        self.button_ultima_instruccion.setText(_translate("MainWindow", "Saltar a la ultima instrucción"))
        item = self.table_alu.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "C"))
        item = self.table_alu.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "P"))
        item = self.table_alu.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "N"))
        item = self.table_alu.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "D"))
        item = self.table_alu.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "BINARIO"))
        item = self.table_alu.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "DECIMAL"))
        __sortingEnabled = self.table_alu.isSortingEnabled()
        self.table_alu.setSortingEnabled(False)
        self.table_alu.setSortingEnabled(__sortingEnabled)
        self.button_compilar.setText(_translate("MainWindow", "Compilar"))
        self.label_ram.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"                        <html><head><meta name=\"qrichtext\" content=\"1\" /><style\n"
"                        type=\"text/css\">\n"
"                        p, li { white-space: pre-wrap; }\n"
"                        </style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\n"
"                        font-weight:400; font-style:normal;\">\n"
"                        <p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px;\n"
"                        margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\"\n"
"                        font-size:14pt; font-weight:600;\">RAM</span></p></body></html>\n"
"                    "))
        self.label_codigo_2.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt;\">                        </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:600;\">CÓDIGO RELOCALIZABLE</span><span style=\" font-size:12pt;\">                   </span></p></body></html>"))
        self.label_codigo.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\">                        </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt; font-weight:600;\">CÓDIGO ASSEMBLER</span>                   </p></body></html>"))
        self.label_alu.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\"\n"
"                        font-size:14pt; font-weight:600;\">INDICADORES ALU</span></p></body></html>\n"
"                    "))
        self.button_siguiente_instruccion.setText(_translate("MainWindow", "Siguiente instrucción"))
        self.label_registros.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"                        <html><head><meta name=\"qrichtext\" content=\"1\" /><style\n"
"                        type=\"text/css\">\n"
"                        p, li { white-space: pre-wrap; }\n"
"                        </style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\n"
"                        font-weight:400; font-style:normal;\">\n"
"                        <p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px;\n"
"                        margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\"\n"
"                        font-size:14pt; font-weight:600;\">REGISTROS</span></p></body></html>\n"
"                    "))
        self.label_unidad_control.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\"\n"
"                        font-size:14pt; font-weight:600;\">UNIDAD DE CONTROL</span></p></body></html>\n"
"                    "))
        self.button_reiniciar.setText(_translate("MainWindow", "Reiniciar"))
        self.textEditCodigoFuente.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">fun</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    var a : entero;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    var b : entero;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    a = 1;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    b = 3;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    a = a + b;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">ffun</span></p></body></html>"))
        item = self.table_unidad_control.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "IC"))
        item = self.table_unidad_control.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "CP"))
        item = self.table_unidad_control.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "BINARIO"))
        __sortingEnabled = self.table_unidad_control.isSortingEnabled()
        self.table_unidad_control.setSortingEnabled(False)
        self.table_unidad_control.setSortingEnabled(__sortingEnabled)
        self.label_codigo_3.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\">                        </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt; font-weight:600;\">CÓDIGO ALTO NIVEL</span>                   </p></body></html>"))
        self.textEditCodigoASM.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt;\">mcd:</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\">                        </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt;\">CargarValor    A, 128</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\">                        </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt;\">CargarValor     B, 244<br />bucle:</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\">                        </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt;\">Copiar        A, C</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\">                        </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt;\">Restar        C, B</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\">                        </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt;\">SaltarSiCero    fin</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt;\">SaltarSiNeg    menor</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\">                        </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt;\">Restar        A, B</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\">                        </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt;\">Saltar        bucle</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\">                        </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt;\">menor:                        </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\">                        </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt;\">Restar        B,A</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\">                        </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt;\">Saltar        bucle</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\">                        </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt;\">fin:</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\">                        </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt;\">Almacenar    A,50</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\">                        </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt;\">Parar</span>                    </p></body></html>"))
        self.table_ram.setSortingEnabled(False)
        __sortingEnabled = self.table_ram.isSortingEnabled()
        self.table_ram.setSortingEnabled(False)
        self.table_ram.setSortingEnabled(__sortingEnabled)
        self.label_codigo_4.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">I/O:</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "Consola"))
        self.label_2.setText(_translate("MainWindow", "Input"))
