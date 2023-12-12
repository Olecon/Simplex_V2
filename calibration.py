# -*- coding: utf-8 -*-

import os
import numpy as np

def Use_calib(Source_Data, pribor, method):
    Calibration_mass = []
    for file in sorted(os.listdir(str(pribor)+'/'+str(method))):
        file = open(str(pribor)+"/"+str(method)+"/"+str(file),"r")
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

    Mass = []
    for EXP in range(0,len(Source_Data[1])):
        Mass_X = []
        Mass_Y = []
        for POINT in range(0,len(Source_Data[1][EXP][0])-4):
            Mass_Y.append(np.polyfit(Source_Data[1][EXP][0][POINT:POINT+4],Source_Data[1][EXP][1][POINT:POINT+4],deg=1).tolist()[0])
            Mass_X.append(Source_Data[1][EXP][0][POINT+2])
        Mass.append([Mass_X,Mass_Y])
    Source_Data.append(Mass)
    
    return Source_Data