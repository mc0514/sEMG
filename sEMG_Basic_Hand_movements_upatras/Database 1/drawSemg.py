
from numpy import *

def loadDataSet():
    dataMat=[];
    scoreMat=[];
    fr=open('/home/chao/git_repository/sEMG/sEMG_Basic_Hand_movements_upatras/Database 1/female_2/femal_2_cyl/female_2_cyl_1.txt')
    for line in fr.readlines():
        lineArr=line.strip().split()
        dataMat.append([float(lineArr[0]),float(lineArr[1])])
    return dataMat

def plotBestFit():
    import matplotlib.pyplot as plt
    dataMat=loadDataSet()
    dataArr=array(dataMat)
    n=shape(dataArr)[0]
    #print n
    xcord=[];ycord=[]
    #xcord2=[];ycord2=[]
    for i in range(n):
        xcord.append(dataArr[i,0]);ycord.append(dataArr[i,1])
        #if int(labelMat[i])==1:
            #xcord1.append(dataArr[i,1]);ycord1.append(dataArr[i,2])
        #else:
            #xcord2.append(dataArr[i,1]);ycord2.append(dataArr[i,2])
    #print xcord
    #print ycord
    fig=plt.figure()
    ax=fig.add_subplot(111)
    #ax.scatter(xcord1,ycord1,s=30,c='red',marker='s')
    #ax.scatter(xcord2,ycord2,s=30,c='green')

    ax.plot(ycord)
    #x=arange(-3.0,3.0,0.1)
    #y=(-weights[0]-weights[1]*x)/weights[2]
    #ax.plot(x,y)
    plt.ylabel('X2');
    #plt.xlabel('X1');plt.ylabel('X2');
    plt.show()

#data=loadDataSet()
#print data
plotBestFit()


