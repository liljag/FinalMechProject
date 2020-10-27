## Live plotting data ##

import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

# x_vals = [0, 1, 2, 3, 4, 5]
# y_vals = [0, 1, 3, 2, 3, 5]


# plt.plot(x_vals, y_vals)
x_vals = []
y_vals = []

index = count()






# def simulate_sensor():
#     data_list = []
#     with open('out.csv','r') as data: 
#         csv_reader = reader(data)
#         data_list = list(csv_reader)
    
#     for row in data_list:
#         highBeta = row[2]




def animate(i):
    ##Reading from a freqently updated csv file##
    data = pd.read_csv('simulated_data.csv')
    x_vals = data['datapoint']
    
    y_vals = data['highBeta']


    plt.cla()
    plt.plot(x_vals,y_vals)
    plt.tight_layout()

ani = FuncAnimation(plt.gcf(), animate, interval=100) #Inserts figure, function to run, time interval


plt.tight_layout()
plt.show()
