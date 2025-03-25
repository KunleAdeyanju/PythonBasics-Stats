
from typing import List
import math

def zcount(data: List[float]) -> float :
    return len(data)

def zmean(data: List[float]) -> float :
    return (sum(data)/len(data))

def zmode(data: List[float]) -> float :
    return max(set(data), key=data.count)

def zmedian(data: List[float]) -> float :
    dat = sorted(data)
    if len(data) % 2 == 1:
        return dat[len(data)/2]
    else:
        return (dat[(len(data)-1)/2] + dat[(len(data)+1)/2])/2
    pass

def zvariance(data: List[float]) -> float :
    sum = 0
    for i in data:
        sum += (i-zmean(data)) ** 2
    
    return sum/(len(data) -1)

	
def zstddev(data: List[float]) -> float :
    # sqrt of variance
    return math.sqrt(zvariance(data))

def zstderr(data: List[float]) -> float :
    return zstddev(data)/ len(data)

def cov(a, b):
    pass

def zcorr(datax: List[float], datay: List[float]) -> float :
    sumx = 0
    for i in datax:
        sumx += (i-zmean(datax)) ** 2

    sumy = 0
    for i in datay:
        sumy += (i-zmean(datay)) ** 2
    
    root_denom = math.sqrt((sumx ** 2)(sumy ** 2))

    return (sumx * sumy) / (root_denom)


def readDataFile(file):
    x,y = [], []
    with open(file) as f:
        first_line = f.readline() # consume headers
        for l in f:
            row = l.split(',')
            #print(row, type(row))
            x.append(float(row[0]))
            y.append(float(row[1]))
    return (x,y)

def readDataSets(files):
    data = {}
    for file in files:
        twoLists = readDataFile(file)
        data[file] = twoLists
    return data
