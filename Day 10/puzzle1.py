
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

def signalStrength(cycle, register):
    prev=None
    for r in register:
        if(r[0] > cycle):
            return cycle*prev[1]
        prev=r

    return 0

def run():
    with open('input') as f:
        read_data = f.readlines()
    
    commands = [line.strip().split(' ') for line in read_data]
    register = runCommands(commands)
    for r in register:
        print(r)

    for i in [20,60,100,140,180,220]:
        print(i,signalStrength(i, register))

    print(signalStrength(20, register) +
        signalStrength(60, register) +
        signalStrength(100, register) +
        signalStrength(140, register) +
        signalStrength(180, register) +
        signalStrength(220, register) )


if __name__ == '__main__':
  run()