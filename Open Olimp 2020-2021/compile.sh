#!/bin/fish
echo Starting...
echo
echo rm ./__pycache__ -rv
rm ./__pycache__ -rv
echo
echo python3 -m py_compile *.py
python3 -m py_compile *.py
echo
echo chmod +x ./__pycache__/* -v
chmod +x ./__pycache__/* -v
echo
echo Finished compiling.
