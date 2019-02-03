# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import core


INSTALL_REQUIRES = []
ENTRY_POINTS = {
    'console_scripts': [
        'myapp=myapp.__main__:main'
    ]
}


setup(
    name='myapp',
    version=core.__version__,
    description=core.__doc__.strip(),
    author='feynm4n',
    packages=find_packages(),
    install_requires=INSTALL_REQUIRES,
    entry_points=ENTRY_POINTS,
    zip_safe=False,
)
