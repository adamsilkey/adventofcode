#!/bin/bash

venvname=adventofcode

if [ ! -d venv/posix/$venvname ]; then
  echo Virtual environment not detected...
  echo Installing virtual environment...
  mkdir -p venv/posix
  cd venv/posix
  python3 -m venv $venvname
  cd ../..
  source venv/posix/$venvname/bin/activate
  if [ -e Requirements.txt ]; then
    echo Installing requirements from Requirements.txt...
    pip install -r Requirements.txt
  fi
fi
source venv/posix/$venvname/bin/activate
