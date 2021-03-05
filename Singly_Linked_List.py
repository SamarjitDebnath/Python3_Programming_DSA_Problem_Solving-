"""
This program contains all the basic operation on a singly Linked List
Singly Linked list is a liner data structure which stores the data and can keep the reference of it's
adjacent node.

Basic Structure of a linked list
Head ---> A -> B -> C -> D -> NULL

@samarjit_debnath
"""

# Node definition - Which contains a Data part and link part


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked-list definition & all the operations


class LinkedList:
    def __init__(self):
        self.head = None

    # create a linked list

    def create_list(self, new_node):
        if not self.head:
            self.head = new_node
            new_node.next = None
        else:
            temp = self.head
            self.head = new_node
            self.head.next = temp
            del temp

    # print the linked list

    def print_list(self):
        if not self.head:
            print('Empty List, Nothing to Print')
            return
        current = self.head
        while True:
            if current:
                print(current.data, end="  ")
                current = current.next
            else:
                break

    # insert an element at the starting position of a linked list

    def insert_head(self, new_node):
        if not self.head:
            print('Empty List')
            return
        temp = self.head
        self.head = new_node
        self.head.next = temp
        del temp

    # insert an element at the ending position of a linked list

    def insert_end(self, new_node):
        if not self.head:
            self.head = new_node
        else:
            last = self.head
            while True:
                if last.next is None:
                    break
                last = last.next
            last.next = new_node
            new_node.next = None

    # insert an element at the given position of a linked list

    def insert_at_node(self, new_node, position):
        if position == 0:
            self.insert_head(new_node)
            return
        if position < 0 or position > self.list_len():
            print('Invalid Entry')
            return
        cur = self.head
        prev = self.head
        cur_pos = 0
        while True:
            if cur_pos == position:
                prev.next = new_node
                new_node.next = cur
                break
            prev = cur
            cur = cur.next
            cur_pos += 1

    # calculate the list length using iterative method

    def list_len(self):
        cur = self.head
        length = 0
        while cur is not None:
            cur = cur.next
            length += 1
        return length

    # delete an element from the ending position of a linked list

    def delete_end(self):
        cur = self.head
        prev = self.head
        while cur.next is not None:
            prev = cur
            cur = cur.next
        prev.next = None

    # check if the list is empty or not

    def is_list_empty(self):
        res = False
        if self.head is None:
            res = True
        return res

    # delete an element from the starting position of a linked list

    def delete_head(self):
        if self.is_list_empty() is False:
            prev = self.head
            self.head = self.head.next
            prev.next = None
        else:
            print('Empty List Nothing to Delete')

    # delete an element from the given position of a linked list

    def delete_between_node(self, position):
        if position < 0 or position > self.list_len():
            print('Invalid Entry')
            return
        if self.is_list_empty() is False:
            if position == 0:
                self.delete_head()
                return
        cur = self.head
        prev = self.head
        cur_position = 0
        while True:
            if cur_position == position:
                prev.next = cur.next
                cur.next = None
                break
            prev = cur
            cur = cur.next
            cur_position += 1

    # reverse the list in by using iterative method

    def reverse_iterative(self):
        prev = None
        cur = self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev

    # reverse the list in by using recursive method

    def reverse_recursive(self):

        def _reverse_recursive(cur, prev):
            if not cur:
                return prev
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            return _reverse_recursive(cur, prev)

        self.head = _reverse_recursive(cur=self.head, prev=None)

    # calculate length of the list in by using recursive method

    def list_len_recursive(self, node):
        if not node:
            return 0
        return 1 + self.list_len_recursive(node.next)

    # check if the list contains cycle or not

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


# main function

if __name__ == '__main__':
    print("****** Menu *******\n")
    print("1.   Create List\n"
          "2.   Insert at the Beginning\n"
          "3.   Insert at the End\n"
          "4.   Insert at any Node\n"
          "5.   Delete from the End\n"
          "6.   Print List\n"
          "7.   Delete Head\n"
          "8.   Delete Between Node\n"
          "9.   Reverse in Iterative way\n"
          "10.  Reverse in Iterative way\n"
          "11.  List Length Iterative\n"
          "12.  List Length Recursive\n"
          "13.  Detect Cycle\n"
          "0.   Exit\n")
    n = input('Enter Option: ')
    n = int(n)

    l_list = LinkedList()
    while n != 0:
        if n == 1:
            if l_list.is_list_empty() is True:
                data = input('Enter Data: ')
                node = Node(data)
                l_list.create_list(node)
                n = input('Enter Option: ')
                n = int(n)
            else:
                print('A List already has been created! try other option...')
                n = input('Enter Option: ')
                n = int(n)
        if n == 2:
            data = input('Enter Data: ')
            node = Node(data)
            l_list.insert_head(node)
            n = input('Enter Option: ')
            n = int(n)
        if n == 3:
            data = input('Enter Data: ')
            node = Node(data)
            l_list.insert_end(node)
            n = input('Enter Option: ')
            n = int(n)
        if n == 4:
            data = input('Enter Data: ')
            node = Node(data)
            pos = input('Enter position: ')
            l_list.insert_at_node(node, int(pos))
            n = input('Enter Option: ')
            n = int(n)
        if n == 5:
            l_list.delete_end()
            n = input('Enter Option: ')
            n = int(n)
        if n == 6:
            l_list.print_list()
            n = input('\nEnter Option: ')
            n = int(n)
        if n == 7:
            l_list.delete_head()
            n = input('Enter Option: ')
            n = int(n)
        if n == 8:
            pos = input('Enter position: ')
            l_list.delete_between_node((int(pos) - 1))
            n = input('Enter Option: ')
            n = int(n)
        if n == 9:
            l_list.reverse_iterative()
            n = input('Enter Option: ')
            n = int(n)
        if n == 10:
            l_list.reverse_recursive()
            n = input('Enter Option: ')
            n = int(n)
        if n == 11:
            print(l_list.list_len())
            n = input('Enter Option: ')
            n = int(n)
        if n == 12:
            print(l_list.list_len_recursive(l_list.head))
            n = input('Enter Option: ')
            n = int(n)
        if n == 13:
            print(l_list.has_cycle())
            n = input('Enter Option: ')
            n = int(n)





