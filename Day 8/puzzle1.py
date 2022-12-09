
def parseGrid(read_data):
    grid=[]
    i=0
    width=0
    for line in read_data:
        grid.append([])
        j=0
        for height in line.strip():
            grid[i].append(int(height))
            j = j+1
        i = i+1
        width = j
    return grid, width, i

def isVisible(tree, pos, grid):
    
    max = 0
    for x in range(pos[0]):
        if grid[pos[1]][x] > max:
            max = grid[pos[1]][x]
    if max < tree:
        return True
    max = 0
    for x in range(pos[0]+1,len(grid)):
        if grid[pos[1]][x] > max:
            max = grid[pos[1]][x]
    if max < tree:
        return True

    max = 0
    for y in range(pos[1]):
        if grid[y][pos[0]] > max:
            max = grid[y][pos[0]]
    if max < tree:
        return True
    max = 0
    for y in range(pos[1]+1, len(grid)):
        if grid[y][pos[0]] > max:
            max = grid[y][pos[0]]
    if max < tree:
        return True

    return False
    

def run():
    with open('input') as f:
        read_data = f.readlines()
    grid, width, height = parseGrid(read_data)

    visible_trees = 0
    for y in range(len(grid)):
        line = grid[y]
        for x in range(len(line)):
            if(isVisible(grid[y][x], [x,y], grid)):
                visible_trees =  visible_trees+1
    visible_trees = visible_trees + len(grid)*4-4
    print(visible_trees)


if __name__ == '__main__':
  run()