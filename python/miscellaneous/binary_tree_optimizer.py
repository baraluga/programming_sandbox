'''
Recall that a full binary tree is one in which each node is either a leaf
node, or has two children. Given a binary tree, convert it to a full one by
removing nodes with only one child.

For example, given the following tree:

        0
    /     \
    1         2
/            \
3                 4
\             /   \
    5          6     7
You should convert it to:

    0
/     \
5         4
        /   \
    6     7
'''


class BinaryTree:
    def __init__(self, fruit_value: int, left_leaf=None, right_leaf=None):
        self.fruit_value = fruit_value
        self.left_leaf = left_leaf
        self.right_leaf = right_leaf

    def __str__(self):
        return (
            f"\n================================\n"
            f"Fruit Value: {self.fruit_value}\n"
            f"Left leaf: {self.left_leaf}\n"
            f"Right leaf: {self.right_leaf}"
        )


INPUT = BinaryTree(0,
                   # Left Branch
                   BinaryTree(1, BinaryTree(3, None, BinaryTree(5))),
                   # Right Branch
                   BinaryTree(2, None, BinaryTree(4, BinaryTree(6),
                                                  BinaryTree(7))))


def prune_dead_branches(infected_tree: BinaryTree):
    # Clean up left branch
    left_leaf = infected_tree.left_leaf
    if left_leaf and bool(left_leaf.left_leaf) != bool(left_leaf.right_leaf):
        print(f"Pruning {left_leaf.fruit_value} leaf as it only have 1 leaf")
        infected_tree.left_leaf = left_leaf.left_leaf or left_leaf.right_leaf
        prune_dead_branches(infected_tree)
    # Clean up right branch
    right_leaf = infected_tree.right_leaf
    if right_leaf and bool(right_leaf.right_leaf) != \
            bool(right_leaf.left_leaf):
        print(f"Pruning {right_leaf.fruit_value} leaf as it only have 1 leaf")
        infected_tree.right_leaf = right_leaf.right_leaf or \
            right_leaf.left_leaf
        prune_dead_branches(infected_tree)
    return infected_tree


if __name__ == "__main__":
    print("Initial tree:")
    print(INPUT)
    print("Pruned bitch:")
    print(prune_dead_branches(INPUT))
