
class Node:
  def __init__(self, cargo=None, next=None):
    self.cargo = cargo
    self.next  = next

  def __str__(self):
    return str(self.cargo)
def printBackward(list):
  if list == None: return
  head = list
  tail = list.next
  printBackward(tail)
  print(head),


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.next = node2
node2.next = node3
printBackward(node1)