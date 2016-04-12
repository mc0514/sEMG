from numpy import *
from scipy.signal import butter, lfilter

def loadDataSet():
    dataMat=[];
    fr=open('/home/chao/git_resposity/sEMG/sEMG_Basic_Hand_movements_upatras/Database 1/female_1/female_1_cyl/female_1_cyl_1.txt')
    for line in fr.readlines():
        lineArr=line.strip().split()
        dataMat.append([float(lineArr[0]),float(lineArr[1])])
    return dataMat

def plotBestFit(dataMat):
    import matplotlib.pyplot as plt
    #dataMat=loadDataSet()
    dataArr=array(dataMat)
    n=shape(dataArr)[0]
    #print n
    xcord=[];ycord=[]
    #xcord2=[];ycord2=[]
    for i in range(n):
        if(i>300 and i<900 and abs(dataArr[i,0])>0.3):
            dataArr[i,0]=random.uniform(0.5, 0.01)
        if(i>900 and i< 1000 and abs(dataArr[i,0])>0.3):
            dataArr[i,0]=random.uniform(0.4, 0.01)
        if(i>1300 and i<1500 and abs(dataArr[i,0])>0.2):
            dataArr[i,0]=random.uniform(0.3, 0.01)
        if(i>1500 and i<2000 and abs(dataArr[i,0])>0.2):
            dataArr[i,0]=random.uniform(0.4, 0.01)
        if(i>2000 and i<2300 and abs(dataArr[i,0])>0.3):
            dataArr[i,0]=random.uniform(0.3, 0.01)
        if(i>2300 and abs(dataArr[i,0])>0.5):
            dataArr[i,0]=random.uniform(0.4, 0.01)
        xcord.append(abs(dataArr[i,0]));ycord.append(abs(dataArr[i,1]))
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
    ax.plot(xcord)
    #x=arange(-3.0,3.0,0.1)
    #y=(-weights[0]-weights[1]*x)/weights[2]
    #ax.plot(x,y)
    plt.ylabel('sEMG');
    #plt.xlabel('X1');plt.ylabel('X2');
    plt.show()
    
def butter_bandpass(lowcut, highcut, fs, order=6):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a


def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y
#data=loadDataSet()
#print data
arr=loadDataSet()
fs = 1000.0
lowcut = 15
highcut = 500
order=9
y=butter_bandpass_filter(arr,lowcut,highcut,fs,order=order)
#yabs=abs(y)
plotBestFit(y)
