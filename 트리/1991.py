# 트리 순회
import sys
sys.stdin = open('input.txt', 'r')


# class Node:
#     def __init__(self, data, left_node, right_node):
#         self.data = data
#         self.left_node = left_node
#         self.right_node = right_node
#
#
# def pre_order(node):
#     print(node.data, end='')
#     if node.left_node != '.':
#         pre_order(tree[node.left_node])
#     if node.right_node != '.':
#         pre_order(tree[node.right_node])
#
#
# def in_order(node):
#     if node.left_node != '.':
#         in_order(tree[node.left_node])
#     print(node.data, end='')
#     if node.right_node != '.':
#         in_order(tree[node.right_node])
#
#
# def post_order(node):
#     if node.left_node != '.':
#         post_order(tree[node.left_node])
#     if node.right_node != '.':
#         post_order(tree[node.right_node])
#     print(node.data, end='')
#
#
# n = int(input())
# tree = {}
#
# for _ in range(n):
#     data, left_node, right_node = input().split(' ')
#     tree[data] = Node(data, left_node, right_node)
#
#
# pre_order(tree['A'])
# print()
# in_order(tree['A'])
# print()
# post_order(tree['A'])

def preorder(c):
    global result
    if c == '.':
        return
    result += c
    preorder(tree[c][0])
    preorder(tree[c][1])

def inorder(c):
    global result
    if c == '.':
        return
    inorder(tree[c][0])
    result += c
    inorder(tree[c][1])

def postorder(c):
    global result
    if c == '.':
        return
    postorder(tree[c][0])
    postorder(tree[c][1])
    result += c


N = int(input())
tree = {}
for _ in range(N):
    parent, left, right = input().split(' ')
    tree[parent] = [left, right]
for i in [preorder, inorder, postorder]:
    result = ''
    i('A')
    print(result)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None
        self.stack = []

    def insert(self, parent, child):
        currentNode = None
        if self.root == None:
            currentNode = Node(parent)
            self.root = currentNode
        else:
            if self.root.data == parent:
                if not self.root.left:
                    self.root.left = Node(child)
                    self.stack.append(self.root.left)
                else:
                    self.root.right = Node(child)
                    self.stack.append(self.root.right)

            else:
                for node in self.stack:
                    if node.data == parent:
                        currentNode = node
                        self.stack.remove(node)
        if currentNode == None:
            return

        if not currentNode.left:
            currentNode.left = Node(child)
            self.stack.append(currentNode.left)
            self.stack.append(currentNode)
        else:
            currentNode.right = Node(child)
            self.stack.append(currentNode.right)


