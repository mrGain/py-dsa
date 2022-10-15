def missElem(arr,len):
    l = arr[0]
    diff = l-0
    for i in range(len):
        if arr[i]-i != diff:
            print("Missing element found is",arr[i]-1)
            return
    

if __name__ == "__main__":
    arr = [6,7,8,9,10,11,13,14,16,17]
    missElem(arr,len(arr))    