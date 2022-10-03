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
        
    def filter(self, f):
        if self._next is None: # Empty case
            return self
        elif self._next._next is None: # Base Case
            t = List135(self._data, List135()) if f(self._data) else List135()
            return t
        else:
            t1 = self._next.filter(f)
            t2 = t1.add(self._data) if f(self._data) else t1
            return t2
                

# The following is a trick to make this testing code be ignored
# when this file is being imported, but run when run directly
# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    a = List135().add(2).add(-1).add(3).add(-2)   # c --> [-2, 3, -1, 2]
    b = List135().add(2)
    print(a.filter(lambda x : x < 0))
    print(b.filter(lambda x : x == 0))
    
