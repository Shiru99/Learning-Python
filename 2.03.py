##################################### More About Function ################################################

#                          ### Lamda Expression (anonymous fn) ###

# def add(a,b):
#     return(a+b)


#      ### lambda num of arguments : return
#      ### lambda a,b,c,d          : a+b*c/d
#      ### we can assign this fn in a Variable  (in general we don't use lamda fn like this)

# Add = lambda a,b : a+b                      # ### one line fn without name 
# multiply = lambda a,b : a*b

# print(Add(33,66))
# print(multiply(9,11))

# print(type(Add))   # =>  function without name
# print(add)         # =>  <function   add    at 0x7fa0e3b3c1e0>
# print(Add)         # =>  <function <lambda> at 0x7fa0e39ae7b8>
# print(multiply)    # =>  <function <lambda> at 0x7fe15a86a950>



###########################################

### Example :

# isEven = lambda a: a%2 == 0
# print(isEven(66))
# print(isEven(99))

# lastchar = lambda string : string[-1]
# lengthOk = lambda string : len(string)>6

########################################### lambda fn with if and else  ##################################


# LengthOk = lambda s : True if len(s)>=6 else False
# print(LengthOk("six"))
# print(LengthOk("Fixsix"))



##########################################################################################################
##########################################################################################################

#                          ### Enumerate fn ###


# ### used in 'For Loop' to track pos. of item in iteration



# names = ["John","Jenny","Josh","Doe"]


# pos = 0
# for name in names:
#     print(f"{pos} - {name}")
#     pos += 1


# for pos,name in enumerate(names):                          ## => dict.items with keys: 0 to ...
#     print(f"{pos} - {name}")


##########################################################################################################