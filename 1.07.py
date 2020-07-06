##########################################################################################################
# ###                         ### TUPLES-dataStructure ###                                             ###
# ###                                                                                                  ###
# ###              # Immutable => once created can't be updated  => no append/inset/remove/pop         ###
# ###              # stores any type of data str/int/float/boolean/"None"                              ###
# ###              # faster                                                                            ###
# ###                                                                                                  ###
##########################################################################################################

# days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday","funday")

# ### Methods :-    count & index & len(Fn) & slicing

# print(days)
# print(len(days))
# print(days.count("Monday"))             # # print(days.count("monday")) => 0

# print(days[4])
# print(days[3:6:2])

##########################################################################################################
#                             ### about TUPLES-dataStructure ###

# ### for loop && while

# days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday","funday")

# for day in days:
#     print(day)

# i = 0
# while i<len(days):
#     print(days[i])
#     i+=1

###################################################

# ### tuple with 1 element

# days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday","funday")
# print(type(days))                        ###  => TUPLE

# freedomYear = (1947)
# print(type(freedomYear))                 ###  => int
# freedomYear = (1947,)
# print(type(freedomYear))                 ###  => tuple

# freedomYear = (1947.0)
# print(type(freedomYear))                 ###  => float
# freedomYear = (1947.0,)
# print(type(freedomYear))                 ###  => tuple

# freedomYear = ("1947")
# print(type(freedomYear))                 ###  => str
# freedomYear = ("1947",)
# print(type(freedomYear))                 ###  => tuple


###################################################

# ### tuple without parenthesis

# days = "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday","funday"

# print(type(days))  ### => BY DEFAULT -> Tuple

###################################################

# ### tuple unpacking  & list in tuple

# days = "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", ["Sunday","funday"]

# day1, day2, day3, day4, day5, day6, day7 = days 
# # ### day1, day2, day3, day4, day5, day6  = days                      ## => ERROR
# # ### day1, day2, day3, day4, day5, day6, day7, day8  = days          ## => ERROR

# print(day1)
# print(day7)

#### #### we can append & pop elements in/from list in tuple

# print(days)

# days[6].pop()
# days[6].append("FUNDAY")
# days[6].append(["Sunday","Funday"])
# print(days[6])

# print(days)


##########################################################################################################
#                             ### some functions ###

# nums = (1,3,5,11,199.47,5.53,0,-17,50,-8.0)

# print(max(nums))
# print(min(nums))
# print(sum(nums))

##########################################################################################################
#                             ### can fn returns more than 1 value? ###

# def op(num1,num2):
#     sum = num1 + num2
#     pro = num1*num2
#     return sum,pro

# print(type(op(9,11)))                # ### output is => TUPLE
### sum1 , pro1 = op(9,11)

#                                    ###   Ans:NO   ###
##########################################################################################################
#                             ### range & creating String & list of tuple ###

# nums = tuple(range(1,11))
# # print(nums)

# num1 = list(nums)                  # ### num1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]    LIST
# print(num1)
# print(type(num1))

# num2 = str(nums)                   # ### num2 = "(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)"  STRING
# print(num2)
# print(type(num2))

# # print(nums)      

######################

# num1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# num3 = str(num1)                   # ### num2 = "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"  STRING
# print(num3)
# print(type(num3))


##########################################################################################################