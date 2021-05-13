from LinkedListVariants import DoubleNode

class SentinelDoubleLinkedList:
    def __init__(self):
        self.head = DoubleNode.DoubleNode(None)
        self.head.next = self.head
        self.head.prev = self.head

    def add(self, data, prev=None):
        newnode = DoubleNode.DoubleNode(data)

        prevnode = self.find(prev)

        newnode.next = prevnode.next
        newnode.prev = prevnode
        newnode.next.prev = newnode
        prevnode.next = newnode

    def remove(self, data):
        rmnode = self.find(data)
        if not rmnode.data == data:
            return

        rmnode.prev.next = rmnode.next
        rmnode.next.prev = rmnode.prev

    def find(self, somedata):
        p = self.head
        if somedata is None:
            return p

        while p.next is not self.head:
            if p.next.data == somedata:
                return p.next
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