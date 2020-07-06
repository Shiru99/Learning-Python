##########################################################################################################
#
#                                   ### SOME OPERATORS ###           
#               
#########################################################################################################

#                  ### intro to *args / * operator   ###    make flexible fns ###

# ### *args as Argument

# def sum(a,b):
#     return(a+b)

# print(sum(2,4))
# ### print(sum(2,4,6))                    # => ERROR 

 
# def sum(*args):                            # *args is convention but one can use anything - *anything
#     total = 0                              # type(args) is  tuple
#     for num in args:
#         total += num
#     return(total)



# print(sum())                       # => no arguments still OK 
# print(sum(2,4,6,9))
# print(sum(1,10,100,1000,10000,100000))



##########################################################################################################

# ### *args with normal parameter


# def multiply(num1,*args):                   # 1st num get stored in num1 & remaining get stored in TUPLE
#     total = num1                            # type(num1) is int  &  type(args) is tuple 
#     for num in args:
#         total *= num
#     return(total)


# # ### print(multiply())                       #  no arguments => ERROR 
# print(multiply(2,4,6,9))
# print(multiply(1,10,100,1000,10000,100000))


# ### multiply(*args ,num1)    => ERROR

##########################################################################################################

# ### *args as Argument


# def multiply(*args):                     # 1st num get stored in num1 & remaining get stored in TUPLE
#     total = 2                            # type(num1) is int  &  type(args) is tuple 
#     for num in args:
#         total *= num
#     return(total)


# l = [1,10,100,1000,10000,100000]            
# print(multiply(l))                          # => output : [1, 10, 100, 1000, 10000, 100000]*2
# print(multiply(*l))                         # gets UNPACKED

# t = (1,10,100,1000,10000,100000)
# print(multiply(t))
# print(multiply(*t))                         # gets UNPACKED


# s = { 1,10,100,1000,10000,100000 }
# print(multiply(*s))                           # gets UNPACKED
# ### print(multiply(s))                      => ERROR set can't be multiplied


##########################################################################################################

# ### Exercise




# l = []

# if not l:                                                # also len(l) > 0
#     print("list is Empty")






# def powerOf(power,*nums):
#     if not nums:
#         return("Your list is Empty")
#     else:
#         return [num**power for num in nums]

# l = [2,3,56,78,90]
# index = 4
# print(powerOf(index,*l))
# #                                    ## OR ##
# nums = [2,3,56,78,90]
# power = 4                                                # NO error
# print(powerOf(power,*nums))





##########################################################################################################
##########################################################################################################
##########################################################################################################

#                  ### KWARGS - keyword arguments : **kwargs(double star operator)  ###


# ### qwargs as Argument

# def fun(**kwargs):                        # **kwargs is convention but one can use anything - **anything
#     for k,v in kwargs.items():            # type(kwargs) is  dict (dictionary)
#         print(f"for key {k} : value is {v} ")                                  

# fun(firstName = "John" , lastName = "Doe")
# print()



# d = {'name' : "John" , 'age' : 27 , 'fav.player' : "DHONI"}

# fun(**d)      ### Dictionary unpacking





# def fun(name,**kwargs):
#     print(name)                    
#     for k,v in kwargs.items():            
#         print(f" {k} => {v} ")                                  

# fun("Doe Family member",firstName = "John" , lastName = "Doe")
# print()




##########################################################################################################


######################  fun with all parameters ##########################################################
###                                                                                                    ###
###    ### def function (normal parameters , *args , default parameters , **kwargs ):                  ###
###                                                                                                    ###
###        ##  Order must be followed to avoid ERRORS                                                  ###
###                                                                                                    ###
##########################################################################################################

# def fun(name , *args , surname = "Unknown" , **kwargs):
#     print(name)
#     print(args)
#     print(surname)
#     print(kwargs)

# fun ("John" , 2,4,6,8, a = "Ronda" , b = "Rousey")


##########################################################################################################

### Example :


# def fun(l,**kwargs):
#     if kwargs.get("reversenames"):                        # true => will enter the if block 
#         return [name[::-1].title() for name in l ]
#     else :
#         return [name.title() for name in l ]              # Doesn't remove extra spaces (or whiteSpaces)


# names = {"joHN    jEnNy","DoE"}

# print(fun(names))                    
# print(fun(names , reversenames = 'True'))
# print(fun(names , reversenames = True))



##########################################################################################################