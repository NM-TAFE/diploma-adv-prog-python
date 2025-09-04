from tree import Tree


def main():
    tree = Tree()
    tree.insert(50, 3.5)
    tree.insert(35, 2.645)
    tree.insert(75, 1.7)
    tree.insert(12, 0.5)
    tree.insert(39, 9.9)

    # tree.traverse(1)
    tree.traverse(2)
    # tree.traverse(3)


if __name__ == '__main__':
    main()
