import cStringIO
import sys

__author__ = "Kazuhiro Oinuma"
__author_email__ = "oinume@gmail.com"
__copyright__ = "2013"
__license__ = "MIT"
__version__ = "0.1.0"
__maintainer__ = "Kazuhiro Oinuma"
__status__ = "Production/Stable"

def capture(stdout=True, stderr=True):
    return IOCapture(stdout, stderr)

__all__ = [ capture ]

class IOCapture(object):
    """"""

    def __init__(self, stdout = True, stderr = True):
        self._stdout = None
        self._stderr = None
        if stdout:
            self._stdout = cStringIO.StringIO()
        if stderr:
            self._stderr = cStringIO.StringIO()

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

#@contextlib.contextmanager
#def capture():
#    import sys
#    from cStringIO import StringIO
#    oldout,olderr = sys.stdout, sys.stderr
#    try:
#        out=[StringIO(), StringIO()]
#        sys.stdout,sys.stderr = out
#        yield out
#    finally:
#        sys.stdout,sys.stderr = oldout, olderr
#        out[0] = out[0].getvalue()
#        out[1] = out[1].getvalue()
#
#with capture() as out:
#    print 'hi'


#from iocapture import capture
#
#with capture() as stdout, stderr:
#    pass

#with iocapture.capture() as captured:
#    captured.stdout
#    captured.stderr