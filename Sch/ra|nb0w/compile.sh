#!/bin/bash
python3  -m py_compile ./gradius.py
python3  -m py_compile ./drawline.py
python3  -m py_compile ./libcolor/__init__.py
cp ./__pycache__/* ../gradio/
cp ./libcolor/__pycache__/* ../gradio

