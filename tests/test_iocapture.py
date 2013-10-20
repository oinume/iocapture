# coding: utf-8
import pytest
import sys
import iocapture

class TestIOCapture(object):

    def setup_method(self, method):
        self.captured = iocapture.IOCapture()

    def teardown_method(self, method):
        pass

    def test_capture_stdout(self):
        self.captured.start()
        sys.stdout.write("hello stdout")
        self.captured.stop()
        assert self.captured.stdout.strip() == "hello stdout"

    def test_capture_stderr(self):
        self.captured.start()
        sys.stderr.write("hello stderr")
        self.captured.stop()
        assert self.captured.stderr.strip() == "hello stderr"

    def test_utf8(self):
        self.captured.start()
        sys.stderr.write(u"こんにちは".encode("utf-8"))
        self.captured.stop()
        assert self.captured.stderr.strip().decode("utf-8") == u"こんにちは"

