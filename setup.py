#!/usr/bin/env python
# -*- coding: utf8 -*-
from setuptools import setup, find_packages


if __name__ == '__main__':
    setup(
        name='ein',
        version='2.0.0',
        long_description=__doc__,
        packages=find_packages(),
        include_package_data=True,
        zip_safe=False,
        install_requires=[
        ]
    )
