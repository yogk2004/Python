def uniquePathsIII(grid):
        m=len(grid)
        n=len(grid[0])

        start_r,start_c,end_r,end_c=0,0,0,0
        bloc=0
        for r in range(m):
            for c in range (n):
                if grid[r][c] == 1:
                   start_r,start_c = r,c
                elif grid[r][c] == 2:
                    end_r, end_c = r,c
                elif grid[r][c] == 0:
                    bloc += 1
        
        global output
        output=0
        visited = []
        def recursion(visited,r,c,covbloc):
            if r == end_r and c == end_c: # why second if is used in it why not "and" can be used for it..!
                if covbloc == bloc+1:
                    output += 1 # meaning of self thing.
                covbloc = 0 # why without this the code is coming to be true.
                return
        
            if 0<=r<m and 0<=c<n and grid[r][c] != -1 and (r,c) not in visited:
                visited.append((r,c))
                for i,j in [(0,-1),(0,1),(1,0),(-1,0)]:
                    recursion(visited,r+i,c+j,covbloc+1)
                visited.remove((r,c))
        
        recursion(visited,start_r,start_c,0)

        return output
grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
uniquePathsIII(grid)