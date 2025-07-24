# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class Stack:
    def __init__(self,val=None):
        self.top=val
        self.body=[]
        if val:
            self.body.append(val)

    def push(self, val):
        self.body.append(val)
        self.top = val
        print(f"{val} was pushed into Stack, the length of stack is {len(self.body)} and stack is now: {self.body}")

    def pop(self,):
        res = self.body.pop()
        self.top = self.body[-1]
        print(f"{res} was popped from Stack, the length of stack is {len(self.body)}  and stack is now: {self.body}")
        return res


class Double_linked_list:
    def __init__(self, node: Node):
        self.head = node
        self.tail = node
        self.length = 1
        print(f"The double linked list was instantiated with the node with value of {node.value}"
              f"and length of {self.length}"
              f"Head.value -> {self.head.value}"
              f"Tail.value -> {self.tail.value}")

    def printa(self):
        next_node = self.head
        while next_node:
            print("-->", next_node.value)
            next_node = next_node.next
        print(f"Linkedlist Head is now {self.head.value}")
        print(f"Linkedlist Tail is now {self.tail.value}")
        print(f"Current length of the linkedlist is {self.length}")

    def append(self, new_node: Node):
        print(f"appending {new_node.value} to the end of the linkedlist")
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        self.length += 1
        self.printa()

    def prepend(self, new_node: Node):
        print(f"prepending the {new_node.value} to the beginning of the linkedlist")
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        self.length += 1
        self.printa()

    def insert(self, ind: int, new_node: Node):
        print(f"inserting {new_node.value} in the index of {ind}")
        if ind == 0:
            self.prepend(new_node)
        elif ind < 0:
            print("Error in in index. We are not allowed to have negative value!!")
        elif ind > self.length - 1:
            self.append(new_node)
        else:
            lead_node = self.head
            for _ in range(ind-1):
                lead_node = lead_node.next
            new_node.next = lead_node.next
            new_node.prev = lead_node
            lead_node.next.prev = new_node
            lead_node.next = new_node
            self.length += 1
            self.printa()

    def deleting(self, ind: int):
        print(f"Deleting from the index of {ind}")
        if ind > self.length - 1 or ind < 0:
            print("Wrong index is selected! the index is out of bound and does not exist")
        else:
            if ind == 0:
                self.head.next.prev = None
                self.head = self.head.next

            elif ind == self.length - 1:
                lead_node = self.head
                for _ in range(ind):
                    lead_node = lead_node.next
                lead_node.prev.next = None
                self.tail = lead_node.prev

            else:
                lead_node = self.head
                for _ in range(ind):
                    lead_node = lead_node.next
                lead_node.prev.next = lead_node.next
                lead_node.next.prev = lead_node.prev
            self.length -= 1
        self.printa()

    def reverse(self):
        cur_node = self.head
        cur_next = cur_node.next
        cur_node.next = None
        while cur_next:
            tmp = cur_next.next
            cur_next.next = cur_node
            cur_node = cur_next
            cur_next = tmp
            self.head = tmp if tmp else cur_node
        print("\n<<== The one sided linked list was successfully reversed !!!")
        self.printa()

def test_linkedlis():
    a, b, c, d, e, f, g, h, i = Node("a"), Node("b"), Node("c"), Node("d"), Node("e"), Node("f"), Node("g"), Node("h"), Node("i")
    lnk = Double_linked_list(a)
    lnk.append(b)
    lnk.prepend(c)
    lnk.append(d)
    lnk.deleting(3)
    lnk.insert(0, e)
    lnk.insert(5, f)
    lnk.insert(9, g)
    lnk.deleting(-10)
    lnk.deleting(3)
    lnk.append(h)
    lnk.insert(2, i)
    lnk.deleting(0)
    lnk.reverse()
    pass

def test_stack():
    s=Stack(1)
    s.push(3)
    s.push(5)
    s.push("ghorbanAli")
    s.pop()
    s.push("aliyar")
    s.pop()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test_linkedlis()  # print_hi('PyCharm')
    test_stack()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
