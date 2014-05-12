#!/usr/bin/env python
# encoding: utf-8
"""ein-server

Commands:
    www             Start the embedded Flask HTTP server.
    db init         Create any missing database tables.

Usage:
    ein-server www [--debug --port=<n> --host=<ip>]
    ein-server db init

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
from flask.ext.sqlalchemy import SQLAlchemy

from ein.version import __version__


babel = Babel()
db = SQLAlchemy()


def create_flask_application():
    """
    An application factory that creates a new instance of the ein.io
    frontend process.
    """
    app = Flask(__name__)
    app.config.from_object('ein.config')
    app.config.from_envvar('EIN_CONFIG', silent=True)

    if app.config['ROUTE_STATIC_ASSETS']:
        import os.path
        from werkzeug import SharedDataMiddleware

        app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
            '/': os.path.join(os.path.dirname(__file__), 'static')
        })

    babel.init_app(app)
    db.init_app(app)

    from ein.views.general import general_views
    app.register_blueprint(general_views)

    return app


def from_cli(argv=None):
    args = docopt(
        __doc__,
        version=__version__,
        argv=argv
    )

    if args['www']:
        # Starts the built-in webserver.
        app = create_flask_application()
        app.run(
            host=args['--host'],
            port=int(args['--port']),
            debug=args['--debug']
        )
    elif args['db']:
        # Database-related commands.
        app = create_flask_application()

        # All of the models we want to create tables for must be imported
        # so they can be seen by SQLAlchemy.
        from ein.models.user import User
        # These asserts are to silence warnings by pyflake8 in a more
        # portable manner than the # NOQA flag.
        assert(User)

        with app.app_context():
            if args['init']:
                db.create_all()


if __name__ == '__main__':
    sys.exit(from_cli())
