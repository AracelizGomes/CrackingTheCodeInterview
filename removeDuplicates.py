#removeDuplicates from linked list
class Node:
  def __init__(self,data):
    self.data = data
    self.Next = None

class LinkedList():
  def __init__(self):
    self.head = None
    self.last = None
  
  def append(self, data):
    if self.last is None:
      self.head = Node(data)
      self.last = self.head
    
    else:
      self.last.Next = Node(data)
      self.last_node = self.last_node.Next
  
  def get_prev_node(self, ref_node):
    current = self.head
    while (current and current.Next != ref_node):
      current = current.Next
    return current
    
  def remove(self, node):
    prev_node = self.get_prev_node(node)
    if prev_node is None: #the node we wanna remove is the head of the list
      self.head = self.head.Next
    else:
      prev_node.Next = node.Next # remove node
      
  def display(self):
    current = self.head
    while current:
      print(current.data, end="")
      current = current.Next
  
  
def removeDuplicates(L):
  current1 = L.head
  while current1:
    data = current1.data
    current2 = current1.Next
    while current2:
      if current2.data == data: #duplicates 
        L.remove(current2)
      current2 = current2.Next
    current1 = current1.Next
