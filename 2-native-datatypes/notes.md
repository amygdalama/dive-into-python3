# Chapter 2 - Data Types

##Booleans

Whoa.

> You can use virtually any expression in a boolean context.

So I tried:

    >>> if 2 + 3:
    ...     print(True)
    ... else:
    ...     print(False)
    ... 
    True
    >>> if 0:
    ...     print(True)
    ... else:
    ...     print(False)
    ... 
    False

I think what happens is something like this:

    >>> if bool(2+3):
    ...     print(True)
    ... else:
    ...     print(False)
    ...  
    True

So Python will take the expression in the if statement and attempt to cast it as a boolean.

Holy shit you can treat booleans like numbers! So you can:

    >>> True + True
    2
    >>> True * 3
    3
    >>> (True + True) ** 16
    65536

##Lists

Slicing - I didn't realize stuff like this wouldn't throw errors!:

    >>> things = ['a', 'b', 'c', 'd', 'e']
    >>> things
    ['a', 'b', 'c', 'd', 'e']
    >>> things[3:-2]
    []
    >>> things[3:-3]
    []
    >>> things[3:-4]
    []
    >>> things[3:-27]
    []
    >>> things[27:-1] 
    []

practicing my list methods:

    >>> things = ['a', 'thing1', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 0, False, True, 'thing2', 'a', 'a', 'a']
    >>> things
    ['a', 'thing1', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 0, False, True, 'thing2', 'a', 'a', 'a']
    >>> len(things)
    17
    >>> while 'a' in things:
    ...     things.remove('a')
    ... 
    >>> things
    ['thing1', 0, False, True, 'thing2']

Are there better/faster/more elegant ways to do this? How do you find ways that are faster/better/more elegant? What are some less elegant/worse ways to do this? Maybe, for some simple lines of code, brainstorm all the different ways one could go about it and then pick the best way. That could be a good exercise. Even think: functionally, recursively, weird builtin methods, etc.

lists as bools:

    >>> bool([])
    False
    >>> bool([''])
    True
    >>> bool([[]])
    True
    >>> bool([False])
    True

##Tuples

Paraphrasing from the book, because I need to drill this into my head:

Why use tuples? When to use them?

* Tuples are immutable, so when you have some data that is list-like but you don't want to accidentally change within your program, use a tuple instead of a list. Then you'll get an error if you or someone else tries to change it.
* Tuples are faster than lists (faster to iterate through, faster to search). So, if you have a list that's just a constant list of constants, you might as well use a tuple instead of a list.
* Tuples can be used as dictionary keys, but lists can't.

