from LinkedListVariants import SingleNode

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def add(self, data, prev=None):
        newnode = SingleNode.SingleNode(data)

        if self.head is None:
            self.add_to_empty_list(newnode)
        else:
            prevnode = self.find(prev)
            self.add_between(prevnode, newnode)
            if prev is None:            # executing only if data adding to head
                self.head = newnode

    def add_to_empty_list(self, newnode):
        self.head = newnode
        newnode.next = newnode

    def add_between(self, prev, newnode):
        newnode.next = prev.next
        prev.next = newnode

    def remove(self, data):
        rmnode = self.find(data)
        if not rmnode.data == data:
            return

        prevnode = self.find_prev(rmnode)

        if rmnode is prevnode:
            self.remove_to_empty()
        else:
            if rmnode is self.head:
                self.head = self.head.next
            self.remove_between(rmnode, prevnode)

    def remove_between(self, rmnode, prevnode):
        prevnode.next = rmnode.next

    def remove_to_empty(self):
        self.head = None

    def find(self, prev):
        p = self.head
        if prev is None:
            while p.next is not self.head:
                p = p.next
            return p

        while p.next is not self.head:
            if p.data == prev:
                return p
            p = p.next

        return p

    def find_prev(self, selfnode):
        p = selfnode
        while p.next is not selfnode:
            p = p.next
        return p

    def __str__(self):
        if self.head is None:
            return "[]"

        s="["
        p = self.head
        while p.next is not self.head:
            s = s+str(p.data)+" "
            p = p.next

        return s+str(p.data)+"]"