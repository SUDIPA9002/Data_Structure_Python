class Tree:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self,child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level +=1
            p = p.parent
        return level

    def print_tree(self):
        prefix1 = ' ' * self.get_level() * 4
        prefix = prefix1 + ":: " if self.parent else ""
        print(prefix + self.data)
        if len(self.children):
            for child in self.children:
                child.print_tree()

def build_tree():
    root = Tree("Root")

    internalnode1 = Tree("Internal Node 1")
    internalnode1.add_child(Tree("Terminal Node 1"))

    internalnode4 = Tree("Internal Node 4")
    internalnode4.add_child(Tree("Terminal Node 5"))
    internalnode4.add_child(Tree("Terminal Node 6"))

    internalnode2 = Tree("Internal Node 2")
    internalnode2.add_child(Tree("Terminal Node 2"))
    internalnode2.add_child(Tree("Terminal Node 3"))

    internalnode3 = Tree("Internal Node 3")
    internalnode3.add_child(Tree("Terminal Node 4"))

    internalnode5 = Tree("Internal Node 5")
    internalnode5.add_child(Tree("Terminal Node 7"))

    root.add_child(internalnode1)
    root.add_child(internalnode2)
    root.add_child(internalnode3)
    internalnode1.add_child(internalnode4)
    internalnode3.add_child(internalnode5)

    # print(internalnode4.get_level())
    return root

if __name__ == '__main__':
    root = build_tree()
    root.print_tree()
    # print(root.get_level())
    pass