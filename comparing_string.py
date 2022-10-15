def compare(str_1,str_2):
    if str_1 == str_2:
        print("Yes strings are same")
    else:
        print("No!,Are not same")    
    return None

def palindrome(_str):
    rev_str = reverse(_str)
    if rev_str == _str:
        print("Yes, Its palindrome")
    else:
        print("No its not Palindrome")  

    return None 

def reverse(_str):
    rev_str = ""
    for i in _str:
        rev_str = i + rev_str
    return rev_str

str_1 = "level"
str_2 = "Painting"

compare(str_1, str_2)
palindrome(str_1)
