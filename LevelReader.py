import re
import numpy as np
import matplotlib.pyplot as plt

text = ''

data = open ("C:\\Users\\Boxitsoft1\\Documents\\Python\\STATSRTM2\\data.csv","r")

listLevels = []

x = 0

for line in data:
        if (x == 0):
                if (re.match('Custom parameter,Event count*',line)):
                        x = 1
        else:
                n = re.split(',',line )
                if (len(n) < 2 or re.match('[^0-9]',line)):
                        break
                n = set(map(int,n))
                listLevels.append(sorted(n))
                
data.close()

finalData = np.array(listLevels)

finalData = finalData[finalData[:,0].argsort()] 

def getInitPerLevel(data):
        a = [(data[0],data[2] / data[1])]
        return a

vidasPorLevel = []

for val in finalData:
        vidasPorLevel.append(getInitPerLevel(val))
vidasPorLevel = np.array(vidasPorLevel)

print("Datos finales:")
print(finalData)
print ("VIDAS POR NIVEL")
print(vidasPorLevel)


