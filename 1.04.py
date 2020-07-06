##########################################LOOOOP##########################################################
#                                    ### While loop ###

# sum = 0
# i = 1
# n = int(input("Enter the num. : "))

# while i <= n:
#     print(f"hey it's {i}")
#     sum +=i
#     i+=1

# print(f"sum is {sum}")

#######################################################

# name = "abcdabcdaabbcdaabbcdacbdabbd"
# temp = ""
# i=0

# while i<len(name):
#     if (name[i] not in temp):                                ### not in        can't use - !
#         temp+=name[i]
#         print(f"{name[i]} = {name.count(name[i])}")
#     i+=1


##########################################################################################################
#                                    ### for loop ###


# n = int(input("Enter the num : "))
# sum = 0

# for i in range(1,n+1) :                 # range(10) =>  0 to ... will stop running as it will reach 10
#     print(f"hey it's {i}")              # range(5,10) =>  5 to ... will stop running as it will reach 10
#     sum +=i

# print(f"Sum is {i-1} terms is {sum}")


# num = input("Enter the num : ")
# sum = 0

# for i in range(len(num)):
#     sum+= int(num[i])

# print(f"Sum is {sum}")

#################################################################

# name = "ab cd ab cdaa bb cdaab   bcdacb da bb d "
# temp = ""

# for i in range(len(name)):                                      # range(0,len(name)) == range(len(name))
#     if (name[i] not in temp):                              
#         temp+=name[i]
#         print(f"'{name[i]}' = {name.count(name[i])}")

#################################################################

# for i in range(10):
#     print(f"num = {i}")
#  ## i+=2                           # no use of this in 'for loop', it will not change value for 'LOOP'
#                                    # value of 'i' get changed till next loop entry

# for i in range(0,11,2):            #          range(0,11,2) => jump of 2   
#     print(f"num = {i}")

# for i in range(10,0,-1):       
#     print(f"num = {i}")

#################################################################
#                   ### MORE about PRINT() ###

# for i in range(1,10,2):
#     print(i,end = " ")

##########################################################################################################
#                                    ### Break / Continue ###


# for i in range(100):
#     if not( i%2 ):
#         if(i==10 or i == 0):
#             continue
#         else:
#             print(f"num : {i}")
#     if(i == 20 ):
#         print(f"exit at {i}")
#         break

##########################################################################################################
# ### infinite for loop:(NOT POSSIBLE IN GENERAL WAY)
 
# for i in range(10):
#     print(f"num - {i}")
#     if(i == 5):
#         print(f"num - {i}")  # => gives i = 5
#         i=0
#         print(f"num - {i}")  # => gives i = 0


##########################################################################################################
#                                    ### NUM. guessing game ###

# import random

# guessNum = random.randint(1,100)          # random.randint(1,100)  : selects random int bet. [1,100]
# i = 0
# print(guessNum)

# while True :
#     i+=1
#     num = int(input("Guess the no. bet. 1 & 100 : "))
#     if ( guessNum == num ):
#         print(f"hureyyy.!!! you have guessed correct num. : {guessNum} in {i}th guess")
#         break
#     elif ( guessNum < num):
#         print(f"Sorry.. your guess '{num}' is bigger than guessnum")
#         continue
#     else:
#         print(f"Sorry.. your guess '{num}' is smaller than guessnum")

##########################################################################################################