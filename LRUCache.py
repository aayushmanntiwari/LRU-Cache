#Steps
#1 .LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
#2.int get(int key) Return the value of the key if the key exists, otherwise return -1.
#3.void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.

from collections import *

class LRUCache:
    def __init__(self,capacity):
        self.capacity = capacity
        self.cache = OrderedDict()
    
    def get(self,key):
        '''
         if key exist we pop out the key value 
        and again we are adding  back key value to cache 
        such that they will be be in new posiiton in cache  
        '''
        if key in self.cache:
            value = self.cache.pop(key)
            self.cache[key] = value 
            return value
        return -1
    
    def put(self,key,value):
        if key in self.cache:
            self.cache.pop(key) #we pop out the key value and self.cache[key] = value will update the key with new pass value  
        if len(self.cache) == self.capacity:
            self.cache.popitem(last=False) # if this condition gets True it will  pop out the (key,value) pair from cache at index 0 
        self.cache[key] = value

cache = LRUCache(2)
cache.put(1,1)                                   
cache.put(2,2)
print(cache.cache)
print(cache.get(1))       # returns 1
cache.put(3,3)            # evicts key 2
print(cache.get(2))       # returns -1 (not found)
cache.put(4,4)            # evicts key 1
print(cache.get(1))       # returns -1 (not found)
print(cache.get(3))       # returns 3
print(cache.get(4))       # returns 4