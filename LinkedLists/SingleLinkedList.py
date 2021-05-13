from LinkedLists import SingleNode

class SingleLinkedList:
    def __init__(self):         # empty list
        self.head = None
        self.tail = None

    def add(self, data, prev=None):
        newnode = SingleNode.SingleNode(data)
        prevnode = self.find(prev)

        if self.head is None:
            self.add_to_empty_list(newnode)
        elif prevnode == self.tail:
            self.add_to_tail(newnode)
        elif prevnode is None:
            self.add_to_head(newnode)
        else:
            self.add_between(prevnode, newnode)

    def add_to_empty_list(self, newnode):  # add to empty list
        # newnode = SingleNode.SingleNode(data)    data = newnode
        self.head = newnode
        self.tail = newnode

    def add_to_tail(self, newnode):
        # newnode = SingleNode.SingleNode(data) data = newnode
        self.tail.next = newnode
        self.tail = newnode

    def add_to_tail_direct(self, data):  #for data test directly add to tail not searching NOT IMPORTANT
        newnode = SingleNode.SingleNode(data)
        self.tail.next = newnode
        self.tail = newnode

    def add_to_head(self, newnode):
        newnode.next = self.head
        self.head = newnode
        return newnode

    def add_between(self, prev, newnode):
        # newnode = SingleNode.SingleNode(data) data = newnode
        newnode.next = prev.next
        prev.next = newnode

    def remove(self, data):
        rmnode = self.find(data)
        if rmnode is None:
            return
        prevnode = self.find_prev(data)

        if rmnode == self.head == self.tail:
            self.remove_to_empty()
        elif rmnode == self.head:
            self.remove_head()
        elif rmnode == self.tail:
            self.remove_tail(prevnode)
        else:
            self.remove_between(rmnode, prevnode)

    def remove_between(self, rmnode, prevnode):
        prevnode.next = rmnode.next

    def remove_head(self):
        self.head = self.head.next

    def remove_tail(self, prevnode):
        self.tail = prevnode
        prevnode.next = None

    def remove_to_empty(self):
        self.head = self.tail = None

    def find(self, prev): # for adding
        if prev is None:
            return None
        p = self.head   # copy of head (we don't want to loose head)
        while p is not None:
            if p.data == prev:
                return p
            p = p.next
        return None

    def find_prev(self, data):  # for remove
        p = self.head
        while p is not None:
            if p.next is not None and p.next.data == data:
                return p
            p = p.next
        return None

    def __str__(self):
        s="[ "
        p = self.head
        while p is not None:
            s = s+str(p.data)+" "
            p = p.next
        return s+"]"