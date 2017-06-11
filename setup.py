#!/usr/bin/env python3
# -*- coding: utf-8

import setuptools

setuptools.setup(
    name='grout',
    version='0.1.0',
    description='Grout tool and library for continuous, clean builds',
    license='MIT',
    author='Tim Süberkrüb',
    author_email='dev@timsueberkrueb.io',
    url='https://www.github.com/tim-sueberkrueb',
    packages=setuptools.find_packages(),
    package_data={
        'grout.core': ('validation/project_schema.yaml',)
    },
    scripts=(
        'bin/grout',
    ),
    install_requires=(
        'pylxd',
        'pyyaml',
        'click',
        'pykwalify',
        'pytest'
    ),
    test_suite='tests',
)
