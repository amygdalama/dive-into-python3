# Ch. 7 - Classes & Iterators

## 7.4 - Instance Variables

* Ah, I'm beginning to understand when you need to use `self.`
for naming variables.

        >>> class Foo:  
        ...     def __init__(self):
        ...             self.a = 7
        ... 
        >>> Foo.a
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
        AttributeError: type object 'Foo' has no attribute 'a'
        >>> f = Foo()
        >>> f.a
        7

        >>> class Bar:
        ...     a = 7     
        ...     def __init__(self):
        ...             self.a = "not 7"
        ... 
        >>> Bar.a
        7
        >>> b = Bar()
        >>> b.a
        'not 7'

        >>> class Bar:
        ...     a = 7
        ...     def __init__(self):
        ...             self.a = "not 7"
        ...             print(locals())
        ... 
        >>> Bar.a
        7
        # `a` is not in the locals() inside __init__, because free 
        # variables aren't included in the locals() inside class methods
        >>> b = Bar()
        {'self': <__main__.Bar object at 0x101b193d0>}
        >>> b.__dict__
        {'a': 'not 7'}
        >>> Bar.__dict__.keys()
        dict_keys(['a', '__init__', '__module__', '__dict__', '__doc__', '__weakref__'])


## A plural rule iterator

* I don't understand the cache-ing...