#!/bin/python3

##########################################################################################################
#                                      ### String formatting ###

# name ,favNum = "John" , 99

# print("Hello {}!!! ur fav num is {}.".format(name,favNum+900))        # Python3
# print(f"Hello {name}!!! ur fav num is {favNum+9900}.")                # Python3.6  # Don't forget f-💀

##########################################################################################################
#                              ### String Indexing & slicing & step-slicing ###

#name = "John"
#        0123  Positions
#       -4321  Positions            ### these are equivalent indices  0:-4, 1:-3, 2:-2, 3:-1


# print(name[0] + name[-3] + name[2] + name[-1])

#name = "John Doe"
#print(name[-2:4])                  # [ start argu.  :  stop argu.  : step        ]
#                                   # [ Default = 0  :  Default =-1 :  Default =1 ] 
#                                   # as stop argu gets it stop before printing that argument
                 
# print(name[:])
# print(name[1:])
# print(name[:3])

# name1 = "abcdefghij"
# print(name1[0:10:2])
# print(name1[::2]) 

# print(name1[9::-1])  # Reverse 9 or -1
# print(name1[::-1])   # Reverse

##########################################################################################################

###################### Slicing ###########################################################################
###                                                                                                    ###
###         name = "John Doe"                                                                          ###
###                           #                [start argu.    :   stop argu.   : step(Default = 1)]   ###
###   print(name[::1])        # if step > 0 => [ Default =  0  :  next of last  :      POSITIVE    ]   ###
###   print(name[::-1])       # if step < 0 => [ Default = -1  :  pre. of 1st   :      NEGATIVE    ]   ###
###                                                                                                    ###
##########################################################################################################

##########################################################################################################
#                            ## String functions & Methods ###

# ### len() is a function

# name = "John Doe"
# print(len(name))           ## len() : also considers spaces  

##################################################
# ###  methods

# name = "JOhN dOe"
# print(name.lower())
# print(name.upper())
# print(name.title())
# print("JOHN   DOE".title())                                         # doesn't remove extra spaces

# print( "JOHN DOE ooo".upper().count("o".upper()) )                  # count("*") method - case sensitive

# #print("myname".count("o"))

##################################################
# ### strip : ( Trim )

# name = "      have u know      tomarrow     is    Holiday         "

# print(name.strip() +"." )
# print(name.lstrip() +"." )
# print(name.rstrip() +"." )

# print(name.replace(" "  ,  ""))

##################################################
# ### replace & find method :

# act = "      He is a good student, but He don't work hard. if He will work hard He will be successful...Heeey."


# print( act.replace("He","she") )            # replace method is CASE SENSITIVE & replaces every -'He' 
# print( act.replace("He","she",4) )          # only 4 'He' gets replaced
# print( act.replace(" He "," she ") )       

#                                             ### Strings are Immutable(unchangeable) => REPLACE ????  

# print(act.find("He"))                         # find("*") method gives position of 1st * in given string
# print(act.find("He",40))                      # starts searching from position 40
# print(act.find("He",act.find("He")+1 ))       # starts searching from ( after position of 1st matching)

##################################################
# ### Center method

# name2 = "alpha"
# print(name2.center( len(name2)+6    , "!"     ))       ### =>   !!!alpha!!!
# ###         center( lenOfFinalWord  , addItem )        ### only 1 char. can be inserted

##########################################################################################################
#                                ### Strings are Immutable(unchangeable) ###

# name11 = "Mukesh"
# print(name11)
# name11 = "Kapil"
# print(name11)
# # name11[2] = "A"               # error #
# name12 = name11.replace("apil","APIL")
# print(name11)
# print(name12)

#########################################################################################################