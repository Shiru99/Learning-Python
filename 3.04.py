##########################################################################################################
##############################              File Handling                #################################
##########################################################################################################

#####################################       Read TEXT file           ######################################

# readfile, open fn, read method, seek method, tell method, readline & readlines method, close method

# f = open('0.txt','r')               # => open("path of file","action mode : by Default-'r' ")
#                                     # => open("/home/jerry/🃏 Start/python 0.0/0.txt" , 'r')

# print("------------------------------------------------------------------")
# print(f"cursor position - {f.tell()}")                   # f.tell() : gives cursor position
# print(f.read())
# print(f"cursor position - {f.tell()}") 
# print("------------------------------------------------------------------")


# print(f"cursor position - {f.tell()}") 
# print(f.read(),end='' )                  # nothing has been printed as cusor position is at end position
# print(f"cursor position - {f.tell()}") 
# print("------------------------------------------------------------------")


# print(f"cursor position before seek  - {f.tell()}") 
# f.seek(0)                                   # f.seek(α) : sets cursor position to "α"
# print(f"cursor position after seek   - {f.tell()}") 
# print(f.read())
# print(f"cursor position - {f.tell()}") 
# print("------------------------------------------------------------------")



# for i in range(0,11):
#     print(f.readline() , end='')                # reads : line by line

# print("____________________________________")



# lines = f.readlines()                           # makes list of lines
# # print(lines)

# for line in lines:
#     print(line , end='')

# f.close()





# f = open('0.txt','r')       # => f object can be iterated

# for line in f:
#     print(line , end='')

# f.seek(0)

# for line in f.readlines()[10:16:1]:
#     print(line , end='')


# f.close()


# ## Data discriptors : name (gives name of file) & closed (gives status of file closed/open)

# print(f.name)              # => 0.txt
# print(f.closed)            # open => False


######################### With Block : 

# with open('0.txt','r') as f:
#     data = f.read()
#     print(data)

# print(f.closed)

###########################################################################################################

#####################################       Write Text file          ######################################


# with open('0.0.txt','w') as f:                  # w mode - creates(if not exists) & overrides 
#     f.write("Hello..\n")                        # override - (deletes previous text 1st)
#     f.write("        John Doe,")           


# with open('0.0.txt','a') as f:                  # a mode - creates(if not exists) & append at end of file
#     f.write(" how are you? & how is Jenny ?")  



# with open('0.0.txt','r+') as f:                  # r+ mode - DOESN'T create! with r+ one can read & write
#     f.write("How is the Josh !!")                # overwrites - (overwrites previous text)
#     f.seek(0)
#     data = f.read()
#     f.write(f"\n{data}")

### EOF => f.seek(0) & f.seek(len(f.read())) 

#####################################   Read & Write Text file       ######################################

# with open('0.txt','r') as rf:
#     with open('0.0.txt','w') as wf:
#         data = rf.read()
#         wf.write(data)


######################### Example 1 (Ex.2 => vid.lec.221) :



# with open('fileHandling/q1.txt','r') as rf:                  # Relative path (to the program file)
#     with open('fileHandling/s1.txt','w') as wf:
#         for line in rf.readlines(): 
#             name,salary = line.split(' , ')
#             wf.write(f"salary of {name} is {salary}")


# Actual path :  /home/jerry/🃏 Start/python 0.0/fileHandling/q1.txt

###################################################

# with open('fileHandling/loveStory.txt','r') as rf:
#     print(rf.encoding)                               # => UTF-8
#     print(rf.read())

# ### sometimes(Windows) uniCodeDecodeError occurs then we need to mention encoding as follow :

# with open('fileHandling/loveStory.txt','r',encoding='TF-8' ) as rf:
#     print(rf.encoding) 
#     print(rf.read())


################################################## handling BIG files part-wise :

# with open('fileHandling/kahaani.txt','r') as rf:
#     data = rf.read(100)                                   # reads 100 charactors at a time
#     while len(data)>0:
#         print(data)
#         data = rf.read(100) 

###########################################################################################################
#######################################     CSV files     #################################################

# CSV files : tables 
#               
#             1st row will be headings
#             values can be seperated by '|' or '*' or ','           (','-most common)





################################### Reading CSV-files using csv module & reader fn

# from csv import reader

# with open('fileHandling/0.csv','r') as rf:
#     CSVreader = reader(rf)                       # CSVreader => iterator 
#     # print(CSVreader)                           # => <_csv.reader object at 0x7f8262e37b38>
#     next(CSVreader)                              # iterators runs only Once
#     for row in CSVreader:                      
#         if int(row[3]) > 500:
#             print(f"{row[0]} - {row[1]}")                              



################################### Reading CSV-files using csv module & DictReader class

# from csv import DictReader

# with open('fileHandling/0.csv','r') as rf:
#     CSVreader = DictReader(rf,delimiter=',')             # By Default => delimiter is comma(',') 
#     for row in CSVreader:                       
#         # print(row)                     # OrderedDict : list of tuples of key-value pair
#         print(row['email'])







################################### Writing CSV-files using csv module & writer fn
 
# from csv import writer

# with open('fileHandling/0.0.csv','w',newline='') as wf:   
#     CSVwriter = writer(wf)                                  # CSVwriter => Object

#     # # method 1 : writerow 
#     # CSVwriter.writerow(['name','counrty'])
#     # CSVwriter.writerow(['John','Unknown country'])
#     # CSVwriter.writerow(['Jenny','Unknown country'])
#     # CSVwriter.writerow(['James','Unknown country'])

#     # method 2 : writerows
#     CSVwriter.writerows([['name','counrty'],['John','Unknown country'],['Jenny','Unknown country']])


################################### Writing CSV-files using csv module & DictWriter class

# from csv import DictWriter

# with open('fileHandling/0.0.csv','w',newline='') as wf:

#     CSVwriter = DictWriter(wf,fieldnames=['firstName','lastName','age']) # fieldnames => Headers
#     CSVwriter.writeheader()                                                 # writes headers
    
#     # # method 1 : writerow 
#     # CSVwriter.writerow({
#     #        'firstName':'John',
#     #        'lastName':'Doe',
#     #        'age':30
#     #     })
#     # CSVwriter.writerow({
#     #        'firstName':'Jenny',
#     #        'lastName':'Doe',
#     #        'age':28
#     #     })
#     # CSVwriter.writerow({
#     #        'firstName':'James',
#     #        'lastName':'Doe',
#     #        'age':2
#     #     })

#     # method 2 : writerows 
#     CSVwriter.writerows([
#         {'firstName':'John','lastName':'Doe','age':30},
#         {'firstName':'Jenny','lastName':'Doe','age':28},
#         {'firstName':'James','lastName':'Doe','age':2}
#     ])





################################### Read & Write CSV files simultaneously

# from csv import DictReader,DictWriter

# with open('fileHandling/0.csv','r') as rf:
#     with open('fileHandling/0.0.csv','w',newline='') as wf:
#         CSVreader = DictReader(rf)
#         CSVwriter = DictWriter(wf,fieldnames=['Name','Email-ID','age'])        # age column will be Empty
#         CSVwriter.writeheader()
#         for row in CSVreader:
#             Name , Email = row['name'] , row['email']
#             CSVwriter.writerow( {'Name':Name.title(),'Email-ID':Email} )



##########################################################################################################
##########################################################################################################


###########################################################################################################
#                                                                                                         #
# NOTE : path in linux/mac => uses '/'                                                                    #
#                windows => uses '\' => use  f = open(r"\home\jerry\🃏 Start\python 0.0\0.txt" , 'r')     #
#                                                                                                         #
###########################################################################################################