
# coding: utf-8

# In[1]:

import numpy as np
fname = "sudoku-task1.txt"
#fname = "sudoku-task2.txt"
array = np.zeros((9,9), dtype=np.int8)
f = open(fname)
inputmas= f.read()
splitted=inputmas.split()
joined=""
for numbers in splitted:
    joined+=numbers
i=0
j=0
for numbers in joined:
    array[i,j]=int(numbers)
    j+=1
    if j>8:
        j=0
        i+=1
print(array)


# In[ ]:



