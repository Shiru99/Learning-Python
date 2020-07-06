##########################################################################################################

#                                ### LIST COMPREHENSION ###

# square = []
# for i in range(1,11):
#     square.append( i**2)

# print(square)



### LIST COMPREHENSION ###

# Square = [ i**2    for i in range(1,11)]
# # list = [ appending element FOR LOOP  ]       

# print(Square)



### Example:
# def reverseword(l):
#     return [name[::-1] for name in l]

# print(reverseword(["one","two","three"]))


##########################################################################################################

### LIST COMPREHENSION with IF condition ###



evenNums = [i for i in range(1,11) if i%2 == 0]
oddNums  = [i for i in range(1,11) if i%2 != 0]

print(evenNums, oddNums, sep="\n" ,end="\t#\n")


# # ### EVENnums = [i  if i%2 == 0  for i in range(1,11)]        ### => Syntex ERROR

##########################################################################################################

### LIST COMPREHENSION with IF-ELSE condition ###


# nums = list(range(1,21))

# nums2 = [i**2 if (i%2 == 0) else -i for i in nums] 
# print(nums2)

# ### elif not possble(I guess)
# ### nums2 = [ if (i%2 == 0) i**2 else -i for i in nums] # => syntex ERROR

##########################################################################################################

### LIST COMPREHENSION in nested list ###

# nestedlist = [ [i for i in range(1,4)]  for i in range(3) ]     # no rel. bet both i's
# print(nestedlist)                                               #  =>  [[1, 2, 3], [1, 2, 3], [1, 2, 3]]





##########################################################################################################
##########################################################################################################
##########################################################################################################

#                                ### DICTIONARY COMPREHENSION ###


# numAndSquare = { f"Square of {i}":i**2  for i in range(1,11)}     
# print(numAndSquare)

# word = "John Doeej"
# wordcount = { char:word.count(char) for char in word }
# print(wordcount)

### Example:
# def reverseword(l):
#     return {name:name[::-1] for name in l}

# print(reverseword({"one","two","three"}))       # {'two': 'owt', 'one': 'eno', 'three': 'eerht'}
# #                                               # above output shows UNORDERED 


##########################################################################################################

### DICTIONARY COMPREHENSION with IF-ELSE condition ###


# nums = list(range(1,11))

# oddEVE = { i:("EVEN" if (i%2 == 0) else "odd") for i in nums } 
# print(oddEVE)





##########################################################################################################
##########################################################################################################
##########################################################################################################

#                                ### SET COMPREHENSION ###


# Square = { f"Square of {i} is {i**2}" for i in range(1,4)}     
# print(Square)                                                  ## => UNORDERED


### Example:

# words = ["one","two","three"]
# FirstL = { word[0] for word in words } 
# print(FirstL)                                  # ### => {'t', 'o'} as UNORDERED & non-repeatative


##########################################################################################################