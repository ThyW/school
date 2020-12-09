jewels = []

def searchJewls(filename):
    visited = []
    DFS(jewels, visited, filename)
    #initialize DFS and return jewls list
def DFS(jewls, visited, filename):
    visited.append(filename)
    with open(filename, "r") as f:
        for line in f.read().splitlines():
            for split in line.split():
                if split.endswith(".txt"):
                    if split in visited: 
                        pass
                    else:
                        DFS(jewels, visited, split.lstrip())
                if split.startswith("x:"):
                    jewels.append(split)
    #Combines linear search for adding jewls to jewls list
    #and recursion for any subsequent text files found in current textfile

#test your code with this command
searchJewls("textfiles/file2.txt")
print(jewels)
