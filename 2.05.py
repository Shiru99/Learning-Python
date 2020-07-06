###################################### ANY & ALL Functions  ##############################################


# ### ALL() fn gives TRUE value if iterable argument for fn contains all TRUE vales       else gives FALSE
# ### ANY() fn gives TRUE value if     "      "       "   "    "   atleast 1 TRUE value   else gives FALSE
 
# nums = [2,4,6,8,10]
# num1 = [2,4,6,9,10]
# num2 = [1,3,5,7,9 ]


# print( all([ i%2 == 0 for i in nums]) ) 
# print( all([ i%2 == 0 for i in num1]) ) 

# print( any([ i%2 == 0 for i in num1]) ) 
# print( any([ i%2 == 0 for i in num2]) ) 

######################### USEFUL to check validity of INPUT ###############################

# def sum(*args):
#     if( all( [ (type(i)==int or type(i)==float) for i in args] ) ):                      
#         total = 0                           
#         for num in args:
#             total += num
#         return(total)
#     else:
#         return("Invalid Input")


# print(sum(2,45,68,9))
# print(sum(2,45,68,9.4))
# print(sum(2,45,68,'9'))


##########################################################################################################
##########################################################################################################

###################################### advance MIN & MAX Functions #######################################

# ### basic MIN & MAX Functions 

# nums = [3,5,8,1,9,6,5]
# print(max(nums))
# print(min(nums))


# names = ["John","Doe","Jenny","Ab","AbDevilliers","AbD"]

# # print(min(names))                                              # => gives random element of list

# def fun(string):
#     return(len(string))

# print(min(names , key = fun))
# print(max(names , key = lambda i: len(i)))





# ### min( IO ,key = function )
#                     ### 'IO' => iterable object 
#                     ### 'key =' => fun returning value from each element acc.towhich we have to find max


#########################  Examples :

# students = [
#     {'name' : "John"       , 'score':72  , 'age': 27},
#     {'name' : "Jenny"      , 'score':72  , 'age': 25},
#     {'name' : "Doe Family" , 'score':144 , 'age': 2}
# ]

# print( max(students,key=lambda i: i.get("score")))             # => gives complete dict.
# # print(students[0]["age"])                                    # => 1st ele.'s age
# print( max(students,key=lambda i: i.get("score"))['name'] )
# print( min(students,key=lambda i: i.get("score"))['name'] )    # => gives only one output which 1 is 1st
# print( max(students,key=lambda i: i.get("age"))['name'] )

# students = {
#     'Jenny'        : { 'score':72  , 'age': 27},
#     'John'         : { 'score':72  , 'age': 25},
#     'Doe Family'   : { 'score':144 , 'age': 2 }
# }

# print(max(students, key= lambda it : students[it]['score']))
# print(min(students, key= lambda it : students[it]['score'])) # =>gives only one output which 1 comes 1st


##########################################################################################################
##########################################################################################################

######################################## SORTED Function #################################################

# ### sort method & sorted Functions :

# names = ["John","Doe","Jenny","Ab","AbDevilliers","AbD"]
# nums = [3,5,8,1,9,6,5]

# nums.sort()
# names.sort()

# print(nums)
# print(names)


# namest = ("John","Doe","Jenny","Ab","AbDevilliers","AbD")
# # ### print(namest.sort())                                           # As tuple can't be modified
# print(sorted(namest))                                                ### SORTED fn: create a sorted list

# namess = {"John","Doe","Jenny","Ab","AbDevilliers","AbD"}
# # ### print(namess.sort())                                           # as sets don't have any order
# print(sorted(namess))                                                ### SORTED fn: create a sorted list




#########################  Examples :

# students = [
#     {'name' : "John"       , 'score':72  , 'age': 27},
#     {'name' : "Jenny"      , 'score':72  , 'age': 25},
#     {'name' : "Doe Family" , 'score':144 , 'age': 2}
# ]

# print( sorted( students, key=lambda d: d['age']                    ))   # reverse= False
# print( sorted( students, key=lambda d: d.get('age'),reverse= True  ))
# print(students)


##########################################################################################################
##########################################################################################################

######################################## More about Function #############################################

#########################  DOC strings :  ( used to give importent info about fn ) :

# def add(a,b):
#     '''This fn takes two nums and returns sum of them '''              #  """/''' Messeage """/'''
#     return a+b

# print(add.__doc__)

# print(sum.__doc__)


#########################  Help fn :

# print(help(sum))

##########################################################################################################
##########################################################################################################