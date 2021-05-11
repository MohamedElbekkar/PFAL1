import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_excel(r'C:\Users\Mohammed\Desktop\UM6P_S2\Informatique 2- C/data.xlsx')
data_km = pd.DataFrame(data, columns=["km"])
data_price= pd.DataFrame(data, columns=["price"])
list_price=data_price.values.tolist()
list_km=data_km.values.tolist()
LengthData=len(list_km)

for i in range(0,LengthData):
    list_km[i]=list_km[i][0]
for i in range(0,LengthData):
    list_price[i]=list_price[i][0]
plt.scatter(list_km,list_price) 
plt.xlabel("Mileage Of A car")
plt.ylabel("Price Of A car")
plt.title("The plot of the dataset")
plt.savefig("Scatterplot_01.png")
plt.show()


tetha0=1
tetha1=2


def estimatePrice(mileage):
    return tetha0 + tetha1*mileage