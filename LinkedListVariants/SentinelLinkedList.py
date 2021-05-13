from LinkedListVariants import SingleNode
#Sentinel Linked list means empty list has always one starter node
class SentinelLinkedList:
    def __init__(self):
        self.head = SingleNode.SingleNode(None)
        self.head.next = self.head

    def add(self, data, prev=None):
        newnode = SingleNode.SingleNode(data)

        prevnode = self.find(prev)

        newnode.next = prevnode.next
        prevnode.next = newnode

    def remove(self, data):
        rmnode = self.find(data)
        if not rmnode.data == data:
            return

        prevnode = self.find_prev(rmnode)

        prevnode.next = rmnode.next

    def find(self, prev):    #finding DATA!!!!!!!!!!!!!!
        p = self.head
        if prev is None:
            return p

        p = self.head
        while p.next is not self.head:
            if p.next.data == prev:
                return p.next
            p = p.next

        return p

    def find_prev(self, selfnode):
        p = selfnode
        while p.next is not selfnode:
            p = p.next
        return p

    def __str__(self):
        if self.head.next is self.head:
            return "[]"

        s="["
        p = self.head
        while p.next is not self.head:
            s = s+str(p.next.data)+" "
            p = p.next

        return s+"]"