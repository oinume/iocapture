.. -*- restructuredtext -*-

.. highlight:: python

.. image:: https://img.shields.io/pypi/v/iocapture.svg
   :target: https://pypi.python.org/pypi/iocapture/

.. image:: https://img.shields.io/travis/oinume/iocapture.svg
   :target: https://travis-ci.org/oinume/iocapture


Capture stdout, stderr easily with iocapture.

How to use
==========

With Python >= 2.5 ::

  import iocapture

  with iocapture.capture() as captured:
      print("hello stdout")
      print(captured.stdout)
  # >>> hello stdout

With Python < 2.5 ::

  import iocapture

  captured = iocapture.capture()
  captured.start()
  print("hello stdout")
  captured.close()
  print(captured.stdout)
  # >>> hello stdout

ChangeLog
=========

https://github.com/oinume/blob/master/changes.rst


For developers
==============
Install iocapture in develop mode. ::

  $ python setup.py develop

Install following modules for testing. ::

  $ pip install -r requirements-dev.txt

Run tests ::

  $ py.test tests
