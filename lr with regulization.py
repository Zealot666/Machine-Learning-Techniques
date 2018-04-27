import numpy as np
import math
def readdata(filename): #读取TXT中的数据
    file1 = open(filename)
    arraylins = file1.readlines()
    numberoflines = len(arraylins)
    X = np.ones((numberoflines, 3))
    Y = []
    index = 0
    for line in arraylins:
        line = line.strip()
        listFromLine = line.split()
        X[index, 1:] = listFromLine[0:2]
        Y.append(int(listFromLine[-1]))
        index +=1
    return X,Y


def sign(x):
    if x >=0 :return 1;
    else: return -1
def test(x_test,y_test,w):
    count = 0
    for i in range (len(x_test)):
        if sign(np.dot(x_test[i],w)) !=y_test[i]:
            count +=1
    print(count/len(x_test))

x_train,y_train = readdata(r"C:/Users/24525/Desktop/train.txt")
x_test,y_test = readdata(r"C:/Users/24525/Desktop/test.txt")
ni =np.linalg.inv(np.dot(np.transpose(x_train),x_train)+10*np.identity(np.dot(np.transpose(x_train),x_train).shape[0]))
w = np.dot(np.dot(ni,np.transpose(x_train)),y_train)
test(x_test,y_test,w)
