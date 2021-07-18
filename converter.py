import sys
from typing import AnyStr
import argparse

import termcolor


def binary_conv(s: AnyStr) -> str:
    """

    :param s: input string
    :return: string in binary
    """

    res = ''
    for i in s:
        res += str(bin(ord(i))[2:]).zfill(8) + ' '
    return res.strip()


def binary_decriptor(s: AnyStr) -> str:
    """

    :param s: input binary stream
    :return:converted output
    """
    res = ''
    for entry in s.split():
        res += str(chr(int(entry, 2)))
    return res


def encode(var_1: str, var_0: str):
    global res
    res = res.replace('1', var_1)
    res = res.replace('0', var_0)


def args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--str', type=str, help="Input string", default=None)
    parser.add_argument('-b', '--bin', type=str, help="input binary strung", default=None)
    parser.add_argument('-e', '--enc', type=str,
                        help='Enable if you want to encode the string', choices=['true', 'false'], default='false')
    parser.add_argument('-o', '--one', help='1\'s to be masked with', type=str, default='xc')
    parser.add_argument('-z', '--zero', help='0\'s to be masked with', type=str, default='io')
    return vars(parser.parse_args())


if __name__ == '__main__':
    argument = args()
    if argument.get('str') is not None and argument.get('bin') is None:
        res = binary_conv(argument.get('str'))
    elif argument.get('bin') is not None and argument.get('str') is None:
        res = binary_decriptor(argument.get('bin'))
    else:
        sys.exit(termcolor.colored('Invalid Input', 'red', attrs=['dark', 'bold']))


    if argument.get('enc') == 'true':
        encode(argument.get('one'), argument.get('zero'))
    print(res)
