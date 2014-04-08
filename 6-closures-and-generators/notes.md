# Ch 6 - Closures and Generators

## 6.2 - Regex

* Spend more time practicing with remembering groups (like the last example in this section)

* Try building myself in a couple different ways without looking

* Use regex on my phonebook lookups!

## 6.3 - A list of functions

* Revisit the pipeline - try to build it myself without looking

* See what it takes to add a new rule to each version of the program - with pipeline, without pipeline

## 6.4 - A List of Patterns

* Ack. How does Python know what "word" is in the lower-order functions?

        def build_match_and_apply_functions(pattern, search, replace):
            def matches_rule(word):                                     
                return re.search(pattern, word)
            def apply_rule(word):                                       
                return re.sub(search, replace, word)
            return (matches_rule, apply_rule)   

* Revisit this list comprehension

        rules = [build_match_and_apply_functions(pattern, search, replace)  
                 for (pattern, search, replace) in patterns]

* Putting the rules for the pluralization in a text file is *so cool* and *such a good idea*... Maybe I should try doing something like this with my phonebook? Like for storing the names of the tables or something for the database?

## 6.5 - A file of patterns


## 6.6 - Generators


## Reconstructing example

* I need to figure out a better way to handle pretty printing. Ex: results of my tests.

## Tom Club

* Whoa! Let's look at the locals() inside a closure:

        >>> def make_contains_function(x):
        ...     print('locals of factory function', locals())
        ...     def contains(s):
        ...         print('locals of inner function', locals())
        ...         return x in s
        ...     return contains
        ...
        >>> contains_a = make_contains_function('a')
        locals of factory function {'x': 'a'}
        >>> contains_a('asdkfj')
        locals of inner function {'x': 'a', 's': 'asdkfj'}
        True

    More details can be given by func.co_varnames, func.freevars (?)

* When we're running a generator, where do we store "where" we are in the generator? A generator object must contain all of the information of the function part but also information on where it was paused! Actually functions must also store this information too, or it must be somewhere.... where does Python store "where" we are in a program??

* My mental model for what is a statement vs an expression was incorrect. I was previously thinking "statements are things that allow you to use spaces" or something of the sort which is wrong. 
    New mental model: statements are things that execute code but don't return values (so you can't bind them to a name)

* Why hadn't I realized this before? 

        >>> from __future__ import division
        >>> division
        _Feature((2, 2, 0, 'alpha', 2), (3, 0, 0, 'alpha', 0), 8192)

    This does more than bind the name `division` - it changes the behavior of the `/` operator.

    Similarly, 

        >>> from __future__ import print_function

    does more than bind the name `print_function`... it actually doesn't perform the standard `import` protocol, I don't believe...

