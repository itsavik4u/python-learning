#!/usr/bin/env python

# author: itsavik4u@gmail.com


class Calc:
    def __init__(self):
        self.msg = "running unit test for calc!!"

    def add(self, n, m):
        return n + m

    def sub(self, n, m):
        return n - m

    def mul(self, n, m):
        return n * m

    def div(self, n, m):
        if m == 0:
            raise ValueError('Can\'t divide by zero')
        print n/m
        return n / m


def main():
    # empty code block
    a = Calc()
    print a.add(4, 5)
    return


if __name__ == '__main__':
    main()
