def draw_tree(depth, indent):
    # The base case prevents infinite recursion by stopping
    # once the smallest possible branch has been reached.
    if depth == 0:
        return

    # Indentation is used to visually represent tree structure,
    # helping the output resemble a branching tree.
    print(" " * indent + "*")

    # Recursive calls are made with reduced depth so that each
    # branch becomes smaller, which is essential for recursion.
    draw_tree(depth - 1, indent + 2)
    draw_tree(depth - 1, indent + 2)

# Main program allows the user to control the size of the tree,
# making the function reusable and flexible.
tree_depth = int(input("Enter tree depth: "))
draw_tree(tree_depth, 0)

