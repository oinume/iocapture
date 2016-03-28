import os
import sys
from iocapture import (
    __author__,
    __author_email__,
    __status__,
    __version__
)

def get_long_description():
    return open("README.rst").read()

try:
    from setuptools import setup
    setup
except ImportError:
    from distutils.core import setup

if sys.version_info < (2, 4):
    print("iocapture requires at least Python 2.4.")
    sys.exit(1)

if sys.argv[-1] == "publish":
    os.system("python setup.py sdist upload")
    sys.exit()

tests_require = []
for package in open("requirements-dev.txt").read().split("\n"):
    if package.strip():
        tests_require.append(package.strip())

setup(
    name = "iocapture",
    version = __version__,
    url = "https://github.com/oinume/iocapture",
    license = "MIT",
    author = __author__,
    author_email = __author_email__,
    description = "Capture stdout, stderr easily.",
    long_description = get_long_description(),
    packages = [ "iocapture" ],
    zip_safe = False,
    platforms = "unix",
    install_requires = [],
    tests_require = tests_require,
    classifiers = [
        "Development Status :: 5 - " + __status__,
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.4",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
