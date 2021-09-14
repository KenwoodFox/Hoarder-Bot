#!/usr/bin/env python

# -*- coding: utf-8 -*-

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from setuptools import setup, find_packages

readme = open('README.md').read()

setup(
    name='hoarder-bot',
    description='''An expandable bot, written in python
    for the datahoarding and homelabbing discord server!!''',
    author='Snowsune',
    author_email='Snowsune#4646',
    url='https://github.com/KenwoodFox/Hoarder-Bot',
    packages=find_packages(include=['hoarder_bot']),
    package_dir={'hoarder-bot': 'hoarder_bot'},
    entry_points={
        'console_scripts': [
            'hoarder-bot=hoarder_bot.__main__:main',
        ],
    },

    python_requires='>=3.6.0',
    version='0.0.0',
    long_description=readme,
    include_package_data=True,
    install_requires=[
        'discord.py',
    ],
    license='MIT',
)
