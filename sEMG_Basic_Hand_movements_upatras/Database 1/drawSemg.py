
from numpy import *
import matplotlib.pyplot as plt
import emd_functions as emd
from scipy.signal import butter, lfilter
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
#import window_stack as slideWin


def loadDataSet():
    dataMat=[];
    scoreMat=[];
    fr=open('/home/chao/git_repository/sEMG/sEMG_Basic_Hand_movements_upatras/Database 1/female_2/femal_2_cyl/female_2_cyl_1.txt')
    for line in fr.readlines():
        lineArr=line.strip().split()
        dataMat.append([float(lineArr[0]),float(lineArr[1])])
    return dataMat

def slidingWindow(dataMat):
    dataArr=array(dataMat)
    #print (dataArr)
    n=shape(dataArr)[0]
    one=[[] for i in range(n)]
    for i in range(n):
        one[i].append(dataArr[i,0])
    #print(one)
    sw=window_stack(one,stepsize=1,width=20)
    #print (sw)
    return sw
    
def calcIEMG(dataMat):
    swdata=slidingWindow(dataMat)
    m,n=shape(swdata)
    print n
    temp=0
    ave=0.00000
    arr=[]
    for i in range(m):
        for j in range(n):
            temp=temp+swdata[i,j]
            #print temp
        ave=temp/n
        #print ave
        temp=0
        arr.append(abs(ave))
    #print arr
    return arr
    #print (len(arr))
    #print (m)
    #print (n)
    #swdata(1)
    #temp=[]
    #for i in range(200):
        #temp.append(swdata[0,i])
def calcIncreaseIEMG(Arr):
    n=shape(Arr)[0]
    print n
    #print Arr
    Increase=0
    ArrIncrease=[]
    num=n-1
    for i in range(num):
        #print Arr[i+1]
        #print Arr[i]
        Increase=abs(Arr[i+1]-Arr[i])
        #print Increase
        ArrIncrease.append(Increase)
    return ArrIncrease

def window_stack(a, stepsize=1, width=3):
    return hstack( a[i:1+i-width or None:stepsize] for i in range(0,width) )

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


def plotBestFit(dataMat):
    import matplotlib.pyplot as plt
    #dataMat=loadDataSet()
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
def getEMD(dataMat):
    
#y=loadDataSet()
    Arr=array(dataMat)
    n=shape(Arr)[0]
    t=range(0,n)
#print t
    one=[]
    for i in range(n):
            xcord.append(yArr[i,1])
#print xcord

    return emd.saw_emd(t,xcord,bc='extrap')
#print shape(c)
#print c[1]
def drawIMF(c):   
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


arr=loadDataSet()
fs = 1000.0
lowcut = 15.0
highcut = 200
order=6
y=butter_bandpass_filter(arr,lowcut,highcut,fs,order=order)
#yy=butter_bandpass_filter(y,51,highcut,fs,order=order)
ave=calcIEMG(y)
#ave=ave*1000
#print ave


plt.axis()  
l=[0,2500,0,3]  
plt.axis(l)  
t=range(0,len(ave))
plt.plot(t,ave)
Increase=calcIncreaseIEMG(ave)
t=range(0,len(Increase))
plt.plot(t,Increase)

#y=butter_bandpass_filter(ave,lowcut,highcut,fs,order=order)
#absy=abs(y)
#t=range(0,len(y))
#plt.plot(t,absy)
plt.show()

    


