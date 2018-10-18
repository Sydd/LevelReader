import re
import numpy as np
import matplotlib.pyplot as plt
import sys
import datetime

text = ''

if (len(sys.argv) == 1):
        print ("missing argument: data path")
        exit()

dataSource = open (sys.argv[1],"r")

listLevels = []

x = 0

for line in dataSource:
        if (x == 0):
                if (re.match('Custom parameter,Event count*',line)):
                        x = 1
        else:
                n = re.split(',',line )
                if (len(n) < 2 or re.match('[^0-9]',line)):
                        break
                n = set(map(int,n))
                listLevels.append(sorted(n))
                
dataSource.close()

finalData = np.array(listLevels)

finalData = finalData[finalData[:,0].argsort()] 

def getInitPerLevel(data):
        a = [(data[0],data[2] / data[1])]
        return a

livesperlevel = []

for val in finalData:
        livesperlevel.append(getInitPerLevel(val))


livesperlevel = np.array(livesperlevel)

def calculatePlot(data):
        t = np.arange(0,30,1)
        x = []
        for i in data:
                 x.append(i[2] / i[1])
        return x

s = np.array(calculatePlot(finalData))

def ShowPlot():
        plt.xlabel = "niveles"
        plt.ylabel="dificultad"
        plt.plot(s,color='red', marker='o',
                 linestyle='dashed', linewidth=2, markersize=5)
        plt.grid(True)
        plt.savefig(datetime.datetime.today().strftime("%d-%m-%Y")+".png")
        plt.show()
               
        


print ("finalData for original array of data.\n livesPerLevel to calculate how many lives takes each level")



