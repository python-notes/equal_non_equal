#  use of NotImplemented constant
# __eq__ (__ne__, e.t.c) can return NotImplemented constant
#  https://docs.python.org/3/library/constants.html#NotImplemented


class A:
    def __init__(self, param_1):
        self.param_1 = param_1

    def __repr__(self):
        return f"A({self.param_1})"

    def __eq__(self, other):
        print(f"in A.__eq__ with {other}")
        if not isinstance(other, A):
            print(f"A.__eq__({other}) return NotImplemented")
            return NotImplemented
        return self.param_1 == other.param_1


class B(A):

    def __repr__(self):
        return f"B({self.param_1})"

    def __eq__(self, other):
        print(f"in B.__eq__ with {other}")
        if not isinstance(other, B):
            print(f"B.__eq__({other}) return NotImplemented")
            return NotImplemented
        return self.param_1 == other.param_1


class C:
    def __init__(self, param_1):
        self.param_1 = param_1

    def __repr__(self):
        return f"C({self.param_1})"

    def __eq__(self, other):
        print(f"in C.__eq__ with {other}")
        if not hasattr(other, "param_1"):
            print(f"C.__eq__({other}) return NotImplemented")
            return NotImplemented
        return self.param_1 == other.param_1


if __name__ == "__main__":
    a1 = A(1)
    a2 = A(2)
    # print(f"a1 == a2: {a1 == a2}")
    # b1 = B(1)
    # print(f"b1 == a1: {b1 == a1}")
    c1 = C(1)
    print(f"a1 == c1: {a1 == c1}")
