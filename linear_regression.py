import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import sys
import pickle 

#This part is dedicated to the command line insertion of the paths
fn = sys.argv[1]
typevisualization = sys.argv[2] #To choose which type of visualization we want to see
if os.path.exists(fn):
    print("Abracadabra")
else:
    print("ERROR WRONG PATH") #If the path is wrong, the program is closed.
    quit()

#This part is made to import the data from excel to python
data = pd.read_excel(sys.argv[1]) #reads the data in the excel given path
xl = pd.ExcelFile(sys.argv[1]) #this line will help me run the program even if i change the excel sheet name (for other datasets)

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
#Turns the lists to numpy arrays
L=np.array(list_price)
J=np.array(list_km)

#Normalizing the arrays 
array_price_normalized = (L-min(L))/(max(L)-min(L))
array_mileage_normalized =  (J-min(J))/(max(J)-min(J))

#Normalized type of visualization 
if typevisualization=='Normalized':
    #Plotting the points cloud
    plt.scatter(array_mileage_normalized,array_price_normalized) 
    plt.xlabel("Mileage Of A car")
    plt.ylabel("Price Of A car")
    plt.title("The plot of the dataset")
    plt.savefig("Data_Cloud_Normalized.png")
    plt.show()

#Not normalized type of visualization
if typevisualization=='Not Normalized':
    plt.scatter(list_km,list_price) 
    plt.xlabel("Mileage Of A car")
    plt.ylabel("Price Of A car")
    plt.title("The plot of the dataset")
    plt.savefig("Data_Cloud_Not_Normalized.png")
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
    #print ("m {}, b {}, cost {} iteration {} md {} bd {}".format(m_curr,b_curr,cost, i, md , bd))
    m_curr=(1/1000)*m_curr
    b_curr=10*b_curr
    L=[x[i]*m_curr+ b_curr for i in range(len(x))]
    plt.scatter(x,y) 
    plt.xlabel("Mileage Of A car")
    plt.ylabel("Price Of A car")
    plt.title("Regression Line Not Normalized")
    plt.savefig("Regression.png")
    plt.plot(x,L, color='red' )
    plt.show()
    f = open('myVariables.txt', 'wb')
    pickle.dump([m_curr,b_curr] , f)
    f.close()
    
def gradient_descent_undernorm(x,y,iterations,learning_rate):
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
    f = open('myVariables.txt', 'wb')
    pickle.dump([m_curr,b_curr] , f)
    f.close()
    
def gradient_descent_Normalized(x,y,iterations,learning_rate):
    list_km_array_reducted = x 
    list_price_array_reducted = y
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
    #print ("m {}, b {}, cost {} iteration {} md {} bd {}".format(m_curr,b_curr,cost, i, md , bd))
    L=[x[i]*m_curr+ b_curr for i in range(len(x))]
    plt.scatter(x,y) 
    plt.xlabel("Mileage Of A car")
    plt.ylabel("Price Of A car")
    plt.title("Regression Line Normalized")
    plt.plot(x,L, color='red' )
    plt.savefig("Regression_normalized.png")
    plt.show()
    
  
if typevisualization=="Normalized":
    gradient_descent_undernorm(list_km,list_price,100000,0.001)
    gradient_descent_Normalized(array_mileage_normalized,array_price_normalized,100000,0.01)
else:
    gradient_descent(list_km,list_price,100000,0.001)

answer1=input("Do you want to estimate the price of a car?\n")
if answer1 in ["yes","Yes","YES","y","oui","ah","Ah"]:
    os.system('python estimate_price.py')
else:
    print("Thanks for your ")
    quit()
quit()
