import matplotlib.pyplot as plt
import pandas as pd
import xlwings as xw
import numpy as np
import os
import sys

#This part is dedicated to the command line insertion of the paths
fn = sys.argv[1]
if os.path.exists(fn):
    print("Abracadabra")
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

def gradient_descent(x,y,iterations,learning_rate):
    #turning lists into arrays to make it easy to manipulate
    list_price_array_reducted=(1/10)*np.array(list_price) # y 
    list_km_array_reducted=(1/10000)*np.array(list_km)   # x
    m_curr = 0
    b_curr = 0
    n = len(x)
    for i in range(iterations):   
        y_predicted = m_curr * list_km_array_reducted + b_curr 
        cost = (1/(2*n)) * sum([val**2 for val in (y_predicted - y)]) 
        md = (1/n)*sum(list_km_array_reducted*(y_predicted - list_price_array_reducted)) 
        bd = (1/n)*sum(y_predicted - list_price_array_reducted)
        m_curr = m_curr - learning_rate * md
        b_curr = b_curr - learning_rate * bd
    print ("m {}, b {}, cost {} iteration {} md {} bd {}".format(m_curr,b_curr,cost, i, md , bd))
    m_curr=(1/1000)*m_curr
    b_curr=10*b_curr
    L=[x[i]*m_curr+ b_curr for i in range(len(x))]
    plt.scatter(x,y) 
    plt.xlabel("Mileage Of A car")
    plt.ylabel("Price Of A car")
    plt.title("The plot of the dataset")
    plt.savefig("Scatterplot_01.png")
    plt.plot(x,L, color='red' )
    plt.show()
    
    
gradient_descent(list_km,list_price,100000,0.001)
quit()

    
