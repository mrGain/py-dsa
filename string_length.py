# s = 'A'
# # print("%d"% int(s))

# # space count in string 
# message = "Hello how are you"
# word = 0
# for i in range(len(message)):
#     if message[i] == ' ' and message[i-1] != ' ':
#         word += 1

# print(word+1)        

## REVERSE STRING 



def reverse(_str):
   rev_str = ""    
   for i in _str:
      rev_str = i +rev_str 

   return rev_str 

string = "Python"
print(reverse(string))
        