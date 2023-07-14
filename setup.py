"""
shifter's setup.py
"""

# pylint:disable=line-too-long

from setuptools import setup

setup(
    name='ctxvalue-shifter',
    version='1.2.0',
    author='Arsalan Kazmi',
    author_email='sonicspeed848@gmail.com',
    description='Contextual Value Shifter, a module for shifting values to different destinations.',
    py_modules=['cxvshifter.cxvshifter'],
    python_requires='>=3.6',
    long_description="""Contextual Value Shifter is a Python module that implements a contextual "shift" function.

Usage
-----

.. code:: python

   from cxvshifter import shift

   # Shifting to variables
   x = 5
   shift(10, 'x')
   print(x)
   # => 10

   # Shifting to a file
   shift("hello", 'file', "hello.txt")

   # Shifting to stdout
   shift("Hello, shifting world!", 'stdout')

   # Shifting to return
   shift(24, 'return')
   # -> 24

Improper usage
--------------

.. code:: python

   x = 5
   shift(10, x)
   # Will attempt to shift to a variable named 5
   # In ctxvalue-shifter, this will result in a TypeError
""",
)
