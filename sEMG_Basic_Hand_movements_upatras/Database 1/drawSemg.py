
from numpy import *
import matplotlib.pyplot as plt
import emd_functions as emd
from scipy.signal import butter, lfilter, hilbert
from matplotlib.ticker import MultipleLocator, FormatStrFormatter


def loadDataSet():
    dataMat = []
    scoreMat = []
    fr = open('/home/chao/git_resposity/sEMG/sEMG_Basic_Hand_movements_upatras/Database 1/female_1/female_1_cyl/female_1_cyl_1.txt')
    for line in fr.readlines():
        lineArr = line.strip().split()
        dataMat.append([float(lineArr[0]), float(lineArr[1])])
    return dataMat


def slidingWindow(dataMat, stepsize, width):
    dataArr = array(dataMat)
    #print (dataArr)
    n = shape(dataArr)[0]
    one = [[] for i in range(n)]
    two = [[] for i in range(n)]
    for i in range(n):
        one[i].append(dataArr[i, 0])
        two[i].append(dataArr[i, 1])
    # print(one)
    ch1 = window_stack(one, stepsize=stepsize, width=width)
    ch2 = window_stack(two, stepsize=stepsize, width=width)
    #print (sw)
    return ch1, ch2


def overLeapWindow(data, stepsize, width):
    return window_stack(data, stepsize=stepsize, width=width)


def calcIEMG(dataMat):
    one, two = slidingWindow(dataMat, 1, 20)
    m, n = shape(one)
    # print n
    tempONE = 0
    tempTWO = 0
    aveONE = 0.00000
    aveTWO = 0.00000
    arrONE = []
    arrTWO = []
    for i in range(m):
        for j in range(n):
            tempONE = tempONE + abs(one[i, j])
            tempTWO = tempTWO + abs(two[i, j])
            # print temp
        aveONE = tempONE / n
        aveTWO = tempTWO / n
        # print aveONE
        # print aveTWO
        tempONE = 0
        tempTWO = 0
        arrONE.append(aveONE)
        arrTWO.append(aveTWO)
    # print arr
    return arrONE, arrTWO
    #print (len(arr))
    #print (m)
    #print (n)


def calcIncreaseIEMG(Arr):
    n = shape(Arr)[0]
    # print n
    # print Arr
    Increase = 0
    ArrIncrease = []
    num = n - 1
    for i in range(num):
        # print Arr[i+1]
        # print Arr[i]
        Increase = abs(Arr[i + 1] - Arr[i])
        # print Increase
        ArrIncrease.append(Increase)
    return ArrIncrease


def window_stack(a, stepsize=1, width=3):
    return hstack(a[i:1 + i - width or None:stepsize] for i in range(0, width))


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
    # dataMat=loadDataSet()
    dataArr = array(dataMat)
    n = shape(dataArr)[0]
    # print n
    xcord = []
    ycord = []
    # xcord2=[];ycord2=[]
    for i in range(n):
        xcord.append(dataArr[i, 0])
        ycord.append(dataArr[i, 1])
    # print xcord
    # print ycord
    fig1 = plt.figure()
    ax = fig1.add_subplot(211)

    ax.plot(xcord)
    yx = fig1.add_subplot(212)
    yx.plot(ycord)


def getEMD(data):

    # y=loadDataSet()
    #Arr = array(dataMat)
    #n = shape(Arr)[0]
    one = overLeapWindow(data, 15, 150)
    #m, n = shape(one)
    n = len(one)
    t = range(0, n)
# print t
    #one = []
    xcord = []
    for i in range(n):
        xcord.append(one[i, 0])
# print xcord

    oneIMF, oneR = emd.saw_emd(t, xcord, bc='extrap')
    # twoIMF,twoR=emd.saw_emd(t,two,bc='extrap')
    # return emd.emd(t, data)
    return oneIMF, oneR
# print shape(c)
# print c[1]


def detectStart(data, threshold):
    n = len(data)
    for i in range(n):
        if (data[i] > threshold):
            return i


def cutdata(dataMat, startNUM, endNUM):
    dataArr = array(dataMat)
    one = [[] for i in range(0, endNUM - startNUM)]
    two = [[]for i in range(0, endNUM - startNUM)]
    for i in range(0, endNUM - startNUM):
        one[i].append(dataArr[startNUM + i, 0])
        two[i].append(dataArr[startNUM + i, 1])
    # print one
    # print two
    return one, two


def drawIMF(c):
    # dataArr=array(c)
    m, n = shape(c)
    x = [i for i in range(0, m)]
    figIMF = plt.figure()
    imf1 = figIMF.add_subplot(311)
    imf1.plot(x, c[:, 0])
    imf2 = figIMF.add_subplot(312)
    imf2.plot(x, c[:, 1])
    imf3 = figIMF.add_subplot(313)
    imf3.plot(x, c[:, 2])
    # print m
    # print n


def hilbertTransform(imf):
    m, n = shape(imf)
    result1 = hilbert(imf[:, 0])
    result2 = hilbert(imf[:, 1])
    result3 = hilbert(imf[:, 2])

    fighilbert = plt.figure()
    figresult = fighilbert.add_subplot(111)
    figresult.plot(result1, 'or')
    figresult.plot(result2, 'og')
    figresult.plot(result3, 'ob')


arr = loadDataSet()

ch1IEMG, ch2IEMG = calcIEMG(arr)
num1 = detectStart(ch1IEMG, 0.8)
endNUM = shape(arr)[0]
actONE, actTWO = cutdata(arr, num1, endNUM)
t1 = [i * 0.002 for i in range(0, len(ch1IEMG))]
t2 = [i * 0.002 for i in range(num1, endNUM)]

# dataEMD1,r1=getEMD(actionData1)
# dataEMD2,r2=getEMD(actionData2)
# print array(actONE)
oneEMD, Rone = getEMD(actONE)
twoEMD, Rtwo = getEMD(actTWO)
m, n = shape(oneEMD)
print m
print n
drawIMF(oneEMD)
drawIMF(twoEMD)
hilbertTransform(oneEMD)
hilbertTransform(twoEMD)
threshold1 = [0.8 for i in range(0, len(ch1IEMG))]
threshold2 = [0.25 for i in range(0, len(ch1IEMG))]
# plt.axis()
#l = [0, 6, 0, 3]
# plt.axis(l)
# plt.plot(t[0:1000],ch1[0:1000])
# plt.plot(t[0:1000],ch2[0:1000])
# plt.show()
# plotBestFit(arr);
fig = plt.figure()
ax1 = fig.add_subplot(221)
# ax.scatter(xcord1,ycord1,s=30,c='red',marker='s')
# ax.scatter(xcord2,ycord2,s=30,c='green')
ax1.plot(t1, ch1IEMG)
ax1.plot(t1, threshold1)
# x=arange(-3.0,3.0,0.1)
# y=(-weights[0]-weights[1]*x)/weights[2]
# ax.plot(x,y)
ax2 = fig.add_subplot(222)
ax2.plot(t1, ch2IEMG)
ax2.plot(t1, threshold2)
# plt.ylabel('X2')
# plt.xlabel('X1');plt.ylabel('X2');
ax3 = fig.add_subplot(223)
ax3.plot(t2, actONE)

ax4 = fig.add_subplot(224)
ax4.plot(t2, actTWO)

plt.show()
