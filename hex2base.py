__author__ = 'mwitas'

import argparse
import base64

debug = True

choice_hex = 'hex'
choice_base64 = 'base64'
choices = [choice_hex, choice_base64]


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_format", choices=choices, help="Format of input data")
    parser.add_argument("output_format", choices=choices, help="Desired format of output data")
    parser.add_argument("input_data", help="Data to convert")
    return parser.parse_args()


def not_implemented_yet(input, output):
    print '[{0} -> {1}] Not implemented yet'.format(input, output)


def hex2base64(data):
    return base64.encodestring(data.decode('hex'))


def base642hex(data):
    return base64.decodestring(data).encode('hex')


def main():
    args = parse_args()

    input_data = args.input_data
    input_format = args.input_format
    output_format = args.output_format

    if debug:
        print("Input data: {0}\nInput format: {1}\nOutput format: {2}".format(input_data, input_format, output_format))

    if input_format == choice_hex:
        if output_format == choice_base64:
            print hex2base64(input_data)
        else:
            not_implemented_yet(input_format, output_format)

    elif input_format == choice_base64:
        if output_format == choice_hex:
            print base642hex(input_data)
        else:
            not_implemented_yet(input_data, output_format)

    else:
        not_implemented_yet(input_format, output_format)


if __name__ == "__main__":
    main()