def missing_elem(arr):
    length = len(arr)
    itrSum = 0
    for i in range(length):
        itrSum = itrSum + arr[i]

    NaturalSum = (arr[length-1]*(arr[length-1]+1))/2   
    
    return int(NaturalSum - itrSum)


arr = [1,2,3,5,6]
missNo = missing_elem(arr)

if missNo:
    print(missNo)
else:
    print("No missing element")        