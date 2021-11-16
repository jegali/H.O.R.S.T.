import re

'''
    Different solver have different cube representations and configutation strings.
    A cube is normaly displayed solved as:

       UUU
       UUU
       UUU
    LLLFFFRRRBBB
    LLLFFFRRRBBB
    LLLFFFRRRBBB
       DDD
       DDD
       DDD

    Kociemba numbers the facelets this way:

             00 01 02
             03 04 05
             06 07 08 
    09 10 11 18 19 20 27 28 29 36 37 38
    12 13 14 21 22 23 30 31 32 39 40 41
    15 16 17 24 25 26 33 34 35 42 43 44
             45 46 47
             48 49 50
             51 52 52

    representing a solved cube in this string:         
    
    WWWWWWWWWOOOOOOOOOGGGGGGGGGRRRRRRRRRBBBBBBBBBYYYYYYYYY
    UUUUUUUUULLLLLLLLLFFFFFFFFFRRRRRRRRRBBBBBBBBBDDDDDDDDD

    My solver numbers it this way

             00 01 02
             03 04 05
             06 07 08
    09 10 11 12 13 14 15 16 17 18 19 20
    21 22 23 24 25 26 27 28 29 30 31 32
    33 34 35 36 37 38 39 40 41 42 43 44
             45 46 47
             48 49 50
             51 52 53             

    representing a solved cube in this string:         

    WWWWWWWWWOOOGGGRRRBBBOOOGGGRRRBBBOOOGGGRRRBBBYYYYYYYYY
    UUUUUUUUULLLFFFRRRBBBLLLFFFRRRBBBLLLFFFRRRBBBDDDDDDDDD
'''

cube_str="WWWWWWWWWOOOGGGRRRBBBOOOGGGRRRBBBOOOGGGRRRBBBYYYYYYYYY"
#cube_str="WWWWWWWWWOOOOOOOOOGGGGGGGGGRRRRRRRRRBBBBBBBBBYYYYYYYYY"



#
# def check_solved_kociemba(cube_str):
# 
# check if the string fits my solver
#

def check_solved(cube_str):
    if re.search(r"^(.)\1{8}", cube_str) and \
       re.search(r"(.)\1{8}$", cube_str) and \
       (cube_str[9:21] == cube_str[21:33]) and (cube_str[9:21] == cube_str[33:45]):
        return True 
    return False


#
# def check_solved_kociemba(cube_str):
#
# Check if the cube is solved with kociemba configuration
#

def check_solved_kociemba(cube_str):
    print(cube_str)
    if re.search(r"^(.)\1{8}(.)\2{8}(.)\3{8}(.)\4{8}(.)\5{8}(.)\6{8}$", cube_str):
        return True
    return False

#
# def check_length(cube_str):
#
# A cube definition string has to have
# the length of 54.
#

def check_length(cube_str):
    if len(cube_str) == 54:
        return True
    return False    



#
# def parse_string(cube_str):
#
# Take the string and parse it into
# a dictionary. A valid string has to have 
# - 6 entries
# - 9 facelets
#

def parse_string(cube_str):
    frequency_dict={}
    for color in cube_str:
        if color in frequency_dict:
            frequency_dict[color]+=1
        else:
            frequency_dict[color] = 1
    return frequency_dict



#
# def check_colorcount(frequency_dict):
#
# Take the length of the dictionary.
# It has to have the length of 6
#

def check_colorcount(frequency_dict):
    if (len(frequency_dict) == 6):
        return True
    return False    



#
# def check_frequency(frequency_dict):
#
# Check, if all values of the frequency_dict have the same value
# this can easily done with the "all" function 
#

def check_frequency(frequency_dict):
    return(all(value == 9 for value in frequency_dict.values()))



def check_cubestring(cube_str="WWWWWWWWWOOOGGGRRRBBBOOOGGGRRRBBBOOOGGGRRRBBBYYYYYYYYY", cube_type="my_solver"):
    if not check_length(cube_str):
        return "Cubestring has no valid length. Please correct"
    frequency_dict = parse_string(cube_str)
    if not check_colorcount(frequency_dict):
        return "Color count does not match 6. Please correct"
    if not check_frequency(frequency_dict):
        return "Facelet count is not 9 across all faces. Please correct"
    return "All checks passed successfully"


print(check_cubestring())
#print("Is the cube kociemba-solved:", check_solved_kociemba(cube_str))
#print("Is the cube solved:", check_solved(cube_str))
