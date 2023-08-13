class Tree:
    def __init__(self, name,dgt):
        self.name = name
        self.dgt = dgt
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

    def print_tree(self,attribute):
        if attribute == 'name':
            value = self.name
        elif attribute == 'designation':
            value = self.dgt
        else:
            value = self.name + " ("+ self.dgt +")"

        prefix1 = ' ' * self.get_level() * 4
        prefix = prefix1 + ":: " if self.parent else ""
        print(prefix + value)
        if len(self.children):
            for child in self.children:
                child.print_tree(attribute)

def build_tree():
    n_ceo = Tree("Nilupul","CEO")

    # CTO node
    cto = Tree("Chinmay","CTO")
    aphead = Tree("Viswa","Infrastructure Head")
    aphead.add_child(Tree("Dhaval","Cloud Manager"))
    aphead.add_child(Tree("Abhijit","App Manager"))
    cto.add_child(Tree("Aamir","Application Head"))

    # HR node
    hrhead = Tree("Gels","HR Head")
    hrhead.add_child(Tree("Peter","Recruitment Manager"))
    hrhead.add_child(Tree("Waqas","Policy Manager"))

    n_ceo.add_child(cto)
    n_ceo.add_child(hrhead)
    cto.add_child(aphead)

    return n_ceo

if __name__ == '__main__':
    root = build_tree()
    root.print_tree("designation")
    # root.print_tree("both")
    # print(root.get_level())
    pass