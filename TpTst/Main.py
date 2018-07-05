class MyMetaClass(type):
    lst_ = []

    def __new__(mcs, *args, **kwargs):
        obj_ = type.__new__(mcs, *args, **kwargs)
        mcs.lst_.append(obj_.__name__)
        return obj_


class test(MyMetaClass):
    pass

t1 = test()

