##########################################################################################################
#                                         ### Functions ###

# def addition(alpha,beta):                 
#    gamma = alpha + beta
#    print(gamma)  

# print(addition(11,33))


#     ### return is compulsary sometimes print may be used in that case it will return "None"   ###     #

################################


# def addition(alpha,beta): 
#    return (alpha + beta)
# #    print(alpha + beta)             #  after "return" fn will not execute

# print(addition(11,33))


################################


# # print(isEven(44))                           # function should be declared before its use  

# def isEven(a = 0):             ### a => parameter & one can set any Default value(u can take it as 'None')
#     if( a%2 == 0 ):
#         return True
#     return False

# print(isEven(43))              ### 43 => argument


################################

# def isEVEN(a):
#     return a%2 == 0                      # def isEVEN(a): return a%2 == 0 # This syntex is also correct.

# print(isEVEN(13))

##########################################################################################################
#                            ### We can also call one fn through other ###                               #
##########################################################################################################

# def isPalindrome(name):
#     rname = name[::-1]                     # name[::-1]  => reverses the string💀
#     if (name == rname):
#         return "palindrome"                # or return name == name[::-1]
#     return "Not Palindrome"

# print(isPalindrome("naman"))
# print(isPalindrome("Naman"))

##########################################################################################################
#                                       ### SCOPE ###


# x = 99                            # Global variable
# y = 88

# def fun():
#     x = 999                       # Local variable
#     global y                      # need to be declared as GLOBLE inside fn 
#     y = 888
#     print(f"x2-{x},y2-{y}")

# print(f"x1-{x},y1-{y}")
# fun()
# print(f"x3-{x},y3-{y}")
# x = y = 0
# print(f"x4-{x},y4-{y}")

##########################################################################################################
#                               ### TYPE fn ###

# s = "Song"
# print(type(s))             ## => <class 'str'>
# s = 3
# print(type(s))             ## => <class 'int'>
# s = 0.72
# print(type(s))             ## => <class 'float'>

##########################################################################################################