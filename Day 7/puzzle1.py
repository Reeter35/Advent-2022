

class Node:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = []
        self.files = []

    def getChild(self, name):
        for child in self.children:
            if child.name == name:
                return child
        return None

    def print(self):
        s = self.name
        for f in self.files:
            s = s + "\n" + str(f)
        for d in self.children:
            s = s + "\n" + d.print()
        return s

    def size(self):
        s = 0
        for f in self.files:
            s = s + int(f[0])
        for d in self.children:
            s = s + d.size()
        return s

    def getRecurseSubDir(self):
        dir=[]
        for d in self.children:
            dir.append(d)
            dir.extend(d.getRecurseSubDir())
        return dir

def build(read_data):
    root = Node("", None)
    node = root
    for line in read_data:
        line = line.strip()
        if line[0] == '$':
            # Parse command
            tokens = line.split(' ')
            if tokens[1] == "cd":
                # change dir
                if tokens[2]== "..":
                    node = node.parent
                elif node.getChild(tokens[2]) == None:
                    node.children.append(Node(tokens[2],node))
                    node = node.getChild(tokens[2])
                else:
                    node = node.getChild(tokens[2])
            #elif tokens[1] == " ls":
                # list dir
                # do nothing until next command
        else:
            # read the line and add the result to current node
            tokens = line.split(' ')
            if tokens[0] == "dir" and node.getChild(tokens[1]) == None:
                node.children.append(Node(tokens[1], node))
            else:
                node.files.append([tokens[0], tokens[1]])
    
    return root

def findDirectoriesUnder100k(root):
    dirs = []
    size = 0
    for d in root.getRecurseSubDir():
        if d.size() < 100000:
            dirs.append([d,d.size()])
            size = size + d.size()
    return dirs, size



def run():
    with open('input') as f:
        read_data = f.readlines()
    root = build(read_data)
    dirs, size = findDirectoriesUnder100k(root)
    print(dirs)
    print(size)

if __name__ == '__main__':
  run()