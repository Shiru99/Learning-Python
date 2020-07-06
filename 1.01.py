#!/bin/python3

########################################    How to run      ###############################################


#Python3 1.01.py
#         OR
#Add “#!/bin/python3” in 1st line of code and run
#Like : ./1.01.py

###########################################hello world####################################################

# print("hello world ")                       
# print("hello 'world'  - \"world\" ")
# print('hello "world"  -  he\'s the hero \nnewline \thobby\\hobby\b\b\b\bapp')

# print("abcd  \\n  \\t \\b \\\\")
# print(r"abcd  \n  \t \b \\")            # r - raw string

# print("""
# hello
# how are you?
# I am fine here!
# """)

##########################################################################################################

# EMOJI
# emoji - https://unicode.org/emoji/charts/full-emoji-list.html

# print("Joker - '\U0001F921 '")    # U+1F921 - \U0001F921   # in PYTHON3
# print("\U0001F602 \U0001F923 \U0001F602 \U0001F923 \U0001F602 \U0001F923")


##########################################################################################################

    ### PRECEDANCE RULE ### 
    # parenthese
    # exponent R-L
    # * / // % L-R
    # + -      L-R


##################################
# # integer division 
                 
# print(5//2)  

##################################
# # floating point division               

# print(5/2)   
# print(4/2)                
# print(5/3)

##################################
# # Modulo

# print(4.5%3)   


##################################
# # Absolute Value

# print(abs(-100))       # ==> 100
# print(abs(-10.45))     # ==> 10.45   

##################################
# # exponent                 

# print(5**2)        
# print(2**1**10)             ### 2**(1**10) R-L
# print(512**(1/3))

##################################
# # round fn :- ( numToBeRounded , decimalDigits )

# #print(round(5/3))                    # => gives 2
# print(round(5/3,2)) 
# print(round(5/3,0))
# print(round(512**(1/3),3))

##########################################################################################################
#                           ### Assignment Operator ###

age = 77
# print(age)
# age +=23                          #   += , -= , *= , /= , %=
# print(age)

age *= 2
print(age)
###########################################VARIBLE########################################################

# yourId = 11
# print(yourId)

# yourId = "Phi (φ)"    # data can be changes => that's why python - Dynamic programming
# print(yourId)


##########################################################################################################

###                # 1num / name$ - Error             # num1 / Num1 / _name - 👍
###                # snake_case_writting              # camelCaseWritting

#######################################String Concatenation###############################################

#                        ###💀only strings can be concated with STRINGS💀###

# name1 = "John"
# name2 = "Doe"
# name3 = name1 + " " + name2 +"."
# print(name1 + " " + name2)
# print(name3)

# print(name3 * 3)    # to print multiple times

# ### print(name1 + 99 )                        # error numbers can't be concated with STRINGS
# print(name1 + "99")
# print(name1 + str(100) + str(99.05))          # str fn - converts int/float into string

# #    str()    =>     converts into string
# #    int()    =>     converts into intergers
# #    float()  =>     converts into float 

# print( int("44") + int(44.99) )                            # int(44.99) => 44
# print( int(44.99) + float("44.44") + float(100))           # int + float => float

###############################################INPUT######################################################

# name = input("Enter your name : ")
# print("hi..!! " + name)

# num = input("Enter your fav. number : ")      # input fn : takes input as a STRING💀
# print("OK ur fav. num is: " + num)            # only strings can be concated with STRINGS
# ### print(num+11)    error

##########################################################################################################
#                          ### multiple variable declaration in one line ###

# name ,favNum = "John" , 99
# print("ur good name is  : "+ name + "\n& ur fav. num is : " + str(favNum))

# x = y = z = 33
# print(x+y+z+1)

##########################################################################################################
#                          ### multiple inputs in one line ###

# name ,favNum = input("Enter ur name & fav. num : ").split()               # split() byDefault is " "
# print("ur good name is  : "+ name + "\n& ur fav. num is : " + str(favNum))

# name ,favNum = input("Enter ur name & fav. num : ").split("**")           # split(",") => sep input by ,
# print("ur good name is  : "+ name + "\n& ur fav. num is : " + str(favNum))

##########################################################################################################