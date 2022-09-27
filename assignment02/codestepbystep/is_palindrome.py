
# The following code passes the is_palindrome tester at
# https://www.codestepbystep.com/problem/view/python/recursion/is_palindrome
# but is not tail-recursive.

    # def _is_palindrome(s, lo, hi): if (hi <= lo): return True else: return
    #     (s[lo].upper() == s[hi].upper()) and _is_palindrome(s, lo+1, hi-1)


    # def is_palindrome(s):
    #     return _is_palindrome(s, 0, len(s)-1)

# Rewrite the _is_palindrome function to be tail-recursive and submit the
# tail-recursive pair of functions to Code-Step-By-Step. Note: This will not
# require using an accumulator; the code can be refactored to be
# tail-recursive.

def _is_palindrome(s, lo, hi):
    if (hi <= lo):
        return True
    elif s[lo].upper() != s[hi].upper():
        return False
    else:
        return _is_palindrome(s, lo+1, hi-1)
    
def is_palindrome(s):
    return _is_palindrome(s, 0, len(s)-1)


#  Transform your tail-recursive function into the loop version following the
#  mechanical transformation seen in class (ie, the one with "while True" in
#  it).

def _is_palindrome_opt(s, lo, hi):
    while True:
        if (hi <= lo):
            return True
        elif s[lo].upper() != s[hi].upper():
            return False
        else:
            lo += 1
            hi -= 1
            
def is_palindrome_opt(s):
    return _is_palindrome_opt(s, 0, len(s)-1)

is_palindrome_opt('racecar')