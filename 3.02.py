##########################################################################################################
##############                             MORE about Class                                  #############
##########################################################################################################


############## Inheritance :

# class Phone:                  # Base / Parent class

#     def __init__(self,brand,model_name,price):
#         self.brand = brand
#         self.finalprice = max(price,0)
#         self.model_name = model_name

#     def fullName(self):
#         return f"{self.brand}-{self.model_name}"

#     def make_a_call(self,phoneNum):
#         print(f"calling {phoneNum}...")

# class Smartphone(Phone):      # Derived / Child class

#     def __init__(self,brand,model_name,price,ram,internalMemory,rearCam):
#         # two ways
#         # 1)
#         # Phone.__init__(self,brand,model_name,price)                            # unCommon method 
#         # 2)
#         super().__init__(brand,model_name,price)
#         self.ram = ram
#         self.internalMemory = internalMemory
#         self.rearCam = rearCam

# # p1 = Smartphone("Nokia",'3311',1800,'16 Gb','1028 Gb','52 Mp')
# # print(p1.brand)

# # multilevel inheritance
# class FlagshipPhone(Smartphone):
#     def __init__(self,brand,model_name,price,ram,internalMemory,rearCam,frontCam):
#         super().__init__(brand,model_name,price,ram,internalMemory,rearCam)
#         self.frontCam = frontCam

# # p2 = FlagshipPhone("Nokia",'3311',1800,'16 Gb','1028 Gb','52 Mp','36 Mp')
# # print(p2.brand)

##########################################################################################################

#########################  Method resolution order & Method overriding : 

# class Phone:

#     def __init__(self,brand,model_name,price):
#         self.brand = brand
#         self.finalprice = max(price,0)
#         self.model_name = model_name

#     def fullName(self):
#         return f"{self.brand}-{self.model_name}"

#     def make_a_call(self,phoneNum):
#         print(f"calling {phoneNum}...")

# class Smartphone(Phone):

#     def __init__(self,brand,model_name,price,ram,internalMemory,rearCam):
#         super().__init__(brand,model_name,price)
#         self.ram = ram
#         self.internalMemory = internalMemory
#         self.rearCam = rearCam

# class FlagshipPhone(Smartphone):

#     def __init__(self,brand,model_name,price,ram,internalMemory,rearCam,frontCam):
#         super().__init__(brand,model_name,price,ram,internalMemory,rearCam)
#         self.frontCam = frontCam
    
#     def fullName(self):                                      # Method Overrided
#         return f"{self.brand}-{self.model_name} with high quality front Cam"


# p1 = Smartphone("Nokia",'3311',1800,'16 Gb','1028 Gb','52 Mp')
# p2 = FlagshipPhone("Nokia",'3311',1800,'16 Gb','1028 Gb','52 Mp','36 Mp')


# print(help(FlagshipPhone))           # gives Method resolution order 

#    Method resolution order:
#        FlagshipPhone                        # order in which sys. will search
#        Smartphone                           # object-elements
#        Phone                                
#        builtins.object                      # Inbuilt class (inheriated by every class)

# print(FlagshipPhone.mro())           # this also gives order 
# print(FlagshipPhone.__mro__)

# print(p2.fullName())

######################### isinstance :

# print(isinstance(p2,FlagshipPhone))            # True
# print(isinstance(p2,Smartphone))               # True
# print(isinstance(p2,Phone))                    # True
# print(isinstance(p1,FlagshipPhone))            # False

#################### issubclass :

# print(issubclass(FlagshipPhone,Smartphone))      # True
# print(issubclass(FlagshipPhone,Phone))           # True

##########################################################################################################

# class A:
#     def classAmethod(self):
#         return "i'm from class A"
#     def hello(self):
#         return "Hello from class A"

# class B:
#     def classBmethod(self):
#         return "i'm from class B"
#     def hello(self):
#         return "Hello from class B"

# class C(A,B):                             # same order get considered in Method resolution order (C,A,B)
#     pass

# instanceOfC = C()
# print(instanceOfC.hello())

##########################################################################################################
##################################   Special Magic / dunder method #######################################
##########################################################################################################


################################## __str__  &  __repr__

# class Phone:

#     def __init__(self,brand,model_name,price):
#         self.brand = brand
#         self.finalprice = price
#         self.model_name = model_name

#     def fullName(self):
#         return f"{self.brand}-{self.model_name}"

# p1 = Phone("Nokia",'3311',1800)

## Magic / dunder method -> "__Name__"

# l = [1,2,3]
# print(l)                # => [1, 2, 3]
# print(p1)               # => <__main__.Phone object at 0x7f97286ce550>
#
#    so __str__  OR  __repr__ are used to give such info


# class Phone:
#     def __init__(self,brand,model_name,price):
#         self.brand = brand
#         self.finalprice = price
#         self.model_name = model_name

#     def fullName(self):
#         return f"{self.brand}-{self.model_name}"

#     # def __repr__(self):
#     #     return f"{self.brand}-{self.finalprice}...    -from __repr__"
    
#     def __str__(self):
#         return f"{self.brand}-{self.finalprice}...    -from __str__"   ## Priority : __str__ > __repr__ 

#     def __repr__(self):
#         return f"Phone('{self.brand}','{self.model_name}','{self.finalprice}')"   

# p1 = Phone("Nokia",'3311',1800)

# print(p1)     # => Nokia-1800...

# print(p1.__str__())                 # can be called as method as well as fn 
# print(repr(p1))

## STR  - nicely formatted string
## REPR - python code (can create complete object)    => Phone('Nokia','3311','1800')
##        developers use REPR to make ease while debugging

################################## __len__ :

# l = [1,2,3]
# t = (1,2,3,4)
# s = {2,3,5,1,8}
# st = "John Doe"
# print(len(l),len(t),len(s),len(st))          # => 3 4 5 8

# print(len(p1))                       # => ERROR - TypeError: object of type 'Phone' has no len()

# class Phone:
#     def __init__(self,brand,model_name,price,phoneNum):
#         self.brand = brand
#         self.finalprice = price
#         self.model_name = model_name
#         self.phoneNum = phoneNum

#     def fullName(self):
#         return f"{self.brand}-{self.model_name}"

#     def __len__(self):
#         return len(self.phoneNum)

# p1 = Phone("Nokia",'3311',1800,'6768553399')

# print(len(p1))
# print(p1.__len__())

################################## Operator overloading ###############################

# 2 + 3 = 5
# 'abc' + 'de' = 'abcde'
# print(p1+p2)                # => TypeError: unsupported operand type(s) for +: 'Phone' and 'Phone'

# class Phone:
#     def __init__(self,brand,model_name,price,phoneNum):
#         self.brand = brand
#         self.finalprice = price
#         self.model_name = model_name
#         self.phoneNum = phoneNum

#     def __add__(self,other):                                ### Plus Operator overloaded
#         return self.finalprice + other.finalprice

# p1 = Phone("Nokia",'3311',1800,'6768553399')
# p2 = Phone("Nokia",'9921',8199,'8539986399')

# print(p1+p2)            # => 9999 total price

### # Other operator for overloading:

# # object.__add__(self, other)
# # object.__sub__(self, other)
# # object.__mul__(self, other)
# # object.__matmul__(self, other)
# # object.__truediv__(self, other)
# # object.__floordiv__(self, other)
# # object.__mod__(self, other)
# # object.__divmod__(self, other)
# # object.__pow__(self, other[, modulo])
# # object.__lshift__(self, other)
# # object.__rshift__(self, other)
# # object.__and__(self, other)
# # object.__xor__(self, other)
# # object.__or__(self, other)

################################## Polymorphism - multiple forms ###############################

### operator overloading is eg of Polymorphism
#
#                  something which is used for multiple operations
#                  eg : + used for sum / concatenation ...
#                  eg : len fn 



# class Phone:

#     def __init__(self,brand,model_name,price):
#         self.brand = brand
#         self.finalprice = max(price,0)
#         self.model_name = model_name

#     def fullName(self):
#         return f"{self.brand}-{self.model_name}"

#     def make_a_call(self,phoneNum):
#         print(f"calling {phoneNum}...")

# class Smartphone(Phone):

#     def __init__(self,brand,model_name,price,ram,internalMemory,rearCam):
#         super().__init__(brand,model_name,price)
#         self.ram = ram
#         self.internalMemory = internalMemory
#         self.rearCam = rearCam
    
#     def fullName(self):
#         return f"{self.brand}-{self.model_name} with {self.rearCam} rearCam for high quality pics.!"


# p1  = Phone("Nokia",'3311',1800)
# sp1 = Smartphone("Nokia",'Lumia 520',14999,'16 Gb','1028 Gb','18 MP')

# print(p1.fullName())
# print(sp1.fullName())


# fullName() => more than 1 form(Method overriding) : Polymorphism

##########################################################################################################
##########################################################################################################