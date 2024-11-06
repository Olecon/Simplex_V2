# -*- coding: utf-8 -*-

import os
import numpy as np
import copy

def Use_calib(Source_data, pribor, method):
    Calib_data = copy.deepcopy(Source_data)
    Calibration_mass = []
    for file in sorted(os.listdir(str(pribor)+'/'+str(method))):
        file = open(str(pribor)+"/"+str(method)+"/"+str(file),"r")
        file = file.readlines()
        file = [i.replace("\n","").split(",") for i in file]
        Calibration_mass.append(file)

    for EXP in range(0,len(Calib_data[0])):
        
        
        Sample = int(Calib_data[0][EXP][0])-1 # Начинается с 0
        Stage = int(Calib_data[0][EXP][5]) # Начинается с 1, потому что в калибровочном файле 0 столбец - исходная температура
        
        Source_Temperature_in_calibtation_file = np.array([float(i[0]) for i in Calibration_mass[Sample]])
        Source_Stage_Temperature_in_calibration_file = np.array([float(i[Stage]) for i in Calibration_mass[Sample]])

        nearest_val_position = np.vectorize(lambda t: (np.abs(t - Source_Temperature_in_calibtation_file)).argmin())
        nearest_val_position = nearest_val_position(np.array(Calib_data[1][EXP][0]))

        Calib_data[1][EXP][0] = Source_Stage_Temperature_in_calibration_file[nearest_val_position]

    Mass = []
    for EXP in range(0,len(Calib_data[1])):
        Mass_X = []
        Mass_Y = []
        for POINT in range(0,len(Calib_data[1][EXP][0])-4):
            Mass_Y.append(np.polyfit(Calib_data[1][EXP][0][POINT:POINT+4],Calib_data[1][EXP][1][POINT:POINT+4],deg=1).tolist()[0])
            Mass_X.append(Calib_data[1][EXP][0][POINT+2])
        Mass.append([Mass_X,Mass_Y])
    Calib_data.append(Mass)
    return Calib_data