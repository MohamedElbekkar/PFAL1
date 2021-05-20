import matplotlib.pyplot as plt
import pandas as pd
import xlwings as xw
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






























