import argparse

__author__ = 'mwitas'


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("in1", help="Data to encode")
    parser.add_argument("in2", help="Key for XOR")
    return parser.parse_args()


def do_xor(in1, in2):
    in1 = in1.decode('hex')
    in2 = in2.decode('hex')

    if len(in1) != len(in2):
        raise IOError("Strings must have equal length")
        return

    res = ''
    for i in range(0, len(in1)):
        res += chr(ord(in1[i]) ^ ord(in2[i]))

    return res.encode('hex')


def main():
    args = parse_args()

    in1 = args.in1
    in2 = args.in2

    print(do_xor(in1, in2))


if __name__ == "__main__":
    main()