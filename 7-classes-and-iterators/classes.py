class Foo:
    def func():
        return 1
    def other_func():
        # The following throws an error because func isn't
        # in the locals() or globals()
        # return func()

        # Instead we need to tell Python where to find func(), like so:
        return Foo.func()

# Usually we instead use the func() as an instance variable, i.e:

class Bar:
    # def __init__(self):
    #     pass
    def func(self):
        return 1
    def other_func(self):
        return self.func()

