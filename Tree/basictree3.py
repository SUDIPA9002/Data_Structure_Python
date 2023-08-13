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

    def print_tree(self,level):
        if self.get_level() > level:
            return
        prefix1 = ' ' * self.get_level() * 4
        prefix = prefix1 + "|__ " if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree(level)

def build_tree():
    root = Tree("Global")
    internalnode1 = Tree("India")
    internalnode2 = Tree("USA")
    root.add_child(internalnode1)
    root.add_child(internalnode2)

    ## India Node
    internalnode3 = Tree("Gujrat")
    internalnode3.add_child(Tree("Ahmedabad"))
    internalnode3.add_child(Tree("Baroda"))

    internalnode4 = Tree("Karnataka")
    internalnode4.add_child(Tree("Bangluru"))
    internalnode4.add_child(Tree("Mysore"))

    internalnode1.add_child(internalnode3)
    internalnode1.add_child(internalnode4)

    ## USA node
    internalnode5 = Tree("New Jersey")
    internalnode5.add_child(Tree("Princeton"))
    internalnode5.add_child(Tree("Trenton"))

    internalnode6 = Tree("California")
    internalnode6.add_child(Tree("San Francisco"))
    internalnode6.add_child(Tree("Mountain View"))
    internalnode6.add_child(Tree("Palo Alto"))

    internalnode2.add_child(internalnode5)
    internalnode2.add_child(internalnode6)

    return root

if __name__ == '__main__':
    root = build_tree()
    root.print_tree(3)
    # print(root.get_level())
    pass