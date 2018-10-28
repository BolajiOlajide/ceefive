#!/bin/bash

set -e
set -o pipefail # if any code doesn't return 0, exit the script

echo 'Running deploy scripts for Ceefive bot!'

# install python & project dependencies
# no need to do this ha HEroku supports pipenv lol 😂
# pip install pipenv
# pipenv install

# starting the bot 😎
echo '😂 💩 😂 😎 😜 ........ 🧐 🤓 😏'
# python cron.py
gunicorn -w 1 -b 0.0.0.0 cron:app -c main.py
