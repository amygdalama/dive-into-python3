def make_counter(x):
    print("entering the make_counter function")
    while True:
        yield x
        print("incrementing x")
        x+=1

def run_counter(x):
    counter = make_counter(x)
    print("entering the run_counter function")
    while True:
        yield next(counter)
