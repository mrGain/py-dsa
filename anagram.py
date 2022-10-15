


def Anagram(str_1, str_2):
    # Terminate if the length of two string are not equal
    if len(str_1) != len(str_2):
        return False
    
    hash = [0]*26
    for i in str_1:
        indx = ord(i) - 97
        hash[indx] = hash[indx] + 1

    for i in str_2:
        indx = ord(i) - 97
        hash[indx] = hash[indx] - 1

    for i in hash:
        if i != 0:
            return False

    return True                    


    



str_1 = "verbose"
str_2 = "observe"

if(Anagram(str_1, str_2)):
    print("Strings are Anagram")
else:
    print("String are't Anagrams")    