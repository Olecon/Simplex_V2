import numpy as np

def Cary_3500(file_name):
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
                    Temp = line[step+1:i].replace('.0','.00')
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
    return True_mass

def Cary_300(file_name):
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
                if line[i] == " ":
                    Conc = line[step+1:i]
                    step = i
                    break
            
            for i in range(step+2,len(line)):
                if line[i] == " ":
                    Temp = line[step+2:i].replace('°C','')
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
    return True_mass

def SimplexV2(file_name):
    file = open(str(file_name),"r")
    file = file.readlines()
    file = [i.replace("\n","").split(";") for i in file]
    True_mass = [[],[]]

    for line in file[0]:
        if len(line) != 0:
            line = line.split('|')
            Sample = line[0].replace('Sample','')
            Name = line[1]
            Conc = line[2]
            Temp = line[3]
            light = line[4]
            Ramp = line[5]
            True_mass[0].append([Sample,Name,Conc,Temp,light,Ramp])

    for Sample in range(0, len(True_mass[0])):
        True_mass[1].append([[],[]])
        for i in file[2:]:
            try:
                if len(i[Sample*2]) > 0:
                    True_mass[1][Sample][0].append(float(i[Sample*2]))
                    True_mass[1][Sample][1].append(float(i[Sample*2+1]))
            except: pass
    return True_mass

def SimplexV1(file_name):
    file = open(str(file_name),"r")
    file = file.readlines()
    file = [i.replace("\n","").split(";") for i in file]
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
                if line[i-4:i] == "Ramp":
                    Ramp = line[i+1:i+2]
                    step = i+2
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
    return True_mass
