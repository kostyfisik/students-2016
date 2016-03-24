import copy

def input_field(filename):
    # empty list
    A = []
    with open(filename) as file:
        for line in file:
            A.append([int(i) for i in line.split()])
    return A

def print_field(field):
    for row in field:
        print(row)



def row_candidates(field, i, j):
    candidates = {k for k in range(1,10)}
    for k in range(9):
        candidates.discard(field[i][k])
    return candidates
    
def col_candidates(field, i, j):
    candidates = {k for k in range(1,10)}
    for k in range(9):
        candidates.discard(field[k][j])
    return candidates

def cell_candidates(field, i, j):
    candidates = {k for k in range(1,10)}
    iCell = i // 3
    jCell = j // 3
    for i in range(3):
        for j in range(3):
            candidates.discard(field[iCell * 3 + i][jCell * 3 + j])
    return candidates

# full candidates
def get_candidates(field, i, j):
    rowcand  = row_candidates(field, i, j)
    colcand  = col_candidates(field, i, j)
    cellcand = cell_candidates(field, i, j)
    return rowcand & colcand & cellcand



# renew nearest candidates
def renew_candidates(field, candidates, i, j):
    # renew row and col
    for k in range(9):
        candidates[i][k] = get_candidates(field, i, k)
        candidates[k][j] = get_candidates(field, k, j)
    #renew cell
    iCell = i // 3
    jCell = j // 3
    for i in range(3):
        for j in range(3):
            candidates[iCell * 3 + i][jCell * 3 + j] = get_candidates(field, iCell * 3 + i, jCell * 3 + j)
            


# win-lose checks
def lose(field, candidates):
    for i in range(9):
        for j in range(9):
            if field[i][j] == 0 and len(candidates[i][j]) == 0:
                return True
    return False

def win(field):
    for i in range(9):
        for j in range(9):
            if field[i][j] == 0:
                return False
    return True





# searching function
def search(field, candidates):
    
   
    # check game result
    if lose(field, candidates):
        return False
        
    if win(field):
        print_field(field)
        exit(0)
         
    # find min-candidates point
    mincand = 9
    min_i   = 0
    min_j   = 0
    for i in range(9):
        for j in range(9):
            if field[i][j] == 0:
                if len(candidates[i][j]) < mincand:
                    min_i = i
                    min_j = j
                    mincand = len(candidates[i][j])
    
    # searching split
    # try candidates
    for cand in candidates[min_i][min_j]:
        newcandidates = copy.deepcopy(candidates)
        newfield      = copy.deepcopy(field)
        newfield[min_i][min_j] = cand        
        renew_candidates(newfield, newcandidates, min_i, min_j)
        search(newfield, newcandidates)
        


### ------- main program ----------- ###
# read from file
A = input_field('example_hard.txt')

# candidates
C = [[set()] * 9 for i in range(9)]

for i in range(9):
    for j in range(9):
        if A[i][j] == 0:
            C[i][j] = get_candidates(A, i, j)

search(A, C)
