#!/usr/bin/env python
from setuptools import setup, find_packages

__version__ = "0.1"


setup(
    name="liason",
    author="Gregory Rehm",
    author_email="grehm87@gmail.com",
    version=__version__,
    description="A simple address book",
    packages=find_packages(),
    package_data={"*": ["*.html"]},
    entry_points={
        "console_scripts": [
            "couch=couch.main:main",
        ],
    },
    install_requires=[
        "psycopg2",
        "sqlalchemy",
    ],
)
