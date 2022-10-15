

def setDifference(arr1, arr2):
    diff_arr = []
    for i in range(len(arr1)):

        for j in range(len(arr2)):
            if arr1[i] == arr2[j]:
                break
            elif arr2[j] == arr2[len(arr2)-1]:
                diff_arr.append(arr1[i])
    
    return diff_arr



a =[]
b = []

len_a = int(input("Enter the number of element in array a:"))
print("Enter the elements ")
for i in range(len_a):
    a.append(int(input()))    


len_b = int(input("Enter the number of element in array b:"))
print("Enter the eloements ")
for i in range(len_b):
    b.append(int(input()))    

print(a)    
print(b) 
result = setDifference(a,b)
print("The set difference is :",result)

