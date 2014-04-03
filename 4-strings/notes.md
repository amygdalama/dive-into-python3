#Ch 4 - Strings

## Unicode

I had some difficulty understanding this section.

1. "Not all the numbers are used"
    > Unicode is a system designed to represent every character from every language. Unicode represents each letter, character, or ideograph as a 4-byte number. Each number represents a unique character used in at least one of the world’s languages. (Not all the numbers are used, but more than 65535 of them are, so 2 bytes wouldn’t be sufficient.)

    Particularly, what does "all the numbers" mean? All the integers? All the positive integers? Some other set of numbers I'm not picking up on?

    Rob explains: 4-byte numbers mean you get to store `4**16` unicode characters. So "all the numbers" means "all of the `4**16` numbers. We don't have nearly that many characters to store, but we have more than what we could store if we used 2-byte numbers. If we used 2-byte numbers, we'd only have `2**16` spots to store characters, which means we could store 

    Also, it seems as if `65535` is actually incorrect, and this sentence would be more precise if it said `65536 == 2**16` instead.

2. "Constant time"

    > There is a Unicode encoding that uses four bytes per character. It’s called UTF-32, because 32 bits = 4 bytes. UTF-32 is a straightforward encoding; it takes each Unicode character (a 4-byte number) and represents the character with that same number. This has some advantages, the most important being that you can find the Nth character of a string in constant time, because the Nth character starts at the 4×Nth byte

    What does "constant time" mean? Is this related to big-O notation?


## A digression on `sys.getsizeof`

1. Why does this happen?

    >>> l = [1]
    >>> sys.getsizeof(l)
    80
    >>> l = []
    >>> l.append(1)
    >>> sys.getsizeof(l)
    104


## Related Links

* http://www.joelonsoftware.com/articles/Unicode.html
* https://www.youtube.com/watch?v=MijmeoH9LT4
* http://nedbatchelder.com/text/unipain.html
