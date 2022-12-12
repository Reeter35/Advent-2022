
import math

ROPE_SIZE=10

def isFar(A,B):
    return abs(A[0]-B[0]) > 1 or abs(A[1]-B[1]) > 1

def sign(x):
    return int(math.copysign(1, x))

# Move head and whole body, and returns new Tail pos
def move(B,direction, nb):
    tail_positions = []
    X_coeff = 1
    Y_coeff = 1
    if(direction=="L"): 
        X_coeff=-1
    if(direction=="U"): 
        Y_coeff=-1

    if(direction=="R" or direction=="L"):
        for n in range(nb):
            B[0][0] = B[0][0] + X_coeff
            # move whole body
            for i in range(1,ROPE_SIZE):
                if(isFar(B[i-1],B[i])): # distance is more than 1 diagonally
                    # adjust B[i] position
                    if B[i-1][1] != B[i][1]:
                        B[i][1] = B[i][1]+sign(B[i-1][1]-B[i][1])
                    if B[i-1][0] != B[i][0]:
                        B[i][0] = B[i][0]+sign(B[i-1][0]-B[i][0])

                    if i == ROPE_SIZE-1:
                        if(B[-1] not in tail_positions):
                            tail_positions.append(tuple(B[-1]))
    else:
        for n in range(nb):
            B[0][1] = B[0][1] + Y_coeff
            # move whole body
            for i in range(1,ROPE_SIZE):
                
                if(isFar(B[i-1],B[i])): # distance is more than 1 diagonally
                    # adjust B[i] position
                    if B[i-1][0] != B[i][0]:
                        B[i][0] = B[i][0] + sign(B[i-1][0]-B[i][0])
                    if B[i-1][1] != B[i][1]:
                        B[i][1] = B[i][1] + sign(B[i-1][1]-B[i][1])
                    if i == ROPE_SIZE-1:
                        if(B[-1] not in tail_positions):
                            tail_positions.append(tuple(B[-1]))
    
    return tail_positions,B

def run():
    with open('input') as f:
        read_data = f.readlines()
        
    B = list([0,0] for i in range (ROPE_SIZE))
    tail_positions=[tuple(B[-1])]
    for line in read_data:
        dir, nb = line.split(' ')[0], int(line.strip().split(' ')[1])
        print(dir,nb)
        pos,B = move(B, dir, nb)
        tail_positions.extend(pos)
        #print("B", B)
        #print("Positions", pos)
        #print("Total", tail_positions)
        #print("---")
        
    
    # remove duplicates
    res = []
    print(len(tail_positions))
    [res.append(x) for x in tail_positions if x not in res]
    print(len(res))


if __name__ == '__main__':
  run()