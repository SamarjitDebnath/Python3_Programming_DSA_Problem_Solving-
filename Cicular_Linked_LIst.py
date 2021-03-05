""" Circular Linked List Implementation

  ---> Head --> A -> B -> C -> D ---|
  |---------------------------------|

 This code itself is self explanatory...

 @samarjit_debnath
 """


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_begin(self, new_node):
        cur = self.head
        new_node.next = self.head
        if self.head is None:
            new_node.next = new_node
        else:
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
        self.head = new_node

    def insert_end(self, new_node):
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def print_list(self):
        if not self.head:
            print('Empty List, Nothing to Print')
            return
        current = self.head
        while current:
            print(current.data, end="  ")
            current = current.next
            if current == self.head:
                break

    def get_id(self):
        cur = self.head
        while cur:
            print('\n' + str(cur.data) + ': ' + str(id(cur)))
            cur = cur.next
            if cur == self.head:
                break

    def is_list_empty(self):
        res = False
        if self.head is None:
            res = True
        return res

    def list_len(self):
        cur = self.head
        length = 0
        while True:
            cur = cur.next
            length += 1
            if cur == self.head:
                break
        return length

    def delete_begin(self):
        if self.is_list_empty() is False:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = self.head.next
            self.head = self.head.next
        else:
            print('Empty')

    def delete_end(self):
        if self.is_list_empty() is False:
            cur = prev = self.head
            while cur.next != self.head:
                prev = cur
                cur = cur.next
            prev.next = self.head

    def delete_at_node(self, position):
        if position < 0 or position > self.list_len():
            print('Invalid Entry')
            return
        if self.is_list_empty() is False:
            if position == 0:
                self.delete_begin()
                return
        cur = prev = self.head
        cur_pos = 0
        while True:
            if cur_pos == position:
                prev.next = cur.next
                cur.next = None
                break
            prev = cur
            cur = cur.next
            cur_pos += 1

    def split_list(self):
        size = self.list_len()
        if size == 0:
            print('Empty')
            return
        if size == 1:
            return self.head

        prev = None
        counter = 0
        cur = self.head
        mid = size // 2

        while cur and counter < mid:
            counter += 1
            prev = cur
            cur = cur.next
        prev.next = self.head

        split_list = CircularLinkedList()
        while cur.next != self.head:
            split_list.insert_end(Node(cur.data))
            cur = cur.next
        split_list.insert_end(Node(cur.data))

        self.print_list()
        print()
        split_list.print_list()

    def josephus_circle(self, step):
        cur = self.head
        while self.list_len() > 1:
            count = 1
            while count != step:
                cur = cur.next
                count += 1
            print('Removed: ' + str(cur.data))
            self.delete_at_node(count)
            cur = cur.next

    def has_cycle(self):
        if self.head is None:
            return False

        ptr = self.head
        fastptr = self.head

        while ptr is not None and fastptr is not None and fastptr.next is not None:
            if ptr == fastptr:
                return True
            ptr = ptr.next
            fastptr = fastptr.next.next
        return False


# Driver code change this in accordance with your need...

if __name__ == '__main__':
    node = Node(1)
    node2 = Node(2)
    llist = CircularLinkedList()
    llist.insert_end(node)
    llist.insert_end(node2)
    llist.insert_begin(Node(10))
    llist.insert_begin(Node(20))
    llist.print_list()
    llist.get_id()
    print("\nLength: {}".format(llist.list_len()))
    llist.split_list()
    llist.delete_at_node(1)
    llist.print_list()
    llist.josephus_circle(2)
    print(llist.has_cycle())
