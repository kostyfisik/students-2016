import numpy as np
# A = np.array([
# 8,3,1, 5,0,7, 0,0,0,
# 0,0,2, 4,0,6, 3,0,0,
# 0,9,0, 0,1,0, 0,2,0,
#
# 2,7,0, 0,0,0, 0,6,8,
# 0,0,3, 0,0,0, 1,0,0,
# 1,4,0, 0,0,0, 0,9,3,
#
# 0,6,0, 0,4,0, 0,5,0,
# 0,0,9, 2,0,5, 6,0,0,
# 0,0,0, 9,0,3, 0,0,0])

A = np.array([
[8,0,0, 0,0,0, 0,0,0],
[0,0,3, 6,0,0, 0,0,0],
[0,7,0, 0,9,0, 2,0,0],
[0,5,0, 0,0,7, 0,0,0],
[0,0,0, 0,4,5, 7,0,0],
[0,0,0, 1,0,0, 0,3,0],
[0,0,1, 0,0,0, 0,6,8],
[0,0,8, 5,0,0, 0,1,0],
[0,9,0, 0,0,0, 4,0,0]])
B=A.reshape((9,9))

def GetRow(matrix,row): # выводим строку
    return(matrix[row])#вся реализация сидит в записи через []

def GetColumn(matrix,col):
    return(matrix[:,col])

def GetCellIndex(row,col):#индекс субматрицы по столбцу и строке
    cell_col=int(col/3)
    cell_row=int(row/3)
    return(cell_row*3+cell_col)

def GetCell(matrix,index): #выводим субматрицу
    cell_col=index%3
    cell_row=int(index/3)
    return(matrix[cell_row*3:cell_row*3+3, cell_col*3:cell_col*3+3])

def CheckZero(matrix):
    for i in range(0, 9):
        for j in range(0, 9):
            if matrix[i, j] == 0:
                return (i, j)
    return False

def PossibleValues(matrix,row,column):
    Row = GetRow(matrix,row)
    Column = GetColumn(matrix, column)
    Cell = GetCell(matrix,GetCellIndex(row,column))
    PossVal = np.zeros(9)
    for i in range(0, 9):
        if i+1 in Row or i+1 in Column or i+1 in Cell:
            PossVal[i] = False
        else:
            PossVal[i] = i+1
    return PossVal

def Contradiction(possible_values):
    for i in range(0, 9):
        if i+1 in possible_values:
            return False
    return True

def Solve(matrix):
   if CheckZero(matrix):
        Temp = np.copy(matrix)
        row = CheckZero(Temp)[0]
        col = CheckZero(Temp)[1]
        PossVal = PossibleValues(Temp, row, col)
        if Contradiction(PossVal):
            return
        else:
            for i in range(0, 9):
                if PossVal[i] != 0:
                    Temp[row][col] = PossVal[i]
                    Solve(Temp)
            return matrix
   else:
       print(matrix, "\n")

Solve(B)