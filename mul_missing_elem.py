
from textwrap import fill


def missElem(arr,len):
    l = arr[0]
    diff = l - 0
    fillArr = []
    for i in range(len):

        if arr[i]-i == diff:
            fillArr.append(arr[i])
        elif arr[i]-i != diff:
            current_diff = arr[i] - i
            noMiss = current_diff - diff 
            for j in range(noMiss):
                missing_element = diff + i +j
                # print("Missing Element is",missing_element)
                fillArr.append(missing_element)
            diff = current_diff

    return fillArr       


if __name__ == "__main__":
    arr = [6,7,8,9,11,12,15,16,17,18,19]
    fillArr = missElem(arr,len(arr))
    print(arr)
    print(fillArr)