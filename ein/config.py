#!/usr/bin/env python
# encoding: utf-8
"""
Default configuration for ein.io.
"""
import os
import os.path

#: True if Ein should handle the routing of static assets - suitable only
#: for debugging and extremely low traffic sites.
ROUTE_STATIC_ASSETS = True

#: The SQLAlchemy connection URI. Do _NOT_ use SQLite in production.
SQLALCHEMY_DATABASE_URI = 'sqlite:///{cwd}/ein_testing.db'.format(
    cwd=os.path.abspath(os.getcwd())
)

#: Log all SQL statements to stderr. Invaluable for debugging.
SQLALCHEMY_ECHO = False
