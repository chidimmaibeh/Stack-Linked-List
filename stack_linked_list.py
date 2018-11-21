from node_linked_list import Node

class LinkedStack:
    
   def __init__(self):#stack class constructor/ create an empty stack
       self._head = None #instance variable
       self._size = 0 #instance variable
       
   def __len__(self):
       return self._size #Returns the length of the stack
    
   def is_empty(self):
       return self._size == 0# Returns true if the stack is empty
    
   def push(self, element):# add elemnt to the top of the stack 
       if element is None:# Returns False if no element is added
          return False
       else:
           new_node = Node(element)# a new node oject is created. 
           new_node.next = self._head# links the old node to the head
           self._head = new_node #links the head to the new node
           self._size +=1 #increases the size of the stack 
           return True#Returns true when an element is addeded 
    
   def top(self): 
       if self.is_empty(): #checks if stack is empty
           return('Stack in empty')#Returns this message if stack is empty
       return self._head._element #Returns and removes the element at the top of the stack
    
   def pop(self):
       if self.is_empty(): #checks if stack is empty
           return('Stack is empty') #Returns this message if stack is empty
       else:
           temp = self._head#create a temp node object
           self._head = self._head.next#head is linked to the next node
           popped = temp._element#the removed element 
           self._size -= 1 #length of the stack decreases by one
           return popped #Returns and remove the element at the top of the stack

        
        
def main():
    
    my_stack = LinkedStack()
    print(my_stack.push("Chemistry"))
    print(my_stack.pop())
    print(my_stack.push(3))
    print(my_stack.push(4))
    print(len(my_stack))
    print(my_stack.pop())
    print(my_stack.top())
    print(len(my_stack))
    print(my_stack.pop())
    
main()
                                    