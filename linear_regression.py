import matplotlib.pyplot as plt
import pandas as pd
import xlwings as xw
import numpy as np
import os
import sys

#This part is dedicated to the command line insertion of the path
fn = sys.argv[1]
if os.path.exists(fn):
    print(os.path.exists(fn))
else:
    print("ERROR WRONG PATH") #If the path is wrong, the program is closed.
    quit()

#This part is made to import the data from excel to python
data = pd.read_excel(sys.argv[1]) #reads the data in the excel given path
xl = pd.ExcelFile(sys.argv[1]) #this line will help me run the program even if i change the excel sheet name (for other datasets)

#first_sheet= urllib.unquote(xl.sheet_names[0]).encode('latin1').decode('unicode_escape')
data_km = pd.DataFrame(data, columns=["km"]) #memorizes the mileage data 
data_price= pd.DataFrame(data, columns=["price"]) #memorizes  the prices data
list_price=data_price.values.tolist() #creates a list of the mileage data 
list_km=data_km.values.tolist()  #creates a list of the prices 
LengthData=len(list_km)


#This part is made to import the data from python to excel
wb = xw.Book(sys.argv[1]) #The xw library helps us to edit the excel file while the program runs
DataSetToUpdate = wb.sheets["data"] #chooses the table

#turns the 2 dimensions unuseful lists to a one dimension list
for i in range(0,LengthData):
    list_km[i]=list_km[i][0]
for i in range(0,LengthData):
    list_price[i]=list_price[i][0]

#Size of my dataset 
sizeData=len(list_price)

#Plotting the points cloud
plt.scatter(list_km,list_price) 
plt.xlabel("Mileage Of A car")
plt.ylabel("Price Of A car")
plt.title("The plot of the dataset")
plt.savefig("Scatterplot_01.png")
plt.show()

#turning lists into arrays to make it easy to manipulate
list_price_array=np.array(list_price)
list_km_array=np.array(list_km)


def gradient_descent(x,y,iterations,learning_rate):
    m_curr = b_curr = 0
    n = len(x)
    for i in range(iterations):   
        y_predicted = m_curr * x + b_curr 
        cost = (1/(2*n)) * sum([val**2 for val in (y_predicted - y)]) 
        md = (1/n)*sum(x*(y_predicted - y)) 
        bd = (1/n)*sum(y_predicted - y)
        m_curr = m_curr - learning_rate * md
        b_curr = b_curr - learning_rate * bd
    print ("m {}, b {}, cost {} iteration {} md {} bd {}".format(m_curr,b_curr,cost, i, md , bd))

#This test function is created to find the best learningRate,iterations number 
def test(x,y):
    iterationsList=[5,10,50,100,500,1000,5000,10000,20000,50000]
    rateList=[0.055,0.005, 0.0001, 0.0001]
    for i in range(len(rateList)):
        for j in range(len(iterationsList)):
            print("--------------------------------")
            print("THIS IS TEST NUMBER {}th, ITERATIONS NUMBERS : {} LEARNING RATE : {} ".format(i,iterationsList[j], rateList[i]))
            gradient_descent(x,y,iterationsList[j], rateList[i])
            
test(list_km_array,list_price_array)
