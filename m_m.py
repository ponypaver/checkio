min = lambda *args, key=None: sorted(iter(args if len(args) > 1 else args[0]), key=key)[0]

def max(*args, key=None):
    if len(args) == 1:
        args = args[0]
    return sorted(args, key=key, reverse=True)[0]

min, max = (lambda *args, key=None, r=r: sorted(args[0] if len(args) == 1 else args, key=key, reverse=r)[0] for r in range(2))

def test():
    #print(min(2.2,5.6,5.9, key=int),min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]))
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"

if __name__ == '__main__':
    test()
