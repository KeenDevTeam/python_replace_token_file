#!/usr/bin/python

import argparse


def str2bool(v):
    if isinstance(v, bool):
       return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


parser = argparse.ArgumentParser(description='Replace tokens in a text file')
parser.add_argument('--token', metavar='t', type=str,
                    help='Token to replace', required=True)
parser.add_argument('--value', metavar='v', type=str,
                    help='Value to substitude with token', required=True)
parser.add_argument('--file', metavar='f', type=str,
                    help='File to be modified', required=True)
parser.add_argument('--all', metavar='a', type=str2bool,
                    help='Replace all occurrences', required=False, default=True)

args = parser.parse_args()


if __name__ == "__main__":
    file_content = ""

    # Read
    with open(args.file, 'r') as fd:
        file_content = fd.read()

    # Modify
    file_content = file_content.replace(
        args.token, args.value) if args.all else file_content.replace(args.token, args.value, 1)

    # Write
    with open(args.file, 'w') as fd:
        fd.write(file_content)
