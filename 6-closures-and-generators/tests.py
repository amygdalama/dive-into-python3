import pluralize


TESTS = (('cheetah', 'cheetahs'),
         ('fax', 'faxes'),
         ('waltz', 'waltzes'), 
         ('coach', 'coaches'),
         ('candy', 'candies'),
         ('day', 'days'),
         ('cat', 'cats'))

if __name__ == '__main__':
    print('singular' + '\t' + 'plural' + '\t' + 'prediction')
    for singular, plural in TESTS:
        prediction = pluralize.plural(singular)
        error = '' if prediction == plural else 'x'
        print('%s\t%s\t%s\t%s' % (singular, plural, prediction, error))
