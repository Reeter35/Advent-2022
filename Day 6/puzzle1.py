import collections


def findMarker(data):
    s = set()
    for i in range(len(data)-4):
        for j in range(4):
            s.add(data[i+j])
        if(len(s)==4):
            marker=""
            for j in range(4):
                marker = marker + data[i+j]
            
            return marker,i+4

        s.clear()


    return "", -1

def run():
    with open('input') as f:
        read_data = f.readlines()
    print(findMarker(read_data[0]))

if __name__ == '__main__':
  run()