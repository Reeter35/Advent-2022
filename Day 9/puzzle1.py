


def run():
    with open('example') as f:
        read_data = f.readlines()
        
    H=[0,0]
    T=tuple([0,0])
    tail_positions=[T]
    for line in read_data:
        dir, nb = line.split(' ')[0], int(line.strip().split(' ')[1])
        if dir == 'R':
            for i in range(nb):
                H[0] = H[0]+1
                if(abs(H[0]-T[0])>1):
                    y=T[1]
                    x = T[0] + 1
                    if H[1] != T[1]:
                        # move diagonally
                        y = H[1]
                    T = tuple([x,y])
                    tail_positions.append(T)
        elif dir == 'L':
            for i in range(nb):
                H[0] = H[0]-1
                if(abs(H[0]-T[0])>1):
                    x = T[0] - 1
                    y = T[1]
                    if H[1] != T[1]:
                        # move diagonally
                        y = H[1]
                    T = tuple([x,y])
                    tail_positions.append(T)
        elif dir == 'U':
            for i in range(nb):
                H[1] = H[1]-1
                if(abs(H[1]-T[1])>1):
                    x = T[0]
                    y = T[1] - 1
                    if H[0] != T[0]:
                        # move diagonally
                        x = H[0]
                    T = tuple([x,y])
                    tail_positions.append(T)
        elif dir == 'D':
            for i in range(nb):
                H[1] = H[1]+1
                if(abs(H[1]-T[1])>1):
                    x=T[0]
                    y = T[1] + 1
                    if H[0] != T[0]:
                        # move diagonally
                        x = H[0]
                    T = tuple([x,y])
                    tail_positions.append(T)
        
        print(H, T,tail_positions)
    
    # remove duplicates
    res = []
    print(len(tail_positions))
    [res.append(x) for x in tail_positions if x not in res]
    print(len(res))


if __name__ == '__main__':
  run()