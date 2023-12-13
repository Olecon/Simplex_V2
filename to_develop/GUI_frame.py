# Form implementation generated from reading ui file 'frame.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(811, 559)
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
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 480))
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetNoConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
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
        self.change_file.setGeometry(QtCore.QRect(0, 270, 161, 71))
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
        self.Baseline_list = QtWidgets.QComboBox(parent=self.Methods)
        self.Baseline_list.setEnabled(False)
        self.Baseline_list.setGeometry(QtCore.QRect(0, 230, 151, 21))
        self.Baseline_list.setObjectName("Baseline_list")
        self.Baseline_check = QtWidgets.QCheckBox(parent=self.Methods)
        self.Baseline_check.setEnabled(False)
        self.Baseline_check.setGeometry(QtCore.QRect(0, 210, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Baseline_check.setFont(font)
        self.Baseline_check.setObjectName("Baseline_check")
        self.Calibration = QtWidgets.QPushButton(parent=self.Methods)
        self.Calibration.setEnabled(False)
        self.Calibration.setGeometry(QtCore.QRect(0, 350, 161, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Calibration.setFont(font)
        self.Calibration.setObjectName("Calibration")
        self.tabWidget.addTab(self.Methods, "")
        self.Parametrs = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Parametrs.setFont(font)
        self.Parametrs.setObjectName("Parametrs")
        self.Calculation = QtWidgets.QPushButton(parent=self.Parametrs)
        self.Calculation.setGeometry(QtCore.QRect(0, 410, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Calculation.setFont(font)
        self.Calculation.setObjectName("Calculation")
        self.frame = QtWidgets.QFrame(parent=self.Parametrs)
        self.frame.setGeometry(QtCore.QRect(0, 0, 161, 331))
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
        self.Enthropy_edit = QtWidgets.QLineEdit(parent=self.frame)
        self.Enthropy_edit.setGeometry(QtCore.QRect(0, 70, 161, 21))
        self.Enthropy_edit.setText("")
        self.Enthropy_edit.setObjectName("Enthropy_edit")
        self.Enthropy = QtWidgets.QCheckBox(parent=self.frame)
        self.Enthropy.setGeometry(QtCore.QRect(0, 50, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Enthropy.setFont(font)
        self.Enthropy.setObjectName("Enthropy")
        self.Bss_edit = QtWidgets.QLineEdit(parent=self.frame)
        self.Bss_edit.setGeometry(QtCore.QRect(0, 119, 161, 21))
        self.Bss_edit.setText("")
        self.Bss_edit.setObjectName("Bss_edit")
        self.Css_edit = QtWidgets.QLineEdit(parent=self.frame)
        self.Css_edit.setGeometry(QtCore.QRect(0, 170, 161, 21))
        self.Css_edit.setText("")
        self.Css_edit.setObjectName("Css_edit")
        self.Bss = QtWidgets.QCheckBox(parent=self.frame)
        self.Bss.setGeometry(QtCore.QRect(0, 100, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Bss.setFont(font)
        self.Bss.setObjectName("Bss")
        self.Css = QtWidgets.QCheckBox(parent=self.frame)
        self.Css.setGeometry(QtCore.QRect(0, 150, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Css.setFont(font)
        self.Css.setObjectName("Css")
        self.point_to_derivative = QtWidgets.QSpinBox(parent=self.frame)
        self.point_to_derivative.setEnabled(True)
        self.point_to_derivative.setGeometry(QtCore.QRect(0, 310, 161, 22))
        self.point_to_derivative.setWrapping(True)
        self.point_to_derivative.setFrame(True)
        self.point_to_derivative.setReadOnly(False)
        self.point_to_derivative.setProperty("showGroupSeparator", True)
        self.point_to_derivative.setMinimum(2)
        self.point_to_derivative.setMaximum(10)
        self.point_to_derivative.setObjectName("point_to_derivative")
        self.Bds = QtWidgets.QCheckBox(parent=self.frame)
        self.Bds.setGeometry(QtCore.QRect(0, 200, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Bds.setFont(font)
        self.Bds.setObjectName("Bds")
        self.Cds_edit = QtWidgets.QLineEdit(parent=self.frame)
        self.Cds_edit.setGeometry(QtCore.QRect(0, 270, 161, 21))
        self.Cds_edit.setText("")
        self.Cds_edit.setObjectName("Cds_edit")
        self.Cds = QtWidgets.QCheckBox(parent=self.frame)
        self.Cds.setGeometry(QtCore.QRect(0, 250, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Cds.setFont(font)
        self.Cds.setObjectName("Cds")
        self.Bds_edit = QtWidgets.QLineEdit(parent=self.frame)
        self.Bds_edit.setGeometry(QtCore.QRect(0, 220, 161, 21))
        self.Bds_edit.setText("")
        self.Bds_edit.setObjectName("Bds_edit")
        self.label_5 = QtWidgets.QLabel(parent=self.frame)
        self.label_5.setGeometry(QtCore.QRect(0, 290, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.Calculation_2 = QtWidgets.QPushButton(parent=self.Parametrs)
        self.Calculation_2.setGeometry(QtCore.QRect(0, 350, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Calculation_2.setFont(font)
        self.Calculation_2.setObjectName("Calculation_2")
        self.tabWidget.addTab(self.Parametrs, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Table_calc = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.Table_calc.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.Table_calc.setDragDropOverwriteMode(False)
        self.Table_calc.setShowGrid(True)
        self.Table_calc.setObjectName("Table_calc")
        self.Table_calc.setColumnCount(0)
        self.Table_calc.setRowCount(0)
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
        self.menubar.setGeometry(QtCore.QRect(0, 0, 811, 18))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(parent=self.menubar)
        self.menu.setObjectName("menu")
        self.menu_5 = QtWidgets.QMenu(parent=self.menu)
        self.menu_5.setObjectName("menu_5")
        self.menu_2 = QtWidgets.QMenu(parent=self.menu_5)
        self.menu_2.setEnabled(False)
        self.menu_2.setObjectName("menu_2")
        self.menu_6 = QtWidgets.QMenu(parent=self.menu_5)
        self.menu_6.setEnabled(False)
        self.menu_6.setObjectName("menu_6")
        self.menu_3 = QtWidgets.QMenu(parent=self.menubar)
        self.menu_3.setObjectName("menu_3")
        self.menu_4 = QtWidgets.QMenu(parent=self.menubar)
        self.menu_4.setEnabled(True)
        self.menu_4.setObjectName("menu_4")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.exit = QtGui.QAction(parent=MainWindow)
        self.exit.setObjectName("exit")
        self.actionCary_3500 = QtGui.QAction(parent=MainWindow)
        self.actionCary_3500.setObjectName("actionCary_3500")
        self.action_4 = QtGui.QAction(parent=MainWindow)
        self.action_4.setEnabled(False)
        self.action_4.setObjectName("action_4")
        self.save_parametrs = QtGui.QAction(parent=MainWindow)
        self.save_parametrs.setObjectName("save_parametrs")
        self.actionSample = QtGui.QAction(parent=MainWindow)
        self.actionSample.setObjectName("actionSample")
        self.action123 = QtGui.QAction(parent=MainWindow)
        self.action123.setObjectName("action123")
        self.Config_Sample = QtGui.QAction(parent=MainWindow)
        self.Config_Sample.setCheckable(True)
        self.Config_Sample.setChecked(False)
        self.Config_Sample.setObjectName("Config_Sample")
        self.Config_Name = QtGui.QAction(parent=MainWindow)
        self.Config_Name.setCheckable(True)
        self.Config_Name.setObjectName("Config_Name")
        self.Config_Concentration = QtGui.QAction(parent=MainWindow)
        self.Config_Concentration.setCheckable(True)
        self.Config_Concentration.setObjectName("Config_Concentration")
        self.Config_Start_temperature = QtGui.QAction(parent=MainWindow)
        self.Config_Start_temperature.setCheckable(True)
        self.Config_Start_temperature.setObjectName("Config_Start_temperature")
        self.Config_End_temperature = QtGui.QAction(parent=MainWindow)
        self.Config_End_temperature.setCheckable(True)
        self.Config_End_temperature.setObjectName("Config_End_temperature")
        self.Config_Light = QtGui.QAction(parent=MainWindow)
        self.Config_Light.setCheckable(True)
        self.Config_Light.setObjectName("Config_Light")
        self.Config_Ramp = QtGui.QAction(parent=MainWindow)
        self.Config_Ramp.setCheckable(True)
        self.Config_Ramp.setObjectName("Config_Ramp")
        self.Config_dH = QtGui.QAction(parent=MainWindow)
        self.Config_dH.setCheckable(True)
        self.Config_dH.setObjectName("Config_dH")
        self.Config_Error_dH = QtGui.QAction(parent=MainWindow)
        self.Config_Error_dH.setCheckable(True)
        self.Config_Error_dH.setObjectName("Config_Error_dH")
        self.Config_dS = QtGui.QAction(parent=MainWindow)
        self.Config_dS.setCheckable(True)
        self.Config_dS.setObjectName("Config_dS")
        self.Config_Error_dS = QtGui.QAction(parent=MainWindow)
        self.Config_Error_dS.setCheckable(True)
        self.Config_Error_dS.setObjectName("Config_Error_dS")
        self.Config_Bss = QtGui.QAction(parent=MainWindow)
        self.Config_Bss.setCheckable(True)
        self.Config_Bss.setObjectName("Config_Bss")
        self.Config_Css = QtGui.QAction(parent=MainWindow)
        self.Config_Css.setCheckable(True)
        self.Config_Css.setObjectName("Config_Css")
        self.Config_Bds = QtGui.QAction(parent=MainWindow)
        self.Config_Bds.setCheckable(True)
        self.Config_Bds.setObjectName("Config_Bds")
        self.Config_Cds = QtGui.QAction(parent=MainWindow)
        self.Config_Cds.setCheckable(True)
        self.Config_Cds.setObjectName("Config_Cds")
        self.Config_dG = QtGui.QAction(parent=MainWindow)
        self.Config_dG.setCheckable(True)
        self.Config_dG.setObjectName("Config_dG")
        self.Config_Tm = QtGui.QAction(parent=MainWindow)
        self.Config_Tm.setCheckable(True)
        self.Config_Tm.setObjectName("Config_Tm")
        self.Config_CKO = QtGui.QAction(parent=MainWindow)
        self.Config_CKO.setCheckable(True)
        self.Config_CKO.setObjectName("Config_CKO")
        self.Graph = QtGui.QAction(parent=MainWindow)
        self.Graph.setObjectName("Graph")
        self.actionSimplexV1 = QtGui.QAction(parent=MainWindow)
        self.actionSimplexV1.setObjectName("actionSimplexV1")
        self.actionSimplexV2 = QtGui.QAction(parent=MainWindow)
        self.actionSimplexV2.setObjectName("actionSimplexV2")
        self.actionSimplexV1_2 = QtGui.QAction(parent=MainWindow)
        self.actionSimplexV1_2.setObjectName("actionSimplexV1_2")
        self.actionSimplexV2_2 = QtGui.QAction(parent=MainWindow)
        self.actionSimplexV2_2.setObjectName("actionSimplexV2_2")
        self.actionSimplexV1_3 = QtGui.QAction(parent=MainWindow)
        self.actionSimplexV1_3.setObjectName("actionSimplexV1_3")
        self.actionSimplexV2_3 = QtGui.QAction(parent=MainWindow)
        self.actionSimplexV2_3.setObjectName("actionSimplexV2_3")
        self.review_table_button = QtGui.QAction(parent=MainWindow)
        self.review_table_button.setEnabled(False)
        self.review_table_button.setObjectName("review_table_button")
        self.Tab_in_buff = QtGui.QAction(parent=MainWindow)
        self.Tab_in_buff.setEnabled(False)
        self.Tab_in_buff.setObjectName("Tab_in_buff")
        self.menu_2.addAction(self.actionSimplexV2)
        self.menu_6.addAction(self.actionSimplexV1_2)
        self.menu_6.addAction(self.actionSimplexV2_2)
        self.menu_5.addAction(self.action_4)
        self.menu_5.addAction(self.menu_2.menuAction())
        self.menu_5.addAction(self.menu_6.menuAction())
        self.menu.addAction(self.menu_5.menuAction())
        self.menu.addAction(self.save_parametrs)
        self.menu.addAction(self.exit)
        self.menu_3.addAction(self.Graph)
        self.menu_4.addAction(self.Config_Sample)
        self.menu_4.addAction(self.Config_Name)
        self.menu_4.addAction(self.Config_Concentration)
        self.menu_4.addAction(self.Config_Start_temperature)
        self.menu_4.addAction(self.Config_End_temperature)
        self.menu_4.addAction(self.Config_Light)
        self.menu_4.addAction(self.Config_Ramp)
        self.menu_4.addAction(self.Config_dH)
        self.menu_4.addAction(self.Config_Error_dH)
        self.menu_4.addAction(self.Config_dS)
        self.menu_4.addAction(self.Config_Error_dS)
        self.menu_4.addAction(self.Config_Bss)
        self.menu_4.addAction(self.Config_Css)
        self.menu_4.addAction(self.Config_Bds)
        self.menu_4.addAction(self.Config_Cds)
        self.menu_4.addAction(self.Config_dG)
        self.menu_4.addAction(self.Config_Tm)
        self.menu_4.addAction(self.Config_CKO)
        self.menu_4.addAction(self.review_table_button)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Прибор"))
        self.label_2.setText(_translate("MainWindow", "Метод"))
        self.label_3.setText(_translate("MainWindow", "Модель"))
        self.change_file.setText(_translate("MainWindow", "Выбрать файл"))
        self.Water.setText(_translate("MainWindow", "Расширение воды"))
        self.label_4.setText(_translate("MainWindow", "Температура dG"))
        self.Baseline_check.setText(_translate("MainWindow", "Базовая линия"))
        self.Calibration.setText(_translate("MainWindow", "Калибровка"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Methods), _translate("MainWindow", "Метод"))
        self.Calculation.setText(_translate("MainWindow", "Точно"))
        self.Entalpy.setText(_translate("MainWindow", "Энтальпия (dH)"))
        self.Enthropy.setText(_translate("MainWindow", "Энтропия (dS)"))
        self.Bss.setText(_translate("MainWindow", "Bss"))
        self.Css.setText(_translate("MainWindow", "Css"))
        self.Bds.setText(_translate("MainWindow", "Bds"))
        self.Cds.setText(_translate("MainWindow", "Cds"))
        self.label_5.setText(_translate("MainWindow", "Производная"))
        self.Calculation_2.setText(_translate("MainWindow", "Примерно"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Parametrs), _translate("MainWindow", "Аппроксимация"))
        self.Run_Command.setText(_translate("MainWindow", "Выполнить"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))
        self.menu_5.setTitle(_translate("MainWindow", "Сохранить как"))
        self.menu_2.setTitle(_translate("MainWindow", "Данные без калибровки"))
        self.menu_6.setTitle(_translate("MainWindow", "Данные с калибровкой"))
        self.menu_3.setTitle(_translate("MainWindow", "Выполнить"))
        self.menu_4.setTitle(_translate("MainWindow", "Конфигурация"))
        self.exit.setText(_translate("MainWindow", "Выход"))
        self.actionCary_3500.setText(_translate("MainWindow", "Cary_3500"))
        self.action_4.setText(_translate("MainWindow", "Таблицу в файл"))
        self.save_parametrs.setText(_translate("MainWindow", "Сохранить конфигурацию"))
        self.actionSample.setText(_translate("MainWindow", "Sample"))
        self.action123.setText(_translate("MainWindow", "123"))
        self.Config_Sample.setText(_translate("MainWindow", "Sample"))
        self.Config_Name.setText(_translate("MainWindow", "Name"))
        self.Config_Concentration.setText(_translate("MainWindow", "Concentration"))
        self.Config_Start_temperature.setText(_translate("MainWindow", "Start temperature"))
        self.Config_End_temperature.setText(_translate("MainWindow", "End temperature"))
        self.Config_Light.setText(_translate("MainWindow", "Light"))
        self.Config_Ramp.setText(_translate("MainWindow", "Ramp"))
        self.Config_dH.setText(_translate("MainWindow", "dH"))
        self.Config_Error_dH.setText(_translate("MainWindow", "Error dH"))
        self.Config_dS.setText(_translate("MainWindow", "dS"))
        self.Config_Error_dS.setText(_translate("MainWindow", "Error dS"))
        self.Config_Bss.setText(_translate("MainWindow", "Bss"))
        self.Config_Css.setText(_translate("MainWindow", "Css"))
        self.Config_Bds.setText(_translate("MainWindow", "Bds"))
        self.Config_Cds.setText(_translate("MainWindow", "Cds"))
        self.Config_dG.setText(_translate("MainWindow", "dG"))
        self.Config_Tm.setText(_translate("MainWindow", "Tm"))
        self.Config_CKO.setText(_translate("MainWindow", "CKO"))
        self.Graph.setText(_translate("MainWindow", "График"))
        self.actionSimplexV1.setText(_translate("MainWindow", "SimplexV1"))
        self.actionSimplexV2.setText(_translate("MainWindow", "SimplexV2"))
        self.actionSimplexV1_2.setText(_translate("MainWindow", "SimplexV1"))
        self.actionSimplexV2_2.setText(_translate("MainWindow", "SimplexV2"))
        self.actionSimplexV1_3.setText(_translate("MainWindow", "SimplexV1"))
        self.actionSimplexV2_3.setText(_translate("MainWindow", "SimplexV2"))
        self.review_table_button.setText(_translate("MainWindow", "Перерисовать таблицу"))
        self.Tab_in_buff.setText(_translate("MainWindow", "Таблицу в буфер"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
