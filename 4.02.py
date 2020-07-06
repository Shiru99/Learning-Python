##########################################################################################################
##############################   'TK-inter' library - Project 米＾_＾米   #################################
##########################################################################################################

# Tkinter library  : useful for - GUI (Graphical User Interface) : 
#               

# Similar Librearies :  WX-python , pycouty  

#######################################    Tkinter library   ##############################################


############  Starter 🙃


# import tkinter     
# root = tkinter.Tk()           # win / window / root (common Names)

# from tkinter import *         # means import all from tkinter lib.            # not preferable
# window = Tk() 



import tkinter as tk  
from tkinter import ttk          # explained later
win = tk.Tk()                    # 'win'object has been created  # Tk() => Class ; calls constructor
win.title("GUI")                 # default title of interface will be "tk"
# win.mainloop()                 # on running program it shows window infinitly otherwise it will blick    #                                # once very fast (so it should be at the end)
 
############  create lable  🙃

# widgets ==> have label,buttons,radio buttons,etc in tk : but their is ttk submodule in tk containing 
#             good looking stuff

nameLable1 = ttk.Label(win,text="Enter your name : ")    #   label class will create label on 'win' but,
#                                                 where should it be (location in window)?


# lable1.pack()                   # it will be centered but still can be moved BUT grid will be more useful
                                               
nameLable1.grid(row=0,column=0,sticky=tk.W)              # Sticky explained later



mailLable1 = ttk.Label(win,text="Enter your mail ID : ") \
# mailLable1.grid(row=0,column=0)                         # it will overwrite
mailLable1.grid(row=1,column=0,sticky=tk.W) 



ageLable1 = ttk.Label(win,text="Enter your age: ") 
ageLable1.grid(row=2,column=0,sticky=tk.W)                          

# nameLable1, mailLable1 & ageLable1 are not alined well !           => sticky=tk.W :: W => West

genderLable1 = ttk.Label(win,text="Enter your gender: ") 
genderLable1.grid(row=3,column=0,sticky=tk.W)   

############  create entry box  🙃

name1Store = tk.StringVar()          # to store the "String"-output by user
nameInputBox = ttk.Entry(win,width = 16,textvariable = name1Store)
nameInputBox.grid(row = 0,column = 1)
nameInputBox.focus()               # need not select; curser, will be set at nameInputBox intially
#                                  # TODO : works for 1st one but how for others

mail1Store = tk.StringVar()          
mailInputBox = ttk.Entry(win,width = 16,textvariable = mail1Store)
mailInputBox.grid(row = 1,column = 1)



age1Store = tk.StringVar()                               #IntVar()    # to store the "Int"-output by user
ageInputBox = ttk.Entry(win,width = 16,textvariable = age1Store)
ageInputBox.grid(row = 2,column = 1)

############  create comboBox 🙃 :

gender1Store = tk.StringVar()  
genderCombobox = ttk.Combobox(win,width = 14,textvariable = gender1Store,state = 'readonly')
genderCombobox['values'] = ("Baby","Male","Female","Other")  # 👶👨👩
genderCombobox.current(0)       # Default value is set as 0th element of "tuple"
genderCombobox.grid(row = 3,column = 1)


############  create Radio button 🙃 :                                # ONLY 1 can be selected

user1Type = tk.StringVar()

radioButtonOpt1 = ttk.Radiobutton(win,text='Student',value='Student',variable = user1Type)
radioButtonOpt1.grid(row=4,column=0)

radioButtonOpt2 = ttk.Radiobutton(win,text='Teacher',value='Teacher',variable = user1Type)
radioButtonOpt2.grid(row=4,column=1)

radioButtonOpt3 = ttk.Radiobutton(win,text='Other',value='Other',variable = user1Type)
radioButtonOpt3.grid(row=4,column=2)
### still USER can enter anydata in combobox => "state" : so user can only select 


############  create Check button 🙃 :  

checkStatus = tk.IntVar()
checkButtonOpt3 = ttk.Checkbutton(win,text='Do you accept our terms & conditions',variable =checkStatus )
checkButtonOpt3.grid(row=5,columnspan = 3)         # Due to large text it disturbing column space of others
#                                                    => columnspace : can take space upto 'n' columns

# TODO : set Default value


##################################### Colouring elements

nameLable1.configure(foreground = "#f2e41d",background = "Black")
mailLable1.configure(foreground = "#f2e41d",background = "Black")
ageLable1.configure(foreground = "#f2e41d",background = "Black")

#### this doen't work for entryboxes,etc for "TTK"  => for it STYLE is need to used
#    tk can work eg. for submit button

# nameInputBox.configure(foreground = "#f2e41d",background = '#eb1515')
# ageInputBox.configure(background = '#eb1515')
# genderCombobox.configure(background = '#eb1515')

###################################

############  create summit button & command 🙃 :

def action():
    userName = name1Store.get()
    userMailID = mail1Store.get()
    userAge = age1Store.get()
    userGender = gender1Store.get()
    userType = user1Type.get()
    userCheckStatus = "No"
    if checkStatus.get():
        userCheckStatus = "YES"     



    ### printing data : 


    # print(f"{userName}'s mail Id - {userMailID}\n{userName}'s Age - {userAge}")
    # print(checkStatus.get())



    ### writing data in TXT file : 

    # with open(f"{userName}.txt",'a') as f:
    #     f.write(f"{userName}\n{userMailID}\n{userAge}\n{userType}\n{userGender}\n{userCheckStatus}\n")



    ### writing data in CSV file : 

    from csv import DictWriter
    import os


    with open(f"UserData.csv",'a') as f:

        dictwriter = DictWriter(f,fieldnames=["User Name","User Mail ID","User Age","User Gender","User Type","User agreed terms and condition"]) 
        if os.stat("UserData.csv").st_size == 0:
            dictwriter.writeheader()

        dictwriter.writerow({
            "User Name" : userName,
            "User Mail ID" : userMailID,
            "User Age" : userAge,
            "User Gender" : userGender,
            "User Type" : userType,
            "User agreed terms and condition" : userCheckStatus
        })


    # NOTE : after submitting once it should get empty for multiple times entries

    nameInputBox.delete(0,tk.END)
    mailInputBox.delete(0,tk.END)
    ageInputBox.delete(0,tk.END)
    
    
    # NOTE : after submitting once it should can be made coloured

    nameLable1.configure(foreground = "Blue",background = "#708a89")
    mailLable1.configure(foreground = "Blue",background = "#708a89")
    ageLable1.configure(foreground = "Blue",background = "#708a89")

    # finish()











# submitButton = ttk.Button(win,text="Submit",command = action) # on submitting command will call fn:action
# submitButton.grid(row = 6,column = 0)
# #                         # As many time u will click submit that many times it will call action function
# #                           but finish will exit the execution
# #                         # if all are not empty

# colored button:  doesn't works with ttk

submitButton = tk.Button(win,text="Submit",command = action)   # on submitting command will call fn:action
submitButton.grid(row = 6,column = 0)
submitButton.configure(foreground = "#ffffff",background = "#000000")











##########################################################################################################

def finish():
    exit()


win.mainloop() 

########################### TODO :
#
#        1. curser need to set everytime in next entryBox : it should be done by Enter-Key
#        may :  nameInputBox.tk_focusNext()
#  
#        2. how to insert EMOJI in tkinter GUI 
#
#
# 
# 
#
###########################################################################################################


########################### NOTE :
#
#   colour : Google => colour picker
# 
# 
#
#
# 
# 
#
###########################################################################################################
##########################################################################################################