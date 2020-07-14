#!/usr/bin/env python3
"""
Implementation of the NoDict assignment
"""

__author__ = 'chrisescobedo0617'


class Node:
    def __init__(self, key, value=None):
        self.hash = hash(key)
        self.key = key
        self.value = value

    def __repr__(self):
        return f'{self.__class__.__name__}({self.key}, {self.value})'

    def __eq__(self, other):
        if self.key == other.key:
            return True
        else:
            return False



class NoDict:
    def __init__(self, num_buckets=10):
        """instance variables"""
        self.num_buckets = num_buckets
        self.buckets = [ [] for _ in range(num_buckets) ]

    def __repr__(self):
        """Return a string representing the NoDict contents."""
        return '\n'.join([f'{self.__class__.__name__}.{i}:{bucket}' for i, bucket in enumerate(self.buckets)])

    def add(self, key, value):
        """accepts a new key and value, and store it into the NoDict instance"""
        newNode = Node(key, value)
        bucket = self.buckets[newNode.hash % self.num_buckets]
        for k in bucket:
            if k.__eq__(newNode):
                bucket.remove(k)     
        bucket.append(newNode)
        

    def get(self, key):
        """performs a key-lookup in the NoDict class"""
        newNode = Node(key)
        bucket = self.buckets[newNode.hash % self.num_buckets]
        for k in bucket:
            if k.__eq__(newNode):
                return k.value
        raise KeyError(f'{key} not found')


    def __getitem__(self, key):
        """enables square-bracket reading behavior."""
        return self.get(key)

    def __setitem__(self, key, value):
        """enables square-bracket assignment behavior"""
        self.add(key,value)

dict1 = NoDict()
print(dict1.add('chris', 7))
print(dict1)