1. What does "first-class object" mean?

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

