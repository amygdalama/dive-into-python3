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
