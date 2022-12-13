
def cycleNb(cmd):
    if(cmd[0]=="noop"):
        return 1
    elif(cmd[0]=="addx"):
        return 2

def apply(cmd, register):
    if(cmd[0]=="addx"):
        return register + int(cmd[1])
    else: # if(cmd[0] == "noop")
        return register

def runCommands(commands):
    register = [(1,1)]  # First entry is the cycle Nb, second one is the register value
    for cmd in commands:
        register.append((register[-1][0] + cycleNb(cmd),apply(cmd,register[-1][1])))

    return register

# returns the pixels covered by the current sprite
def spriteCover(sprite_pos):
    # screen width is 40
    # screen height is 6
    sprite=[]
    for i in range(6):
        sprite.append(sprite_pos-1+40*i)
        sprite.append(sprite_pos+40*i)
        sprite.append(sprite_pos+1+40*i)
    return sprite

def getSpritePos(cycle, register):
    prev=None
    for r in register:
        if(r[0] > cycle):
            return prev[1]
        prev=r
    return -100

def display(register):
    pixel_array=[]
    for cycle in range(1, 40*6):
        if((cycle-1) in spriteCover(getSpritePos(cycle,register))):
            pixel_array.append('#')
        else:
            pixel_array.append('.')
    
    return pixel_array

def printScreen(pixel_array):
    out=""
    for column in pixel_array:
        out = out + column
        if(len(out) == 40):
            print(out)
            out=""
    print(out)

def run():
    with open('input') as f:
        read_data = f.readlines()
    
    commands = [line.strip().split(' ') for line in read_data]
    register = runCommands(commands)
    printScreen(display(register))
    
    


if __name__ == '__main__':
  run()