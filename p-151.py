from tkinter import *

root = Tk()
root.configure(background="Red")
root.title("Sales tax application")
root.geometry("500x400")
root.config(bg="white")

lblMonth=Label(root)
lblProfit=Label(root)
maxProfit=Label(root)
minProfit=Label(root)

month=("January","Febuary", "March","April","May","June","July","August","August","September","October","November","December")
profits=(69,420,69420,42069,48930,123,312312,48983,20832938,3203920)

lblMonth["text"]="months"+str(month)
lblProfit["text"]="months"+str(profits)

def maxprofit():
    max_profit = max(profits)
    print(max_profit)

    max_profit_index=profits.index(max_profit)

    print(max_profit_index)

    max_profit_month = month[max_profit_index]
    print(max_profit_month)
    
    maxProfit["text"]="The Maximum profit of "+str(max_profit)+"observed in the month of "+str(max_profit_month)

def minprofit():
    min_profit = min(profits)
    print(min_profit)

    min_profit_index=profits.index(min_profit)

    print(min_profit_index)

    min_profit_month = month[min_profit_index]
    print(min_profit_month)
    
    minProfit["text"]="The Minimum profit of "+str(min_profit)+"observed in the month of "+str(min_profit_month)    
    
    
MaxProfit_btn=Button(root,text="Maximum profit", command=maxprofit)    
MinProfit_btn=Button(root,text="Minimum profit", command=minprofit)    


lblMonth.pack()
lblProfit.pack()
MaxProfit_btn.pack()
maxProfit.pack()
MinProfit_btn.pack()
minProfit.pack()

root.mainloop()