simple-python-shell
===================

This is a small Python interpreter that runs its own functions as commands.

To add a command, simply add a function and give it a docstring formatted
for Sphinx documentation, and a description of the syntax.
It should then be picked up.

Also, functions with two underscores preceding are special functions for the
interpreter, i.e. `__executeCmd()`

Python's code module could potentially be helpful here.
http://docs.python.org/2/library/code.html
