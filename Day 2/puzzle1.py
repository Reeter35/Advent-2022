


shape_value = {
  'X': 1,
  'Y': 2,
  'Z': 3
}

# First star array
#results = {
#  "AX": 3,
#  "AY": 6,
#  "AZ": 0,
#   "BX": 0,
#  "BY": 3,
#  "BZ": 6,
#  "CX": 6,
#  "CY": 0,
#  "CZ": 3
#}

# second star array
results = {
  "AX": 3,
  "AY": 4,
  "AZ": 8,
  "BX": 1,
  "BY": 5,
  "BZ": 9,
  "CX": 2,
  "CY": 6,
  "CZ": 7
}



def calcul(opponent, me):
  return results[opponent+me] # + shape_value[me]


def run():
  with open('input_1') as f:
    read_data = f.readlines()
  #values = list(map(int, read_data))
  result=0
  for line in read_data:
    (opponent, me)=line.strip().split(' ')
    #print(calcul(opponent,me))
    result = result + calcul(opponent,me) 
  print(result)
  
    

if __name__ == '__main__':
  run()