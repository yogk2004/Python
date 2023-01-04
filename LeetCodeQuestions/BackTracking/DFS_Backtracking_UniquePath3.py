def uniquePathsIII(grid):
    row = len(grid)
    col = len(grid[0])
    row_i, col_j, rowf_i, colf_j = 0, 0, 0, 0
    neededColumns = 2
    obs = []

    for i in range (row) :
        for j in range (col) :
            if grid[i][j] == 1 : row_i, col_j = i, j
            elif grid[i][j] == 2 : rowf_i, colf_j = i, j
            elif grid[i][j] == 0 : neededColumns += 1
            else : 
                obs.append([i,j])

    visitedPath = []
    solution, no_box = 0, 0

    def recursion(visitedPath, currentCoor_i, currentCoor_j, no_box) :
        if currentCoor_i == rowf_i and currentCoor_j == colf_j:
            if no_box == neededColumns-1 :
                solution+=1
                no_box=0
                return
        
        if 0<=currentCoor_i<row  and 0<=currentCoor_j<col and (currentCoor_i,currentCoor_j) not in obs and (currentCoor_i,currentCoor_j) not in visitedPath:
            visitedPath.append([currentCoor_i,currentCoor_j])
            no_box+=1
            for i,j in [(-1,0),(1,0),(0,-1),(0,1)] :
                if 0<=currentCoor_i+i<row and 0<=currentCoor_j+j<col:
                    recursion(visitedPath,currentCoor_i+i,currentCoor_j+j,no_box)
            visitedPath.remove([currentCoor_i,currentCoor_j])
            
    recursion(visitedPath,row_i,col_j,no_box)
    return solution
grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
uniquePathsIII(grid)