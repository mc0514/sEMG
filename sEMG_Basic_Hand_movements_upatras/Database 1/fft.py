import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack


def loadDataSet():
    dataMat=[];
    scoreMat=[];
    fr=open('/home/chao/git_repository/sEMG/sEMG_Basic_Hand_movements_upatras/Database 1/female_2/femal_2_cyl/female_2_cyl_1.txt')
    for line in fr.readlines():
        lineArr=line.strip().split()
        dataMat.append([float(lineArr[0]),float(lineArr[1])])
    return dataMat

def getFFt(dataMat):
    dataArr=np.array(dataMat)
    n=np.shape(dataArr)[0]
    #print n
    one=[]
    for i in range(n):
        one.append(dataArr[i,0])
    
    # Number of samplepoints
    #N = 600
    # sample spacing
    Time=6.0
    T = Time/ n
    #x = np.linspace(0.0, n*T, n)
    #y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)
    yf = scipy.fftpack.fft(one)
    #print len(yf)
    xf = np.linspace(0.0, 500.0, n)
    #print 1.0/(2.0*T)
    fig, ax = plt.subplots()
    #ax.plot(xf, 2.0/n * np.abs(yf[:n/2]))
    ax.plot(xf,np.abs(yf))
    plt.show()

mat=loadDataSet()
getFFt(mat)
