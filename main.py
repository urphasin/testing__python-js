people: list[str | int] = ["Mario", "Dog", "Trump", 2]

cpy__people = 2

print(people)


cnt_string = "mongodb+srv://portugal:<db_password>@cluster0.uqcbmq9.mongodb.net/?appName=Cluster0"

class GraphNode:
    def __init__(self, value):
        self.value = value
        self.neighbors = []  # list of GraphNode

    def add_edge(self, node):
        self.neighbors.append(node)
a = GraphNode("A")
b = GraphNode("B")
c = GraphNode("C")
a.add_edge(b)
a.add_edge(c)        


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)