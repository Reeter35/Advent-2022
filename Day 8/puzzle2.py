
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

def scenicScore(pos, grid):
    print("---- ",pos[0],pos[1], " ----")
    # looking left
    left=0
    # print("left")
    for x in range(pos[0]-1,-1,-1):
        # print(grid[pos[1]][x], grid[pos[1]][pos[0]])
        if grid[pos[1]][x]<grid[pos[1]][pos[0]]:
            left = left+1
        else:
            left = left+1
            break;

    right=0
    # print("right")
    for x in range(pos[0]+1,len(grid),1):
        # print(grid[pos[1]][x], grid[pos[1]][pos[0]])
        if grid[pos[1]][x]<grid[pos[1]][pos[0]]:
            right = right+1
        else:
            right = right+1
            break;
    
    up=0
    # print("up")
    for y in range(pos[1]-1,-1,-1):
        # print(grid[y][pos[0]], grid[pos[1]][pos[0]])
        if grid[y][pos[0]] < grid[pos[1]][pos[0]]:
            up = up+1
        else:
            up = up+1
            break;

    down=0
    # print("down")
    for y in range(pos[1]+1,len(grid),1):
        if grid[y][pos[0]]<grid[pos[1]][pos[0]]:
            down = down+1
        else:
            down = down+1
            break;
    print(pos, left, right, up, down)
    return left*right*up*down



def run():
    with open('input') as f:
        read_data = f.readlines()
    grid, width, height = parseGrid(read_data)

    max_score=0
    for y in range(1,len(grid)-1):
        line = grid[y]
        for x in range(1,len(line)-1):
            score = scenicScore([x,y], grid)
            if score > max_score:
                max_score = score
    
    print(max_score)


if __name__ == '__main__':
  run()