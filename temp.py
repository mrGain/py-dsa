

def findFirstMissing(array, start, end):

	if (start > end):
		return end + 1

	if (start != array[start]):
		return start;

	mid = int((start + end) / 2)

	if (array[mid] == mid):
		return findFirstMissing(array, mid+1, end)

	return findFirstMissing(array, start, mid)


# driver program to test above function
# arr = [0, 1, 2, 3, 4, 5, 6, 7, 10]
# n = len(arr)
# print("Smallest missing element is",
# 	findFirstMissing(arr, 0, n-1))

# This code is contributed by Smitha Dinesh Semwal

def printSubsequences(arr, index, subarr):
    missingElem = []
    findElem = 0
    if index == len(arr):
        if len(subarr) != 0:
            n = len(subarr)
            sortedSubarr = sorted(subarr)
            findElem = findFirstMissing(subarr,sortedSubarr[0],sortedSubarr[-1])
            missingElem.append(findElem)
            print(missingElem)
            #print(subarr)

    else:
        printSubsequences(arr, index + 1, subarr)
        
        printSubsequences(arr, index + 1,subarr+[arr[index]])

    return
		
arr = [1, 2, 1]

printSubsequences(arr, 0, [])

# This code is contributed by Mayank Tyagi
'''

[] - 1
[1] - 2
[1,2] - 3
[1,2,1] - 3
[2] - 1
[2,1] - 3
[1] - 2
[1,1] - 2

'''