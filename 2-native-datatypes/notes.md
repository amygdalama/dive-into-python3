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
