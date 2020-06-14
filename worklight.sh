#!/bin/bash
PY_PATH=$(echo $PATH | tr ":" "\n" | head -n1)
python3.8 $PY_PATH/py-scripts/worklight.py $1 $2