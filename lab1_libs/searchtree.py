class SearchNode:
    def __init__(self, label="", heuristic=1, children=None):
        self.label = label
        self.heuristic = heuristic
        tc = self.__typecheck__(children)
        if tc == 1:
            self.children = [children]
        else:
            self.children = children

    # returns 1 if ch is a SearchNode, 2 if it's a list of SearchNodes, 0 otherwise
    def __typecheck__(self, ch):
        return 1 * (type(ch) == type(self)) + 2 * (type(ch) is list and sum([type(c) == type(self) for c in ch]) == len(ch))

    def add_children(self, new_children):
        if self.children is None:
            self.children = []
        
        tc = self.__typecheck__(new_children)
        if tc == 2:
            self.children += new_children
        elif tc == 1:
            self.children.append(new_children)
        else:
            raise TypeError("Children must be SearchNode or list of SearchNodes!")