##########################################################################################################
##############                                  Errors                                       #############
##########################################################################################################

### Syntex Error:

### Indentation Error:

### Name variable : when 1 uses undefined variable

        # x = 2
        # print(x,y)               =>  # NameError: name 'y' is not defined

### Type Error :

        # x = 2
        # print(2+"John")          => TypeError: unsupported operand type(s) for +: 'int' and 'str'       

### Index Error :

        # l = [1,2,3]
        # print(l[5])              =>  IndexError: list index out of range  

### Value Error :

        # s = "five"
        # print(int(s))            => ValueError: invalid literal for int() with base 10: 'five' 

### Attribute Error :
                              
        # l = [1,2,3]                                       # there is no such fn as "Push"
        # l.push(4)                 => AttributeError: 'list' object has no attribute 'push'

### Key Error : 

        # d = {'name' : "John"}
        # print(d['age'])           => KeyError: 'age'

### ZeroDivisionError : 

        # division by Zero

########################################   Raise Error     ###############################################

# def add(a,b):
#     if (type(a) is int) and (type(b) is int):
#         return a+b
#     raise TypeError("OOPs u hv entered data with inappropriate datatypes")
        
# print(add('3','66'))

# ### raising error is better than printing it
# #                     as in somecases (databases) it avoids storing these invalid inputs

#########################  Example : 

### Raise error is used to make compulsary to define particular fn in class :


# class Animals:
#     def __init__(self,name):
#         self.name = name
#     # this method called Abstract method in Java 
#     def sound(self):
#         raise NotImplementedError("u have to define Sound fn in every child class of this class")

# class Cat(Animals):
#     def __init__(self,name,bread):
#         super().__init__(name)
#         self.bread = bread


# class Dog(Animals):
#     def __init__(self,name,bread):
#         super().__init__(name)
#         self.bread = bread

#     def sound(self):
#         return "bhow bhow..."


# doggg = Dog('boony','pug')
# cattt = Cat('kit','kat')

# print(doggg.sound())
# print(cattt.sound())


#########################  Example : 

### to allow only smartphone be in Mobilestore:


# class Smartphone:
#     def __init__(self,brand):
#         self.brand = brand

# class Mobilestore:
#     def __init__(self):
#         self.mobiles = []
    
#     def addNewMob(self,newMob):
#         if isinstance(newMob,Smartphone):
#             self.mobiles.append(newMob)
#         else:
#             raise TypeError(f"Sorry, but {newMob} is Not a SmartPhone .!!!")


# oneplus = Smartphone('one plus 7T-pro')

# mobileShowRoomofPBN = Mobilestore()
# mobileShowRoomofPBN.addNewMob(oneplus)

# # mobileShowRoomofPBN.addNewMob('NOKIA 8.1')
# print(mobileShowRoomofPBN.mobiles[0].brand)


##########################################################################################################


########################################  Exception handling #############################################

## when we are wishing not to stop our running program due to small error


########################## try except :

# # age = int(input("Enter ur age :"))             # seven => ERROR

# while True:
#     try:
#         age = int(input("Enter ur age :"))           # if error occurs it will reach except block
#         break
#     except ValueError :                              # no need to mention type of error
#         print("Invalid input (Value Error), Try Again")
#     except:
#         print("Unexpected Error")


# if age >= 18:
#     print("ur Eligible")

# else:
#     print("Sorry ur NOT eligible.")


########################## try except Else & Finally :

# while True:
#     try:
#         age = int(input("Enter ur age :"))           # if No Error => will reach to else block
#     except ValueError :                              # no need to mention type of error
#         print("Invalid input (Value Error), Try Again")
#     except:
#         print("Unexpected Error")
#     else:
#         print(f"user input : {age}")
#         break
#     finally:                                             
#         print("finally block always runs unconditionally.")   # useful for databases


## Example:
 
# def divide(a,b):
#     try :
#         return a/b
#     except ZeroDivisionError as err:
#         print(f"ERROR : {err}")
#     except TypeError as err:
#         print(f"ERROR : {err}")
#     except :
#         print("unexpected Error")

# print(divide(10,0))

#########################  Custom exceptions :

# class NameTooShortError(ValueError):
#     pass

# def validate(name):
#     if len(name) < 6:
#         # raise ValueError("Name is too short")               # we can use any error
#         raise NameTooShortError("Name is too short")

# username = input("Enter user name :")
# validate(username)
# print(f"Hello {username}.!") 

##########################################################################################################
############################################   Debugging  ################################################
##########################################################################################################

# steps for debugging:
#      1) set trace fn
#      2) execute code line by line



# import pdb    # module
# # module - python file containing usefull classes & fns by developers


# pdb.set_trace()                             # debugging starts from here onwards

# name = input("Enter ur name : ")
# age = input("Enter ur age : ")

# # pdb.set_trace()  

# print(f"ur name is {name} & ur age is {age}")
# ageAfter5Years = int(age) + 5
# print(f"ur age after 5 years will be {ageAfter5Years}")


# ### some commands in debugging:
# #
# #             l - shows status of execution 
# #             n - next step for execution
# #             q - quit from debugging
# #             c - continue execution as Normal program


##########################################################################################################
##########################################################################################################