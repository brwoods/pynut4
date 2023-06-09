# using __init_subclass__
class C:
    def __init_subclass__(cls, foo=None, **kw):
        print(cls, kw)
        super().__init_subclass__(**kw)

class D(C, foo='bar'):
    pass



# using __set_name__
class Attrib:
    def __set_name__(self, cls, name):
        print(f'Attribute {name!r} added to {cls}')

class AClass:
    some_name = Attrib()



class MyMeta(type):
    def __str__(cls):
        return f"Beautiful class {cls.__name__!r}"

class MyClass(metaclass=MyMeta): pass

x = MyClass()
print(type(x))
