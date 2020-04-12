class LRU_Cache:

    def __init__(self, capacity):
        if not isinstance(capacity, int) or capacity < 1:
            raise ValueError("The capacity should be a positive integer!")
        else:
            self.capacity = capacity
        self.cache = {}
        self.doubly_linked_list = self._DoublyLinkedList()

    def set(self, key, value):
        if key in self.cache:
            existing_node = self.cache[key]
            existing_node.value = value
            self.doubly_linked_list._set_head(existing_node)
        else:
            new_node = self._Node(key, value)
            if len(self.cache) == self.capacity:
                oldest_node = self.doubly_linked_list._pop()
                del self.cache[oldest_node.key]
            self.cache[key] = new_node
            self.doubly_linked_list._prepend(new_node)

    def get(self, key):
        if key in self.cache:
            target_node = self.cache[key]
            self.doubly_linked_list._set_head(target_node)
            return target_node.value
        else:
            return -1
        
    class _DoublyLinkedList:
    
        def __init__(self):
            self.head = None
            self.tail = None

        def _prepend(self, new_node):
            head = self.head
            if head:
                head.prev_node = new_node
                new_node.next_node = head
                self.head = new_node
            else:
                self.head = new_node
                self.tail = self.head

        def _pop(self):
            head = self.head
            tail = self.tail
            if head is tail:
                self.head = None
                self.tail = None
                return head
            else:
                tail = self.tail
                tail.prev_node.next_node = None
                self.tail = tail.prev_node
                tail.prev_node = None
                return tail

        def _set_head(self, existing_node):
            if existing_node.key == self.head.key:
                return
            elif existing_node.key == self.tail.key:
                tail = self._pop()
                self._prepend(tail)
            else:
                existing_node.prev_node.next_node = existing_node.next_node
                existing_node.next_node.prev_node = existing_node.prev_node
                existing_node.prev_node = None
                existing_node.next_node = None
                self._prepend(existing_node)
        
    class _Node:
        
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.prev_node = None
            self.next_node = None


if __name__ == "__main__":
    print("Test 1 - Normal Case")
    our_cache = LRU_Cache(5)
    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)
    print(our_cache.get(1))   # returns 1
    print(our_cache.get(2))   # returns 2
    print(our_cache.get(9))  # returns -1 because 9 is not present in the cache
    our_cache.set(5, 5) 
    our_cache.set(6, 6)
    print(our_cache.get(3))  # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
    print("Test 2 - Edge Case 1") # Case where LRU cache has only one slot
    our_cache = LRU_Cache(1)
    our_cache.set(0, 1)
    print(our_cache.get(0))   # returns 1
    print(our_cache.get(1))   # returns -1
    our_cache.set(3, 2)
    our_cache.set(4, 2)
    print(our_cache.get(0))   # returns -1
    print(our_cache.get(3))   # returns -1
    print(our_cache.get(4))   # returns 2
    print("Test 3 - Edge Case 2") # Case where an insertion of duplicate key causes an update of existing value
    our_cache = LRU_Cache(2)
    our_cache.set(0, 1)
    our_cache.set(1, 0)
    print(our_cache.get(0)) # returns 1
    print(our_cache.get(1)) # returns 0
    our_cache.set(1, 3)
    print(our_cache.get(1)) # returns 3