
############## Message Box & Exception handlinng :
#  

###########################################################################################################

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mBox



win = tk.Tk()

win.title(' 米＾_＾米     Message Box     米＾_＾米 ')

labelFrame = ttk.LabelFrame(win,text="   please Enter your details here !   ")
labelFrame.grid(row = 0,column = 0,padx = 40,pady = 30)





labels = [f"name : ","Mobile No. : "]

Label1 = ttk.Label(labelFrame,text="Name : ",font = ('Helvetica',14,'bold')) 
Label1.grid(row=0,column=0,sticky=tk.W)              # Helvetica => font family

Label2 = ttk.Label(labelFrame,text="Mobile No. : ",font = ('Helvetica',14,'bold')) 
Label2.grid(row=0,column=1,sticky=tk.E) 

namestored = tk.StringVar()
nameInput = ttk.Entry(labelFrame,width = 16,textvariable = namestored)
nameInput.grid(row = 1,column = 0)

Mobilestored= tk.StringVar()
MobileInput = ttk.Entry(labelFrame,width = 16,textvariable = Mobilestored)
MobileInput.grid(row = 1,column = 1)

################## padding using winfo_children => for adding padding to each element of label frame

for child in labelFrame.winfo_children():
    child.grid_configure(padx=35,pady=5)



################################################

def submitAction():
    # mBox.showinfo('Title','Content of this message box is ...!! ')
    name = namestored.get()
    Mobile = Mobilestored.get()
    if name == "" or Mobile == "":
        mBox.showerror('Warning',"fields Can't be Empty" )
    else:
        try:
            Mobile = int(Mobile)
        except ValueError:
            mBox.showerror('Error',"Mobile number must contain digits only" )
        else:
            mBox.showinfo('Confirmed','Submitted Successfully ')
            print(f"{name} : {Mobile}")
    exit()

submitButton = tk.Button(win,text="Submit",command = submitAction)
submitButton.grid(row = 1,column = 0,padx = 80,pady =10)
submitButton.configure(foreground = "#ffffff",background = "#000000")

################################################

win.mainloop()


###########################################################################################################
##########################################################################################################