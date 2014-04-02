#Ch. 3 - Comprehensions

##3.2 Working with Files and Directories

I didn't know these things about `os`!:

* os.path
* os.getcwd()
* os.chdir()

Does os.chdir() also add the new current working directory to the front of the import path? Nope. Tested using `working-directory.py`.

Whoa!:

    >>> import os
    >>> os.path.sys
    <module 'sys' (built-in)>

##3.3 List Comprehensions

This is an awesome definition/explanation:

> A list comprehension provides a compact way of mapping a list into another list by applying a function to each of the elements of the list.






##Notes from Tom Club

* Read about __eq__ and __hash__ object methods
* all functions are < all lists    >:(