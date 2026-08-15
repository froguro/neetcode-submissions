class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next= self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.head, self.tail = Node(0, 0), Node(0, 0)
        self.cache = {}
        self.capacity = capacity
        self.head.next, self.tail.prev = self.tail, self.head

    def remove(self, node):
        next, prev = node.next, node.prev
        prev.next = next
        next.prev = prev

    def insert(self, node):
        next, prev = self.tail, self.tail.prev
        prev.next = next.prev = node
        node.next, node.prev = next, prev
        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1




    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        if len(self.cache) > self.capacity:
            head = self.head.next
            self.remove(head)
            del self.cache[head.key]
        
        
