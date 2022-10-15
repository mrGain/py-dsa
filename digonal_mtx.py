def set(n,i,j,k):
    if(i==j):
        mat[i-1] = k 
    


def get(i,j):
    if i == j:
        return mat[i-1]
    else:
        return 0    

def display(mat):
    for i in range(len(mat)):
        for j in range(len(mat)):
            if i == j:
                print(mat[i],end=" ")
            else:
                print(0 ,end=" ")  
        print()           
     


if __name__ == "__main__":
    mat = [0]*4
    set(4,1,1,4)
    set(4,2,2,9)
    set(4,3,3,3)
    set(4,4,4,7)

    display(mat)

