


def isIncluded(range1, range2):
    print(0)


def parse(line):
    pairs=list(map(str.strip('-'),line.strip(',')))
    print(pairs)

def run():
    with open('input') as f:
        read_data = f.readlines()
    input=list(map(parse, read_data))
    #for pair in input:
    #    isIncluded(pair[0], pair[1])

if __name__ == '__main__':
  run()