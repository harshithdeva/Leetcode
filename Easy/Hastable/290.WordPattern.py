def wordPattern(self, pattern: str, s: str) -> bool:
        t = s.split()
        return [*map(pattern.index, pattern)] == [*map(t.index, t)]

# Index return the index of first occurance of an element
# The map() function in Python is a built-in function that allows you to apply a specified function to each item in an iterable (like a list or tuple) and returns a map object (which is an iterator) of the results.
# * operator is used to unpack the map into a list