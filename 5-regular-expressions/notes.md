### Roman Numerals

* I tried making a version of this that programmatically generated a regex. Something like "for each character, we could possibly have three or less of the current character OR one previous character plus one of the current character" but it totally failed. I guess manually creating the regex is easier, and probably easier to read.

## Phone Numbers

* My first instinct would be to get rid of everything that isn't a digit and then try to cut up the phone numbers based on length of the entry. So our different entry types would be reduced to:

    * 8005551212
    * 18005551212
    * 80055512121234
    * 180055512121234
    
    I think this would work except when an extension was one digit long. So if we have a number, like 80055512121, where the last digit is the extension number, would we be able to tell if the original entry was of the form 800-555-1212 ext 1 or 8-005-551-2121? We'd have to add some extra logic for this case.

* `.groups()` is cool!

## Notes from Tom Club

* debuggex.com is cool