"""This is a module intended to help learn what `from X import Y` does.

If we, in the Python interpreter, or in another module, type

    >>> from thing import Foo

do we also have access to Bar? Will initializing a Foo object throw
an error, since we're only importing Foo and not Bar? Or does the 
`from X import Y` statement import all of X?

What actually happens is all of `thing` is imported, but only `Foo` is
bound to a name and added to our globals.

    >>> from thing import Foo
    >>> import sys
    >>> 'thing' in sys.modules
    True
    >>> thing
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    NameError: name 'thing' is not defined
    >>> globals().keys()
    ['__builtins__', '__package__', 'sys', '__name__', 'Foo', '__doc__']

"""


class Foo(object):
    
    def __init__(self):
        self.b = Bar()

class Bar(object):    
    pass