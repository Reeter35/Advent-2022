import collections

PACKET_LENGTH=14

def findMarker(data):
    s = set()
    for i in range(len(data)-PACKET_LENGTH):
        for j in range(PACKET_LENGTH):
            s.add(data[i+j])
        if(len(s)==PACKET_LENGTH):
            marker=""
            for j in range(4):
                marker = marker + data[i+j]
            
            return marker,i+PACKET_LENGTH

        s.clear()


    return "", -1

def run():
    with open('input') as f:
        read_data = f.readlines()
    print(findMarker(read_data[0]))

if __name__ == '__main__':
  run()