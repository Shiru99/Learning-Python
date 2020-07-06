
############## Notebook & tabbed control widget :
#  

###########################################################################################################


import tkinter as tk
from tkinter import ttk


win = tk.Tk()
win.title(' 米＾_＾米     Notebook    米＾_＾米 ')



nb = ttk.Notebook(win)
page1 = ttk.Frame(nb)
page2 = ttk.Frame(nb)


nb.add(page1,text="page no.1")
nb.add(page2,text="page no.2")

# nb.grid(row = 0,column = 0)          # => notebook takes only that much size as widget in it 

nb.pack(expand = True,fill='both')     # NB takes all space not used in widget's parent
#                                      # fill => None(Default),X-Horizontally,Y-vertically,both

############ page1

labels = [f"name : ","age : ","mail ID : ","city : " ,"country : ","phone number : "]

for i in range(len(labels)):
    currentLabel = ttk.Label(page1,text=labels[i]) 
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
    currentEntryBox = ttk.Entry(page1,width = 16,textvariable = userDict[i])
    currentEntryBox.grid(row = index,column = 1,padx = 30,pady =5)
    index+=1


############ page2

labels = [f"name : ","phone number : ","age : ","mail ID : ","city : " ,"country : "]

for i in range(len(labels)):
    currentLabel = ttk.Label(page2,text=labels[i]) 
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
    currentEntryBox = ttk.Entry(page2,width = 16,textvariable = userDict[i])
    currentEntryBox.grid(row = index,column = 1,padx = 30,pady =5)
    index+=1


################################################

def submitAction():
    for i in userDict:
        print(f"{userDict[i].get()}")
    exit()

submitButton = tk.Button(page1,text="Submit",command = submitAction)
submitButton.grid(row = index,column = 0,padx = 80,pady =10)
submitButton.configure(foreground = "#ffffff",background = "#000000")

submitButton = tk.Button(page2,text="Submit",command = submitAction)
submitButton.grid(row = index,column = 0,padx = 80,pady =10)
submitButton.configure(foreground = "#ffffff",background = "#000000")

################################################

win.mainloop()


###########################################################################################################
##########################################################################################################