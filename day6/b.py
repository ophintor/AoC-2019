from anytree import Node, RenderTree, find_by_attr, findall, Walker
import sys

def print_tree(t):
    for pre, _, node in RenderTree(t):
        print("%s%s" % (pre, node.name))

def find_root(l):
    for x in l:
        found = 0
        for y in l:
            if x.split(')')[0] == y.split(')')[1]:
                found = 1
        if not found:
            root=x.split(')')[0]

    return root

def add_children(lines,node,tree):
    for x in lines:
        parent = x.split(')')[0]
        child  = x.split(')')[1]
        if parent == node:
            Node(child, parent=find_by_attr(tree, node))
            add_children(lines,child,tree)

    return tree

def main():
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()
        root=find_root(lines)
        tree=Node(root)
        tree=add_children(lines,root,tree)
        print_tree(tree)

        w = Walker()
        (upwards, common, downwards)=w.walk(find_by_attr(tree, 'YOU'), find_by_attr(tree, 'SAN'))
        up=(len(str(upwards).split(',')))
        down=(len(str(downwards).split(',')))
        print(up+down-2)

if __name__ == '__main__':
    main()
