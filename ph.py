# !/CConjecture/ph.py

# ================================================================
"""

Collatz Conjecture, ph.py
Parental Hierarchy

Definitions:

node: a number in your parental hierarchy
root row: the values that are solved only by upper parents, m0
upper parent (parent 1): the previous node that resolves to the node by dividing by 2
lower parent (parent 2): the previous node that resolves to the node by multiplying by 3 and adding 1
parental hierarchy: the matrix of every node based off of the root row
static: a row does not generate any lower parents
fluid: a row generates lower parents
binary (boolean): a node is binary if it has two parents


Configuration:

There are a lot of dictionaries in this file.
The matrix is a dictionary where matrix[rowname] = row
rowname: type=string, is either rootrow or m-i
i: index from root row
m: height of the matrix, since this goes to infinity we write it as m-i
row: type=dictionary, where row[key] = nodes
key: type=string, formatted by n such as [a0, b0, a1, b1, ... , an, bn]
nodes: type=Node, node object created down below


"""
# ================================================================


class Node:
    """
    Node class creates nodes for the parental hierarchy. This allows us to view trends based on various traits of
    each value instead of being restricted to integers.

    arguments:
    num: integer -> self.num
    binary: boolean -> self.binary
    parent1: integer -> self.parent1
    parent2: boolean, unless an integer is passed -> self.parent2

    """
    def __init__(self, num, row, binary, parent1, parent2=False):
        self.num = num
        self.parent1 = parent1
        self.binary = binary
        self.row = row
        if parent2:
            self.parent2 = parent2
        else:
            self.parent2 = None

    def getNum(self):
        return self.num

    def getUpperParent(self):
        return self.parent1

    def getLowerParent(self):
        return self.parent2

    def getBinary(self):
        return self.binary

    def getRow(self):
        return self.row


class Row:
    """
    name: type=string -> self.name, formatted as [row: 0, row: 1, row: 2, ..., row: m-2, row: m-1, row: m]
    static: type=boolean -> self.static, defaults to False which implies row is fluid
    a row is classified as fluid until it is proven static
    self.nodes: type=dictionary, -> self.nodes, contains all of the nodes in the row self.nodes[key] = node
    key: type=string, formatted as "an" or "bn" based on node
    node: type=Node

    """
    def __init__(self, name, static):
        self.name = name
        self.static = static
        self.nodes = {}

    def getName(self):
        return self.name

    def getStatic(self):
        return self.static

    def getNodes(self):
        return self.nodes


def genRootRow(n):
    rootrow = {}
    parent1 = 0
    counter = 1
    for k in range(n):
        name = counter
        counter += 1
        
        num = 4**k
        num1 = Num(num, True, parent1)
        row[name] = num1

        name = counter
        counter += 1

        num = 2*num
        parent1 = num1.getNum()
        num2 = Num(num,False,parent1)
        row[name] = num2

        parent1 = num2.getNum()

    for entry in row:
        print()
        print(entry)
        print(row[entry].getNum())
    return None


def getNext(n):
    # n is previous value
    return 2*n


def genMatrix():
    return {}


def main():
    return None


def lowerGen(num):
    newnum = num - 1
    if newnum % 3 != 0:
        return False
    else:
        return True


def higherGen(num):
    return num * 2


def run():
    print("there will be a parental simulation here")
    main()
    return None

run()
