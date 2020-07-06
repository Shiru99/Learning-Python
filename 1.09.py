##########################################################################################################
#                                     ### SET ###

# ###
# ###              # Unordered collection of UNQUIE items
# ###              # stores ONLY type of data str/int/float/boolean/"None"  NOT list/tuple/dict
# ###


# li = [1,1.0,2,4,5,7,9,6,3,1,3,5,6,5,7,3,1,2,4,6,8]

# se = set(li)                # #### => {1, 2, 3, 4, 5, 6, 7, 8, 9}
# print(se)                   # #### => 1 & 1.0 are considered as SAME

# li2 = list(set(li))            # ### => to remove repeating elements
# print(li2)

##########################################################################################################
#                                  ### Some fn/methods ###


# sett = {1,2,3,4}                 ##############
# sett.add(4)                      ###        ### 
# sett.add(5)                      ###  ADD   ###
# sett.add(5)                      ### method ### 
# print(sett)                      ##############

# sett = {1,2,3,4}                    ##############
# print(sett.remove(4))               ## REMOVE   ##    => None
# ### sett.remove(5)                  ## => ERROR if element is not available 
# print(sett)

# sett = {1,2,3,4}                   ##############
# print(sett.discard(4))             ### => None                    ### DISCARD ###
# print(sett.discard(5))             ### => None although element is not available 
# print(sett)

# sett = {1,2,3,4}
# sett.clear()                                                      ### CLEAR ###
# print(sett)                    

# s1 = sett.copy()                                                  ### COPY ###
# print(s1)


##########################################################################################################
#                                  ### IN & for ###

# s = { 'a', 'b', 'c'} 

# if 'a' in s:
#     print("present")
# else:
#     print("Absent")


# for item  in s:
    # print(item)                ### order get changes as it is not fixed 



#################################### math of SET  ########################################################

# s1 = { 1,2,3,4 }
# s2 = { 3,4,5,6 }

# ### UNION -  OR('|')
# s3 = s1 | s2
# print(s3)

# ### INTERSECTION - AND('&')
# s4 = s1 & s2
# print(s4)

##########################################################################################################