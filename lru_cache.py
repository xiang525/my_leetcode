"""
论坛里 Double LinkedList的解法
"""
class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.dic = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key in self.dic:
            n = self.dic[key]
            self._remove(n)
            self._add(n)
            return n.val
        return -1

    def set(self, key, value):
        if key in self.dic:
            self._remove(self.dic[key])
        n = Node(key, value)
        self._add(n)
        self.dic[key] = n
        if len(self.dic) > self.capacity:
            n = self.head.next
            self._remove(n)
            del self.dic[n.key]

    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def _add(self, node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail



"""
# solution 2 使用Python的OrderedDict有序字典
# An OrderedDict is a dict that remembers the order that keys were first inserted. 
  If a new entry overwrites an existing entry, the original insertion position is left 
  unchanged. Deleting an entry and reinserting it will move it to the end.
  Python 2.7 中的OrderedDict 可以在迭代字典Items的时候保证按每项插入的顺序输出。
  当删除某项再用同样的key写入时，此项排在迭代的最后，同样是插入顺序排列的。
  可以用popitem的last=True/False来控制pop进返回最近插入的还是最早插入的，实际上就是维护了一个双向链表。
"""
class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
    	self.capacity = capacity
    	self.cache = collections.OrderedDict()
        

    # @return an integer
    def get(self, key):
    	if key not in self.cache:
    		return -1
    	value = self.cache.pop(key)
    	self.cache[key] = value # reinsert the key but the order index is changed
    	return value
        

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
    	if key in self.cache:
    		self.cache.pop(key)
    	elif len(self.cache) == self.capacity:
    		self.cache.popitem(last=False)
    	self.cache[key] = value




"""
另一种用OrderedDict()的写法;论坛里的写法
"""
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.hash = collections.OrderedDict()
        

    def get(self, key):
        """
        :rtype: int
        """
        if key not in self.hash:
            return -1
        value = self.hash.pop(key)
        self.hash[key] = value # set key as the latest one
        return value
            
        

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.hash:
            self.hash.pop(key)
        else:
            if self.capacity > 0:
                self.capacity -= 1
            else:
                self.hash.popitem(last=False) # FIFO
        self.hash[key] = value






"""
jiuzhang solution: single LinkedList 
"""
class LinkedNode:
    
    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next

class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.hash = {}
        self.head = LinkedNode()
        self.tail = self.head
        self.capacity = capacity
    
    def push_back(self, node):
        self.hash[node.key] = self.tail
        self.tail.next = node
        self.tail = node
    
    def pop_front(self):
        del self.hash[self.head.next.key]
        self.head.next = self.head.next.next
        self.hash[self.head.next.key] = self.head
        
    # change "prev->node->next...->tail"
    # to "prev->next->...->tail->node"
    def kick(self, prev):
        node = prev.next
        if node == self.tail:
            return
        prev.next = node.next
        if node.next is not None:
            self.hash[node.next.key] = prev
            node.next = None
        self.push_back(node)

    # @return an integer
    def get(self, key):
        if key not in self.hash:
            return -1
        self.kick(self.hash[key])
        return self.hash[key].next.value

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.hash:
            self.kick(self.hash[key])
            self.hash[key].next.value = value
        else:
            self.push_back(LinkedNode(key, value))
            if len(self.hash) > self.capacity:
                self.pop_front()
        






















