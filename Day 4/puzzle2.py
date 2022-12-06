


def overlaps(pair1, pair2):

    if(pair1[0] >= pair2[0] and pair1[0]<=pair2[1]
        or pair1[1] >= pair2[0] and pair1[1]<=pair2[1]):
        return True
    if(pair2[0] >= pair1[0] and pair2[0]<=pair1[1]
        or pair2[1] >= pair1[0] and pair2[1]<=pair1[1]):
        return True
    
    return False

def splitDash(line):
    return list(map(int,line.split('-')))

def parse(line):
    pairs=list(map(splitDash,line.strip().split(',')))
    return pairs

def run():
    with open('input') as f:
        read_data = f.readlines()
    input=list(map(parse, read_data))

    nb=0
    for pair in input:
        if(overlaps(pair[0], pair[1])):
            nb = nb+1
    print(nb)

if __name__ == '__main__':
  run()