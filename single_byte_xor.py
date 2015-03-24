import argparse
import os

__author__ = 'mwitas'


def simple_score(data):
    result = 0
    for i in range(0, len(data)):
        if data[i] in 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890 ':
            result += 2
        else:
            result -= 1

    return result


def generate_list():


def frequency_score(sample, data):
    if not os.path.isfile(sample):
        raise IOError('Sample must be file')
    else:
        handle_sample = open(sample, 'r')
        text_sample = handle_sample.readall()

    if os.path.isfile(data):
        handle_data = open(data, 'r')
        text_data = handle_data.readall()
    else:
        text_data = data

    src = []
    dst = []

    # for i in xrange(0, 1):
        # generate list






def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="Ciphertext to crack", type=str)
    parser.add_argument("-n", "--results_num", help="Number or best matching results printed to screen (put 0 for all)",
                        default=3, type=int, dest="results_num")
    return parser.parse_args()


def do_single_byte_xor_brute_force(ciphertext):
    results = []
    for i in range(0x00, 0xff):
        res = ''

        for j in range(0, len(ciphertext)):
            ch = ciphertext[j]
            res += chr(ord(ch) ^ i)

        result_string = "{:04d}: {}".format(simple_score(res), res)
        results.append(result_string)

    return results


def main():
    args = parse_args()

    data = args.input
    results_num = args.results_num

    result = do_single_byte_xor_brute_force(data.decode('hex'))
    result.sort()

    if results_num > 0:
        border = len(result) - results_num
    else:
        border = 0

    for i in range(border, len(result)):
        print(result[i])


if __name__ == "__main__":
    main()