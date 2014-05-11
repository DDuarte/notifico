#!/usr/bin/env python
# encoding: utf-8
"""ein-server

Commands:
    www             Start the embedded Flask HTTP server.

Usage:
    ein-server www [--debug --port=<n> --host=<ip>]

Options:
    --debug         Run with debugging enabled.
    --port=<n>      Bind the server to <n>.
    --host=<ip>     Bind the server to <ip>.
"""
import sys

from docopt import docopt

from ein.version import __version__


def from_cli(argv=None):
    args = docopt(
        __doc__,
        version=__version__,
        argv=argv
    )

    if args['www']:
        pass


if __name__ == '__main__':
    sys.exit(from_cli())
