#travese a matrix
def row_wise_traverse(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end=' ')
        print()

def column_wise_traverse(matrix):
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            print(matrix[i][j], end=' ')
        print()
#general matrix representation
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
#here matrix[0][1] = 2
row_wise_traverse(matrix)
print("-------")
column_wise_traverse(matrix)