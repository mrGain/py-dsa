class Sparxmatrix:
    def displayMatrix(self,mat,row,column):
        print("Sparse matrix is shown here:")
        for i in range(row):
            for j in range(column):
                if i == mat[i][0] and j == mat[i][1]:
                    print(mat[i][2],end=" ")
                else:
                    print(0,end=" ")  
            print()          
    
    def CreateSparseMatrix(self,row):
        Smatrix = []
        print("Enter the non-zero element :")
        for i in range(row):
            r = [int(x) for x in input().split(' ')]
            Smatrix.append(r)

        return Smatrix    


if __name__ == "__main__":
    # dimention = [int(x) for x in input().replace('  ',' ').strip().split(' ')] 
    print("enter the dimention :",end="")
    row, column = map(int, input().replace('  ',' ').strip().split(' '))
    ob = Sparxmatrix()
    sp_mat = ob.CreateSparseMatrix(row)
    ob.displayMatrix(sp_mat,row,column)

    # print(len(matrix))    
    # print(len(matrix[0]))    
            