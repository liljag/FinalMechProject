import time
import bluetooth
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from MindwaveDataPoints import EEGPowersDataPoint
from MindwaveDataPointReader import MindwaveDataPointReader
from datetime import datetime
import numpy as np
import csv


#def animate(time,dataPoint):
   # graph_data = open('example.txt','r').read()
    #lines = graph_data.split('\n')
    #xs = []
    #ys = []
    #for line in lines:
     #   if len(line) > 1:
      #      x, y = line.split(',')
       #     xs.append(float(x))
        #    ys.append(float(y))
    #ax1.clear()
    #print("HEY YOU GUYS")
    #print(dataPoint)
    #print(type(dataPoint))
    #ax1.plot(time, dataPoint)
    #print("sup")


if __name__ == '__main__':
    mindwaveDataPointReader = MindwaveDataPointReader()
    mindwaveDataPointReader.start()
    file = open("out.csv", "w")
    cr = csv.writer(file, delimiter=";", lineterminator="\n")
    cr.writerow(["highAlpha", "lowAlpha", "highBeta", "lowBeta", "midGamma", "lowGamma", "delta", "theta"])
    style.use('fivethirtyeight')
    dataA1 = []
    dataA2 = []
    dataB1 = []
    dataB2 = []
    dataG1 = []
    dataG2 = []
    dataD = []
    dataT = []
    data_sum = []
    data_sum2 = []
    #tim = [1,2, 3, 4, 5, 6,7, 8, 9, 10]
    tim = []

    

    #now = datetime.now()
    #current_time = now.strftime("%H:%M:%S")

    fig = plt.figure()

    ax1f = plt.figure()
    ax1 = ax1f.gca()
    ax1.set_title("Alpha high")

    ax2f = plt.figure()
    ax2 = ax2f.gca()
    ax2.set_title("Alpha low")

    bx1f = plt.figure()
    bx1 = bx1f.gca()
    bx1.set_title("Beta high")

    bx2f = plt.figure()
    bx2 = bx2f.gca()
    bx2.set_title("Beta low")

    gx1f = plt.figure()
    gx1 = gx1f.gca()
    gx1.set_title("Gamma mid")

    gx2f = plt.figure()
    gx2 = gx2f.gca()
    gx2.set_title("Gamma low")

    df = plt.figure()
    d = df.gca()
    d.set_title("Delta")

    tf = plt.figure()
    t = tf.gca()
    t.set_title("Theta")

    tbf = plt.figure()
    tb = tbf.gca()
    tb.set_title("Delta Beta average")

    tbf2 = plt.figure()
    tb2 = tbf2.gca()
    tb2.set_title("theta Beta ave")

    #fig.legend((ax1, ax2, bx1, bx2, gx1, gx2, d, t),("highA", "lowA", "highB", "lowB", "highG", "lowG", "delta", "theta"))
    #ax1.xaxis_date()


    count = 0

    

    while(count < 100):
        dataPoint = mindwaveDataPointReader.readNextDataPoint()
        if ( dataPoint.__class__ is EEGPowersDataPoint):
            print(dataPoint.highAlpha)
            print(type(dataPoint.highAlpha))
            #ani = animation.FuncAnimation(fig, animate(now, dataPoint.highAlpha), interval=1000)
            print("sfhsdk")
            dataA1.append(dataPoint.highAlpha)
            dataA2.append(dataPoint.lowAlpha)
            dataB1.append(dataPoint.highBeta)
            dataB2.append(dataPoint.lowBeta)
            dataG1.append(dataPoint.midGamma)
            dataG2.append(dataPoint.lowGamma)
            dataD.append(dataPoint.delta)
            dataT.append(dataPoint.theta)
            data_sum.append(int((dataPoint.lowBeta + dataPoint.delta)/2))
            data_sum2.append(int((dataPoint.lowBeta + dataPoint.theta)/2))
            cr.writerow([dataPoint.highAlpha, dataPoint.lowAlpha, dataPoint.highBeta, dataPoint.lowBeta, dataPoint.midGamma, dataPoint.lowGamma, dataPoint.delta, dataPoint.theta])
            #now = datetime.now()
            #tim.append(int(now.second))
            tim.append(count)
            print("Count: ", count)
            #print("skjdhfksh")
            #print(int(now.second))
            count += 1
            print(dataPoint)
            #time.sleep(3)
    print("sdkjfhsdkfhishfisdflkhaewklfh")
    #print(data)
    print(tim)
    y = np.array(dataA1)
    x = np.array(tim)
    ax1.plot(x, y)
    #plt.show()
    y = np.array(dataA2)
    x = np.array(tim)
    ax2.plot(x, y)
    #plt.show()
    y = np.array(dataB1)
    x = np.array(tim)
    bx1.plot(x, y)
    #plt.show()
    y = np.array(dataB2)
    x = np.array(tim)
    bx2.plot(x, y)
    #plt.show()
    y = np.array(dataG1)
    x = np.array(tim)
    gx1.plot(x, y)
    #plt.show()
    y = np.array(dataG2)
    x = np.array(tim)
    gx2.plot(x, y)
    #plt.show()
    y = np.array(dataD)
    x = np.array(tim)
    d.plot(x, y)
    #plt.show()
    y = np.array(dataT)
    x = np.array(tim)
    t.plot(x, y)
    #
    y = np.array(data_sum)
    x = np.array(tim)
    tb.plot(x, y)
    #
    y = np.array(data_sum2)
    x = np.array(tim)
    tb2.plot(x, y)
    plt.show()
        #    print("lkfjgd")
        #    print(dataPoint)