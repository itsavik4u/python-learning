
# description: google workshop day 1
import sys


def main():
    raw = r'this is \t hello \n world'
    print raw.rfind(r'this')

    a = ['a', 'b', 'c']
    b = '-----'
    print b.join(a)


if __name__ == '__main__':
    main()
