import sys
from six import b, u

def string(s):
    if sys.version_info > (3, 0):
        return u(s)
    else:
        if isinstance(s, unicode):
            return s.encode("utf-8")
        else:
            return b(s)
