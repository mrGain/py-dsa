

def largestElem(arr,len):
    largest = 0
    for i in range(len):
        if arr[i] > largest:
            largest = arr[i]

    return largest  

def duplicateElem(arr,len):
    largest = largestElem(arr,len)
    tempArr = [0]*(largest+1)
    # print(tempArr)
    for i in range(len):
        temp = arr[i]
        # print(temp)
        tempArr[temp] = tempArr[temp] + 1

    return tempArr

if __name__ == "__main__":
    # n = int(input("Enter the size of the list "))
    # arr = [int(i) for i in input("Enter elements :").split(' ')][:n] 
    arr = [1,3,5,3,6,5,5,8,6]
    duplicateArr = duplicateElem(arr, len(arr))
    print(duplicateArr)
    for i in range(len(duplicateArr)):
        print(i ,'-',duplicateArr[i])

   
    
