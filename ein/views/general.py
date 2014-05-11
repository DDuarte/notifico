#!/usr/bin/env python
# encoding: utf-8
"""
General views which do not fit into a specific category, such as
an about page or contact page.
"""
from flask import Blueprint, render_template

general_views = Blueprint(
    'general',
    __name__
)


@general_views.route('/')
def landing_page():
    """
    The default landing page shown to anonymous users.
    """
    return render_template('general/landing.jinja')
