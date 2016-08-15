#!/usr/bin/python

from setuptools import setup
from zmqshelltools import __version__

ENTRY_POINTS = dict(
    console_scripts=[
        'zat = zmqshelltools.zat:main',
        'zee = zmqshelltools.zee:main',
    ])

CLASSIFIERS = [
    "Development Status :: 1 - Planning",
    "Environment :: Console",
    "Intended Audience :: Developers",
    "Intended Audience :: System Administrators",
    "License :: OSI Approved :: MIT License",
    "Operating System :: POSIX",
    "Topic :: Scientific/Engineering :: Interface Engine/Protocol Translator",
    "Topic :: System :: Networking",
    "Topic :: Utilities",
]

INSTALL_REQUIRES = [
    'pyzmq>=15',
    'click>=6',
]


setup(
    name="zmq-shell-tools",
    version=__version__,
    py_modules=['zmqshelltools'],
    description="Shell pipeline tools for ZeroMQ",
    url="https://www.github.com/arsatiki/zmq-shell-tools",
    author="Antti Rasinen",
    author_email="ars@iki.fi",
    install_requires=INSTALL_REQUIRES,
    entry_points=ENTRY_POINTS,
    classifiers=CLASSIFIERS,
)
