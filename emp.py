#!/usr/bin/env python

# description: demo unittest concepts


class Employee:
    # private variable
    _raise_amount = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        # r = self.first + "." + self.last + "@email.com"
        # return r
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self._raise_amount)

    # concept of mocking


def main():
    # empty code block
    return


if __name__ == '__main__':
    main()
