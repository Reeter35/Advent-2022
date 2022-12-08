
import collections

def parseCrates(read_data):
    stacks = {}
    for line in read_data:
        if line.find('1') != -1:
            break

        index= line.find('[')
        while(index!=-1):
            stackName = str(int(index/4)+1)
            if(stackName not in stacks.keys()):
                stacks[stackName] = collections.deque()
            stacks[stackName].appendleft(line[index+1])
            index = line.find('[',index+1)
    return stacks

def parseCommand(line):
    tokens = line.split(' ')
    nb = tokens[1]
    source = tokens[3]
    dest = tokens[5].strip()
    return nb, source, dest

def moveCrates(read_data, stacks):
    for line in read_data:
        if line.find('move') != -1:
            nb, src, dst= parseCommand(line)
            
            temp = collections.deque()
            for i in range(int(nb)):
                temp.append(stacks[src].pop())


            for i in range(int(nb)):
                stacks[dst].append(temp.pop())

def run():
    with open('input') as f:
        read_data = f.readlines()
    stacks = parseCrates(read_data)

    moveCrates(read_data, stacks)
    s=""
    for i in range(len(stacks)):
        s = s + (stacks[str(i+1)][-1])
    print(s)

if __name__ == '__main__':
  run()