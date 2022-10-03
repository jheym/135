# Immutable list data structure for Sac State CSC 135 by Ted Krovetz
# Adding is done only at fronts of lists, preserving existing lists.

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
        
    def reduce(self, f, acc):
        if self._next is None: # Base case
            return acc
        else:
            return self._next.reduce(f, f(acc, self._data))
            
            
        
        
    

# The following is a trick to make this testing code be ignored
# when this file is being imported, but run when run directly
# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    a = List135()  # a --> []
    b = a.add(1)   # b --> [1]
    c = b.add(2)   # c --> [2,1]
    # print(a)
    # print(b)
    # print(c)
    print(a.reduce(lambda acc, v : acc + 1, 0))