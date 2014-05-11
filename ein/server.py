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
                    [default: 5000]
    --host=<ip>     Bind the server to <ip>.
                    [default: localhost]
"""
import sys

from docopt import docopt
from flask import Flask
from flask.ext.babel import Babel

from ein.version import __version__


babel = Babel()


def create_flask_application():
    """
    An application factory that creates a new instance of the ein.io
    frontend process.
    """
    app = Flask(__name__)
    app.config.from_object('ein.config')
    app.config.from_envvar('EIN_CONFIG', silent=True)

    # Use babel for localization.
    babel.init_app(app)

    return app


def from_cli(argv=None):
    args = docopt(
        __doc__,
        version=__version__,
        argv=argv
    )

    if args['www']:
        app = create_flask_application()
        app.run(
            host=args['--host'],
            port=int(args['--port']),
            debug=args['--debug']
        )

        return 0


if __name__ == '__main__':
    sys.exit(from_cli())
