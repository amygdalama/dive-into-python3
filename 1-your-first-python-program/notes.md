1. What does "first-class object" mean?
    An [answer](http://stackoverflow.com/a/245208) but I still don't fully understand. I'll probably have to learn another language that has objects that aren't first class to begin to get it.

2. Whitespace defining codeblocks doesn't have to be four spaces! Cool!

3. What if we didn't use `raise ValueError`?

    With the raise statement:
        
        >>> import humansize
        >>> humansize.approximate_size(-1)
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
          File "./humansize.py", line 30, in approximate_size
            raise ValueError('number must be non-negative')
        ValueError: number must be non-negative

    Without it:

        >>> import humansize
        >>> humansize.approximate_size(-1)
        '-0.0 KiB'

4. You can do:
    
        multiple = 1024 if a_kilobyte_is_1024_bytes else 1000

Cool! I didn't know that!