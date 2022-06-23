
class Node:
    def __init__(self, head,left,right,val):
        self.head = head
        self.left = left
        self.right = right
        self.val = val


    def set_left(self,left):
        self.left = left
    
    def set_right(self,right):
        self.right = right

    def set_val(self,val):
        self.val = val


head = Node(None,None,None,1)
left = Node(head,None,None,2)
right = Node(head,None,None,3)

head.set_left(left)
head.set_right(right)

left1 = Node(head,None,None,4)
right1 = Node(head,None,None,5)

left.set_left(left1)
left.set_right(right1)
       