import time
import bluetooth
from MindwaveDataPoints import RawDataPoint
from MindwaveDataPointReader import MindwaveDataPointReader
#from plot import animate


if __name__ == '__main__':
    mindwaveDataPointReader = MindwaveDataPointReader()
    mindwaveDataPointReader.start()


    while(True):
        dataPoint = mindwaveDataPointReader.readNextDataPoint()
        if (not dataPoint.__class__ is RawDataPoint):
            print( dataPoint)


