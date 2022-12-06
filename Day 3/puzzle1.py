


def find(ruck1, ruck2):
    for c in ruck1:
        if(c in ruck2):
            if(ord(c)<ord('a')):
                return ord(c)-ord('A')+27
            else:
                return ord(c)-ord('a')+1
            break

def run():
  with open('input') as f:
    read_data = f.readlines()
  #values = list(map(int, read_data))
  


  result = 0
  for line in read_data:
    ruck1=line[0:int(len(line)/2)]
    ruck2=line[int(len(line)/2):len(line)]
    
    result = result + find(ruck1,ruck2)
    
  print(result)
    

if __name__ == '__main__':
  run()