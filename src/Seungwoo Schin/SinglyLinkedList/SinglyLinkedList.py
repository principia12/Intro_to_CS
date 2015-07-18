class SingleNode():
    def __init__(self, content, next_node):
        self.content = content
        self.next_node = next_node
        
    def __repr__(self):
        return self.content
    
    
class SinglyLinkedList():
    def __init__(self, head):
        self.head = head
        
    def 