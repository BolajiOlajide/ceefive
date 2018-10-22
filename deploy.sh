#!/bin/bash

set -e
set -o pipefail # if any code doesn't return 0, exit the script

echo 'Running deploy scripts for Ceefive bot!'

# install python & project dependencies
pip install pipenv
pipenv install

exit 0
