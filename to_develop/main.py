import GUI_frame
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QFileDialog, QWidget, QVBoxLayout
import pyqtgraph as pg 
import configparser,codecs
import sys
import os
import read_file, calibration, copy
import pandas as pd
import numpy as np
from lmfit import Model
import math
import pyperclip
import keyboard
import time 

class Window(QtWidgets.QMainWindow,GUI_frame.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Source_data = []
        self.Calib_Data = []
        self.Table_data = []
        self.Start_conf = []
        self.selected_row = 0

        Function.read_configure(self)
        Function.Plot_graph(self)

        self.save_parametrs.triggered.connect(lambda: Function.write_configure(self))
        self.pribor.activated.connect(lambda: Function.update_pribor_combobox(self))
        self.change_file.clicked.connect(lambda: Function.change_file(self))
        self.Calibration.clicked.connect(lambda: Function.use_calib(self))
        self.Graph.triggered.connect(lambda:Function.Plot_graph(self))
        self.Table_calc.clicked.connect(lambda: Function.review_data(self,True))
        self.Baseline_check.stateChanged.connect(lambda: Function.Usage_baseline(self))
        self.Calculation.clicked.connect(lambda: Function.Approximation(self))

        self.actionSimplexV2.triggered.connect(lambda: Function.Save_data(self,"SV2",'without_calib'))
        self.actionSimplexV1_2.triggered.connect(lambda: Function.Save_data(self,"SV1",'with_calib'))
        self.actionSimplexV2_2.triggered.connect(lambda: Function.Save_data(self,"SV2",'with_calib'))
        self.review_table_button.triggered.connect(lambda: Function.reviev_Table(self))
        self.Calculation_2.clicked.connect(lambda: Function.Bad_Approximation(self))
        self.action_4.triggered.connect(lambda: Function.Save_Table(self))

        self.Entalpy_edit.returnPressed.connect(lambda: Function.Data_add(self,'dH',self.Entalpy_edit.text()))
        self.Enthropy_edit.returnPressed.connect(lambda: Function.Data_add(self,'dS',self.Enthropy_edit.text()))

        self.Bds_edit.returnPressed.connect(lambda: Function.Data_add(self,'Bds',self.Bds_edit.text()))
        self.Cds_edit.returnPressed.connect(lambda: Function.Data_add(self,'Cds',self.Cds_edit.text()))
        self.Bss_edit.returnPressed.connect(lambda: Function.Data_add(self,'Bss',self.Bss_edit.text()))
        self.Css_edit.returnPressed.connect(lambda: Function.Data_add(self,'Css',self.Css_edit.text()))

        self.point_to_derivative.valueChanged.connect(lambda: Function.Recalc_dA(self, self.point_to_derivative.value()))
        self.Run_Command.clicked.connect(lambda: Function.Write(self))
        keyboard.add_hotkey('ctrl+C', lambda: Function.HotKeyCopyTable(self))
        keyboard.add_hotkey('ctrl+shift+C', lambda: Function.HotKeyCopyData(self))


class Function(Window):
    
    def read_configure(self):
        config = configparser.ConfigParser()
        config.readfp(codecs.open("config.ini", "r", "utf8"))
        self.model.addItems(config['Standard']['Model_list'].split(','))
        self.pribor.addItems(config['Standard']['Pribor_list'].split(','))
        self.dG_temp.setValue(int(config['Standard']['Gibbs_Temp']))
        self.Water.setChecked(eval(config['Standard']['water']))
        
        self.Config_Sample.setChecked(eval(config['Display']['Sample']))
        self.Config_Name.setChecked(eval(config['Display']['Name']))
        self.Config_Concentration.setChecked(eval(config['Display']['Concentration']))
        self.Config_Start_temperature.setChecked(eval(config['Display']['Start_temperature']))
        self.Config_End_temperature.setChecked(eval(config['Display']['End_temperature']))
        self.Config_Light.setChecked(eval(config['Display']['Light']))
        self.Config_Ramp.setChecked(eval(config['Display']['Ramp']))
        self.Config_dH.setChecked(eval(config['Display']['dH']))
        self.Config_Error_dH.setChecked(eval(config['Display']['Error_dH']))
        self.Config_dS.setChecked(eval(config['Display']['dS']))
        self.Config_Error_dS.setChecked(eval(config['Display']['Error_dS']))
        self.Config_Bss.setChecked(eval(config['Display']['Bss']))
        self.Config_Css.setChecked(eval(config['Display']['Css']))
        self.Config_Bds.setChecked(eval(config['Display']['Bds']))
        self.Config_Cds.setChecked(eval(config['Display']['Cds']))
        self.Config_dG.setChecked(eval(config['Display']['dG']))
        self.Config_Tm.setChecked(eval(config['Display']['Tm']))
        self.Config_CKO.setChecked(eval(config['Display']['CKO']))

    def write_configure(self):
        config = configparser.ConfigParser()
        config.readfp(codecs.open("config.ini", "r", "utf8"))
        config['Standard']['Gibbs_Temp'] = str(self.dG_temp.value())
        config['Standard']['Water'] = str(self.Water.isChecked())
        config['Display']['Sample'] = str(self.Config_Sample.isChecked())
        config['Display']['Name'] = str(self.Config_Name.isChecked())
        config['Display']['Concentration'] = str(self.Config_Concentration.isChecked())
        config['Display']['Start_temperature'] = str(self.Config_Start_temperature.isChecked())
        config['Display']['End_temperature'] = str(self.Config_End_temperature.isChecked())
        config['Display']['Light'] = str(self.Config_Light.isChecked())
        config['Display']['Ramp'] = str(self.Config_Ramp.isChecked())
        config['Display']['dH'] = str(self.Config_dH.isChecked())
        config['Display']['Error_dH'] = str(self.Config_Error_dH.isChecked())
        config['Display']['dS'] = str(self.Config_dS.isChecked())
        config['Display']['Error_dS'] = str(self.Config_Error_dS.isChecked())
        config['Display']['Bss'] = str(self.Config_Bss.isChecked())
        config['Display']['Css'] = str(self.Config_Css.isChecked())
        config['Display']['Bds'] = str(self.Config_Bds.isChecked())
        config['Display']['Css'] = str(self.Config_Cds.isChecked())
        config['Display']['dG'] = str(self.Config_dG.isChecked())
        config['Display']['Tm'] = str(self.Config_Tm.isChecked())
        config['Display']['CKO'] = str(self.Config_CKO.isChecked())

        with codecs.open("config.ini", "w", "utf-8") as configfile:
            config.write(configfile)

    def update_pribor_combobox(self):
        self.method.clear()
        try:
            folders = [i for i in os.listdir(self.pribor.currentText()) if '.' not in i and i != '__pycache__']
            self.method.addItems(folders)
        except:
            pass
        
    def change_file(self):
        try:
            file = QFileDialog.getOpenFileName()[0]
            if len(file) == 0:
                return
            exec("result = read_file."+str(self.pribor.currentText())+"(file)",globals(),locals())
        except:
            print("Не смог распарсить файл")
            return
        
        self.Source_data = locals()['result']
        self.File_open = copy.deepcopy(file)
        self.menu_2.setDisabled(True)
        self.menu_6.setDisabled(True)
        self.Baseline_list.setDisabled(True)
        self.Baseline_check.setDisabled(True)
        self.Baseline_check.setChecked(False)
        self.Baseline_list.clear()
        self.Calibration.setDisabled(True)
        self.Table_calc.setRowCount(0)
        self.action_4.setDisabled(True)

        try:
            if self.pribor.currentText() == 'SimplexV1' or self.pribor.currentText() == 'SimplexV2' :
                self.Calib_Data = copy.deepcopy(self.Source_data)
                Mass = []
                for EXP in range(0,len(self.Source_data[1])):
                    Mass_X = []
                    Mass_Y = []
                    for POINT in range(0,len(self.Source_data[1][EXP][0])-4):
                        Mass_Y.append(np.polyfit(self.Source_data[1][EXP][0][POINT:POINT+4],self.Source_data[1][EXP][1][POINT:POINT+4],deg=1).tolist()[0])
                        Mass_X.append(self.Source_data[1][EXP][0][POINT+2])
                    Mass.append([Mass_X,Mass_Y])
                
                self.Calib_Data.append(Mass)
                self.Baseline_list.clear()
                self.Baseline_list.addItems(set([i[4] for i in self.Calib_Data[0]]))
                self.Baseline_list.setDisabled(False)
                self.Baseline_check.setDisabled(False)
                self.menu_6.setDisabled(False)
                Function.Create_Table_Data(self)
            else:
                self.menu_2.setDisabled(False)
                self.Calibration.setDisabled(False)
        except:
            pass

    def use_calib(self):
        self.Calib_Data = calibration.Use_calib(self.Source_data, self.pribor.currentText(), self.method.currentText())
        self.Calibration.setDisabled(True)
        self.Baseline_list.clear()
        self.Baseline_list.addItems(set([i[4] for i in self.Source_data[0]]))
        self.Baseline_list.setDisabled(False)
        self.Baseline_check.setDisabled(False)
        self.menu_6.setDisabled(False)
        Function.Create_Table_Data(self)

    def Create_Table_Data(self):
        self.Table_data = pd.DataFrame({"Sample":[str(i[0]) for i in self.Calib_Data[0]], 
                                       "Name":[str(i[1]) for i in self.Calib_Data[0]],
                                       "Conc":[str(i[2]) for i in self.Calib_Data[0]],
                                       "Dev": [4 for i in self.Calib_Data[0]],
                                       "sT":[5.0 for i in self.Calib_Data[0]],
                                       "eT":[95.0 for i in self.Calib_Data[0]],
                                       "light":[i[4] for i in self.Calib_Data[0]],
                                       "Ramp":[i[5] for i in self.Calib_Data[0]],
                                       "dH":[-90000 for i in self.Calib_Data[0]],
                                       "ErrordH":[0.0 for i in self.Calib_Data[0]],
                                       "dS":[-220 for i in self.Calib_Data[0]],
                                       "ErrordS":[0.0 for i in self.Calib_Data[0]],
                                       "Bss":[max(i[1]) for i in self.Calib_Data[1]],
                                       "Css":[0.0 for i in self.Calib_Data[0]],
                                       "Bds":[min(i[1]) for i in self.Calib_Data[1]],
                                       "Cds":[0.0 for i in self.Calib_Data[0]],
                                       "dG":[0.0 for i in self.Calib_Data[0]],
                                       "Tm":[0.0 for i in self.Calib_Data[0]],
                                       "CKO":[0.0 for i in self.Calib_Data[0]]})
        #print(self.Table_data)
        Function.reviev_Table(self)
   
    def reviev_Table(self):
        self.Name_list = ["Sample", "Name","Conc","sT","eT","light","Ramp","dH","ErrordH","dS","ErrordS","Bss","Css","Bds","Cds","dG","Tm","CKO"]
        Config_list = [self.Config_Sample, self.Config_Name,self.Config_Concentration,self.Config_Start_temperature, self.Config_End_temperature, self.Config_Light, self.Config_Ramp, self.Config_dH, 
                       self.Config_Error_dH, self.Config_dS, self.Config_Error_dS, self.Config_Bss, self.Config_Css, self.Config_Bds,self.Config_Cds,self.Config_dG,self.Config_Tm,self.Config_CKO]
        self.Name_list = [self.Name_list[i] for i in range(0,len(Config_list)) if Config_list[i].isChecked()]
        self.Table_calc.setColumnCount(len(self.Name_list))
        self.Table_calc.setHorizontalHeaderLabels(self.Name_list)
        self.Table_calc.resizeColumnsToContents()
        self.Table_calc.setRowCount(len(self.Calib_Data[0]))
        for column in range(0,len(self.Name_list)):
            for row in range(0,len(self.Calib_Data[0])):
                if self.Name_list[column] == "Sample":
                    self.Table_calc.setItem(row,column, QtWidgets.QTableWidgetItem("Sample "+str(self.Table_data.loc[row,'Sample'])))
                elif self.Name_list[column] in ["dH",'dS','ErrordH','ErrordS',"Bss","Css","Bds","Cds","dG","Tm","CKO"]:
                    self.Table_calc.setItem(row,column, QtWidgets.QTableWidgetItem(str(round(float(self.Table_data.loc[row,self.Name_list[column]]),2))))
                else:
                    self.Table_calc.setItem(row,column, QtWidgets.QTableWidgetItem(str(self.Table_data.loc[row,self.Name_list[column]])))
        self.Table_calc.resizeColumnsToContents()
        self.review_table_button.setDisabled(False)
        self.action_4.setDisabled(False)

    def Plot_graph(self):
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
        
        self.min_line_to_PLT.sigPositionChangeFinished.connect(lambda: Function.Infinity_line_usage(self,"min_line_to_PLT"))
        self.max_line_to_PLT.sigPositionChangeFinished.connect(lambda: Function.Infinity_line_usage(self,"max_line_to_PLT"))
        self.min_line_to_DPLT.sigPositionChangeFinished.connect(lambda: Function.Infinity_line_usage(self,"min_line_to_DPLT"))
        self.max_line_to_DPLT.sigPositionChangeFinished.connect(lambda: Function.Infinity_line_usage(self,"max_line_to_DPLT"))

        self.layout.addWidget(self.PLT)
        self.layout.addWidget(self.DPLT)
        self.Plot_window.show()

    def Infinity_line_usage(self,item):
        if item == "min_line_to_PLT": 
            self.Table_data.loc[self.selected_row,'sT'] = round(float(self.min_line_to_PLT.getPos()[0]),1)
            try: self.Table_calc.setItem(self.selected_row,self.Name_list.index('sT'),QtWidgets.QTableWidgetItem(str(round(float(self.min_line_to_PLT.getPos()[0]),1))))
            except:pass
            self.min_line_to_DPLT.setPos(self.min_line_to_PLT.getPos())
        elif item == "max_line_to_PLT":
            self.Table_data.loc[self.selected_row,'eT'] = round(float(self.max_line_to_PLT.getPos()[0]),1)
            try:self.Table_calc.setItem(self.selected_row,self.Name_list.index('eT'),QtWidgets.QTableWidgetItem(str(round(float(self.max_line_to_PLT.getPos()[0]),1))))
            except:pass
            self.max_line_to_DPLT.setPos(self.max_line_to_PLT.getPos())
        elif item == "min_line_to_DPLT":
            self.Table_data.loc[self.selected_row,'sT'] = round(float(self.min_line_to_DPLT.getPos()[0]),1)
            try:self.Table_calc.setItem(self.selected_row,self.Name_list.index('sT'),QtWidgets.QTableWidgetItem(str(round(float(self.min_line_to_PLT.getPos()[0]),1))))
            except:pass
            self.min_line_to_PLT.setPos(self.min_line_to_DPLT.getPos())
        elif item == "max_line_to_DPLT":
            self.Table_data.loc[self.selected_row,'eT'] = round(float(self.max_line_to_DPLT.getPos()[0]),1)
            try:self.Table_calc.setItem(self.selected_row,self.Name_list.index('eT'),QtWidgets.QTableWidgetItem(str(round(float(self.max_line_to_PLT.getPos()[0]),1))))
            except:pass
            self.max_line_to_PLT.setPos(self.max_line_to_DPLT.getPos())
        else:
            print("ERROR")
        #self.Start_temp_edit.setText(str(self.Table_data.loc[self.selected_row,'sT']))
        #self.End_temp_edit.setText(str(self.Table_data.loc[self.selected_row,'eT']))
    
    def review_data(self,edit):
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
        if self.model.currentText() == "Несамокомплемент":
            MassX = np.linspace(int(min(self.Calib_Data[1][self.selected_row][0])),int(max(self.Calib_Data[1][self.selected_row][0])),2000).tolist()
            MassY = NoSelfComp(MassX, self.Table_data.loc[self.selected_row,'dH'],
                                self.Table_data.loc[self.selected_row,'dS'],
                                self.Table_data.loc[self.selected_row,'Bss'],
                                self.Table_data.loc[self.selected_row,'Css'],
                                self.Table_data.loc[self.selected_row,'Bds'],
                                self.Table_data.loc[self.selected_row,'Cds'],self.Start_conf,
                                self.Table_data.loc[self.selected_row,'Conc'])
            self.PlotGraph = self.PLT.plot(MassX,MassY,  pen='r',width=50)
            Mass_X, Mass_Y = DNoSelfComp(MassX, self.Table_data.loc[self.selected_row,'dH'],
                                self.Table_data.loc[self.selected_row,'dS'],
                                self.Table_data.loc[self.selected_row,'Bss'],
                                self.Table_data.loc[self.selected_row,'Css'],
                                self.Table_data.loc[self.selected_row,'Bds'],
                                self.Table_data.loc[self.selected_row,'Cds'],self.Start_conf,
                                self.Table_data.loc[self.selected_row,'Conc'])
            self.DPlotGraph = self.DPLT.plot(Mass_X,Mass_Y,  pen='r')
        elif self.model.currentText() == "Cамокомплемент":
            MassX = np.linspace(int(min(self.Calib_Data[1][self.selected_row][0])),int(max(self.Calib_Data[1][self.selected_row][0])),2000).tolist()
            MassY = SelfComp(MassX, self.Table_data.loc['dH',self.selected_row,],
                                self.Table_data.loc[self.selected_row,'dS'],
                                self.Table_data.loc[self.selected_row,'Bss'],
                                self.Table_data.loc[self.selected_row,'Css'],
                                self.Table_data.loc[self.selected_row,'Bds'],
                                self.Table_data.loc[self.selected_row,'Cds'],self.Start_conf,
                                self.Table_data.loc[self.selected_row,'Conc'])
            self.PlotGraph = self.PLT.plot(MassX,MassY,  pen='r')
            Mass_X, Mass_Y = DSelfComp(MassX, self.Table_data.loc[self.selected_row,'dH'],
                                self.Table_data.loc[self.selected_row,'dS'],
                                self.Table_data.loc[self.selected_row,'Bss'],
                                self.Table_data.loc[self.selected_row,'Css'],
                                self.Table_data.loc[self.selected_row,'Bds'],
                                self.Table_data.loc[self.selected_row,'Cds'],self.Start_conf,
                                self.Table_data.loc[self.selected_row,'Conc'])
            self.DPlotGraph = self.DPLT.plot(Mass_X,Mass_Y,  pen='r')
        elif self.model.currentText() == "Шпилька":
            MassX = np.linspace(int(min(self.Calib_Data[1][self.selected_row][0])),int(max(self.Calib_Data[1][self.selected_row][0])),2000).tolist()
            MassY = loop(MassX, self.Table_data.loc[self.selected_row,'dH'],
                                self.Table_data.loc[self.selected_row,'dS'],
                                self.Table_data.loc[self.selected_row,'Bss'],
                                self.Table_data.loc[self.selected_row,'Css'],
                                self.Table_data.loc[self.selected_row,'Bds'],
                                self.Table_data.loc[self.selected_row,'Cds'],self.Start_conf,
                                self.Table_data.loc[self.selected_row,'Conc'])
            self.PlotGraph = self.PLT.plot(MassX,MassY,  pen='r', )
            Mass_X, Mass_Y = Dloop(MassX, self.Table_data.loc[self.selected_row,'dH'],
                                self.Table_data.loc[self.selected_row,'dS'],
                                self.Table_data.loc[self.selected_row,'Bss'],
                                self.Table_data.loc[self.selected_row,'Css'],
                                self.Table_data.loc[self.selected_row,'Bds'],
                                self.Table_data.loc[self.selected_row,'Cds'],self.Start_conf,
                                self.Table_data.loc[self.selected_row,'Conc'])
            self.DPlotGraph = self.DPLT.plot(Mass_X,Mass_Y,  pen='r',width=5)
        
        self.PLT.setXRange(min(self.Calib_Data[1][self.selected_row][0]),max(self.Calib_Data[1][self.selected_row][0]))
        self.PLT.setYRange(min(self.Calib_Data[1][self.selected_row][1]),max(self.Calib_Data[1][self.selected_row][1]))

        self.DPLT.setXRange(min(self.Calib_Data[2][self.selected_row][0]),max(self.Calib_Data[2][self.selected_row][0]))
        self.DPLT.setYRange(min(self.Calib_Data[2][self.selected_row][1]),max(self.Calib_Data[2][self.selected_row][1]))

        self.min_line_to_PLT.setPos(self.Table_data.loc[self.selected_row,'sT']) 
        self.max_line_to_PLT.setPos(self.Table_data.loc[self.selected_row,'eT'])
        self.min_line_to_DPLT.setPos(self.Table_data.loc[self.selected_row,'sT']) 
        self.max_line_to_DPLT.setPos(self.Table_data.loc[self.selected_row,'eT'])
        self.point_to_derivative.setValue(self.Table_data.loc[self.selected_row,'Dev'])

        if edit == True:
            self.Entalpy_edit.setText(str(round(self.Table_data.loc[self.selected_row,'dH'],2)))
            self.Enthropy_edit.setText(str(round(self.Table_data.loc[self.selected_row,'dS'],2)))
            self.Bss_edit.setText('{:.6e}'.format(self.Table_data.loc[self.selected_row,'Bss']))
            self.Css_edit.setText('{:.6e}'.format(self.Table_data.loc[self.selected_row,'Css']))
            self.Bds_edit.setText('{:.6e}'.format(self.Table_data.loc[self.selected_row,'Bds']))
            self.Cds_edit.setText('{:.6e}'.format(self.Table_data.loc[self.selected_row,'Cds']))
        #self.Start_temp_edit.setText(str(round(self.Table_data.loc[self.selected_row,'sT'],1)))
        #self.End_temp_edit.setText(str(round(self.Table_data.loc[self.selected_row,'eT'],1)))

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

                self.menu_6.setDisabled(True)
        else:
            if self.Baseline_list.currentText() in [self.Calib_Data[0][i][4] for i in range(0,len(self.Calib_Data[0]))]:
                self.Calib_Data = self.Before_Copy
            [self.Table_calc.showRow(i) for i in set([j[1] for j in prepare_mass])] # Показать строки базовой линии
            self.Baseline_list.setEnabled(True)
            self.menu_6.setDisabled(False)
        for EXP in range(0,len(self.Calib_Data[0])):
            self.Table_data.loc[EXP,'Dev'] = 4

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
            Start_TEMP_INDEX = [abs(float(i) - float(self.Table_data.loc[EXP,'sT'])) for i in self.Calib_Data[1][EXP][0]].index(min([abs(float(i) - float(self.Table_data.loc[EXP,'sT'])) for i in self.Calib_Data[1][EXP][0]]))
            END_TEMP_INDEX = [abs(float(i) - float(self.Table_data.loc[EXP,'eT'])) for i in self.Calib_Data[1][EXP][0]].index(min([abs(float(i) - float(self.Table_data.loc[EXP,'eT'])) for i in self.Calib_Data[1][EXP][0]]))
            if Start_TEMP_INDEX > END_TEMP_INDEX:
                Start_TEMP_INDEX, END_TEMP_INDEX = END_TEMP_INDEX,Start_TEMP_INDEX
           
            if self.model.currentText() == "Несамокомплемент":
                model = Model(NoSelfComp)
            elif self.model.currentText() == "Самокомплемент":
                model = Model(SelfComp)
            elif self.model.currentText() == "Шпилька":
                model = Model(loop)
            else:
                print('Модель не найдена')

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
            params['C0'].set(float(self.Table_data.loc[int(EXP),'Conc']), vary=False)

            result = model.fit(self.Calib_Data[1][EXP][1][Start_TEMP_INDEX:END_TEMP_INDEX],params,
                                x = self.Calib_Data[1][EXP][0][Start_TEMP_INDEX:END_TEMP_INDEX])                                            
            
            if bool(self.Start_conf[0]) == True: 
                try:self.Table_calc.setItem(EXP,self.Name_list.index('dH'), QtWidgets.QTableWidgetItem(str(round(result.params['dH'].value,2))))
                except:pass
                try: self.Table_calc.setItem(EXP,self.Name_list.index('ErrordH'), QtWidgets.QTableWidgetItem(str(round(result.params['dH'].stderr,2))))
                except:pass
                self.Table_data.loc[EXP,'dH'] = result.params['dH'].value
                self.Table_data.loc[EXP,'ErrordH'] = result.params['dH'].stderr
            else: 
                self.Table_data.loc[EXP,'dH'] = Start_parametrs[0]
                self.Table_data.loc[EXP,'ErrordH'] = 0
                try: self.Table_calc.setItem(EXP,self.Name_list.index('ErrordH'), QtWidgets.QTableWidgetItem("0"))
                except:pass
            if bool(self.Start_conf[1]) == True: 
                try:self.Table_calc.setItem(EXP,self.Name_list.index('dS'), QtWidgets.QTableWidgetItem(str(round(result.params['dS'].value,2))))
                except:pass    
                try:self.Table_calc.setItem(EXP,self.Name_list.index('ErrordS'), QtWidgets.QTableWidgetItem(str(round(result.params['dS'].stderr,2))))
                except:pass
                self.Table_data.loc[EXP,'dS'] = result.params['dS'].value
                self.Table_data.loc[EXP,'ErrordS'] = result.params['dS'].stderr
            else: 
                self.Table_data.loc[EXP,'dS'] = Start_parametrs[1]
                self.Table_data.loc[EXP,'ErrordS'] = 0
                try: self.Table_calc.setItem(EXP,self.Name_list.index('ErrordH'), QtWidgets.QTableWidgetItem("0"))
                except:pass
           
            for i in range(0,4):
                mass_name = ['Bss','Css','Bds','Cds']
                if bool(self.Start_conf[2+i]):
                    try:self.Table_calc.setItem(EXP,self.Name_list.index(mass_name[i]), QtWidgets.QTableWidgetItem('{:.2e}'.format(result.params[mass_name[i]].value)))
                    except:pass
                    self.Table_data.loc[EXP,mass_name[i]] = result.params[mass_name[i]].value
                else:
                    try:self.Table_calc.setItem(EXP,self.Name_list.index(mass_name[i]), QtWidgets.QTableWidgetItem(str(Start_parametrs[2+i])))
                    except:pass 
                    self.Table_data.loc[EXP,mass_name[i]] = Start_parametrs[2+i]
           
            self.Table_data.loc[EXP,'dG'] = result.params['dH'].value-(self.dG_temp.value()+273.15)*result.params['dS'].value
            try:self.Table_calc.setItem(EXP,self.Name_list.index('dG'), QtWidgets.QTableWidgetItem(str(round(result.params['dH'].value - (self.dG_temp.value()+273.15)*result.params['dS'].value,2))))
            except:pass

            try:self.Table_calc.setItem(EXP,self.Name_list.index('CKO'), QtWidgets.QTableWidgetItem('{:.2e}'.format(result.chisqr)))
            except:pass
            self.Table_data.loc[EXP,'CKO'] = result.chisqr

            if self.model.currentText() == "Несамокомплемент":
                Tm = result.params['dH'].value/(result.params['dS'].value+1.9872*math.log(float(self.Table_data.loc[EXP,'Conc'])/4))
            elif self.model.currentText() == "Самокомплемент":
                Tm = result.params['dH'].value/(result.params['dS'].value+1.9872*math.log(float(self.Table_data.loc[EXP,'Conc'])/2))
            elif self.model.currentText() == "Шпилька":
                Tm = result.params['dH'].value/result.params['dS'].value
            self.Table_calc.setItem(EXP,self.Name_list.index('Tm'), QtWidgets.QTableWidgetItem(str(round(Tm-273.15,2))))
            self.Table_data.loc[EXP,'Tm'] = Tm-273.15
            print("Температура плавления: " +str(Tm-273.15))
            Function.review_data(self, True)

    def Bad_Approximation(self):
        for EXP in set([i.row() for i in self.Table_calc.selectionModel().selectedIndexes()]):
            Start_TEMP_INDEX = [abs(float(i) - float(self.Table_data.loc[EXP,'sT'])) for i in self.Calib_Data[1][EXP][0]].index(min([abs(float(i) - float(self.Table_data.loc[EXP,'sT'])) for i in self.Calib_Data[1][EXP][0]]))
            END_TEMP_INDEX = [abs(float(i) - float(self.Table_data.loc[EXP,'eT'])) for i in self.Calib_Data[1][EXP][0]].index(min([abs(float(i) - float(self.Table_data.loc[EXP,'eT'])) for i in self.Calib_Data[1][EXP][0]]))
            if Start_TEMP_INDEX > END_TEMP_INDEX:
                Start_TEMP_INDEX, END_TEMP_INDEX = END_TEMP_INDEX,Start_TEMP_INDEX


            def Gauss(x,a,b,c,d):
                return a*(2.718**(-((x-b)**2)/(2*c**2))) + d

            model = Model(Gauss)
            params = model.make_params()

            params['a'].set(1, vary=True)
            params['b'].set(self.Calib_Data[2][EXP][0][Start_TEMP_INDEX:END_TEMP_INDEX][self.Calib_Data[2][EXP][1][Start_TEMP_INDEX:END_TEMP_INDEX].index(max(self.Calib_Data[2][EXP][1][Start_TEMP_INDEX:END_TEMP_INDEX]))], vary=True)
            params['c'].set(5, vary=True)
            params['d'].set(0, vary=True)


            result = model.fit(self.Calib_Data[2][EXP][1][Start_TEMP_INDEX:END_TEMP_INDEX],params,
                            x = self.Calib_Data[2][EXP][0][Start_TEMP_INDEX:END_TEMP_INDEX])

            w = abs(2.35482*result.params['c'].value)
            
            if self.model.currentText() == "Несамокомплемент":
                dH = -4.37/(1/(result.params['b'].value+273.15)-1/(result.params['b'].value+273.15+w/2))
                dS = (dH - 1.9872*(result.params['b']+273.15)*math.log(float(self.Table_data.loc[EXP,'Conc'])/4))/(result.params['b']+273.15)
            elif self.model.currentText() == "Самокомплемент":
                dH = -4.37/(1/(result.params['b'].value+273.15)-1/(result.params['b'].value+273.15+w/2))
                dS = (dH - 1.9872*(result.params['b']+273.15)*math.log(float(self.Table_data.loc[EXP,'Conc'])/2))/(result.params['b']+273.15)
            elif self.model.currentText() == "Шпилька":
                dH = -4.37/(1/(result.params['b'].value+273.15)-1/(result.params['b'].value+273.15+w/2))
                dS = dH/(result.params['b']+273.15)
            else:
                print('Модель не найдена')
            

            try:
                self.Table_calc.setItem(EXP,self.Name_list.index('dH'), QtWidgets.QTableWidgetItem(str(round(dH,2))))
                self.Table_calc.setItem(EXP,self.Name_list.index('dS'), QtWidgets.QTableWidgetItem(str(round(dS,2))))
            except:
                pass
            self.Table_data.loc[EXP,'dH'] = dH
            self.Table_data.loc[EXP,'dS'] = dS
            if not self.Bss.isChecked():
                self.Table_data.loc[EXP,'Bss'] = self.Calib_Data[1][EXP][1][Start_TEMP_INDEX]
            if not self.Bds.isChecked():
                self.Table_data.loc[EXP,'Bds'] = self.Calib_Data[1][EXP][1][END_TEMP_INDEX]
            Function.review_data(self, True)

    def Save_data(self, savetype, method):
        file_out , check = QFileDialog.getSaveFileName(None, "QFileDialog.getOpenFileName()","", "All Files (*);;Python Files (*.py);;Text Files (*.txt)")
        if len(file_out) == 0: 
            return 
        Save_data = []
        if method == 'without_calib':
            Save_data = copy.deepcopy(self.Source_data)
        elif method == 'with_calib':
            Save_data = copy.deepcopy(self.Calib_Data)
            New_save_data = [[],[]]
            if self.Baseline_check.isChecked():
                for EXP in range(0,len(Save_data[0])):
                    if Save_data[0][EXP][4] != self.Baseline_list.currentText():
                        New_save_data[0].append(Save_data[0][EXP])
                        New_save_data[1].append(Save_data[1][EXP])
                Save_data = New_save_data


        if savetype == 'SV1':
            Ramp_list = set(sorted([Save_data[0][i][5] for i in range(0,len(Save_data[0]))]))
            for RAMP in Ramp_list:
                file_out_SV1 = open(file_out.replace('ramp',str(RAMP)),"a")
                Experiment_list = []
                
                for i in range(0,len(Save_data[0])):
                    if Save_data[0][i][5] == RAMP:
                        Experiment_list.append(i)
                Save_data_with_ramp = [[],[]]
                
                for i in Experiment_list:
                    Save_data_with_ramp[0].append(Save_data[0][i])
                    Save_data_with_ramp[1].append(Save_data[1][i])
                
                line = []
                for EXP in Save_data_with_ramp[0]:
                    #['1', 'RM15_DN1_10mM_CaCNa_15mM_MgCl2', '2e-6', '95.00-5.00°C', '260', '2']
                    #'Sample1_OSN4_TZ_1@1e-5  95.00-5.00°C Ramp 2_260'
                    line_names = 'Sample'+str(int(EXP[0]))+'_'+str(EXP[1])+'@'+str(EXP[2]+'  '+str(EXP[3])+'°C Ramp '+str(EXP[5])+'_'+str(int(float(EXP[4]))))
                    line.append("".join(line_names))
                file_out_SV1.write(";;".join(line) + "\n")
                
                line = []
                for EXP in Save_data_with_ramp[0]:
                    line.append('Temperature (°C)')
                    line.append("Abs")
                file_out_SV1.write(";".join(line)+ "\n")

                for stroka in range(0,max([len(i[0]) for i in Save_data_with_ramp[1]])):
                    line = []
                    for EXP in range(0,len(Save_data_with_ramp[0])):
                        try:
                            line.append(str(Save_data_with_ramp[1][EXP][0][stroka])+";"+str(Save_data_with_ramp[1][EXP][1][stroka]))
                        except:
                            line.append(";")
                    file_out_SV1.write(";".join(line)+ "\n")
        elif savetype == 'SV2':
            file_out = open(file_out,"a")
            line = []
            for EXP in Save_data[0]:
                line_names = []
                for data in range(0,len(EXP)):
                    if data == 0:
                        line_names.append('Sample'+str(EXP[data]))
                    else:
                        line_names.append(str(EXP[data]))
                line.append("|".join(line_names))
            file_out.write(";;".join(line) + "\n")
            
            line = []
            for EXP in Save_data[0]:
                line.append('Temperature')
                line.append("Absorbtion")
            file_out.write(";".join(line)+ "\n")

            for stroka in range(0,max([len(i[0]) for i in Save_data[1]])):
                line = []
                for EXP in range(0,len(Save_data[0])):
                    try:
                        line.append(str(Save_data[1][EXP][0][stroka])+";"+str(Save_data[1][EXP][1][stroka]))
                    except:
                        line.append(";")
                file_out.write(";".join(line)+ "\n")
        else:
            print('Не нашел метод')

    def Save_Table(self):
            file , check = QFileDialog.getSaveFileName(None, "QFileDialog.getOpenFileName()","", "All Files (*);;Python Files (*.py);;Text Files (*.txt)")
            if len(file) == 0: 
                return 
            file=open(file,"a")
            table = ["Sample", "Name","Conc","sT","eT","light","Ramp","dH","ErrordH","dS","ErrordS","Bss","Css","Bds","Cds","dG","Tm","CKO"]
            file.write(';'.join(table)+"\n")
            for row in range(0,len(self.Table_data.index)):
                row_data = []
                for col in range(0,len(self.Table_data.columns)):
                        row_data.append(str(self.Table_data.loc[row,table[col]]))
                row_data = ";".join(row_data).replace(".",",")
                file.write(str(row_data)+"\n")

    def Data_add(self,Name, data):
        try:self.Table_calc.setItem(self.selected_row,self.Name_list.index(Name), QtWidgets.QTableWidgetItem('{:.6e}'.format(float(data))))
        except: pass
        self.Table_data.loc[self.selected_row,Name] = float(data)
        Function.review_data(self, False)

    def Recalc_dA(self, point):
        Mass_X = []
        Mass_Y = []

        for POINT in range(0,len(self.Calib_Data[1][self.selected_row][0])-point):
            Mass_Y.append(np.polyfit(self.Calib_Data[1][self.selected_row][0][POINT:POINT+point],self.Calib_Data[1][self.selected_row][1][POINT:POINT+point],deg=1).tolist()[0])
            Mass_X.append(sum(self.Calib_Data[1][self.selected_row][0][POINT:POINT+point])/len(self.Calib_Data[1][self.selected_row][0][POINT:POINT+point]))
        self.Calib_Data[2][self.selected_row] = [Mass_X,Mass_Y]
        self.Table_data.loc[self.selected_row,'Dev'] = self.point_to_derivative.value()
        Function.review_data(self,True)

    def HotKeyCopyTable(self):
        if not self.Table_calc.hasFocus():
            return
        time.sleep(0.5)
        list_row = [i for i in set([i.row() for i in self.Table_calc.selectionModel().selectedIndexes()])]
        data = str(self.File_open) +"\n"+ self.Table_data.iloc[list_row].to_csv().replace(',',';').replace('.',',')
        pyperclip.copy(data)
    
    def HotKeyCopyData(self):
        if not self.Table_calc.hasFocus():
            return
        time.sleep(0.5)
        list_row = [i for i in set([i.row() for i in self.Table_calc.selectionModel().selectedIndexes()])]
        data = [[]]
        for EXP in range(len(list_row)):
            line_data = [str(i) for i in self.Calib_Data[0][list_row[EXP]]]
            if self.Baseline_check.isChecked():
                line_data.append('baseline_' + str(self.Baseline_list.currentText())+';')
            else:
                line_data.append(';')
            data[0].append('_'.join(line_data))

        for line in range(len(self.Calib_Data[1][0][0])):
            data.append([])
            for EXP in range(len(list_row)):
                data[line+1].append(str(self.Calib_Data[1][list_row[EXP]][0][line]).replace('.',','))
                data[line+1].append(str(self.Calib_Data[1][list_row[EXP]][1][line]).replace('.',','))
        data_to_copy = '\n'.join([';'.join(i) for i in data])
        pyperclip.copy(data_to_copy)
    
    def Write(self):
        for cell in [[i.row(),i.column()] for i in self.Table_calc.selectionModel().selectedIndexes()]:
            self.Table_calc.setItem(cell[0],cell[1], QtWidgets.QTableWidgetItem(self.CommandLine.text()))
            try:
                self.Table_data.loc[cell[0],self.Name_list[cell[1]]] = float(self.CommandLine.text())
            except:
                self.Table_data.loc[cell[0],self.Name_list[cell[1]]] = float(self.CommandLine.text())

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()