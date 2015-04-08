import argparse
import scoring

__author__ = 'mwitas'


def do_single_byte_xor_brute_force(source, mode):
    results = []
    ciphertext = source.decode('hex')
    for i in range(0x00, 0xff):
        decoded = ''

        for j in range(0, len(ciphertext)):
            ch = ciphertext[j]
            decoded += chr(ord(ch) ^ i)

        if mode == 'simple':
            score = scoring.simple_score(decoded)
        else:
            score = scoring.frequency_score(decoded)

        results.append({'source': source, 'score': score, 'text': decoded, 'key': i})

    return results


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="File with ciphertext to crack", type=str)
    parser.add_argument("-m", "--mode", help="Mode of scoring", default='simple', type=str,
                        choices=['simple', 'frequency'], dest='mode')
    parser.add_argument("-n", "--results_num", help="Number or best matching results printed to screen (put 0 for all)",
                        default=3, type=int, dest="results_num")
    return parser.parse_args()


def main():
    args = parse_args()

    data = args.input_file
    results_num = args.results_num
    mode = args.mode

    f = open(data, 'r')
    result = []
    for line in f:
        stripped = line.rstrip()
        r = do_single_byte_xor_brute_force(stripped, mode)
        r.sort(key=lambda res: res['score'])

        for i in xrange(0, 3):
            result.append(r[i])

        print '.',

    result.sort(key=lambda res: res['score'] * -1)

    if results_num > 0:
        border = len(result) - results_num
    else:
        border = 0

    for i in range(border, len(result)):
        print('{}: ({} ^ {}) {} '.format(result[i]['score'], result[i]['source'], hex(result[i]['key']), result[i]['text'].rstrip()))


if __name__ == "__main__":
    main()
