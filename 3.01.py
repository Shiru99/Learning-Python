##########################################################################################################
##############                        OBJECT ORIENTED PROGRAMMING                            #############
##########################################################################################################

### # CLASS , OBJECT/INSTANCE , METHOD  :

######################### Example  : 

# list,tuple,set,dictionary           =>    class(BLUEPRINT)

# l = [1,2,3,5,7,9]                   =>    Object 
# l = ["abc","bcd","cde","def"]       =>    Object

# l.append(72)                        =>    Method

########################################      OOP INTRO    ###############################################

# class Person:                                        # convention => 1st letter capital
#     def __init__(self,name,last,age):                # constructor in PYTHON
#         # print("INIT has been called.")               
#         self.firstname = name
#         self.lastname = last
#         self.age = age                               # firstname , lastname , age => Instance variable
#         self.alive = True

#     def fullName(self):
#         return(f"{self.firstname} {self.lastname}")

#     def is18(self):
#         return self.age >= 18

# p1 = Person("John","Doe",30)
# p2 = Person("Jenny","Doe",28)
# p3 = Person("James","Doe",3)


# print(p2.age)
# print(p2.is18())
# print(Person.fullName(p3))                              # p3 == self
# print(p3.fullName())                                    # this is how self works


# # l = [1,2,3,5,88,99]

# # print(l.pop())            # l.append(55)
# # print(list.pop(l))        # list.append(l,55)

##########################################################################################################
##########################################################################################################
###                                                                                                    ###
###   fn defined inside class called => METHOD :                                                       ###
###                                                                                                    ###
###  for every method(including constructor(__init__)                                                  ###
###                               1st argu. must be given (SELF-convention, but one can use any name   ###
###                                                                                                    ###
##########################################################################################################
##########################################################################################################

######################### CLASS VARIABLE / class attribute:

# class Circle:

#     pi = 3.14                             ### => Class variable saves memory as common for all instances

#     def __init__(self, radius):
#         self.radius = radius
    
#     def circumferance(self):
#         return 2*Circle.pi*self.radius

#     def area(self):
#         return Circle.pi*(self.radius**2)


######################### Example :

# class Laptop :
    
#     discount = 10

#     def __init__(self, brand ,modelName, price):
#         self.brand = brand
#         self.momodelName = modelName
#         self.price = price


#     # def discountedPrice(self):
#     #     return (100-Laptop.discount)*self.price/100

#     def discountedPrice(self):
#         return (100-self.discount)*self.price/100 # 1st it check at self if not there uses class varible

# m1 = Laptop("HP","dx0001q",52000)
# m2 = Laptop("pixelbook","GA00124-US", 247999)

# print(m1.__dict__)
# print(m1.discountedPrice())

# Laptop.discount = 5
# print(m1.discountedPrice())

# print(m2.__dict__ , m2.discountedPrice(), sep="\n")
# m2.discount = 31
# print(m2.__dict__ , m2.discountedPrice(), sep="\n")


#################### class method (rear):

# class Person:                                        # convention => 1st letter capital

    # numOfPeople = 0

    # @classmethod                      # inbulit decorator for class method to pass class to the same class
    # def countInstances(classname):
    #     return(f"{classname.numOfPeople} instances of '{classname.__name__}' class has been created")

    # def __init__(self,name,last,age):                # constructor in PYTHON
    #     # print("INIT has been called.") 
    #     Person.numOfPeople += 1              
    #     self.firstname = name
    #     self.lastname = last
    #     self.age = age                               # firstname , lastname , age => Instance variable
    #     self.alive = True

#     def fullName(self):
#         return(f"{self.firstname} {self.lastname}")

#     def is18(self):
#         return self.age >= 18


# p1 = Person("John","Doe",30)
# p2 = Person("Jenny","Doe",28)
# p3 = Person("James","Doe",3)


# # print(Person.numOfPeople)
# print(Person.countInstances())                        ### instances can also access class method



#################### class method as Constructor :


# class Person:     

#     @classmethod
#     def rawInput(classname,raw):                                  ### classmethod as  CONSTRUCTOR
#         print("classmethod as  CONSTRUCTOR !")
#         first , last , age = raw.split(',')
#         return classname(first,last,age)

#     def __init__(self,name,last,age):
#         print("Default Constructor !")                        
#         self.firstname = name
#         self.lastname = last
#         self.age = age                  
#         self.alive = True

#     def fullName(self):
#         return(f"{self.firstname} {self.lastname}")

#     def is18(self):
#         return self.age >= 18


# p3 = Person("James","Doe",5)

# p4 = Person.rawInput("Lilly,Doe,2")



#################### STATIC method as Constructor :

# class Person:     

#     def __init__(self,name,last,age):
#         print("Default Constructor !")                        
#         self.firstname = name
#         self.lastname = last
#         self.age = age                  
#         self.alive = True


#     @staticmethod                                    # similar to normal fn defined 'IN' class 
#     def hello():
#         print("Static method -'Hello' has been called")

#     @classmethod
#     def rawInput(classname,raw):
#         print("classmethod as  CONSTRUCTOR !")
#         first , last , age = raw.split(',')
#         return classname(first,last,age)

#     def fullName(self):
#         return(f"{self.firstname} {self.lastname}")

#     def is18(self):
#         return self.age >= 18


# Person.hello()



##########  Encapsulation, Abtraction, naming convention, name Mangling ##################################

# class Phone:

#     def __init__(self,brand,model_name,price):
#         self.brand = brand
#         self.model_name = model_name
#         self.__price = price

#     def fullName(self):
#         return f"{self.brand}-{self.model_name}"

#     def make_a_call(self,phoneNum):
#         print(f"calling {phoneNum}...")

#     def sendMessage(self):
#         pass # twillio

################## 
# 
# Encapsulation - declaring all methods & variables at same place (as above)

##################
#
# one will able to use with any info about what algo... has used => Abtraction

# l = [22,5,11,77]
# l.sort()            # TIM sort
# print(l)



########################################
# 
#  naming convention :    there is nothing like private & public in python like other lang. still to let 
#                         reader understand that he should not change handle this private is declared
#                         as "_nameOfVariable" 

#  _Name   - private name
# __Name__ - dunder/magic method


###################### name Mangling - (NOT convention) : "__Name"          # useful for inheritance
#                                                         just change __name to _Class__Name 

# p1 = Phone("Nokia",'3311',1800)

# # print(p1.__price)   # 'Phone' object has no attribute '__price'

# # print(p1.__dict__) # => {'brand': 'Nokia', 'model_name': '3311', '_Phone__price': 1800}

# print(p1._Phone__price)
# p1._Phone__price  = 900




##########  Some decorators- Property , setter   ##################################

# class Phone:

#     def __init__(self,brand,model_name,price):
#         self.brand = brand
    #     self.finalprice = max(price,0)            # sol to (1)
    #     self.model_name = model_name
    #     #self.completeSpecs = f"{self.brand}-{self.model_name} : price - {self.price}"

    # # def completeSpecs(self):                                        # sol to (2) - make a fun
    # #     return f"{self.brand}-{self.model_name} : price - {self.price}"

    # @property
    # def completeSpecs(self):
    #     return f"{self.brand}-{self.model_name} : price - {self.price}"

    # @property
    # def price(self):
#         return self.finalprice

#     @price.setter
#     def price(self,newPrice):
#         self.finalprice = max(newPrice,0)
        

#     def fullName(self):
#         return f"{self.brand}-{self.model_name}"

#     def make_a_call(self,phoneNum):
#         print(f"calling {phoneNum}...")



# p1 = Phone("Nokia",'3311',1800)


# print(p1._price)
# print(p1.completeSpecs)

# PROBLEM :
#           1) price can't -ve => solution |
#           2) change in price doesn't change price inside completeSpecs
#           3) after allowing only +ve price also, one can change value to -ve 

### (1) - Done in class 

### (2) - property decorator

# p1._price = -400
    # # print(p1.completeSpecs)           => Error
    # # print(p1.completeSpecs())

    ###  use of property decorator one can call instance method in class as instance variable: 
    # print(p1.completeSpecs())           => Error 
    # print(p1.completeSpecs)

### (3) setter decorator (must be used after Propery decorator(also called getter for settor) )
# p1.price = -200

# print(p1.finalprice)
# print(p1.price)

# p1.finalprice = -800          # still one can change "_price"

# print(p1.finalprice)
# print(p1.price)                 # => Still -ve 


# print(p1.__dict__)

##########################################################################################################
##########################################################################################################