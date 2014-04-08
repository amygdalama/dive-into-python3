import re


def build_match_and_apply_functions(pattern, search, replace):

    def matches_rule(word):
        return re.search(pattern, word)

    def apply_rule(word):
        return re.sub(search, replace, word)

    return (matches_rule, apply_rule)


def rules(filename='rules.txt'):
    with open(filename) as rules_file:
        for line in rules_file:
            pattern, search, replace = line.split()
            yield build_match_and_apply_functions(pattern, search, replace)


def plural(word):
    for matches_rule, apply_rule in rules():
        if matches_rule(word):
            return apply_rule(word)


if __name__ == '__main__':
    rules('rules.txt')