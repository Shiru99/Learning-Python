################## PADDING 

# Padding : space bet. both sides


###########################################################################################################

import tkinter as tk
from tkinter import ttk


win = tk.Tk()

win.title('Loop')

labels = [f"name : ","age : ","mail ID : ","city : " ,"country : ","phone number : "]

for i in range(len(labels)):
    currentLabel = ttk.Label(win,text=labels[i]) 
    currentLabel.grid(row=i,column=0,sticky=tk.W,padx = 40,pady =5) 

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
    currentEntryBox = ttk.Entry(win,width = 16,textvariable = userDict[i])
    currentEntryBox.grid(row = index,column = 1,padx = 30,pady =5)
#                                                            # top-bottom padding is bydefault due to label
    index+=1

def submitAction():
    for i in userDict:
        print(f"{userDict[i].get()}")
    exit()


submitButton = tk.Button(win,text="Submit",command = submitAction)
submitButton.grid(row = index,column = 0,padx = 80,pady =25)
submitButton.configure(foreground = "#ffffff",background = "#000000")

################################################

win.mainloop()


###########################################################################################################
##########################################################################################################