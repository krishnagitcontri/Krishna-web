"""
This type stub file was generated by pyright.
"""

"""Compatibility tricks for Python 3. Mainly to do with unicode.

This file is deprecated and will be removed in a future version.
"""
def decode(s, encoding=...):
    ...

def encode(u, encoding=...):
    ...

def cast_unicode(s, encoding=...):
    ...

def safe_unicode(e):
    """unicode(e) with various fallbacks. Used for exceptions, which may not be
    safe to call unicode() on.
    """
    ...

def input(prompt=...):
    ...

def execfile(fname, glob, loc=..., compiler=...): # -> None:
    ...

PYPY = ...
def no_code(x, encoding=...):
    ...

cast_bytes_py2 = ...