class A:
    pass


def eq_by_default():
    a1 = A()
    a2 = A()
    return a1 == a2


def ne_by_default():
    a1 = A()
    a2 = A()
    return a1 != a2


class B:
    def __eq__(self, other):  #  a == b ---> a.__eq__(b)
        return self is other

    def __ne__(self, other):  #  a != b ---> a.__ne__(b)
        return not self == other


def eq_by_self():
    b1 = B()
    b2 = B()
    return b1 == b2


def ne_by_self():
    b1 = B()
    b2 = B()
    return b1 != b2


if __name__ == "__main__":
    import timeit

    print("__eq__ by default", min(timeit.repeat("eq_by_default()", globals=globals())))
    print("__ne__ by default", min(timeit.repeat("ne_by_default()", globals=globals())))

    print("-" * 80)

    print("__eq__ by python", min(timeit.repeat("eq_by_self()", globals=globals())))
    print("__ne__ by python", min(timeit.repeat("ne_by_self()", globals=globals())))
