#  __eq__, __ne__ - by default
# dic - https://docs.python.org/3/reference/expressions.html#value-comparisons
# doc - https://docs.python.org/3/reference/datamodel.html#object.__eq__
# doc - https://docs.python.org/3/reference/datamodel.html#object.__ne__


class A:
    pass


if __name__ == "__main__":
    a1 = A()
    a1_1 = a1

    print(f"a1 == a1_1: {a1 == a1_1}")
    print(f"a1 != a1_1: {a1 != a1_1}")
    print("-" * 10)
    a2 = A()
    print(f"a1 == a2: {a1 == a2}")
