from __future__ import with_statement
import pytest
import sys
import iocapture

if sys.version_info < (2, 5):
    print("with statement test requires at least Python 2.5 .")
    sys.exit(1)

def test_with_statement():
    with iocapture.capture() as captured:
        sys.stdout.write("hello world")
        assert captured.stdout.strip() == "hello world"
