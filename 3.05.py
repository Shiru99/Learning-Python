#!/bin/python3

###########################################     datetime     ############################################

# from datetime import datetime as dt

# print(dt.now())               # ==> 2020-05-09 13:37:45.807528



##########################################################################################################
##############################              OS & shutil module           #################################
##########################################################################################################



# module - python file containing usefull classes & fns by developers

# OS & shutil modules : useful for - file move,... ,extensions,....


###########################################     OS module     ############################################


# import os

# open('0.0.txt','a').close()        # creates file if doesn't exists


# os.mkdir('Movies')               # => creates folder
# #                                # if already exists => FileExistsError: [Errno 17] File exists: 'Movies'

# print(os.path.exists('Movies') )        # => checks such folder exists or not

#################

# if os.path.exists('Movies'):
#     print("already such folder exists.")
# else:
#     os.mkdir('Movies') 

##################


# os.getcwd()                      # => gives current directory
# print(os.getcwd())               # => /home/jerry/🃏 Start/python 0.0


# os.chdir('/home/jerry/🃏 Start') # => changes directory


# print(os.listdir())              # => gives list of directories in this directory
# print(os.listdir('/home/jerry/🃏 Start'))

# to print complete path of all folders & files of current directories

# for item in os.listdir():
#     path = os.path.join(os.getcwd(),item)
#     print(path)

# to print complete path of 'all folders their files' & 'all files' of current directories

# import os

# fileiter = os.walk('/home/jerry/🃏 Start/python 0.0')    # => gives iterator  # walk('path of directory')

# for currentPath, folderNames, fileNames in fileiter:
#     print(f"current path : {currentPath} ")
#     print(f"folders      : {folderNames} ")
#     print(f"files        : {fileNames} \n")


################# makes folder inside folder :

# os.makedirs('Movies/marathi movies')

################# delete folder:

# os.rmdir('Movies')      # deletes only empty folders => OSError: [Errno 39] Directory not empty: 'Movies'
 





###########################################    shutil module   ############################################


# import os
# import shutil

# shutil.rmtree('Movies')     # deletes permanent doesn't even allow recycle bin 


# shutil.copytree('fileHandling','/home/jerry/Documents/advanced filehandling')            # copies folder


# shutil.copy('0.txt','/home/jerry/Documents/new 0.txt')                                   # copies file 


# shutil.move('0.0.txt','/home/jerry/Documents/new 0.0.txt')                               # file moved &
# shutil.move('/home/jerry/Documents/new 0.0.txt','0.0.txt')                               #     renamed


#                                                                             # folder moved & renamed 
# shutil.move('fileHandling','/home/jerry/Documents/advanced Filehandling')                
# shutil.move('/home/jerry/Documents/advanced Filehandling','/home/jerry/🃏 Start/python 0.0/fileHandling')


# # shutil.move('/home/jerry/Documents/advanced Filehandling',os.getcwd() )


############################# Extension :

# for item in os.listdir():
#     if item.endswith('.txt'):                          
#         print(item)

##########################################################################################################
##########################################################################################################