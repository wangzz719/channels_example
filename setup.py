#!/usr/bin/python
# -*-coding: utf8-*-

from setuptools import setup

setup(
    name='channels_example',
    version='0.0.1',
    author='wzz',
    packages=['channels_example', 'example'],
    install_requires=[
        'django',
        'channels',
        'asgi_redis'
    ]
)
