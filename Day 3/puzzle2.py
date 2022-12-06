
def priority(item):
    if(ord(item) < ord('a')):
        return (ord(item)-ord('A')+27)
    else:
        return ord(item)-ord('a')+1

def findItem(ruck):
    return priority(list(set.intersection(set(ruck[0]), set(ruck[1])))[0])

def findBadge(ruck1, ruck2, ruck3):
    item = list(set.intersection(set(ruck1[0]+ruck1[1]), set(ruck2[0]+ruck2[1]), set(ruck3[0]+ruck3[1])))[0]
    return priority(item)


def run():
    with open('input') as f:
        read_data = f.readlines()
    input=list(map(str.strip, read_data))
    #print(input)
    
    rucksacks = [[x[0:int(len(x)/2)],x[int(len(x)/2):len(x)]] for x in input]
    #print(rucksacks)

    result=0
    for i in range(0,len(rucksacks), 3):
        result = result + findBadge(rucksacks[i], rucksacks[i+1], rucksacks[i+2])
    print(result)

if __name__ == '__main__':
  run()
