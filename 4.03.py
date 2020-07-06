import tkinter as tk
from tkinter import ttk


win = tk.Tk()

win.title('Loop')


############ Time consuming :

# nameLable1 = ttk.Label(win,text="Enter your name : ") 
# nameLable1.grid(row=0,column=0,sticky=tk.W) 

# ageLable1 = ttk.Label(win,text="Enter your age: ") 
# ageLable1.grid(row=1,column=0,sticky=tk.W) 

# countryLable1 = ttk.Label(win,text="Enter your country: ") 
# countryLable1.grid(row=2,column=0,sticky=tk.W)

# mailLable1 = ttk.Label(win,text="Enter your mail ID : ") 
# mailLable1.grid(row=3,column=0,sticky=tk.W) 


############ Loop :


labels = [f"name : ","age : ","mail ID : ","city : " ,"country : ","phone number : "]

for i in range(len(labels)):
    # currentLabel = f"label{i}"                     # without declaring also it will work fine
    currentLabel = ttk.Label(win,text=labels[i]) 
    currentLabel.grid(row=i,column=0,sticky=tk.W) 

userDict = {
    'name':tk.StringVar(),
    'age':tk.StringVar(),
    'mail':tk.StringVar(),
    'city':tk.StringVar(),
    'country':tk.StringVar(),
    'phone':tk.StringVar(),
}

index = 0

for i in userDict:
    # currentEntryBox = f"entry{i}"
    currentEntryBox = ttk.Entry(win,width = 16,textvariable = userDict[i])
    currentEntryBox.grid(row = index,column = 1)
    index+=1

def submitAction():
    for i in userDict:
        # print(f"{userDict[i].get()}")
        print(f"{userDict.get(i).get()}")           # their is get() method in dictionary too
    exit()


submitButton = tk.Button(win,text="Submit",command = submitAction)
submitButton.grid(row = index,column = 0)
submitButton.configure(foreground = "#ffffff",background = "#000000")

################################################

win.mainloop()


###########################################################################################################
##########################################################################################################