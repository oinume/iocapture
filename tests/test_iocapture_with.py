from __future__ import with_statement
import pytest
import sys
import iocapture
from six import b, u
from util import string

if sys.version_info < (2, 5):
    print("with statement test requires at least Python 2.5 .")
    sys.exit(1)

def test_with_statement():
    with iocapture.capture() as captured:
        sys.stdout.write(string("hello world"))
        assert captured.stdout.strip() == string("hello world")
