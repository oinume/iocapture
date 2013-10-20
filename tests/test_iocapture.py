# coding: utf-8
import pytest
import sys
import iocapture
from six import b, u
from util import string

class TestIOCapture(object):

    def setup_method(self, method):
        self.captured = iocapture.IOCapture()

    def teardown_method(self, method):
        pass

    def test_capture_stdout(self):
        self.captured.start()
        sys.stdout.write(string("hello stdout"))
        self.captured.stop()
        assert self.captured.stdout.strip() == string("hello stdout")

    def test_capture_stderr(self):
        self.captured.start()
        sys.stderr.write(string("hello stderr"))
        self.captured.stop()
        assert self.captured.stderr.strip() == string("hello stderr")

    # def test_utf8(self):
    #     self.captured.start()
    #     sys.stderr.write(string(u("こんにちは")))
    #     self.captured.stop()
    #     assert self.captured.stderr.strip() == string("こんにちは")

