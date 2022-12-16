
class Monkey:
    def __init__(self, items, op, test, falseMonkey, trueMonkey):
        self._items = items
        self._op = op
        self._divTest = test
        self._nextMonkey = (falseMonkey, trueMonkey)

    def operate(self):
        old = self._items[0]
        self._items[0] = eval(self._op) % 9699690  # keep only the rest of the division by all divisors in the input
        #print(self._items[0])
        ret = self._items.pop(0)
        if (ret % self._divTest == 0):
            return self._nextMonkey[1],ret
        else:
            return self._nextMonkey[0],ret



    def inspect(self):
        next_monkeys=[]
        for i in range(len(self._items)):
            next_monkeys.append(self.operate())
        return next_monkeys

    def takeItem(self,item):
        self._items.append(item)

    def __str__ (self):
        s = "Items: " + str(self._items) + \
            "\n operation: " + str(self._op) + \
            "\n test: " + str(self._divTest) + \
            "\n next: " + str(self._nextMonkey)
        return s

def parse(read_data):
    monkeys = []
    for i in range(0,len(read_data),7):
        monkeyNb = int(read_data[i].split(' ')[1][0])
        items = [int(x) for x in read_data[i+1].split(':')[1].split(',')]
        operation = read_data[i+2].split('=')[1]
        test = int(read_data[i+3].split("by")[1])
        trueM = int(read_data[i+4].split("monkey")[1])
        falseM = int(read_data[i+5].split("monkey")[1])
        monkey = Monkey((items), operation, test, falseM, trueM)
        monkeys.append(monkey)

    return monkeys

def run():
    with open('input') as f:
        read_data = [s.strip() for s in f.readlines()]
    monkeys = parse(read_data)

    for m in monkeys:
        print(str(m))

    stats = [0 for m in monkeys]
    for i in range(10000):
        print("-------- iteration " + str(i))
        monkey_idx=0
        for monkey in monkeys:
            next_monkeys = monkey.inspect()
            stats[monkey_idx] = stats[monkey_idx] + len(next_monkeys)
            for m in next_monkeys:
                #print(" dest: ", m[0], "->", m[1])
                monkeys[m[0]].takeItem(m[1])
            monkey_idx = monkey_idx+1
    
    for m in monkeys:
        print(m._items)
    print(stats)
    print(sorted(stats)[-1]*sorted(stats)[-2])

if __name__ == '__main__':
  run()