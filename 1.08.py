##########################################################################################################
#                          ### DICTIONARIES ###
#                                           ### unorderd collection of data in KEY : VALUE pair 

# user = ["john Doe",27,"$999",["Coco","Matrix"],["palying Violin","Coding","Sleeping","Watching Movies"]]

# user = {'Name':"john Doe",  'Hobby': ["palying Violin", "Coding", "Sleeping", "Watching Movies"]}
# #                                                                           ### kays MUST be STRINGS

# print(type(user))                       # ### => dict
# print(user)

# user1 = dict(Name = "john Doe", Hobby = ["palying Violin", "Coding", "Sleeping", "Watching Movies"])
# print(type(user1))
# print(user1)

##########################################################################################################
#                             ###  Element Access  ###


# user = dict(Name = "john Doe", Hobbies = ["palying Violin", "Coding", "Sleeping", "Watching Movies"])
# print(user)

# # ## print(user[0])    # => ERROR as Dictionaries are UNORDERS collections
# print(user["Name"]) 
# print(user["Hobbies"]) 


##########################################################################################################
#                             ### Stores any type of values ###


# user0 = {
#     "intro"                   : {'Name':"john Doe",  "age": 33 } ,
#     "income"                  : "$999",
#     "BtechYear"               : 2,
#     'class9MidsemMarks'       : 86.88,
#     'Hobbies'                 : ["palying Violin", "Coding", "Sleeping", "Watching Movies"],
#     'haveFailedEverInSchool'  : True,
#     'whichiPhoneYouHave'      : None
# }

# print(user0)
# print(user0["intro"])

# # ### ADD data to DICTIONARY

# user0["fav. game"] = "Cricket"
# print(user0)

##########################################################################################################


# user0 = {
#     "intro"                   : {'Name':"john Doe",  "age": 33 } ,
#     "income"                  : "$999",
#     "BtechYear"               : 2,
#     'class9MidsemMarks'       : 86.88,
#     'Hobbies'                 : ["palying Violin", "Coding", "Sleeping", "Watching Movies"],
#     'haveFailedEverInSchool'  : True,
#     'whichiPhoneYouHave'      : None
# }

# ###          # IN-keyword

# ## for "KEYS"

# if "intro" in user0:
#     print("Intro is there.")
# else:
#     print("Intro is NOT available.")

# ## for "VALUES"

# if 86.88 in user0.values():               # ### for finding list ,one need mention complete list 
#     print("It is there.")
# else:
#     print("It's NOT available.")

####################################################
#               ### LOOPS ###

user0 = {
    "intro"                   : {'Name':"john Doe",  "age": 33 } ,
    "income"                  : "$999",
    "BtechYear"               : 2,
    'class9MidsemMarks'       : 86.88,
    'Hobbies'                 : ["palying Violin", "Coding", "Sleeping", "Watching Movies"],
    'haveFailedEverInSchool'  : True,
    'whichiPhoneYouHave'      : None
}

for info in user0:                  # ### Keys
    print(info,user0[info],sep="<==>")
    

print()

for info in user0.keys():           # ### Values
    print(info)

##########################################################################################################
#                             ### More about Dictionary ###

# user0 = {
#     "intro"                   : {'Name':"john Doe",  "age": 33 } ,
#     "income"                  : "$999",
#     "BtechYear"               : 2,
#     'class9MidsemMarks'       : 86.88,
#     'Hobbies'                 : ["palying Violin", "Coding", "Sleeping", "Watching Movies"],
#     'haveFailedEverInSchool'  : True,
#     'whichiPhoneYouHave'      : None
# }

######################################
# ### Keys Method

# user0Keys = user0.keys()
# print(type(user0Keys))                  # ### => type = "dict_keys"
# print(user0Keys)                        ###💀 this is not a LIST


# ### one CAN'T delete/add from/to data dic_keys   BUT 1 can iterate(LOOPING) through dic_keys

# for i in user0Keys:
#     print(i)

######################################
# ### Values Method

# user0Values = user0.values()
# print(type(user0Values))                  # ### => type = "dict_values"
# print(user0Values)                        ###💀 this is not a LIST


# ### 1 CAN'T delete/add from/to data dic_values   BUT 1 can iterate(LOOPING) through dic_values

# for i in user0Values:
#     print(i)
#                              ### OR ###
# for i in user0:
#     print(user0[i])

######################################
# ### item Method
# user0Items = user0.items()
# # print(type(user0Items))                  # ### => type = "dict_items"
# print(user0Items)                            ###💀 this is similar to list (NOT list) of tuple
##                                                            ###  tuple of a key and it's value

# for i in user0.items():                       
#     print(i)                               #### => tuples

# for key,value in user0.items():
#     print(f"key is {key} and value is {value}. ")

##########################################################################################################
#                         ###  Some methods & functions###


# user0 = {
#     "intro"                   : {'Name':"john Doe",  "age": 33 } ,
#     "income"                  : "$999",
#     "BtechYear"               : 2,
#     'haveFailedEverInSchool'  : True,
#     'whichiPhoneYouHave'      : None,
#     'class9MidsemMarks'       : 86.88,
#     'Hobbies'                 : ["palying Violin", "Coding", "Sleeping", "Watching Movies"]
# }


# # ### ADD data to DICTIONARY

# user0["fav. songs"] = ["song1","song2"]
# print(user0)
# print()

# # ### POP Method
# print(user0.pop("Hobbies"))            # ### type == type of value
# print()
# print(user0)

# # ### POPITEM Method
# print(user0.popitem())           # pops => tuple  ### pops X(randomly)X last 1 key & its value 
# print()
# print(user0)


##########################################################################################################
#                             ### Update ###

# user0 = {
#     "name"                    : "John",
#     "income"                  : "$999",
#     "BtechYear"               : 2,
#     'haveFailedEverInSchool'  : True,
#     'whichiPhoneYouHave'      : None,
#     'class9MidsemMarks'       : 86.88,
# }

# user0more ={
#     "name" : "Alphanso",
#     "age" : 27,
#     'Hobbies'                 : ["palying Violin", "Coding", "Sleeping", "Watching Movies"]
# }

# print(user0)
# print()
# user0.update(user0more)
# print(user0)                      # ### common keys get updated & new keys get added

##########################################################################################################
#                             ### More Methods ###

# # ### FROMKEYS Method                    # for similar values

# di = dict.fromkeys(["name","rollNo","mobNo"],["unknown","unknown"])      # ### => list
# print(di)

# di = dict.fromkeys(("name","rollNo","mobNo"),["unknown","unknown"])      # ### => tuple
# print(di)

# di = dict.fromkeys("AGE",["unknown","unknown"])                          # ### => tuple
# print(di)


# # ### GET Method 

# user = {
#     "name"                    : "John",
#     "income"                  : "$999",
#     "BtechYear"               : 2
# }

# # ## print(user["Name"])              ### => gives error
# print(user.get("Name"))

###########################################
#
# if "name" in user:
#     print("present")
# else:
#     print("Not Available.")
#
# if user.get('name'):
#     print("present")
# else:
#     print("Not Available.")
#
###########################################

# # ### CLEAR Method

# user = {
#     "name"                    : "John",
#     "income"                  : "$999",
#     "BtechYear"               : 2
# }

# print(user)
# user.clear()
# print(user)


# # ### COPY Method

# user = {
#     "name"                    : "John",
#     "income"                  : "$999",
#     "BtechYear"               : 2
# }

# user2 = user.copy()
# print(user2)
# print(user2 == user)
# print(user2 is user)
# print()


# user3 = user2       # both are same (same memory) if 1 makes changes in u2 it will reflect in u3
# print(user3)
# print(user3 == user2)
# print(user3 is user2)

##########################################################################################################
#                             ### GET Methods ###

# user = {
#     "name"                    : "John",
#     "income"                  : "$999",
#     "BtechYear"               : 2,
#     "name"                    : "JOHN DOE"              ###  => get() method  overwrites it
# }

# print(user.get("name","NOT found"))
# print(user.get("Name","NOT found"))

##########################################################################################################
#                             ###            ###

# word = {'a' : 3 , 'b' :2 , 'a' : 3}
# print(word)

# def wordCount (l):
#     count ={}
#     for char in l:
#         count[char] = l.count(char)
#     return count

# print(wordCount("JohnnDooe"))

##########################################################################################################