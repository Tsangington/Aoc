part1List = []
part2List = []
class Directory:
    def __init__(self, name, parent = None, size = 0 ) -> None:
        self.name = name
        self._subfolders = dict()
        self._parent = parent
        self.size = size

    def add_child(self, directory):
        self._subfolders[directory.name] = directory

    def select_child(self, name):
        return self._subfolders[name]

    def parent(self):
        return self._parent       

    def traverse(self):
        print(self.name, self.size)
        if self._subfolders:
            for subFolders in self._subfolders:
                self._subfolders[subFolders].traverse()

    def get_size(self):
        totalSize = 0
        for folders in self._subfolders:
            totalSize += self._subfolders[folders].size
        return(totalSize)
    
    def part1(self):
        if self.size <= 100000 and self._subfolders:
            part1List.append(self.size)
        if self._subfolders:
            for subFolders in self._subfolders:
                self._subfolders[subFolders].part1()
    
    def part2(self):
        unusedSize = 70000000 - root_folder.size
        minSize = 30000000 - unusedSize
        if self.size >= minSize and self._subfolders:
            part2List.append(self.size)
        if self._subfolders:
            for subFolders in self._subfolders:
                self._subfolders[subFolders].part2()

root_folder = Directory("/")
current_node = root_folder
f = open("2022\Day 7\input.txt","r")

for line in f:
    line = line.strip("\n")
    cmd = line.split(" ")
    if cmd[0] == "$": #ignore ls
        if cmd[1] == "cd":
            if cmd[2] == "/":
                current_node = root_folder
            elif cmd[2] == "..":
                current_node.size = current_node.get_size()
                current_node = current_node.parent()
            else:
                current_node.size = current_node.get_size()
                current_node = current_node.select_child(cmd[2])
                
    else: # entry is a file or folder
        if cmd[0] == 'dir': #Folder
            current_node.add_child(Directory(cmd[1], current_node))
            current_node.size = current_node.get_size()
        else: #File, input size
            current_node.add_child(Directory(cmd[1], current_node, int(cmd[0])))
            current_node.size = current_node.get_size()

#now need to traverse back up root node
while current_node.name != "/":
    totalSize = 0
    current_node.size = current_node.get_size()
    current_node = current_node.parent()
totalSize = 0
root_folder.size = root_folder.get_size()

print(f"Total folder size: {root_folder.size}")

root_folder.part1()
print(f"The total of the directories smaller than 100,000 is: {sum(part1List)}")

root_folder.part2()
part2List.sort()
print(f"The smallest directory that can be deleted is: {part2List[0]}")