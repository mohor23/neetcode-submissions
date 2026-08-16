class Node():
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.prev=None
        self.next=None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}
        self.left=Node(0,0)
        self.right=Node(0,0)
        self.left.next=self.right
        self.right.prev=self.left
        
    def insert(self,node):
        prev_node=self.right.prev
        prev_node.next=node
        node.prev=prev_node
        node.next=self.right
        self.right.prev=node

    def remove(self,node):
        prev=node.prev
        nxt=node.next
        prev.next=nxt
        nxt.prev=prev

    def get(self, key: int) -> int:
        if key in self.cache:
            node=self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.insert(node)
        else:
            node=Node(key,value)
            self.insert(node)
            self.cache[key]=node
            if len(self.cache)>self.capacity:
                lru = self.left.next
                self.remove(lru)
                del self.cache[lru.key]


