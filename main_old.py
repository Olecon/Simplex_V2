import os
import copy
import numpy as np
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget, QVBoxLayout
import pyqtgraph as pg 
from PyQt6 import QtCore, QtGui, QtWidgets
import math
from lmfit import Model





class Ui_MainWindow(object):
    def __init__(self):
        self.Calib_Data = []
        self.Before_Copy = []
        self.Start_conf = []
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Simplex_V2")
        MainWindow.setWindowTitle('Simplex_V2')  
        MainWindow.resize(757, 463)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 460))
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetNoConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 171, 431))
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidget.setMaximumWidth(172)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(180, 0))
        self.tabWidget.setObjectName("tabWidget")
        self.Methods = QtWidgets.QWidget()
        self.Methods.setObjectName("Methods")
        self.label = QtWidgets.QLabel(parent=self.Methods)
        self.label.setGeometry(QtCore.QRect(0, 0, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.pribor = QtWidgets.QComboBox(parent=self.Methods)
        self.pribor.setGeometry(QtCore.QRect(0, 20, 151, 22))
        self.pribor.setObjectName("pribor")
        self.method = QtWidgets.QComboBox(parent=self.Methods)
        self.method.setGeometry(QtCore.QRect(0, 60, 151, 22))
        self.method.setObjectName("method")
        self.label_2 = QtWidgets.QLabel(parent=self.Methods)
        self.label_2.setGeometry(QtCore.QRect(0, 40, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.model = QtWidgets.QComboBox(parent=self.Methods)
        self.model.setGeometry(QtCore.QRect(0, 100, 151, 22))
        self.model.setObjectName("model")
        self.label_3 = QtWidgets.QLabel(parent=self.Methods)
        self.label_3.setGeometry(QtCore.QRect(0, 80, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.change_file = QtWidgets.QPushButton(parent=self.Methods)
        self.change_file.setGeometry(QtCore.QRect(0, 320, 151, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.change_file.setFont(font)
        self.change_file.setObjectName("change_file")
        self.Water = QtWidgets.QCheckBox(parent=self.Methods)
        self.Water.setGeometry(QtCore.QRect(0, 130, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Water.setFont(font)
        self.Water.setObjectName("Water")
        self.label_4 = QtWidgets.QLabel(parent=self.Methods)
        self.label_4.setGeometry(QtCore.QRect(0, 150, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.dG_temp = QtWidgets.QSpinBox(parent=self.Methods)
        self.dG_temp.setGeometry(QtCore.QRect(10, 170, 141, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dG_temp.setFont(font)
        self.dG_temp.setObjectName("dG_temp")
        self.tabWidget.addTab(self.Methods, "")
        self.Parametrs = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Parametrs.setFont(font)
        self.Parametrs.setObjectName("Parametrs")
        self.Calculation = QtWidgets.QPushButton(parent=self.Parametrs)
        self.Calculation.setGeometry(QtCore.QRect(0, 320, 151, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Calculation.setFont(font)
        self.Calculation.setObjectName("Calculation")
        self.Calculation.clicked.connect(lambda: Ui_MainWindow.Approximation(self))
        self.frame = QtWidgets.QFrame(parent=self.Parametrs)
        self.frame.setGeometry(QtCore.QRect(0, 0, 161, 51))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.Entalpy = QtWidgets.QCheckBox(parent=self.frame)
        self.Entalpy.setGeometry(QtCore.QRect(0, 0, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Entalpy.setFont(font)
        self.Entalpy.setObjectName("Entalpy")
        self.Entalpy_edit = QtWidgets.QLineEdit(parent=self.frame)
        self.Entalpy_edit.setGeometry(QtCore.QRect(0, 20, 161, 21))
        self.Entalpy_edit.setText("")
        self.Entalpy_edit.setObjectName("Entalpy_edit")
        self.frame_2 = QtWidgets.QFrame(parent=self.Parametrs)
        self.frame_2.setGeometry(QtCore.QRect(0, 50, 161, 51))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.Enthropy = QtWidgets.QCheckBox(parent=self.frame_2)
        self.Enthropy.setGeometry(QtCore.QRect(0, 0, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Enthropy.setFont(font)
        self.Enthropy.setObjectName("Enthropy")
        self.Enthropy_edit = QtWidgets.QLineEdit(parent=self.frame_2)
        self.Enthropy_edit.setGeometry(QtCore.QRect(0, 20, 161, 21))
        self.Enthropy_edit.setText("")
        self.Enthropy_edit.setObjectName("Enthropy_edit")
        self.frame_3 = QtWidgets.QFrame(parent=self.Parametrs)
        self.frame_3.setGeometry(QtCore.QRect(0, 100, 161, 51))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.Start_temp = QtWidgets.QLabel(parent=self.frame_3)
        self.Start_temp.setGeometry(QtCore.QRect(0, 0, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Start_temp.setFont(font)
        self.Start_temp.setObjectName("Start_temp")
        self.Start_temp_edit = QtWidgets.QLineEdit(parent=self.frame_3)
        self.Start_temp_edit.setGeometry(QtCore.QRect(0, 20, 161, 21))
        self.Start_temp_edit.setText("")
        self.Start_temp_edit.setObjectName("Start_temp_edit")
        self.Start_temp.setText("Начальная температура")
        self.frame_5 = QtWidgets.QFrame(parent=self.Parametrs)
        self.frame_5.setGeometry(QtCore.QRect(0, 200, 161, 51))
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.Bss = QtWidgets.QCheckBox(parent=self.frame_5)
        self.Bss.setGeometry(QtCore.QRect(0, 0, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Bss.setFont(font)
        self.Bss.setObjectName("Bss")
        self.Bss_edit = QtWidgets.QLineEdit(parent=self.frame_5)
        self.Bss_edit.setGeometry(QtCore.QRect(0, 20, 81, 21))
        self.Bss_edit.setText("")
        self.Bss_edit.setObjectName("Bss_edit")
        self.Css_edit = QtWidgets.QLineEdit(parent=self.frame_5)
        self.Css_edit.setGeometry(QtCore.QRect(80, 20, 81, 21))
        self.Css_edit.setText("")
        self.Css_edit.setObjectName("Css_edit")
        self.Css = QtWidgets.QCheckBox(parent=self.frame_5)
        self.Css.setGeometry(QtCore.QRect(80, 0, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Css.setFont(font)
        self.Css.setObjectName("Css")
        self.frame_6 = QtWidgets.QFrame(parent=self.Parametrs)
        self.frame_6.setGeometry(QtCore.QRect(0, 250, 161, 51))
        self.frame_6.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_6.setObjectName("frame_6")
        self.Bds = QtWidgets.QCheckBox(parent=self.frame_6)
        self.Bds.setGeometry(QtCore.QRect(0, 0, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Bds.setFont(font)
        self.Bds.setObjectName("Bds")
        self.Bds_edit = QtWidgets.QLineEdit(parent=self.frame_6)
        self.Bds_edit.setGeometry(QtCore.QRect(0, 20, 81, 21))
        self.Bds_edit.setText("")
        self.Bds_edit.setObjectName("Bds_edit")
        self.Cds = QtWidgets.QCheckBox(parent=self.frame_6)
        self.Cds.setGeometry(QtCore.QRect(80, 0, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Cds.setFont(font)
        self.Cds.setObjectName("Cds")
        self.Cds_edit = QtWidgets.QLineEdit(parent=self.frame_6)
        self.Cds_edit.setGeometry(QtCore.QRect(80, 20, 81, 21))
        self.Cds_edit.setText("")
        self.Cds_edit.setObjectName("Cds_edit")
        self.frame_7 = QtWidgets.QFrame(parent=self.Parametrs)
        self.frame_7.setGeometry(QtCore.QRect(0, 150, 161, 51))
        self.frame_7.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_7.setObjectName("frame_7")
        self.End_temp = QtWidgets.QLabel(parent=self.frame_7)
        self.End_temp.setGeometry(QtCore.QRect(0, 0, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.End_temp.setFont(font)
        self.End_temp.setObjectName("End_temp")
        self.End_temp.setText("Конечная температура")
        self.End_temp_edit = QtWidgets.QLineEdit(parent=self.frame_7)
        self.End_temp_edit.setGeometry(QtCore.QRect(0, 20, 161, 21))
        self.End_temp_edit.setText("")
        self.End_temp_edit.setObjectName("End_temp_edit")
        #######################
        self.Baseline_list = QtWidgets.QComboBox(parent=self.Methods)
        self.Baseline_list.setGeometry(QtCore.QRect(0, 230, 151, 21))
        self.Baseline_list.setObjectName("Baseline_list")
        self.Baseline_check = QtWidgets.QCheckBox(parent=self.Methods)
        self.Baseline_check.setGeometry(QtCore.QRect(0, 210, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Baseline_check.setFont(font)
        self.Baseline_check.setObjectName("Baseline_check")

        #######################
        self.tabWidget.addTab(self.Parametrs, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Table_calc = QtWidgets.QTableWidget(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.Table_calc.sizePolicy().hasHeightForWidth())
        self.Table_calc.setSizePolicy(sizePolicy)
        self.Table_calc.setObjectName("Table_calc")
        self.verticalLayout.addWidget(self.Table_calc)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetFixedSize)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.CommandLine = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.CommandLine.setObjectName("CommandLine")
        self.horizontalLayout_2.addWidget(self.CommandLine)
        self.Run_Command = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Run_Command.setObjectName("Run_Command")
        self.horizontalLayout_2.addWidget(self.Run_Command)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 757, 18))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(parent=self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtGui.QAction(parent=MainWindow)
        self.action.setObjectName("action")
        self.action_3 = QtGui.QAction(parent=MainWindow)
        self.action_3.setObjectName("action_3")
        self.actionCary_3500 = QtGui.QAction(parent=MainWindow)
        self.actionCary_3500.setObjectName("actionCary_3500")
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_3)
        self.menubar.addAction(self.menu.menuAction())
        self.action_4 = QtGui.QAction(parent=MainWindow)
        self.menu_5 = QtWidgets.QMenu(parent=self.menu)
        self.menu_5.setObjectName("menu_5")
        self.action_4.setObjectName("action_4")
        self.menu_5.addAction(self.action_4)
        self.action_Baseline = QtGui.QAction(parent=MainWindow)
        self.action_Baseline.setObjectName("action_Baseline")
        self.menu_5.addAction(self.action_Baseline)
        self.menu.addAction(self.menu_5.menuAction())
        self.menu.addAction(self.action_3)
        self.menubar.addAction(self.menu.menuAction())
        self.action_4.triggered.connect(lambda: Ui_MainWindow.Save_Table(self))
        self.action_Baseline.triggered.connect(lambda: Ui_MainWindow.Save_Data(self))




        self.change_file.clicked.connect(lambda: Ui_MainWindow.add_file_and_start_calibration(self))
        self.action.triggered.connect(lambda: self.Plot_window.show())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        Ui_MainWindow.Run_Plot(self)
        
        self.Table_calc.clicked.connect(self.review_data)
        #self.Table_calc.setEditTriggers(QtWidgets.QAbstractItemView.editTriggers)
    
    def Run_Plot(self):
        #Graph
        self.Plot_window = QWidget()
        self.Plot_window.setWindowTitle('Graph')
        self.layout = QVBoxLayout(self.Plot_window)
        self.PLT = pg.PlotWidget(parent=self.Plot_window)
        self.Plot_window.resize(300,600)
        self.PLT.showGrid(x=True,y=True)
        self.PLT.setBackground('w')
        self.PLT.setLabel('left', 'Absorbtion', units='u.e.')
        self.PLT.setLabel('bottom', 'Temperature', units='°C')
        self.PLT.setXRange(0,100)
        self.PLT.setYRange(0,1)

        self.DPLT = pg.PlotWidget(parent=self.Plot_window)
        self.DPLT.showGrid(x=True,y=True)
        self.DPLT.setBackground('w')
        self.DPLT.addLegend()
        self.DPLT.setLabel('left', 'Absorbtion', units='u.e.')
        self.DPLT.setLabel('bottom', 'Temperature', units='°C')
        self.DPLT.setXRange(0,100)
        self.DPLT.setYRange(0,1)

        self.min_line_to_PLT = pg.InfiniteLine(angle=90, movable=True, pen=pg.mkPen(width=5, color='b'), label="Start")
        self.max_line_to_PLT = pg.InfiniteLine(angle=90, movable=True, pen=pg.mkPen(width=5, color='r'), label="Stop")
        self.min_line_to_DPLT = pg.InfiniteLine(angle=90, movable=True, pen=pg.mkPen( width=5, color='b'), label="Start")
        self.max_line_to_DPLT = pg.InfiniteLine(angle=90, movable=True, pen=pg.mkPen( width=5, color='r'), label="Stop")

        self.min_line_to_PLT.setPos(5)
        self.min_line_to_DPLT.setPos(5)
        self.max_line_to_PLT.setPos(95)
        self.max_line_to_DPLT.setPos(95)

        self.PLT.addItem(self.min_line_to_PLT)
        self.PLT.addItem(self.max_line_to_PLT)
        self.DPLT.addItem(self.min_line_to_DPLT)
        self.DPLT.addItem(self.max_line_to_DPLT)

        self.min_line_to_PLT.sigPositionChangeFinished.connect(lambda: Ui_MainWindow.Infinity_line_usage(self,"min_line_to_PLT"))
        self.max_line_to_PLT.sigPositionChangeFinished.connect(lambda: Ui_MainWindow.Infinity_line_usage(self,"max_line_to_PLT"))
        self.min_line_to_DPLT.sigPositionChangeFinished.connect(lambda: Ui_MainWindow.Infinity_line_usage(self,"min_line_to_DPLT"))
        self.max_line_to_DPLT.sigPositionChangeFinished.connect(lambda: Ui_MainWindow.Infinity_line_usage(self,"max_line_to_DPLT"))

        self.layout.addWidget(self.PLT)
        self.layout.addWidget(self.DPLT)
        self.Plot_window.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Simplex_V2"))
        self.label.setText(_translate("MainWindow", "Прибор"))
        self.label_2.setText(_translate("MainWindow", "Метод"))
        self.label_3.setText(_translate("MainWindow", "Модель"))
        self.change_file.setText(_translate("MainWindow", "Выбрать файл"))
        self.Water.setText(_translate("MainWindow", "Расширение воды"))
        self.label_4.setText(_translate("MainWindow", "Температура dG"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Methods), _translate("MainWindow", "Метод"))
        self.Calculation.setText(_translate("MainWindow", "Расчет"))
        self.Entalpy.setText(_translate("MainWindow", "Энтальпия (dH)"))
        self.Enthropy.setText(_translate("MainWindow", "Энтропия (dS)"))
        self.Bss.setText(_translate("MainWindow", "Bss"))
        self.Css.setText(_translate("MainWindow", "Css"))
        self.Bds.setText(_translate("MainWindow", "Bds"))
        self.Cds.setText(_translate("MainWindow", "Cds"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Parametrs), _translate("MainWindow", "Параметры"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))
        self.action.setText(_translate("MainWindow", "График"))
        self.End_temp.setText(_translate("MainWindow", "Конечная температура"))
        self.Baseline_check.setText(_translate("MainWindow", "Базовая линия"))
        self.action_3.setText(_translate("MainWindow", "Выход"))
        self.actionCary_3500.setText(_translate("MainWindow", "Cary_3500"))
        self.action_4.setText(_translate("MainWindow", "Таблицу"))
        self.action_Baseline.setText(_translate("MainWindow", "Данные"))
        self.menu_5.setTitle(_translate("MainWindow", "Сохранить как"))

    def add(self):
        self.pribor.addItem("Cary_300")
        self.pribor.addItem("Cary_3500")
        self.method.addItems(os.listdir("./Cary_300/"))

        self.pribor.activated.connect(lambda: update_pribor_combobox(self))
        self.model.addItem("Не самокомплимент")
        self.model.addItem("Самокомплимент")
        self.model.addItem("Шпилька")
        
        self.dG_temp.setValue(37)
        self.Water.setChecked(True)
        self.Baseline_check.stateChanged.connect(lambda: Ui_MainWindow.Usage_baseline(self))

        def update_pribor_combobox(self):
            if self.pribor.currentText() == "Cary_300":
                self.method.clear()
                method_list = os.listdir("./Cary_300/")
            elif self.pribor.currentText() == "Cary_3500":
                self.method.clear()
                method_list = os.listdir("./Cary_3500/")
            else:
                self.method.clear()
                method_list = []
            self.method.addItems(method_list)

    def add_file_and_start_calibration(self):
        file = QFileDialog.getOpenFileName()[0]

        def Parsing_Cary300(file_name):
            file = open(str(file_name),"r")
            file = file.readlines()
            file = [i.replace("\n","").split(",") for i in file]
            True_mass = [[],[]]

            #Sample,Name,Cell,Conc,start/endT,light, rang

            for line in file[0]:
                if len(line) != 0:
                    for i in range(0,len(line)):
                        if line[i] == "_":
                            Sample = line[0:i].replace("Sample","")
                            step = i
                            break
                    
                    for i in range(step+1,len(line)):
                        if line[i] == "@":
                            Name = line[step+1:i]
                            step = i
                            break
        
                    for i in range(step+1,len(line)):
                        if line[i] == " ":
                            Conc = line[step+1:i]
                            step = i
                            break
                    
                    for i in range(step+2,len(line)):
                        if line[i] == " ":
                            Temp = line[step+2:i]
                            step = i
                            break
                    
                    for i in range(step+1,len(line)):
                        if line[i] == "_":
                            Ramp = line[step+1:i].replace("Ramp ","")
                            step = i
                            break

                    light = line[step+1:]
                    True_mass[0].append([Sample,Name,Conc,Temp,light,Ramp])

            for Sample in range(0, len(True_mass[0])):
                True_mass[1].append([[],[]])
                for i in file[2:]:
                    try:
                        True_mass[1][Sample][0].append(float(i[Sample*2]))
                        True_mass[1][Sample][1].append(float(i[Sample*2+1]))
                    except:
                        break
            self.Baseline_list.addItems(set([i[4] for i in True_mass[0]]))
            return True_mass

                
        def Parsing_Cary3500(file_name):
            file = open(str(file_name),"r")
            file = file.readlines()
            file = [i.replace("\n","").split(",") for i in file]
            True_mass = [[],[]]

            for line in file[0]:
                if len(line) != 0:
                    for i in range(0,len(line)):
                        if line[i] == "_":
                            Sample = line[0:i].replace("Sample","")
                            step = i
                            break
                    
                    for i in range(step+1,len(line)):
                        if line[i] == "@":
                            Name = line[step+1:i]
                            step = i
                            break
                    for i in range(step+1,len(line)):
                        if line[i] == "_":
                            Conc = line[step+1:i]
                            step = i
                            break
                    
                    for i in range(step+1,len(line)):
                        if line[i] == "_":
                            light = line[step+1:i].replace('nm','')
                            step = i
                            break

                    for i in range(step+1,len(line)):
                        if line[i] == "C":
                            Temp = line[step+1:i]
                            step = i
                            break
                    True_mass[0].append([Sample,Name,Conc,Temp,light])

            #Add RAMP 
            sample_range = (np.arange(1,int(len(True_mass[0])/(len(set([i[0] for i in True_mass[0]]))*len(set([i[4] for i in True_mass[0]]))))+1)).tolist()
            step=0
            for i in range(0,len(True_mass[0])):
                if step < len(sample_range)-1: 
                    True_mass[0][i].append(sample_range[step])
                    step = step+1
                else:
                    True_mass[0][i].append(sample_range[step])
                    step=0
        
            for Sample in range(0, len(True_mass[0])):
                True_mass[1].append([[],[]])
                for i in file[2:]:
                    try:
                        True_mass[1][Sample][0].append(float(i[Sample*2]))
                        True_mass[1][Sample][1].append(float(i[Sample*2+1]))
                    except:
                        break
            self.Baseline_list.addItems(set([i[4] for i in True_mass[0]]))
            return True_mass
        
        
        def Use_calib(Source_Data, method):
            Calibration_mass = []
            for file in sorted(os.listdir(str(method))):
                file = open(str(method)+str(file),"r")
                file = file.readlines()
                file = [i.replace("\n","").split(",") for i in file]
                Calibration_mass.append(file)

            for EXP in range(0,len(Source_Data[0])):
                Sample = int(Source_Data[0][EXP][0])-1 # Начинается с 0
                Stage = int(Source_Data[0][EXP][5]) # Начинается с 1, потому что в калибровочном файле 0 столбец - исходная температура
                New_Temperature_Mass = []
                Source_Temperature_in_calibtation_file = [i[0] for i in Calibration_mass[Sample]]
                Source_Stage_Temperature_in_calibration_file = [i[Stage] for i in Calibration_mass[Sample]]

                for Source_Temperature in Source_Data[1][EXP][0]:
                    Position = [abs(float(i) - float(Source_Temperature)) for i in Source_Temperature_in_calibtation_file].index(min([abs(float(i) - float(Source_Temperature)) for i in Source_Temperature_in_calibtation_file]))
                    New_Temperature_Mass.append(float(Source_Stage_Temperature_in_calibration_file[Position]))
                
                Source_Data[1][EXP][0] = New_Temperature_Mass
            
            return Source_Data
        
        if self.pribor.currentText() == "Cary_300":
            Source_Data = Parsing_Cary300(file)
            self.Calib_Data = Use_calib(Source_Data,"./"+str(self.pribor.currentText())+"/"+str(self.method.currentText())+"/")

        elif self.pribor.currentText() == "Cary_3500":
            Source_Data = Parsing_Cary3500(file)
            self.Calib_Data = Use_calib(Source_Data,"./"+str(self.pribor.currentText())+"/"+str(self.method.currentText())+"/")        
        
        Mass = []

        for EXP in range(0,len(Source_Data[1])):
            Mass_X = []
            Mass_Y = []
            for POINT in range(0,len(Source_Data[1][EXP][0])-4):
                Mass_Y.append(np.polyfit(Source_Data[1][EXP][0][POINT:POINT+4],Source_Data[1][EXP][1][POINT:POINT+4],deg=1).tolist()[0])
                Mass_X.append(Source_Data[1][EXP][0][POINT+2])
            Mass.append([Mass_X,Mass_Y])
        Source_Data.append(Mass)
    
        Ui_MainWindow.add_table_data(self)

    def add_table_data(self):
        self.Table_calc.setColumnCount(18)
        self.Table_calc.setHorizontalHeaderLabels(["Sample", "Name","Conc","sT","eT","light","Ramp","dH","ErrordH","dS","ErrordS","Bss","Css","Bds","Cds","dG","Tm","СКО"])
        self.Table_calc.resizeColumnsToContents()
        self.Table_calc.setRowCount(len(self.Calib_Data[0]))
        
        for row in range(0,len(self.Calib_Data[0])):
            self.Table_calc.setItem(row,0, QtWidgets.QTableWidgetItem("Sample "+str(self.Calib_Data[0][row][0])))
            self.Table_calc.setItem(row,1, QtWidgets.QTableWidgetItem(str(self.Calib_Data[0][row][1])))
            self.Table_calc.setItem(row,2, QtWidgets.QTableWidgetItem(str(self.Calib_Data[0][row][2])))
            self.Table_calc.setItem(row,3,QtWidgets.QTableWidgetItem("5"))
            self.Table_calc.setItem(row,4,QtWidgets.QTableWidgetItem("95"))
            self.Table_calc.setItem(row,5, QtWidgets.QTableWidgetItem(str(self.Calib_Data[0][row][4])))
            self.Table_calc.setItem(row,6, QtWidgets.QTableWidgetItem(str(self.Calib_Data[0][row][5])))
            self.Table_calc.setItem(row,7,QtWidgets.QTableWidgetItem(str(float("-90000"))))
            self.Table_calc.setItem(row,8,QtWidgets.QTableWidgetItem(str("")))     
            self.Table_calc.setItem(row,9, QtWidgets.QTableWidgetItem(str(float("-220"))))
            self.Table_calc.setItem(row,10, QtWidgets.QTableWidgetItem(str("")))
            self.Table_calc.setItem(row,11, QtWidgets.QTableWidgetItem(str(min(self.Calib_Data[1][row][1]))))  
            self.Table_calc.setItem(row,12, QtWidgets.QTableWidgetItem(str("0")))
            self.Table_calc.setItem(row,13, QtWidgets.QTableWidgetItem(str(max(self.Calib_Data[1][row][1]))))    
            self.Table_calc.setItem(row,14, QtWidgets.QTableWidgetItem(str("0")))  
            self.Table_calc.setItem(row,15, QtWidgets.QTableWidgetItem(str("")))    
            self.Table_calc.setItem(row,16, QtWidgets.QTableWidgetItem(str("")))  
            self.Table_calc.setItem(row,17, QtWidgets.QTableWidgetItem(str("")))  
    # Reviev data on plot's and parametrs when i clicked in table_calc
    def review_data(self):
        self.selected_row = self.Table_calc.currentItem().row()
        try:
            self.PLT.removeItem(self.plot)
            self.DPLT.removeItem(self.dplot)
            self.PLT.removeItem(self.PlotGraph)
            self.DPLT.removeItem(self.DPlotGraph)
        except: 
            pass
        
        self.plot = self.PLT.plot(self.Calib_Data[1][self.selected_row][0],self.Calib_Data[1][self.selected_row][1], pen=None,symbolBrush = 0.1)
        self.dplot = self.DPLT.plot(self.Calib_Data[2][self.selected_row][0],self.Calib_Data[2][self.selected_row][1], pen=None,symbolBrush = 0.1)
        
        #Функции для построения графика
        #Не самокомплимент
        def NoSelfComp(Tmass,dH,dS,Bss,Css,Bds,Cds, Start_conf, C0):
            Y_mass = []
            for T in Tmass:
                T=float(T)
                try:
                    if Start_conf[6]:
                        Ct = float(C0)*1.00303/(1+(-1)*0.0000000000013*(T-4)**5+0.00000000042*(T-4)**4-0.000000065*(T-4)**3+0.0000083*(T-4)**2-0.000005*(T-4))
                    else:
                        Ct = float(C0)
                except: Ct=float(C0)
                
                K = np.exp((-dH + (T+273.15)*dS)/(1.987*(T+273.15)))                
                alpha= (1+Ct*K-np.sqrt(1+2*Ct*K))/(Ct*K)
                A = (Bss+Css*T)*(1-alpha)+(Bds+Cds*T)*alpha
                Y_mass.append(A)
            return Y_mass 
        #Самокомплимент
        def SelfComp(Tmass,dH,dS,Bss,Css,Bds,Cds, Start_conf, C0):
            Y_mass = []
            for T in Tmass:
                T=float(T)
                try:
                    if Start_conf[6]:
                        Ct = float(C0)*1.00303/(1+(-1)*0.0000000000013*(T-4)**5+0.00000000042*(T-4)**4-0.000000065*(T-4)**3+0.0000083*(T-4)**2-0.000005*(T-4))
                    else:
                        Ct = float(C0)
                except: Ct=float(C0)
                
                K = np.exp((-dH + (T+273.15)*dS)/(1.987*(T+273.15)))                
                alpha = 1+1/(2*K*Ct)-np.sqrt(4*K*Ct+1)/(2*K*Ct)
                A = (Bss+Css*T)*(1-alpha)+(Bds+Cds*T)*alpha
                Y_mass.append(A)
            return Y_mass     
        #Шпилька
        def loop(Tmass,dH,dS,Bss,Css,Bds,Cds, Start_conf, C0):
            Y_mass = []
            for T in Tmass:
                T=float(T)
                try:
                    if Start_conf[6]:
                        Ct = float(C0)*1.00303/(1+(-1)*0.0000000000013*(T-4)**5+0.00000000042*(T-4)**4-0.000000065*(T-4)**3+0.0000083*(T-4)**2-0.000005*(T-4))
                    else:
                        Ct = float(C0)
                except: Ct=float(C0)
                
                K = np.exp((-dH + (T+273.15)*dS)/(1.987*(T+273.15)))                
                alpha = K/(1+K)
                A = (Bss+Css*T)*(1-alpha)+(Bds+Cds*T)*alpha
                Y_mass.append(A)
            return Y_mass
        
        #Функции для построения графика производной 
        def DNoSelfComp(Tmass,dH,dS,Bss,Css,Bds,Cds, Start_conf, C0):
            Y_mass = []
            for T in Tmass:
                T=float(T)
                try:
                    if Start_conf[6]:
                        Ct = float(C0)*1.00303/(1+(-1)*0.0000000000013*(T-4)**5+0.00000000042*(T-4)**4-0.000000065*(T-4)**3+0.0000083*(T-4)**2-0.000005*(T-4))
                    else:
                        Ct = float(C0)
                except: Ct=float(C0)
                
                K = np.exp((-dH + (T+273.15)*dS)/(1.987*(T+273.15)))                
                alpha= (1+Ct*K-np.sqrt(1+2*Ct*K))/(Ct*K)
                A = (Bss+Css*T)*(1-alpha)+(Bds+Cds*T)*alpha
                Y_mass.append(A)
            Mass_X = []
            Mass_Y = []

            for POINT in range(0,len(Tmass)-4):
                Mass_Y.append(np.polyfit(Tmass[POINT:POINT+4],Y_mass[POINT:POINT+4],deg=1).tolist()[0])
                Mass_X.append(Tmass[POINT+2])
            
            return Mass_X, Mass_Y
        def DSelfComp(Tmass,dH,dS,Bss,Css,Bds,Cds, Start_conf, C0):
            Y_mass = []
            for T in Tmass:
                T=float(T)
                try:
                    if Start_conf[6]:
                        Ct = float(C0)*1.00303/(1+(-1)*0.0000000000013*(T-4)**5+0.00000000042*(T-4)**4-0.000000065*(T-4)**3+0.0000083*(T-4)**2-0.000005*(T-4))
                    else:
                        Ct = float(C0)
                except: Ct=float(C0)
                
                K = np.exp((-dH + (T+273.15)*dS)/(1.987*(T+273.15)))                
                alpha = 1+1/(2*K*Ct)-np.sqrt(4*K*Ct+1)/(2*K*Ct)
                A = (Bss+Css*T)*(1-alpha)+(Bds+Cds*T)*alpha
                Y_mass.append(A)
            
            Mass_X = []
            Mass_Y = []

            for POINT in range(0,len(Tmass)-4):
                Mass_Y.append(np.polyfit(Tmass[POINT:POINT+4],Y_mass[POINT:POINT+4],deg=1).tolist()[0])
                Mass_X.append(Tmass[POINT+2])
            
            return Mass_X, Mass_Y
        def Dloop(Tmass,dH,dS,Bss,Css,Bds,Cds, Start_conf, C0):
            Y_mass = []
            for T in Tmass:
                T=float(T)
                try:
                    if Start_conf[6]:
                        Ct = float(C0)*1.00303/(1+(-1)*0.0000000000013*(T-4)**5+0.00000000042*(T-4)**4-0.000000065*(T-4)**3+0.0000083*(T-4)**2-0.000005*(T-4))
                    else:
                        Ct = float(C0)
                except: Ct=float(C0)
                
                K = np.exp((-dH + (T+273.15)*dS)/(1.987*(T+273.15)))                
                alpha = K/(1+K)
                A = (Bss+Css*T)*(1-alpha)+(Bds+Cds*T)*alpha
                Y_mass.append(A)
            
            Mass_X = []
            Mass_Y = []

            for POINT in range(0,len(Tmass)-4):
                Mass_Y.append(np.polyfit(Tmass[POINT:POINT+4],Y_mass[POINT:POINT+4],deg=1).tolist()[0])
                Mass_X.append(Tmass[POINT+2])
            
            return Mass_X, Mass_Y
        ###########################################
        try:
            if self.model.currentText() == "Не самокомплимент":
                MassX = np.linspace(int(min(self.Calib_Data[1][self.selected_row][0])),int(max(self.Calib_Data[1][self.selected_row][0])),200000).tolist()
                MassY = NoSelfComp(MassX, float(self.Table_calc.model().data(self.Table_calc.model().index(self.selected_row, 7))),
                                float(self.Table_calc.model().data(self.Table_calc.model().index(self.selected_row, 9))),
                                float(self.Table_calc.model().data(self.Table_calc.model().index(self.selected_row, 11))),
                                float(self.Table_calc.model().data(self.Table_calc.model().index(self.selected_row, 12))),
                                float(self.Table_calc.model().data(self.Table_calc.model().index(self.selected_row, 13))),
                                float(self.Table_calc.model().data(self.Table_calc.model().index(self.selected_row, 14))), self.Start_conf,
                                float(self.Table_calc.model().data(self.Table_calc.model().index(self.selected_row, 2))))
                self.PlotGraph = self.PLT.plot(MassX,MassY,  pen='r')
                Mass_X, Mass_Y = DNoSelfComp(self.Calib_Data[1][self.selected_row][0],
                                float(self.Table_calc.model().data(self.Table_calc.model().index(self.selected_row, 7))),
                                float(self.Table_calc.model().data(self.Table_calc.model().index(self.selected_row, 9))),
                                float(self.Table_calc.model().data(self.Table_calc.model().index(self.selected_row, 11))),
                                float(self.Table_calc.model().data(self.Table_calc.model().index(self.selected_row, 12))),
                                float(self.Table_calc.model().data(self.Table_calc.model().index(self.selected_row, 13))),
                                float(self.Table_calc.model().data(self.Table_calc.model().index(self.selected_row, 14))), self.Start_conf,
                                float(self.Table_calc.model().data(self.Table_calc.model().index(self.selected_row, 2))))
                self.DPlotGraph = self.DPLT.plot(Mass_X,Mass_Y,  pen='r')
            elif self.model.currentText() == "Самокомплимент":
                MassX = np.linspace(int(min(self.Calib_Data[1][self.selected_row][0])),int(max(self.Calib_Data[1][self.selected_row][0])),200000).tolist()
                MassY = SelfComp(MassX, float(self.Table_calc.model().data(self.Table_calc.model().index(self.selected_row, 7))),
                                float(self.Table_calc.model().data(self.Table_calc.model().index(self.selected_row, 9))),
                                float(self.Table_calc.model().data(self.Table_calc.model().index(self.selected_row, 11))),
                                float(self.Table_calc.model().data(self.Table_calc.model().index(self.selected_row, 12))),
                                float(self.Table_calc.model().data(self.Table_calc.model().index(self.selected_row, 13))),
                                float(self.Table_calc.model().data(self.Table_calc.model().index(self.selected_row, 14))), self.Start_conf,
                                float(self.Table_calc.model().data(self.Table_calc.model().index(self.selected_row, 2))))
                self.PlotGraph = self.PLT.plot(MassX,MassY,  pen='r')
                Mass_X, Mass_Y = DSelfComp(self.Calib_Data[1][self.selected_row][0],
                                float(self.Table_calc.model().data(self.Table_calc.model().index(self.selected_row, 7))),
                                float(self.Table_calc.model().data(self.Table_calc.model().index(self.selected_row, 9))),
                                float(self.Table_calc.model().data(self.Table_calc.model().index(self.selected_row, 11))),
                                float(self.Table_calc.model().data(self.Table_calc.model().index(self.selected_row, 12))),
                                float(self.Table_calc.model().data(self.Table_calc.model().index(self.selected_row, 13))),
                                float(self.Table_calc.model().data(self.Table_calc.model().index(self.selected_row, 14))), self.Start_conf,
                                float(self.Table_calc.model().data(self.Table_calc.model().index(self.selected_row, 2))))
                self.DPlotGraph = self.DPLT.plot(Mass_X,Mass_Y,  pen='r')
            elif self.model.currentText() == "Шпилька":
                MassX = np.linspace(int(min(self.Calib_Data[1][self.selected_row][0])),int(max(self.Calib_Data[1][self.selected_row][0])),200000).tolist()
                MassY = loop(MassX, float(self.Table_calc.model().data(self.Table_calc.model().index(self.selected_row, 7))),
                                float(self.Table_calc.model().data(self.Table_calc.model().index(self.selected_row, 9))),
                                float(self.Table_calc.model().data(self.Table_calc.model().index(self.selected_row, 11))),
                                float(self.Table_calc.model().data(self.Table_calc.model().index(self.selected_row, 12))),
                                float(self.Table_calc.model().data(self.Table_calc.model().index(self.selected_row, 13))),
                                float(self.Table_calc.model().data(self.Table_calc.model().index(self.selected_row, 14))), self.Start_conf,
                                float(self.Table_calc.model().data(self.Table_calc.model().index(self.selected_row, 2))))
                self.PlotGraph = self.PLT.plot(MassX,MassY,  pen='r')
                Mass_X, Mass_Y = Dloop(self.Calib_Data[1][self.selected_row][0],
                                float(self.Table_calc.model().data(self.Table_calc.model().index(self.selected_row, 7))),
                                float(self.Table_calc.model().data(self.Table_calc.model().index(self.selected_row, 9))),
                                float(self.Table_calc.model().data(self.Table_calc.model().index(self.selected_row, 11))),
                                float(self.Table_calc.model().data(self.Table_calc.model().index(self.selected_row, 12))),
                                float(self.Table_calc.model().data(self.Table_calc.model().index(self.selected_row, 13))),
                                float(self.Table_calc.model().data(self.Table_calc.model().index(self.selected_row, 14))), self.Start_conf,
                                float(self.Table_calc.model().data(self.Table_calc.model().index(self.selected_row, 2))))
                self.DPlotGraph = self.DPLT.plot(Mass_X,Mass_Y,  pen='r')
        except:
            print("Не смог отрисовать")
        
        self.PLT.setXRange(min(self.Calib_Data[1][self.selected_row][0]),max(self.Calib_Data[1][self.selected_row][0]))
        self.PLT.setYRange(min(self.Calib_Data[1][self.selected_row][1]),max(self.Calib_Data[1][self.selected_row][1]))

        self.DPLT.setXRange(min(self.Calib_Data[2][self.selected_row][0]),max(self.Calib_Data[2][self.selected_row][0]))
        self.DPLT.setYRange(min(self.Calib_Data[2][self.selected_row][1]),max(self.Calib_Data[2][self.selected_row][1]))

        self.min_line_to_PLT.setPos(self.Table_calc.model().data(self.Table_calc.model().index(self.selected_row, 3))) 
        self.max_line_to_PLT.setPos(self.Table_calc.model().data(self.Table_calc.model().index(self.selected_row, 4)))
        self.min_line_to_DPLT.setPos(self.Table_calc.model().data(self.Table_calc.model().index(self.selected_row, 3))) 
        self.max_line_to_DPLT.setPos(self.Table_calc.model().data(self.Table_calc.model().index(self.selected_row, 4)))

        self.Plot_window.setWindowTitle(self.Calib_Data[0][self.selected_row][1])
        
        self.Entalpy_edit.setText(str(round(float(self.Table_calc.model().data(self.Table_calc.model().index(self.selected_row, 7))),2)))
        self.Enthropy_edit.setText(str(round(float(self.Table_calc.model().data(self.Table_calc.model().index(self.selected_row, 9))),2)))
        self.Start_temp_edit.setText(self.Table_calc.model().data(self.Table_calc.model().index(self.selected_row, 3)))
        self.End_temp_edit.setText(self.Table_calc.model().data(self.Table_calc.model().index(self.selected_row, 4)))
        self.Bss_edit.setText(str(round(float(self.Table_calc.model().data(self.Table_calc.model().index(self.selected_row, 11))),5)))
        self.Css_edit.setText(str(round(float(self.Table_calc.model().data(self.Table_calc.model().index(self.selected_row, 12))),5)))
        self.Bds_edit.setText(str(round(float(self.Table_calc.model().data(self.Table_calc.model().index(self.selected_row, 13))),5)))
        self.Cds_edit.setText(str(round(float(self.Table_calc.model().data(self.Table_calc.model().index(self.selected_row, 14))),5)))
    
    def Infinity_line_usage(self,item):
        if item == "min_line_to_PLT": 
            try: self.Table_calc.setItem(self.selected_row,3,QtWidgets.QTableWidgetItem(str(round(float(self.min_line_to_PLT.getPos()[0]),1))))
            except:pass
            self.min_line_to_DPLT.setPos(self.min_line_to_PLT.getPos())
        elif item == "max_line_to_PLT":
            try: self.Table_calc.setItem(self.selected_row,4,QtWidgets.QTableWidgetItem(str(round(float(self.max_line_to_PLT.getPos()[0]),1))))
            except:pass
            self.max_line_to_DPLT.setPos(self.max_line_to_PLT.getPos())
        elif item == "min_line_to_DPLT":
            try:self.Table_calc.setItem(self.selected_row,3,QtWidgets.QTableWidgetItem(str(round(float(self.min_line_to_DPLT.getPos()[0]),1))))
            except:pass
            self.min_line_to_PLT.setPos(self.min_line_to_DPLT.getPos())
        elif item == "max_line_to_DPLT":
            try: self.Table_calc.setItem(self.selected_row,4,QtWidgets.QTableWidgetItem(str(round(float(self.max_line_to_DPLT.getPos()[0]),1))))
            except:pass
            self.max_line_to_PLT.setPos(self.max_line_to_DPLT.getPos())
        else:
            print("ERROR")
        self.Start_temp_edit.setText(self.Table_calc.model().data(self.Table_calc.model().index(self.selected_row, 3)))
        self.End_temp_edit.setText(self.Table_calc.model().data(self.Table_calc.model().index(self.selected_row, 4)))
        pass

    def Usage_baseline(self):

        prepare_mass = []
        
        for first in range(0,len(self.Calib_Data[0])):
            for second in range(0,len(self.Calib_Data[0])):
                if self.Calib_Data[0][first][0] == self.Calib_Data[0][second][0] and  self.Calib_Data[0][first][5] == self.Calib_Data[0][second][5] and self.Calib_Data[0][second][4]== self.Baseline_list.currentText() and first != second:
                    prepare_mass.append([first,second])

        if self.Baseline_check.isChecked():
            self.Baseline_list.setEnabled(False)
            self.Before_Copy = copy.deepcopy(self.Calib_Data)
            

            for i in prepare_mass:
                self.Calib_Data[1][i[0]][1] = [self.Calib_Data[1][i[0]][1][line] - self.Calib_Data[1][i[1]][1][line] for line in range(0,len(self.Calib_Data[1][i[0]][1]))]
            
            [self.Table_calc.hideRow(i) for i in set([j[1] for j in prepare_mass])] # Cкрыть строки базовой линии

            # Пересчитал производную после замены
            Mass = []
            for EXP in range(0,len(self.Calib_Data[1])):
                Mass_X = []
                Mass_Y = []
                for POINT in range(0,len(self.Calib_Data[1][EXP][0])-4):
                    Mass_Y.append(np.polyfit(self.Calib_Data[1][EXP][0][POINT:POINT+4],self.Calib_Data[1][EXP][1][POINT:POINT+4],deg=1).tolist()[0])
                    Mass_X.append(self.Calib_Data[1][EXP][0][POINT+2])
                Mass.append([Mass_X,Mass_Y])
                self.Calib_Data[2] = Mass
        else:
            if self.Baseline_list.currentText() in [self.Calib_Data[0][i][4] for i in range(0,len(self.Calib_Data[0]))]:
                self.Calib_Data = self.Before_Copy
            [self.Table_calc.showRow(i) for i in set([j[1] for j in prepare_mass])] # Показать строки базовой линии
            self.Baseline_list.setEnabled(True)
    
    def Usage_parametrs():
        pass

    def Approximation(self):
        Start_parametrs = []
        for i in [self.Entalpy_edit.text(),
                  self.Enthropy_edit.text(),
                  self.Bss_edit.text(),
                  self.Css_edit.text(),
                  self.Bds_edit.text(),
                  self.Cds_edit.text()]:
            try: 
                i = float(i)
                Start_parametrs.append(i)
            except:
                Start_parametrs.append(1)
        
        self.Start_conf = [self.Entalpy.isChecked(),
                      self.Enthropy.isChecked(),
                      self.Bss.isChecked(),
                      self.Css.isChecked(),
                      self.Bds.isChecked(),
                      self.Cds.isChecked()]
        self.Start_conf = [not i for i in self.Start_conf]
        
        self.Start_conf.append(self.Water.isChecked())
        
        def NoSelfComp(x,dH,dS,Bss,Css,Bds,Cds,WATER,C0):
            #Учет воды
            if WATER == 0:
                Ct = float(C0)*1.00303/(1+(-1)*0.0000000000013*(x-4)**5+0.00000000042*(x-4)**4-0.000000065*(x-4)**3+0.0000083*(x-4)**2-0.000005*(x-4))
            else:
                Ct = float(C0)
            
            K = np.exp(-(dH-(x+273.15)*dS)/(1.9872*(x+273.15)))
            alpha= (1+Ct*K-np.sqrt(1+2*Ct*K))/(Ct*K)
            return (Bss+Css*x)*(1-alpha)+(Bds+Cds*x)*alpha
            
        def SelfComp(x,dH,dS,Bss,Css,Bds,Cds,WATER,C0):
            if WATER == 0:
                Ct = float(C0)*1.00303/(1+(-1)*0.0000000000013*(x-4)**5+0.00000000042*(x-4)**4-0.000000065*(x-4)**3+0.0000083*(x-4)**2-0.000005*(x-4))
            else:
                Ct = float(C0)
            K = np.exp(-(dH-(x+273.15)*dS)/(1.9872*(x+273.15)))
            alpha = 1+1/(2*K*Ct)-np.sqrt(4*K*Ct+1)/(2*K*Ct)
            return (Bss+Css*x)*(1-alpha)+(Bds+Cds*x)*alpha  

        def loop(x,dH,dS,Bss,Css,Bds,Cds,WATER,C0):
            if WATER == 0:
                Ct = float(C0)*1.00303/(1+(-1)*0.0000000000013*(x-4)**5+0.00000000042*(x-4)**4-0.000000065*(x-4)**3+0.0000083*(x-4)**2-0.000005*(x-4))
            else:
                Ct = float(C0)
            K = np.exp(-(dH-(x+273.15)*dS)/(1.9872*(x+273.15)))
            alpha = K/(1+K)
            return (Bss+Css*x)*(1-alpha)+(Bds+Cds*x)*alpha

        for EXP in set([i.row() for i in self.Table_calc.selectionModel().selectedIndexes()]):
            Start_TEMP_INDEX = [abs(float(i) - float(self.Table_calc.model().data(self.Table_calc.model().index(EXP, 3)))) for i in self.Calib_Data[1][EXP][0]].index(min([abs(float(i) - float(self.Table_calc.model().data(self.Table_calc.model().index(EXP, 3)))) for i in self.Calib_Data[1][EXP][0]]))
            END_TEMP_INDEX = [abs(float(i) - float(self.Table_calc.model().data(self.Table_calc.model().index(EXP, 4)))) for i in self.Calib_Data[1][EXP][0]].index(min([abs(float(i) - float(self.Table_calc.model().data(self.Table_calc.model().index(EXP, 4)))) for i in self.Calib_Data[1][EXP][0]]))
            if Start_TEMP_INDEX > END_TEMP_INDEX:
                Start_TEMP_INDEX, END_TEMP_INDEX = END_TEMP_INDEX,Start_TEMP_INDEX
           
            if self.model.currentText() == "Не самокомплимент":
                #["Sample", "Name","Conc","sT","eT","light","Ramp","dH","ErrordH","dS","ErrordS","dU1","dU2","dG","Tm","СКО"])
                model = Model(NoSelfComp)
            elif self.model.currentText() == "Самокомплимент":
                model = Model(SelfComp)
                print("Самокомплимент")
            elif self.model.currentText() == "Шпилька":
                model = Model(loop)
                print("Шпилька")

            params = model.make_params()
            params['dH'].set(Start_parametrs[0], vary=self.Start_conf[0], max=0)
            params['dS'].set(Start_parametrs[1], vary=self.Start_conf[1],max=0)
            params['Bss'].set(Start_parametrs[2], vary=self.Start_conf[2])
            params['Css'].set(Start_parametrs[3], vary=self.Start_conf[3])
            params['Bds'].set(Start_parametrs[4], vary=self.Start_conf[4])
            params['Cds'].set(Start_parametrs[5], vary=self.Start_conf[5])
            if self.Start_conf[6]:
                params['WATER'].set(0 , vary=False)
            else:
                params['WATER'].set(1 , vary=False)
            params['C0'].set(float(self.Table_calc.model().data(self.Table_calc.model().index(EXP, 2))), vary=False)

            result = model.fit(self.Calib_Data[1][EXP][1][Start_TEMP_INDEX:END_TEMP_INDEX],params,
                                x = self.Calib_Data[1][EXP][0][Start_TEMP_INDEX:END_TEMP_INDEX])                                            
            if bool(self.Start_conf[0]) == True: 
                self.Table_calc.setItem(EXP,7, QtWidgets.QTableWidgetItem(str(result.params['dH'].value)))
                self.Table_calc.setItem(EXP,8, QtWidgets.QTableWidgetItem(str(result.params['dH'].stderr)))
            else: 
                self.Table_calc.setItem(EXP,7, QtWidgets.QTableWidgetItem(str(Start_parametrs[0])))
                self.Table_calc.setItem(EXP,8, QtWidgets.QTableWidgetItem(""))
            if bool(self.Start_conf[1]) == True: 
                self.Table_calc.setItem(EXP,9, QtWidgets.QTableWidgetItem(str(result.params['dS'].value)))
                self.Table_calc.setItem(EXP,10, QtWidgets.QTableWidgetItem(str(result.params['dS'].stderr)))
            else: 
                self.Table_calc.setItem(EXP,9, QtWidgets.QTableWidgetItem(str(Start_parametrs[1])))
                self.Table_calc.setItem(EXP,10, QtWidgets.QTableWidgetItem(""))
            if  bool(self.Start_conf[2]) == True: self.Table_calc.setItem(EXP,11, QtWidgets.QTableWidgetItem(str(result.params['Bss'].value)))
            else: self.Table_calc.setItem(EXP,11, QtWidgets.QTableWidgetItem(str(Start_parametrs[2])))
            if  bool(self.Start_conf[3]) == True: self.Table_calc.setItem(EXP,12, QtWidgets.QTableWidgetItem(str(result.params['Css'].value)))
            else: self.Table_calc.setItem(EXP,12, QtWidgets.QTableWidgetItem(str(Start_parametrs[3])))
            if  bool(self.Start_conf[4]) == True: self.Table_calc.setItem(EXP,13, QtWidgets.QTableWidgetItem(str(result.params['Bds'].value)))
            else: self.Table_calc.setItem(EXP,13, QtWidgets.QTableWidgetItem(str(Start_parametrs[4])))
            if  bool(self.Start_conf[5]) == True: self.Table_calc.setItem(EXP,14, QtWidgets.QTableWidgetItem(str(result.params['Cds'].value)))
            else: self.Table_calc.setItem(EXP,14, QtWidgets.QTableWidgetItem(str(Start_parametrs[5])))
            dG = result.params['dH'] - (self.dG_temp.value()+273.15)*result.params['dS']
            self.Table_calc.setItem(EXP,15, QtWidgets.QTableWidgetItem(str(dG)))
            self.Table_calc.setItem(EXP,17, QtWidgets.QTableWidgetItem(str(result.chisqr)))
            
            if self.model.currentText() == "Несамокомплемент":
                Tm = result.params['dH'].value/(result.params['dS'].value+1.9872*math.log(float(self.Table_calc.model().data(self.Table_calc.model().index(EXP, 2)))/4))
            elif self.model.currentText() == "Самокомплемент":
                Tm = result.params['dH'].value/(result.params['dS'].value+1.9872*math.log(float(self.Table_calc.model().data(self.Table_calc.model().index(EXP, 2)))/2))
            elif self.model.currentText() == "Шпилька":
                Tm = result.params['dH'].value/result.params['dS'].value
            self.Table_calc.setItem(EXP,16, QtWidgets.QTableWidgetItem(str(Tm-273.15)))
            print("Температура плавления: " +str(Tm-273.15))
        Ui_MainWindow.review_data(self)

    def Save_Table(self):
        file , check = QFileDialog.getSaveFileName(None, "QFileDialog.getOpenFileName()","", "All Files (*);;Python Files (*.py);;Text Files (*.txt)")
        file=open(file,"a")
        file.write("Sample;Name;Conc;sT;eT;light;Ramp;dH;ErrordH;dS;ErrordS;Bss;Css;Bds;Cds;dG;Tm;СКО\n")
        for row in range(0,self.Table_calc.rowCount()):
            row_data = []
            for col in range(0,self.Table_calc.columnCount()):
                try:
                    row_data.append(self.Table_calc.model().data(self.Table_calc.model().index(row,col)))
                except:
                    row_data.append('')
            row_data = ";".join(row_data).replace(".",",")
            file.write(str(row_data)+"\n")

    def Save_Data(self):
        file , check = QFileDialog.getSaveFileName(None, "QFileDialog.getOpenFileName()","", "All Files (*);;Python Files (*.py);;Text Files (*.txt)")
        file=open(file,"a")
        line = []
        for EXP in self.Calib_Data[0]:
            EXP = [str(i) for i in EXP]
            line.append("_".join(EXP))
        line = ";;".join(line)
        file.write(str(line)+"\n")
        for stroka in range(0,len(self.Calib_Data[1][0][0])):
            stroka_pobolshe = []
            for EXP in self.Calib_Data[1]:
                try:
                    stroka_pobolshe.append(str(EXP[0][stroka])+";"+str(EXP[1][stroka]).replace('.',','))
                except:
                    stroka_pobolshe.append(";")
            stroka_pobolshe = ";".join(stroka_pobolshe)
            file.write(str(stroka_pobolshe)+"\n")

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.add()
    ui.Run_Plot()
    MainWindow.show()
    sys.exit(app.exec())
