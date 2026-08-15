class ListNode:
    def __init__(self, key = 0, val = 0, next = None, prev = None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache = {}

        
    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev
    
    def insert(self, node):
        prev, nxt = self.tail.prev, self.tail
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = ListNode(key, value)
        self.insert(self.cache[key])
        print(len(self.cache))
        if len(self.cache) > self.capacity:
            head= self.head.next
            self.remove(head)
            del self.cache[head.key]


        
