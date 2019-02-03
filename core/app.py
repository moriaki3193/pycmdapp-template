# -*- coding: utf-8 -*-
"""Define the command line application.
"""
from argparse import ArgumentParser


PARSER_CONFIG = {
    'prog': '### REWRITE HERE ###',
    'description': '### REWRITE HERE ###',
}

parser = ArgumentParser(**PARSER_CONFIG)
# parser.add_argument('--dir', '-d', help='help', requred=True)


def main() -> None:
    cmdargs = vars(parser.parse_args())
