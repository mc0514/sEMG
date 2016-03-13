
from numpy import *
import matplotlib.pyplot as plt
import emd_functions as emd



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
#plotBestFit()
y=loadDataSet()
yArr=array(y)
n=shape(yArr)[0]
t=range(0,n)
#print t
xcord=[]
for i in range(n):
        xcord.append(yArr[i,1])
#print xcord

c,r=emd.saw_emd(t,xcord,bc='extrap')
#print shape(c)
#print c[1]
mode1=[]
mode2=[]
mode3=[]
mode4=[]
mode5=[]
mode6=[]
mode7=[]
for i in range(n):
        mode1.append(c[i,0])
        mode2.append(c[i,1])
        mode3.append(c[i,2])
        mode4.append(c[i,3])
        mode5.append(c[i,4])
        mode6.append(c[i,5])
        mode7.append(c[i,6])
#pf, = plt.plot(t, xcord)
#pr, = plt.plot(t, r)
#pcs = plt.plot(t, c, 'k-')
#p1=plt.plot(t,mode1)
#p2=plt.plot(t,mode2)
#p3=plt.plot(t,mode3)
#p4=plt.plot(t,mode4)
#p5=plt.plot(t,mode5)
#p6=plt.plot(t,mode6)
p7=plt.plot(t,mode7)

#plt.legend((p4,p5,p6),('IMF3','IMF4','IMF5'))

#plt.legend((pf, pcs[0], pr), ('original function', 'modes', 'residual'))
plt.show()


