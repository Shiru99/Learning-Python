##########################################################################################################
##########################################################################################################

######################################## Decorators Function #############################################

#########################  diff names of fn :

# def sqr(a):
#     return a*a

# square = sqr

# print(sqr(7))
# print(square(7))

# print(square)         ### => <function sqr at 0x7fbeac4cd1e0> name of fn is "sqr" only
# print(sqr)            ### => <function sqr at 0x7fbeac4cd1e0>

# ### it just shows same fn with diff name both have same memory location

###################################   passing fn in other fn :

# ### Inbuilt Map fn:

# def sqr(a):
#     return a*a

# nums = list(range(1,6))

# print(list(map(sqr,nums)))


#########################

# def sqr(a):
#     return a*a

# nums = list(range(1,6))

# # def my_map( fun , l ):
# #     squares = []
# #     for i in l:
# #         squares.append( fun(i))
# #     return squares

# def my_map( fun , l ):
#     return [fun(i) for i in l]

# print(my_map(sqr,nums))
# print(my_map(lambda a:a**3 ,nums))


###################################  fn returning fn (Closures / 1st class fn):

# def outerFun(msg):
#     def innerFun():
#         print(f"message is {msg}")
#     return(innerFun)                             # to return fn from fn one need to define returing fn

# wow = outerFun("Holiday.!!!!")

# wow()                                            # output => message is Holiday.!!!!

#########################  Example :

# def toPower(x):
#     def calPower(n):
#         return n**x
#     return calPower

# square = toPower(2)
# cube   = toPower(3)

# print(square(5))
# print(cube(5))



##########################################################################################################
##########################################################################################################

######################################## Decorators INTRO  ###############################################

#########################  : enhances the funtionality of other fn

# def decoratorsFun(fun):
#     def wrapperFun():
#         print("This is awesome.")
#         fun()
#     return wrapperFun

# def fun1():
#     print("     this is 'fun1' .")

# def fun2():
#     print("     this is 'fun2' .")

# dfun1 = decoratorsFun(fun1)
# dfun1()

# dfun1 = decoratorsFun(fun2)
# dfun1()

# fun1 = decoratorsFun(fun1)
# fun1()

######################### SHORTCUT => @ use for decorator :

# def decoratorsFun(fun):
#     def wrapperFun():
#         print("This is Beginning..!! ")
#         fun()
#         print("This is Ending..!! ")
#     return wrapperFun

# @decoratorsFun
# def fun1():
#     print("     this is 'fun1' :")

# @decoratorsFun
# def fun2():
#     print("     this is 'fun2' .")


# fun1()
# print()
# fun2()

######################### more about decorator :

# def decoratorsFun(fun):
#     def wrapperFun():
#         print("This is Beginning..!! ")
#         fun()
#         print("This is Ending..!! ")
#     return wrapperFun

# @decoratorsFun
# def fun1(a):
#     print(f"     this is 'fun1' with input : {a} .")

# ### fun1('Yesss..!') => ERROR TypeError: wrapperFun() takes 0 positional arguments but 1 was given

####################:

# def decoratorsFun(fun):
#     def wrapperFun(*args,**kwargs):
#         """ this is Wrapper fn """
#         print("This is Beginning..!! ")
#         return fun(*args,**kwargs)
#     return wrapperFun

# @decoratorsFun
# def fun1(a,b):
#     """ this is mutiplication fn """
#     print(f"     this is 'fun1' with input : {a},{b} .")
#     return a*b

# print(fun1(11,9))
# print(fun1.__doc__)           # =>  this is Wrapper fn 

############## how to get it??

# from functools import wraps                      ###

# def decoratorsFun(fun):
#     @wraps(fun)                                  ###
#     def wrapperFun(*args,**kwargs):
#         """ this is Wrapper fn """
#         print("This is Beginning..!! ")
#         return fun(*args,**kwargs)
#     return wrapperFun

# @decoratorsFun
# def fun1(a,b):
#     """ this is mutiplication fn """
#     print(f"     this is 'fun1' with input : {a},{b} .")
#     return a*b

# print(fun1.__doc__)           # => this is mutiplication fn 


######################### Example :

# # from functools import wraps

# def decoratorsFun(fun):
#     # @wraps(fun)
#     def wrapper(*args,**kwargs):
#         """this wrapper fn"""
#         print(f"u r calling '{fun.__name__}' function.")
#         print(fun.__doc__)
#         print("so use this great function.")
#         return fun(*args,**kwargs)
#     return wrapper

# @decoratorsFun
# def add(a,b):
#     '''this fn takes two int & returns their sum. '''
#     return a+b

# print(add(45,54))



######################### Exercise decorator (calculateTime):
# import time

# def calculateTime(fun):
#     def wrapper(*args,**kwargs):
#         t1 = time.time()                                                  # time at this pos. in seconds
#         returenedValue = fun(*args,**kwargs)
#         t2 = time.time() 
#         print(f"time taken by this fun is : {t2-t1}")
#         return returenedValue
#     return wrapper

# @calculateTime
# def func(x):
#     return [i**3 for i in range(1,x+1)]

# print(func(10))

######################### Exercise decorator:
# from functools import wraps 

# def validityfn(fun):
#     @wraps(fun)
#     def wrapper(*args,**kwargs):
#         if all([type(arg) == int   for arg in args]):
#             return fun(*args,**kwargs)
#         return "Invalid Input"
#     return wrapper

# @validityfn
# def summation(*args):
#     summ = 0
#     for arg in args:
#         summ += arg 
#     return summ


# print(summation(1,2,4,5,7,8,9,[1,2,3],11,23,45,4,6))
# print(summation(1,2,4,5,7,8,9))


#########################  decorator with ARGUMENT :

# from functools import wraps

# def decodecorator(dataType):
#     def decorator(fun):
#         @wraps(fun)
#         def wrapper(*args,**kwargs):
#             if all([type(arg) == dataType for arg in args]):
#                 return fun(*args,**kwargs)
#             return "Invalid Input"
#         return wrapper
#     return decorator

# @decodecorator(str)
# def stingjoin(*args):
#     st = ''
#     for i in args:
#         st += i
#     return st

# @decodecorator(int)
# def summation(*args):
#     summ = 0
#     for arg in args:
#         summ += arg 
#     return summ

# print(stingjoin("ABCDE",'fghij',"KLMNO",'pqrst',"UVWXY","z"))
# print(stingjoin("abcd",11,33,"efgh",'IJ'))


# print(summation(1,2,4,5,7,8,9))
# print(summation(1,2,4,5,7,8,9,[1,2,3],11,23,45,4,6))

##########################################################################################################
##########################################################################################################

######################### GENERATORS :

 
# l = [1,2,3]          # iterable

# i = iter(l)          # iterator
# print(next(i))
# print(next(i))
# print(next(i))

# ### print(next(l))   => ERROR : next fn works only on iterators
# for loop works on iterator if we pass iterable then for loop converts it 1st in iterator. 

# for i in map(lambda a: a**2,l ):            # iterator
#     print(i)



##########################################################################################################
##########################################################################################################
##############        genetetors are sequences like lists but they are iterators             #############
###                                                                                                    ###
###                                                                                                    ###
###    list consumes as much memory as much elments*theirMemory                                        ###
###    list are better if we want to use sequence multiple times                                       ###
###                                                                                                    ###
###                                                                                                    ###
###    generators generates 1 element at a time so consumes memory as that of element at that instant  ###
###    generators are better if we want to use sequence only once                                      ###
###                                                                                                    ###
###                                                                                                    ###
##########################################################################################################
##########################################################################################################

######################### creating GENERATORS using generator fn :


# def nums(a):
#     for i in range(1,a+1):
#         yield i                           # yield(i)  => yiels - keyword 

# numbers = nums(4)                         # generator
# print(numbers)                            # => <generator object nums at 0x7f47e05f2480>

# for i in numbers:
#     print(i)                              # as print required i generator gives it and creates new one  
# print()

# for i in numbers:                         # no output as their is no elemant inside numbers
#     print(i)                                  
# print()

# ### BUT 

# for i in nums(6):
#     print(i)
# print()

# for i in nums(6):                        # this will get printed again as u call nums(X) it creates obj.
#     print(i)




##################### Example generator :

# # def evenGenerator(n):
# #     for i in range(1,n+1):
# #         if i%2 == 0:
# #             yield i 

# def evenGenerator(n):
#     for i in range(2,n+1,2):
#         yield i 


# evenNums = evenGenerator(11)

# for num in evenNums:
#     print(num)


##########################################################################################################

######################### creating GENERATORS using generator comprehension :

# l = [i**2 for i in range(1,5)]
# print(l)
# print()


# g = (i**2 for i in range(1,5))
# # print(g)                          # => <generator object <genexpr> at 0x7f9102b69480>

# for sqr in g :
#     print(sqr)

# for sqr in g :
#     print(sqr)                      # no output




##########################################################################################################
##############                            list vs genetetor                                  #############
##########################################################################################################
###                                                                                                    ###
###    calculated using task manager :                                                                 ###
###                                                                                                    ###
###    l = [i**2 for i in range(1,10000000)]  # 10M squares ( space => nearly 400 Mb)                  ###
###    g = (i**2 for i in range(1,10000000))  # 10M squares ( space => nearly 0Kb                      ###
###                                                                                                    ###

# import time                                                                                          ###

# t1 = time.time()                                                                                     ###
# l = [i**2 for i in range(1,10000000)]                                                                ###
# t2 = time.time()                                                                                     ###

# a = 0                                                                                                ###
# for t in l:                                                                                          ###
    # a+=1                                                                                             ###
# t3 = time.time()                                                                                     ###

# t4 = time.time()                                                                                     ###
# g = (i**2 for i in range(1,10000000))                                                                ###
# t5 = time.time()                                                                                     ###

# a = 0                                                                                                ###
# for t in g:                                                                                          ###
    # a+=1                                                                                             ###
# t6 = time.time()                                                                                     ###

# print(f"Time taken by list   : {t2 - t1}   &   Time taken by generator  : {t5 - t4} "     )          ###
# print(f"somthing about list  : {t3 - t2}   &   somthing about generator : {t6 - t5} "     )          ###

###                                                                                                    ###
##########################################################################################################
##########################################################################################################




##########################################################################################################
##########################################################################################################