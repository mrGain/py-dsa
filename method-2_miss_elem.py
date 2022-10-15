
# For finding the largest element in the array
def largestElem(arr,len):
    largest = arr[0]
    for i in range(len):
        if(arr[i]>=largest):
            largest = arr[i]
    return largest        

def missElem(arr,len):
    largest = largestElem(arr,len)
    fillArr = [0]*(largest+1)
    #print(fillArr)
    for i in range(len):
        A = arr[i]
        # print(A)
        fillArr[A] = 1
    
    
    return fillArr


if __name__=="__main__":
    arr = [3,7,4,9,12,6,1,11,2,10]
    fillArr = missElem(arr,len(arr))

    for i in range(1,len(fillArr)):
        if fillArr[i] == 0:
            print("Missing elements",i)