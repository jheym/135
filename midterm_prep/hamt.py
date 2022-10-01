# Add to the hamt class a method called reduce that behaves similarly to reduce
# on lists. It should take an initial value 'init' and a two-input function
# 'f(acc, value)' and accumulate the result of applying f to each value in the
# tree along with an accumulator that gets updated with each call.
#
# For example, if 1, 2, 3, 4 were the values in hamt x, then x.reduce(f, 0)
# should evaluate to f( f( f( f(0, 1), 2), 3), 4). You may assume that the
# operation f is associative and commutative, so the order of visiting the
# values does not matter.
#
# An example of such a reduce function would be to count elements (ie, like the
# len function from homework). x.reduce(lambda a, v: a + 1, 0) would start with
# 0 and add one for each value visited.
#
# Hint: if "acc" holds a value after reducing one of your subtrees, acc =
# (other child).reduce(f, acc) will update acc with the reduction of the next
# child's tree
##############################################################################
##############################################################################
# Hash Array Mapped Trie - Used in CSC 135, Sacramento State Written by Ted
# Krovetz, February 2022; updated September 2022
# 
# This implementation assumes that the objects pointed at by the key and value
# references stored in the HAMT structure do not change during the lifetime of
# the structure.
class hamt:
    
    DEG  = 4     # Children per node (must be power of 2)
    BITS = 2     # log2(DEG), bits needed to select child
    MASK = 0b11  # Bitmask for extracting low BITS bits (DEG - 1)
    
    def __init__(self, key, value, children=None):
        self._key = key
        self._value = value
        if children == None:
            self._children = [None] * hamt.DEG
        else:
            self._children = children
    
    def _set(self, key, value, hashbits):
        # Each node encountered during search will get altered.
        # To maintain persistence, each is duplicated, updated, returned.
        if (self._key == key):
            # This node matches key. Return duplicate with new value
            return hamt(self._key, value, self._children)
        else:
            # Will make copy of self, update a child reference, and return copy
            copyofself = hamt(self._key, self._value, list(self._children))
            # Continue search using hashbits to pick direction
            child_num = hashbits & hamt.MASK
            # Check if subtree exists in that direction
            if (self._children[child_num] == None):
                # End of search, key not found, add new node to copy of self
                copyofself._children[child_num] = hamt(key, value)
            else:
                # Ask appropriate child to set key/value, receive updated ref
                updatedchildtree = self._children[child_num].     \
                                    _set(key, value, hashbits >> hamt.BITS)
                # Add updated child tree to copy of self
                copyofself._children[child_num] = updatedchildtree
            return copyofself
    
    def set(self, key, value):
        # Pass key/value and hashbits to recursive helper
        return self._set(key, value, hash(key))
    
    def __str__(self):
        s = "[({},{})".format(str(self._key),str(self._value))
        for i in range(hamt.DEG):
            if (self._children[i] == None):
                s = s + "X"
            else:
                s = s + str(self._children[i])
        return s + "]"
        
    def _get(self, key, hashbits):
        if self._key == key:
            return self._value
        else:
            child_num = hashbits & hamt.MASK
            if self._children[child_num]._key == key:
                return self._children[child_num]._value
            else:
                return self._children[child_num]._get(key, hashbits >> hamt.BITS)
   
    # Returns the value that key maps to, or None if not mapped
    def get(self, key):
        return self._get(key, hash(key))
    
    
    # Returns a Python set containing all the values in the HAMT
    def valueset(self):
        
        # Private helper function for clarity
        def _noChildren(children):
            for i in range(hamt.DEG):
                if children[i] != None:
                    return False
            return True
        
        
        if _noChildren(self._children): # base case
            return {self._value}
        else:
            s = set()
            for i in range(hamt.DEG):
                if self._children[i] != None:
                    s = s | self._children[i].valueset()
            return s | {self._value}
    
    # f is a function that takes two values
    def reduce(self, f, init=None):
        
        acc = init
        
        def _noChildren(children):
            for i in range(hamt.DEG):
                if children[i] != None:
                    return False
            return True
    
        if _noChildren(self._children): # base case
            acc = f(acc, self._value)
            return acc
        else:
            for element in range(hamt.DEG):
                if self._children[element] is not None:
                    acc = self._children[element].reduce(f, acc)
            return f(acc, self._value)

# The following is a trick to make this testing code be ignored
# when this file is being imported, but run when run directly
# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    a = hamt("A", "a")
    b = a.set("B", "b")
    c = b.set("C", "c")
    d = c.set("D", "d")
    e = d.set("E", "e")
    f = e.set("F", "f")
    # print(a)
    # print(b)
    # print(c)
    # print(d)
    # print(e)
    # print(f)
    # print(f.get("F"))
    # print(f.valueset())
    print(f.reduce((lambda a, v : a + v)))
