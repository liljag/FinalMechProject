import time
import bluetooth
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from MindwaveDataPoints import EEGPowersDataPoint
from MindwaveDataPointReader import MindwaveDataPointReader
from datetime import datetime
import numpy as np


def animate(time,dataPoint):
   # graph_data = open('example.txt','r').read()
    #lines = graph_data.split('\n')
    #xs = []
    #ys = []
    #for line in lines:
     #   if len(line) > 1:
      #      x, y = line.split(',')
       #     xs.append(float(x))
        #    ys.append(float(y))
    ax1.clear()
    print("HEY YOU GUYS")
    print(dataPoint)
    print(type(dataPoint))
    ax1.plot(time, dataPoint)
    print("sup")


if __name__ == '__main__':
    mindwaveDataPointReader = MindwaveDataPointReader()
    mindwaveDataPointReader.start()
    style.use('fivethirtyeight')
    data = []
    tim = []

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    fig = plt.figure()
    ax1 = fig.add_subplot(1,1,1)
    ax1.xaxis_date()


    count = 0

    while(count < 10):
        dataPoint = mindwaveDataPointReader.readNextDataPoint()
        if ( dataPoint.__class__ is EEGPowersDataPoint):
            print(dataPoint.highAlpha)
            print(type(dataPoint.highAlpha))
            ani = animation.FuncAnimation(fig, animate(now, dataPoint.highAlpha), interval=1000)
            print("sfhsdk")
            data.append(dataPoint.highAlpha)
            tim.append(now)
            count += 1
    print("sdkjfhsdkfhishfisdflkhaewklfh")
    print(data)
    print(tim)
    y = np.array(data)
    x = np.array(tim)
    ax1.plot(x, y)
    plt.show()
        #    print("lkfjgd")
        #    print(dataPoint)
