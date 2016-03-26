import numpy as np
import copy as cp
#fname = "sudoku-task1.txt"
fname = "sudoku-task2.txt"

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
    return array[index]

def get_column(array, index):
    return array[:, index]

def get_cell(array, row, column):
    temp = np.zeros(9, dtype=np.int8)
    count=0
    for i in range((row//3)*3, (row//3)*3+3):
        for j in range((column//3)*3, (column//3)*3+3):
            temp[count]=array[i,j]
            count+=1
    return temp
         
                
def get_options(array):
    list_of_options=[]    
    for row in range(9):
        for column in range(9): 
            temp=[]
            for value in range(1,10):
                if (not is_in_array(get_row(array, row), value) 
                    and not is_in_array(get_column(array, column), value) 
                    and not is_in_array(get_cell(array, row, column), value)):
                    temp.append(value)
            list_of_options.append(np.array((temp), dtype=np.int8))
    return list_of_options
            
def step_1(array):
    changed = True
    while changed:
        changed = False
        list_of_options=get_options(array)            
        for i in range(9):
            if changed:
                break            
            else:
                for j in range(9):
                    if changed:
                        break
                    else:
                        if len(list_of_options[i*9+j])==1 and array[i,j]==0:
                            #print(i*9+j)
                            array[i,j] = int(list_of_options[i*9+j]) 
                            #print('row= ',i,'column= ',j,'value= ',array[i,j])
                            changed = True                           
    return array

def step_2(array):
    temp=cp.copy(array)
    changed = True
    while changed:
        changed = False
        list_of_options=get_options(array) 
        for i in range(9):
            if changed:
                break            
            for j in range(9):
                if changed:
                    break                    
                if len(list_of_options[i*9+j])==2 and array[i,j]==0:
                    row=i
                    column=j
                    value2=list_of_options[2]
                    temp[i,j] = int(list_of_options[i*9+j][1])                    
                    step_1(temp)
                    if is_correct(temp):
                        changed = True
                        return temp                                
                    else:
                        array[row, column] = value2
                        step_1(array)
                        changed = True
                        return array                                    
                                
def step_3(array):
    temp=cp.copy(array)    
    changed = True
    while changed:
        changed = False
        list_of_options=get_options(array)       
        for i in range(9):
            if changed:
                break            
            for j in range(9):
                if changed:
                    break                    
                if len(list_of_options[i*9+j])==3 and array[i,j]==0:
                    row=i
                    column=j
                    value2=list_of_options[2]
                    value3=list_of_options[3]
                    array[i,j] = int(list_of_options[i*9+j][1])
                    changed = True 
                    step_1(array)
                    if is_correct(array):
                        return array                                
                    else:                       
                        array=np.copy(temp)
                        array[row, column] = value2
                        step_1(array)
                        if is_correct(array):
                            return array 
                        else:
                            array=np.copy(temp)
                            array[row, column] = value3
                            step_1(array)
                            return array   
                
def is_changed(array1, array2):
    if array1==array2:
        return False
    else:
        return True
                
def get_choise(array):
    list_of_options=get_options(array)
    n=9
    for count in range(81):        
        if len(list_of_options[count])<n and array[count//9, count-count//9*9]==0:
            n=len(list_of_options[count])
            #print('count= ',count,'n =',len(list_of_options[count],n))
    return n
                
                
def is_solved(array):
    if 0 in array:
        return False
    else:
        return True

def validation(array):   
    if is_correct(array):        
        return(array)       
    else:
        print('ERROR! Last statement:')
        print(array)
        raise
                                                   
def is_correct(array):
    correct=True
    for row in range(9):
        if not correct:
            break
        for value in range(1,10):
            if not correct:
                break
            if get_row(array, row).tolist().count(value)>1:
                correct=False 
                break
    for column in range(9):
        if not correct:
            break
        for value in range(1,10):
            if not correct:
                break
            if get_column(array, column).tolist().count(value)>1:
                correct=False 
                break
    for row in [0,3,6]:
        if not correct:
            break
        for column in [0,3,6]:
            if not correct:
                break
            for value in range(1,10):
                if get_cell(array, row, column).tolist().count(value)>1:
                    correct=False 
                    break
    if correct:
        return True
    else:
        return False
                                           

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
                  
                  
#print(get_options(sudoku)[23])

#print(get_choise(sudoku))
temp_sudoku=cp.copy(sudoku)
#temp_sudoku=step_1(temp_sudoku)
#print(temp_sudoku)
#print(get_choise(temp_sudoku))
count=0
while not is_solved(sudoku):
    choise=get_choise(sudoku)
    if choise==1:
        temp_sudoku=step_1(temp_sudoku)
        #if not is_changed(temp_sudoku, sudoku):
        #    choise+=1
        #    temp_sudoku=step_2(temp_sudoku)
        sudoku=validation(temp_sudoku)
    elif choise==2:
        temp_sudoku=step_2(temp_sudoku)
        #if not is_changed(temp_sudoku, sudoku):
        #    choise+=1
        #    temp_sudoku=step_3(temp_sudoku)
        sudoku=validation(temp_sudoku)
    elif choise==3:
        temp_sudoku=step_3(temp_sudoku)
        sudoku=validation(temp_sudoku)
    else:
        print('need for step ',choise)
        raise
    print()
    print('step ',count+1)
    print('use algorithm №',choise)
    print(temp_sudoku)
    count+=1
    if count>10:
        print('cannot solve')
        raise
print()
print('Sudoku is solved. Ansewer: ')
print(sudoku) 
#sudoku=np.copy(validation(temp_sudoku))
#if is_solved(sudoku):
#    print('Sudoku is solved. Ansewer: ')
#    print(sudoku)    
#else:
#    print('Sudoku is not solved. The last statement: ')
#    print(sudoku)
#print(45//9)
#print(sudoku[count//9, count-count//9*9])
#temp_sudoku=cp.copy(sudoku)
#temp_sudoku=step_1(temp_sudoku)
#sudoku=np.copy(validation(temp_sudoku))
#if is_solved(sudoku):
#    print('Sudoku is solved. Ansewer: ')
#    print(sudoku)
#    raise
#temp_sudoku=cp.copy(sudoku)
#temp_sudoku=step_2(temp_sudoku)
#sudoku=np.copy(validation(temp_sudoku))
#if is_solved(sudoku):
#    print('Sudoku is solved. Ansewer: ')
#    print(sudoku)
#    raise
#temp_sudoku=cp.copy(sudoku)
#temp_sudoku=step_3(temp_sudoku)
#temp_sudoku=step_3(temp_sudoku)
#temp_sudoku=step_3(temp_sudoku)
#temp_sudoku=step_3(temp_sudoku)
#sudoku=np.copy(validation(temp_sudoku))
#if is_solved(sudoku):
#    print('Sudoku is solved. Ansewer: ')
#    print(sudoku)    
#else:
#    print('Sudoku is not solved. The last statement: ')
#    print(sudoku)
#print(get_options(sudoku, 0, 2))
#print(sudoku[0,3])
#print(sudoku)
