#!/usr/bin/zsh

#brew
NONINTERACTIVE=1 /bin/bash -c \
   "$(curl -fsSL \
      https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

brew install python
python -m venv venv
source venv/bin/activate
pip3 -r install requirements.txt
python build.py