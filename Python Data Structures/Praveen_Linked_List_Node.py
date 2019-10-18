class Node():
    def __init__(self, data):
        self.data = data

a = Node(10)
b = Node(20)

# a.next , next will become automatically part of a, we can also mention it inside the class if needed (as done in the main Linked list program)
a.next = b
b.next = None

print(a.data)
print(a.next.data)