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
    
#g=options[0][0]
#print(g)
#for j in range(9):
#    if not array[1,j]==0:
#        c=array[1,k]
#        print(c)
#        for k in range(0,8):
#            if not options[k]==0:
#                options[1+j][c]=0

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
    for i in range(row-1, row+2):
        for j in range(column-1, column+2):
            temp[count]=array[i,j]
            count+=1
    return temp
           
                   
def simple_solution(array):
    changes = True
    while changes:
        changes=False
        for i in range(9):
            for j in range(9):
                if not array[i,j]==0:
                    continue
                counts = 0
                new_value = 0
                for value in range(1,9):
                    if not is_value_used(array, value, i, j):
                        counts += 1
                        new_value = value
                    if counts > 1:
                        break
                if counts == 1:
                    field[i,j]=new_value
                    changes = True
    return(array)

def get_options(array, row, column):
    temp=[]
    for value in range(1,9):
        if not is_in_array(get_row(array,row), value) and not is_in_array(get_column(array, column), value) and not is_in_array(get_cell(array, row, column), value):
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
                list_of_options.append(get_options(array, i, j))
        count1=0
        for i in range(9):
            for j in range(9):
                if len(list_of_options[count])==1 and array[i,j]==0:
                    array[i,j] = join(list_of_options[count1])
                    changed=True
                count1+=1
    return array

#print(get_row(sudoku,4))
#print(get_column(sudoku,1))
print(get_cell(sudoku,2,2))
if is_in_array(get_row(sudoku,1),4):
    print('yes')
else:
    print('no')
print(get_options(sudoku, 1, 1))
#print(simple_solution(sudoku))
print(6//3+1)
