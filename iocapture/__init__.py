import sys

if sys.version_info > (3, 0):
    from io import StringIO
else:
    from cStringIO import StringIO

__author__ = "Kazuhiro Oinuma"
__author_email__ = "oinume@gmail.com"
__copyright__ = "2013"
__license__ = "MIT"
__version__ = "0.1.0"
__maintainer__ = "Kazuhiro Oinuma"
__status__ = "Production/Stable"

def capture(stdout=True, stderr=True):
    return IOCapture(stdout, stderr)

class IOCapture(object):
    """"""

    def __init__(self, stdout = True, stderr = True):
        self._stdout = None
        self._stderr = None
        if stdout:
            self._stdout = StringIO()
        if stderr:
            self._stderr = StringIO()

    def start(self):
        if self._stdout:
            sys.stdout = self._stdout
        if self._stderr:
            sys.stderr = self._stderr
        return self

    def stop(self):
        if self._stdout:
            sys.stdout = sys.__stdout__
        if self._stderr:
            sys.stderr = sys.__stderr__
        return self

    @property
    def stdout(self):
        self._stdout.flush()
        return self._stdout.getvalue()

    @property
    def stderr(self):
        self._stderr.flush()
        return self._stderr.getvalue()

    def close(self):
        if self._stdout:
            self._stdout.close()
        if self._stderr:
            self._stderr.close()
        return self

    def __enter__(self):
        return self.start()

    def __exit__(self, type, value, traceback):
        self.stop().close()

__all__ = [ capture, IOCapture ]
