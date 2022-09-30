# Sanity tester. This is not a thorough test of your submission. It
# is your responsibility to test thoroughly. The sole purpose of this
# file is to do one test to make sure your submission is callable
# and type-correct

from hamt_hw import hamt

a = hamt("A", "a")
b = a.set("B", "b")
c = b.set("C", "c")
d = c.set("D", "d")
e = d.set("E", "e")
f = e.set("F", "f")
print("Pass" if f.get("D") == "d" else "Fail")
print("Pass" if f.valueset() == {"a","b","c","d","e","f"} else "Fail")
