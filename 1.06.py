#!/bin/python3
##########################################################################################################
#                                      ### List ###

# mixed = [ 1, 2, 3,"four", "five", 6.0, 7.0, None, True, False ]
# print(mixed)
# print(mixed[3] , mixed[7],sep="     ", end="\n")
# print(mixed[0:6])                                          # Slicing
# print(mixed[:0:-1])  



# mixed = [ 1, 2, 3,"four", "five", 6.0, 7.0, None, True, False ]
# mixed[1] = "TWO" 
# print(mixed)

# mixed[2:] = [3.0,4.0,5.0,"SIX"]              
# print(mixed)

# mixed[2:] = "abc"               # Replaces all after pos.1 with a,b,c *AS "abc" - ('a','b','c')
# print(mixed)


##########################################################################################################
#                                      ### Append/Add ###


# fruits = []

# print(fruits)
# fruits.append("Mango")                                           # append method :  adds at end of list 
# fruits.append("Apple")
# fruits.append("Grapes")
# print(fruits)

# fruits.insert(1,"Orange")
# print(fruits)                # insert method : shifts remaining list by placing things at given position


##########################################################################################################
#                                      ### Concatenate ###

# fr1 = ["Mango","Orange"]
# fr2 = ["Grapes","Apple"]

# Fruits =  fr1+fr2
# print(Fruits)

##########################################################################################################
#                                          ### Extend ###

# fr1 = ["Mango","Orange"]
# fr2 = ["Grapes","Apple"]

# fr1.extend(fr2)
# print(fr1)
# print(fr2)

# fr1.append(fr2)                                                      # complete list gets added as it is !
# print(fr1)
# print(fr2)

# nums = [1,4,6,8,9]
# print(nums.extend([100,200,300]))
# print(nums)

##########################################################################################################
#                                      ### Delete => POP && REMOVE ###

# Fruits = ['Mango', 'banana', 'Orange', 'Grapes', 'Apple','banana', 'banana', 'banana', 'Anjeer']
        
# print(Fruits.pop())                        # by default removes last element by returning it 
# print(Fruits)

# Fruits.pop(1)
# print(Fruits)        #   <-::::
# #                             ::::-> both are Same  but del is a OPERATOR *and must require aregument
# del Fruits[1]        #   <-::::
# print(Fruits)     
#                    # print( del Fruits[1]) => ERROR


################################ Problem with REMOVE #####################################################

# Fruits = ['Mango', 'banana', 'Orange', 'Grapes', 'Apple','banana', 'banana', 'banana', 'Anjeer']

# Fruits.remove("banana")            # removes only ONCE
# print(Fruits)

# Fruits.remove("Cake")            # ERROR


#         # remove  works only if element is available in list otherwise shows ERROR
##########################################################################################################
#                                      ### IN ###

# Fruits = ['Mango', 'banana', 'Orange', 'Grapes', 'Apple','banana', 'banana', 'banana', 'Anjeer']

# if "mango" in Fruits:
#     print("'Mango' is available.")
# else:
#     print("'mango' is NOT available.")

##########################################################################################################
#                              ### MIN && MAX "FUNCTIONS"of list ###

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# print(min(nums))
# print(max(nums))
# print(sum(nums))

##########################################################################################################
#                                    ### SOME METHODS ###
#                        COUNT / SORT / SORT(fn) / REVERSE /CLEAR / COPY

######################## COPY ###################################

# Fruits = ['Mango', 'Banana', 'Orange', 'Grapes', 'Apple','Banana', 'banana', 'banana', 'Anjeer']

# fruits1 = []
# print(fruits1)

# fruits1 = Fruits                                  # Same memory location (just something like diff. names)
# print(fruits1)                                   

# Fruits_Copy = Fruits.copy()                       # copy with diff name & mem. location
# print(Fruits_Copy)

#################### COUNT #######################################

# Fruits = ['Mango', 'Banana', 'Orange', 'Grapes', 'Apple','banana', 'banana', 'banana', 'Anjeer']

# print(Fruits.count("banana"))
# print(Fruits.count("mango"))

###################### SORT #####################################

# Fruits = ['Mango', 'Banana', 'Orange', 'Grapes', 'Apple','banana', 'banana', 'banana', 'Anjeer']

# Fruits.sort()                             # sorts the list
# print(Fruits)                             # capital letter have high priority A-Z >> a-z

# num = [16,45,7,34,89,10,85,23,79,57,92,14]
# num.sort()
# print(num)

###################### SORTED Fn #####################################

# num = [16,45,7,34,89,10,85,23,79,57,92,14]
# print(num)
# print(sorted(num))                          # doesn't make changes in the list ONLY gives Sorted OUTPUT
# print(num)
 
#################### CLEAR #######################################

# num = [16,45,7,34,89,10,85,23,79,57,92,14]

# print(num)
# num.clear()                                 # clears the list
# print(num)

######################## Split ###################################

# userInfo = "john doe 54 45000 Audi"

# userInfoMod = userInfo.split()                # s String to LIST
# print(userInfoMod)                            # by Default split() =>  " "

# userInfo1 = "john,doe,54,45000,Audi"
# userInfo1Mod = userInfo1.split(",")
# print(userInfo1Mod) 

# name , surname , age , income , car = "john , doe,     54,45000,Audi".split(",")

# #name , surname , age , income , car = input("Enter ur name, surname, age, income, car : ").split(",")

# print(name)
# print(age)
# print(car)

####################### Split only n-times ####################################

# s = "aaaabaaabaabaaabbbb"
# print(s.split('b', 2))      # 2 ==> two times 


####################### Join ####################################


# userInfo = ["John" , "Doe", "27" , "$999"]
# print("|".join(userInfo))                  # join joins the list elements(must be strings) to a STRING 

# me = "my name John Doe"
# splitList = me.split()
# print(splitList)
# print(" ".join(splitList)) 



##########################################################################################################
##########################################################################################################

#                                  ### Loop in list ###

# Fruits = ['Mango', 'Banana', 'Orange', 'Grapes', 'Apple', 'Anjeer']
# print(type(Fruits))

# ### FOR loop:

# for fruit in Fruits:
#     print(fruit)

# ### WHILE loop:

# i=0
# while i< len(Fruits):
#     print(Fruits[i])
#     i+=1

##########################################################################################################
#                                  ### List in list => 2D-List ###

# matrix = [[1,2,3],['a','b','c'],['A','B','C']]
# print(type(matrix))

# print(matrix)

# for sublist in matrix:
#     print(sublist) 


# for sublist in matrix:
#     for elements in sublist:
#         print(elements)

# print(matrix[2][2])


##########################################################################################################
#                                  ### Making list using RANGE ###

# num = list(range(1,21))
# print(num)

#                                  ### INDEX in list ###

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,7,7]

# print(nums.index(7))             ## => gives 1st position of matching

# print(nums.index(7,10))          ## => gives position of 1st matching after 10th position
# print(nums.index(7,10,20))     ## => gives position of 1st matching after 10th pos. b4 20th pos. if 
#                                ##    present else shows ERROR
 
##########################################################################################################
#                                  ### passing List in fn ###

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# def negNums(l):
#     negative = []
#     for element in l:
#         negative.append(-element)
#     return negative

# print(negNums(nums))

################### NOTE  ### Reverse Methods : reverses original list ###

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# revNums = nums.reverse()
# print(revNums)                   ## => Empty list    ==>         # print(nums.reverse())  => gives None 
# print(nums)                      ## => d list

# print(num[::-1])                 ##  REVERSE


# def reverseNums(l):
#     rev_l = []
#     for ele in range(len(l)):
#         rev_l.append(l.pop())
#     return rev_l

# print(reverseNums(nums))


##########################################################################################################

# ### EXAMPLES

## 1)

# names = ["alpha","beta","gamma"]

# def reverseElements(l):
#     reversedL = []
#     for i in l:
#         reversedL.append(i[::-1])
#     return reversedL

# print(reverseElements(names))

################################################## IS or == ########################################### 

# fr1 = ["Mango","Orange"]
# fr2 = ["Mango","Orange"]
# fr3 = ["Grapes","Apple"]
# fr4 = fr1

# print(fr1 == fr2)               # == checks Are both equal or Not
# # print(fr1 == fr3)

# print(fr1 is fr2)               # is checks whether fr1 & fr2 consumes same memory locations or NOT
# print(fr1 is fr4)  

##########################################################################################################
#                                  ### list vs array & String ###

# # list - any datatype                but        # array - samedatatype 
# # lists are mutable                  but        # strings are immutable

##########################################################################################################

##################################################################
##################################################################
#############  NOTE                               ################
##############                                  ##################
############      fn:                                     ########
##########          even = []                          ###########
##########          odd = []                            ##########
###########         output = [odd , even]                #########
########            return output                     ############
#############                                     ################
##################################################################
##################################################################


############################ TYPE ####################################################################
###                                                                                                ###
###    Fruits = ['Mango', 'Banana', 'Orange', 'Grapes', 'Apple', 'Anjeer']                         ###
###    print(type(Fruits))                                                                         ###
###                                                                                                ###
###    ###      if type(days) == list:                                                             ### 
###                                                                                                ###
######################################################################################################

######################  MORE about PRINT() ###############################################################
###                                                                                                    ###
###           # for i in range(1,10,2):                                                                ###
###           #     print(i,end = " ")                                                                 ###
###                                                                                                    ###
###                                                                                                    ###
###           # mixed = [ 1, 2, 3,"four", "five", 6.0, 7.0, None, True, False ]                        ###
###           # print(mixed[3] , mixed[7],sep="     ", end="\n")                                       ###
###                                                                                                    ###
##########################################################################################################

###################### Slicing ###########################################################################
###                                                                                                    ###
###         name = "John Doe"                                                                          ###
###                           #                [ start argu.   :   stop argu.   :  step(Default = 1) ] ###
###   print(name[::1])        # if step > 0 => [ Default =  0  :  next of last  :      POSITIVE      ] ###
###   print(name[::-1])       # if step < 0 => [ Default = -1  :  pre. of 1st   :      NEGATIVE      ] ###
###                                                                                                    ###
##########################################################################################################

##########################################################################################################