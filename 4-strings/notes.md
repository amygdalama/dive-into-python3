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

    Why does the Nth character start at the 4xNth byte? Ah, I think it's because each character takes up 4 bytes. So this statement (the Nth character starts at the MxNth byte) is true for any M... So why is this an advantage of the UTF-32 system? Isn't it an advantage of *any* system with a constant number of bytes per character?
    Oh, I see. If you have a 2-byte per character system (i.e. UTF 16), then you don't have enough spaces for characters. So characters that are rarely used take up more bytes! So you can assume *most of the time* that characters are two bytes and that the Nth character of a string starts at the 2xNth byte, *except when the string has a rare "astral plane" character.*

3. Big-endian vs Little-endian
    
    > But there are also non-obvious disadvantages to both UTF-32 and UTF-16. Different computer systems store individual bytes in different ways. That means that the character U+4E2D could be stored in UTF-16 as either 4E 2D or 2D 4E, depending on whether the system is big-endian or little-endian.

    I should figure out what this means.

## Formatting Strings

1. I'm not super familiar with the syntax:

    ```
    >>> username = 'mark'
    >>> password = 'papayawhip'
    >>> "{0}'s password is {1}".format(username, password)
    ```

  This is more familiar to me:

    ```
    >>> "%s's password is %s" % (username, password)
    ```

  Are they equivalent?


## A digression on `sys.getsizeof`

1. Why does this happen?

    ```
    >>> l = [1]
    >>> sys.getsizeof(l)
    80
    >>> l = []
    >>> l.append(1)
    >>> sys.getsizeof(l)
    104
    ```

## Related Links

* http://www.joelonsoftware.com/articles/Unicode.html
* https://www.youtube.com/watch?v=MijmeoH9LT4
* http://nedbatchelder.com/text/unipain.html
