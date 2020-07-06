########################################## MAP Function ##################################################

# nums = [1,2,3,4,5,6]

# Squares = [ i**2 for i in nums]             # ### List comprehension
# print(Squares)

# print(list( map( lambda a:a**3 ,   nums       )))
# ##          map( fn/name of fn , list(iterable) )    => gives iterator object       # fn name without ()


##########################################################################################################
###                                                                                                    ###
###     # List comprehension    use for       easy fn like i**2/ i+2                                   ###
###                                                                                                    ###
###     # map fn                use for       inbuilt fn / bigger fn that u are creating in program    ###
###                                                                                                    ###
##########################################################################################################

####################################### FILTER Function ##################################################


# to get FILTERED output (containig only satisfying Elements)



# nums = list(range(1,11))
# # evens = [ i for i in nums if i%2 == 0 ]

# def isEven(a):
#     return a%2 == 0

# # Even = list(filter(isEven,nums))
# Even = tuple(filter(isEven,nums))
# print(Even)

# Even = (filter(lambda a:a%2==0,nums))                     # ### => gives iterator filter object
# print(list(Even))

# print(Even)                # ### => <filter object at 0x7f8e54613470>

# Even = list(filter(isEven,nums))
# ### => gives iterable object

# for i in Even:
#     print(i)                     # ### can be iterated only ONCE
# for i in Even:
#     print(i)                     # NO OUTPUT



##########################################################################################################
###                                                                                                    ###
###          output of map fn & filter fn is iterator objects                                          ###
###          AND,                                                                                      ###
###              it can be RUN only ONCE                                                               ###
###                                                                                                    ###
##########################################################################################################

################################ ITERATOR vs ITERABLE ####################################################
###                                                                                                    ###
###   map fn / filter fn => (map/filter object) =>  iterator                                           ###
###                                                                                                    ###
###   tuples / lists / Strings => iterable                                                             ###
###              iterable creates iterator object which call itself using 'next' fn                    ###
###                                                                                                    ###
###                                                                                                    ###
##########################################################################################################



##########################################################################################################
##########################################################################################################
##########################################################################################################

## How for loop works 
##          as for loop starts it call "iter fn"
##          iter fn creates interator
##          interableObject = iter(list) ----> this is now iterator
##          calls next(interableObject)
##          ..........................
##          calls next(interableObject)

## Explanation:

# nums = [1,2,3,4,5,6]

# num_iter = iter(nums)                             # ---------> iterator created by iterable ...
# print(next(num_iter))
# print(next(num_iter))
# print(next(num_iter))
# print(next(num_iter))
# print(next(num_iter))
# print(next(num_iter))

# nums = [1,2,3,4,5,6]
# Even = (filter(lambda a:a%2==0,nums))             # iterator  
# print(next(Even)) 
# print(next(Even)) 
# print(next(Even)) 




##########################################################################################################
##########################################################################################################
##########################################################################################################

########################################## ZIP Function ##################################################

# userID    =  ['User2', 'User1', 'User3'] 
# UserName  =  [ 'John', 'Jenny', 'Josh' ]
# highscore =  [  793  ,   669  ,  901   ]

# obj = zip(userID,UserName,highscore)     # iterator zip object of tuples (containing 1 term of each)
# print(type(obj))                         # =>type - Zip
# print(obj)                               # <zip object at 0x7f54e4d54488> (iterator)

# obj1 = list(obj)
# print(obj1)                              # that many tuples as elements in smallest list involved in zip

# l = list(zip(userID,UserName))           # to CONVERT LIST into DICTIONARY
# print(dict(l))                           # list must containing lists/tuples each of two elements 

# t = tuple(zip(userID,highscore))
# print(dict(t))


####################################################

### #  * operator with Zip fn:                  UNPACKING

# l = [(1,9),(2,8),(3,7),(4,6),(5,5)]

# # l1 , l2 =(zip(*l))                  # iterator object of two tuples  (1, 2, 3, 4, 5) & (9, 8, 7, 6, 5)
# l1 , l2 =list(zip(*l))                # list of seperated tuples => [ (1, 2, 3, 4, 5) , (9, 8, 7, 6, 5)]
# print(l1)
# print(l2)
# print(list(l2))


### # Example :

# l1 = [9,4,7,9]
# l2 = [2,9,9,6]
# newList = []

# for pair in zip(l1,l2):
#     newList.append(max(pair))

# print(newList)



### # Example :

# avg = lambda *args: [sum(pair)/len(pair) for pair in zip(*args)]

# print(avg([1,2,3],[4,5,6],[7,8,9]))

##########################################################################################################