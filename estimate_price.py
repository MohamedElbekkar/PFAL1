import tkinter as tk
import pickle
 
 
f = open('myVariables.txt', 'rb')
m_curr , b_curr = pickle.load(f)
f.close()
#print(m_curr , b_curr)
 
root= tk.Tk()
 
canvas1 = tk.Canvas(root, width = 400, height = 300)
canvas1.pack()
 
entry1 = tk.Entry (root) 
canvas1.create_window(200, 140, window=entry1)
 
lbl=tk.Label(root, text="Enter your mileage", fg='black', font=("Helvetica", 26))
lbl.place(x=60, y=50)
root.resizable(0, 0)

def getEstimatePrice ():  
    mileage = entry1.get()
 	  result = m_curr*float(mileage) + b_curr
 	  if result < 0 :
 		      result = 0 #Because the price can't be negative 
   label1 = tk.Label(root, text= result)
   canvas1.create_window(200, 230, window=label1)
 
 
button1 = tk.Button(text='Get the estimated price', command=getEstimatePrice)
canvas1.create_window(200, 180, window=button1)
 
root.mainloop()
