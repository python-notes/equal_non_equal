# general pattern
# IMPORTANT!!!
# a big problem is complete copying of the pattern.
# Take the minimum necessary: as a rule, it will work faster.
# Although, of course, deciding what and when to use is the prerogative of the programmer alone.


class A:
    def __init__(self, main_param_1, main_param_2, additional_param):
        self.main_param_1 = main_param_1
        self.main_param_2 = main_param_2
        self.additional_param = additional_param

    def __eq__(self, other):
        if not isinstance(other, A):
            return NotImplemented
        return (
            self.main_param_1 == other.main_param_1
            and self.main_param_2 == other.main_param_2
        )

    def __hash__(self):
        return hash((self.main_param_1, self.main_param_2))
