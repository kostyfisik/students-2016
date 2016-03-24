import numpy as np
fname = "sudoku-task1.txt"
#fname = "sudoku-task2.txt"
sudoku = np.zeros((9,9), dtype=np.int8)
f = open(fname)
inputmas= f.read()
splitted=inputmas.split()
joined=""
for numbers in splitted:
    joined+=numbers
i=0
j=0
for numbers in joined:
    sudoku[i,j]=int(numbers)
    j+=1
    if j>8:
        j=0
        i+=1
print('Sudoku to solve:')
print(sudoku)

def get_options_temp(array):
    temp=np.array([1,2,3,4,5,6,7,8,9])
    options=[]
    for i in range(9):
        for j in range(9):
            if array[i,j]==0:
                options.append(a)
            else:
                options.append(0)   
    print(a)
    print(options)
    
def is_in_array(array, char):
    if char in array:
        return True
    else:
        return False

def get_row(array, index):
    return array[index-1]

def get_column(array, index):
    return array[:, index-1]

def get_cell(array, row, column):
    temp = np.zeros(9, dtype=np.int8)
    count=0
    for i in range(((row-1)//3)*3, ((row-1)//3)*3+3):
        for j in range(((column-1)//3)*3, ((column-1)//3)*3+3):
            temp[count]=array[i,j]
            count+=1
    return temp
         
                
def get_options(array, row, column):
    temp=[]
    for value in range(1,10):
        if (not is_in_array(get_row(array, row), value) 
            and not is_in_array(get_column(array, column), value) 
            and not is_in_array(get_cell(array, row, column), value)):
            temp.append(value)
    answer=np.array((temp), dtype=np.int8)
    return answer
            
def simple_solution(array):
    changed = True
    while changed:
        changed = False
        list_of_options=[]
        for i in range(9):
            for j in range(9):
                list_of_options.append(get_options(array, i+1, j+1))
        count=0
        for i in range(9):
            if changed:
                break            
            else:
                for j in range(9):
                    if changed:
                        break
                    else:
                        if len(list_of_options[count])==1 and array[i,j]==0:
                            array[i,j] = int(list_of_options[count])
                            print('row = ', i+1, ', column = ', j+1, ', value = ', array[i,j])
                            changed = True                        
                        count+=1                        
    return array

def is_solved(array):
    if 0 in array:
        return False
    else:
        return True

#print(get_row(sudoku,3))
#print(get_column(sudoku,5))
#print(get_cell(sudoku,3,5))
#if is_in_array(get_row(sudoku,1),4):
#    print('yes')
#else:
#    print('no')
#print(get_options(sudoku, 3, 5))
#print(simple_solution(sudoku))
#print(6//3+1)
print(get_options(sudoku, 4, 7))
simple_solution(sudoku)
if is_solved(sudoku):
    print('Sudoku is solved. Ansewer: ')
    print(sudoku)
else:
    print('Sudoku is not solved. Last statement:')
    print(sudoku)
#print(get_cell(sudoku, 3, 7))
#print(get_row(sudoku, 3))
#print(get_column(sudoku, 7))

#print(len(get_options(sudoku, 3, 7)))
#for i in range(9):
#    for j in range(9):
#        if len(get_options(sudoku, i+1, j+1))==1 and sudoku[i,j]==0:
#             print('row = ', i+1, ', column = ', j+1, ', value = ', int(get_options(sudoku, i+1, j+1)))
        
