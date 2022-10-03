# Add to the list135 class a method called sorted that returns a sorted list135
# That begins at self. Because we want to maintain persistence, the current
# version of the list135 should not be altered. The easiest way to do this is
# to build a python list from the List135, sort that list with python's sort
# method, and then build a List135 from the result. Note: lst.sort() sorts lst
# in place, and lst.append(x) appends x fo the end of lst. Building off of your
# solution from the previous question, copy your method from the previous question
# and now finish sorted so that it returns the sorted list135.

# Immutable list data structure for Sac State CSC 135 by Ted Krovetz
# Adding is done only at fronts of lists, preserving existing lists.

from typing import Callable


class List135:
    
    # create new list node. Defaults to a node representing the empty list
    def __init__(self, data=None, next=None):
        self._data = data
        self._next = next
    
    # is the list beginning with self empty?
    def empty(self):
        return self._next == None
    
    # return the first element of the list that starts with self
    def first(self):
        return self._data
    
    # return the list that begins after the list that starts with self
    def rest(self):
        return self._next
    
    # return a list beginning with data and followed by the current list
    def add(self, data):
        return List135(data, self)
   
    # Appends data to the end of a List135
    def append(self, data):
        if self._next == None:
            return List135().add(data)
        else:
            tmp = self
            while (tmp._next != None):
                last = tmp
                tmp = tmp._next
            last._next = List135().add(data)
            return self
            
    
    # Inserts a new List135 at the specified position
    def insert(self, data, position):
        pass
    
    # Extends to the end of the list
    def extend(self, data: list):
        pass
    
    # returns the number of nodes in the list
    def size(self):
        count = 0
        while (self._next != None):
            count += 1
            self = self._next
        return count
    
    
    # return a sorted list135 that begins at self
    def sort(self):
        if self._next == None:
            return self
        tmp = self
        acc = []
        while (tmp._next != None):
            acc.append(tmp._data)
            tmp = tmp._next
        acc = sorted(acc)
        new135 = List135(acc.pop(0))
        tmp = new135
        for i in range(len(acc)):
            # last node is alwaxs2 an empty List135 object
            tmp._next = List135(acc.pop(0), List135())
            tmp = tmp._next
        return new135
        
    def map(self, f : Callable):
        if self._next is None:
            # The last node of a list is points to None
            return self
        else:
            new_front = List135(f(self._data), self._next)
            cur = new_front
            while cur._next._next:
                cur._next = List135(f(cur._next._data),cur._next._next)
                cur = cur._next
            return new_front
        
    def reduce(self, f: Callable, acc):
        if self._next is None:
            return acc
        else:
            return self._next.reduce(f,f(acc,self._data))

    
    def __str__(self):
        if self._next == None:
            return "[]"
        else:
            cur = self
            acc = "[" + str(cur._data)
            cur = cur._next
            while (cur._next != None):
                acc = acc + "," + str(cur._data)
                cur = cur._next
            return acc + "]"
    

# The following is a trick to make this testing code be ignored
# when this file is being imported, but run when run directly
# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    a = List135().add(6).add(7)  # a --> []
    b = List135().add(1).add(5).add(2)   # b --> [1]
    # c = b.add(2).add(5).add(1).add(0).add(9).add(6)   # c --> [2,1]
 #   print(a)
 #   print(b)
 #   print(c)
    # print(a.sort())
    # print(List135()._append(3))
    # print(b.append(3))
    # print(a.append(3))
    # print(b.size())
    # print(b.map(lambda x : x * 2))
    # print(c.reduce(lambda acc, v : acc + 1, 0))
 
    # List135 concat
    def concat(xs1, xs2):
        if xs1.empty():
            return xs2
        elif xs2.empty():
            return xs1
        else:
            tmp = concat(xs1.rest(), xs2)
            return tmp.add(xs1.first())
    
    print(concat(a, b))