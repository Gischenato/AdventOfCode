class Directory:
    def __init__(self, root:str):
        self.parent = None
        self.name = root
        self.children = []
        self.files = []
        self.size = 0

    def addChildren(self, path, new):
        location = self.goTo(path)
        location.children.append(Directory(new))


    def addFile(self, path, file):
        location = self.goTo(path)
        location.files.append(file)
        pass

    def goTo(self, path):
        dyr = self
        for p in path:
            dyr = dyr.find(p)
        return dyr

    def myChild(self, child, path):
        if path == []: return False
        location = self.goTo(path)
        return child in location.children

    def find(self, child):
        for c in self.children:
            if c.name == child:
                return c
        return None

    def __str__(self, qnt=0) -> str:
        return self.toString(0)

    def toString(self, qnt) -> str:
        string = ''
        for _ in range(qnt):
            string += ' '
        string += f'> {self.name} ({self.size})\n'
        for child in self.children:
            string += child.toString(qnt+2)
        for f in self.files:
            for _ in range(qnt+2):
                string += ' '
            name = f['name']
            size = f['size']
            string += f'- *{name} (size: {size})\n'
        return string

    def calculateSize(self):
        for file in self.files:
            self.size += file['size']
        if len(self.children) == 0: return self.size
        for child in self.children:
            self.size += child.calculateSize()
        return self.size
    
    def atMost100000(self):
        total = 0
        if self.size <= 100000: total += self.size
        for child in self.children:
            total += child.atMost100000()
        return total

    def smallest(self, size):
        small = 99999999999999
        if self.size >= size: small = min(small, self.size)
        for child in self.children:
            small = min(small, child.smallest(size))
        return small

def main():
    a = Directory('/')
    path = []
    for line in open('in'):
        line = line.strip().split()
        if line[0] == '$':
            if line[1] == 'cd':
                if line[2] == '/': continue
                if line[2] == '..': path.pop()
                else: 
                    path.append(line[2])
            elif line[1] == 'ls': pass
        else:
            if line[0] == 'dir':
                a.addChildren(path, line[1])
            else:
                file = {'name': line[1], 'size': int(line[0])}
                a.addFile(path, file)
    a.calculateSize()
    max_used = 70000000 - 30000000
    total_used = a.size
    toDelete = total_used - max_used
    print(a.smallest(toDelete))
main()