
from typing import List

def zcount(data: List[float]) -> float :
    return len(data)

def zmean(data: List[float]) -> float :
    return (sum(data)/len(data))

def zmode(data: List[float]) -> float :
    return max(set(data), key=data.count)

def zmedian(data: List[float]) -> float :
    pass

def zvariance(data: List[float]) -> float :
    pass
	
def zstddev(data: List[float]) -> float :
    # sqrt of variance
    pass

def zstderr(data: List[float]) -> float :
    pass

def cov(a, b):
    pass

def zcorr(datax: List[float], datay: List[float]) -> float :
    pass


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
