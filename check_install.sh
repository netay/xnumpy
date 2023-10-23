#!/bin/bash
pip install wheels/xnumpy-1.0.1-cp38*.whl
pip install wheels/xnumpy_base-1.0.1-cp38*.whl

python3.8 examples/quadratic_equation.py
