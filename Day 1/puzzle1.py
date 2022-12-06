
def grande (sommes):
    max=0
    for s in sommes:
        if s > max:
            max = s
    print (max)        
     

def prout(calories):
    somme=0
    tableau=[]
    for nb in calories:
        if nb != '\n':
           somme = int(nb)+somme
        else:
            tableau.append(somme)
            #print(somme)
            somme = 0
    grande (tableau)
    


def run():
  with open('input_1') as f:
    read_data = f.readlines()
  #values = list(map(int, read_data))
  prout(read_data)
  
    

if __name__ == '__main__':
  run()