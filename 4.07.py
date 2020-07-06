
############## MenuBar :
#  

###########################################################################################################


import tkinter as tk
from tkinter import ttk


win = tk.Tk()
win.title(' 米＾_＾米     MenuBar    米＾_＾米 ')



###########---------Simple menubar-----------  :

# menubar = tk.Menu(win)

# def saveit():
#     print("Saved 🙃 ")

# menubar.add_command(label='save',command = saveit)
# menubar.add_command(label='save as',command = saveit)
# menubar.add_command(label='copy',command = saveit)
# menubar.add_command(label='paste',command = saveit)

# win.config(menu = menubar)

###########---------Extended menubar-----------  :

MainMenubar = tk.Menu(win)

def action():
    pass

#                                                                   # ascade => Adding one by one

####### File Menu :

fileManu = tk.Menu(MainMenubar,tearoff = 0)
MainMenubar.add_cascade(label="File",menu = fileManu)          

fileManu.add_command(label="New File",command = action)
fileManu.add_command(label="New Window",command = action)
fileManu.add_separator()                                            # will seperate menu options
fileManu.add_command(label="Open File",command = action)
fileManu.add_command(label="Open Folder",command = action)

####### File Menu : 

editManu = tk.Menu(MainMenubar,tearoff = 0)      # tearoff : submenu will not come out of main window
#                                                # with tearoff that submenu can be pulled out of main menu
MainMenubar.add_cascade(label="Edit",menu = editManu) 
editManu.add_command(label="New File",command = action)
editManu.add_separator()
editManu.add_command(label="New Window",command = action)
editManu.add_separator()
editManu.add_command(label="Open File",command = action)
editManu.add_separator()
editManu.add_command(label="Open Folder",command = action)


viewManu = tk.Menu(MainMenubar,tearoff = 0)
MainMenubar.add_cascade(label="View",menu = viewManu) 
helpManu = tk.Menu(MainMenubar,tearoff = 0)
MainMenubar.add_cascade(label="Help",menu = helpManu) 

win.config(menu = MainMenubar)

################################################

win.mainloop()


###########################################################################################################
##########################################################################################################