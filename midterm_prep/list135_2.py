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
    def _append(self, data):
        val = List135().add(data)
        cur = self
        if cur._next == None:
            return val
        while (cur._next._next != None):
            cur = cur._next
        cur._next = val
        return self
    
    # return a sorted list135 that begins at self
    def sort(self):
        cur = self
        acc = [cur._data]
        cur = cur._next
        while (cur._next != None):
            acc.append(cur._data)
            cur = cur._next
        slist = sorted(acc)
        new135 = List135()
        for i in slist:
            a = new135._append(i) # Why doesn't this work???
        return new135
        
    
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
    a = List135()  # a --> []
    b = a.add(1).add(5).add(2)   # b --> [1]
    c = b.add(2).add(5).add(1).add(0).add(9).add(6)   # c --> [2,1]
 #   print(a)
 #   print(b)
 #   print(c)
    print(c.sort())
 #   print(List135()._append(3))