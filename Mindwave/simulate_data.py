import csv
from csv import reader
import random
import time

data_list = []
with open('out.csv','r') as data: 
    csv_reader = reader(data)
    data_list = list(csv_reader)
    # print(data_list)
    
        
            
datapoint = 0
highBeta = 0




fieldnames = ["datapoint", "highBeta"]


with open('simulated_data.csv','w') as csv_file:
    csv_writer = csv.DictWriter(csv_file,fieldnames=fieldnames)
    csv_writer.writeheader()



for row in data_list:

    highBeta = row[2]
    
    if highBeta == 'highBeta':
        continue
    

    

    with open('simulated_data.csv','a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        info = {
            "datapoint": datapoint,
            "highBeta": highBeta
        }

        csv_writer.writerow(info)
        print(datapoint,highBeta)

    
    datapoint += 1
    time.sleep(1)
