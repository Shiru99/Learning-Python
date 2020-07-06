
############## LABEL FRAME 

###########################################################################################################

import tkinter as tk
from tkinter import ttk


win = tk.Tk()

win.title(' 米＾_＾米     Label Frame     米＾_＾米 ')

labelFrame = ttk.LabelFrame(win,text="   please Enter your details here !   ")
labelFrame.grid(row = 0,column = 0,padx = 40,pady = 30)





labels = [f"name : ","age : ","mail ID : ","city : " ,"country : ","phone number : "]

for i in range(len(labels)):
    currentLabel = ttk.Label(labelFrame,text=labels[i]) 
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
    currentEntryBox = ttk.Entry(labelFrame,width = 16,textvariable = userDict[i])
    currentEntryBox.grid(row = index,column = 1)
    index+=1

################## padding using winfo_children => for adding padding to each element of label frame

for child in labelFrame.winfo_children():
    child.grid_configure(padx=35,pady=5)



################################################

def submitAction():
    for i in userDict:
        print(f"{userDict[i].get()}")
    exit()

submitButton = tk.Button(win,text="Submit",command = submitAction)
submitButton.grid(row = 1,column = 0,padx = 80,pady =10)
submitButton.configure(foreground = "#ffffff",background = "#000000")

################################################

win.mainloop()


###########################################################################################################
##########################################################################################################