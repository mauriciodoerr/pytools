# pytools 
[![Build Status](https://app.travis-ci.com/mauriciodoerr/pytools.svg?branch=main)](https://app.travis-ci.com/mauriciodoerr/pytools) 
[![Updates](https://pyup.io/repos/github/mauriciodoerr/pytools/shield.svg)](https://pyup.io/repos/github/mauriciodoerr/pytools/)
[![Python 3](https://pyup.io/repos/github/mauriciodoerr/pytools/python-3-shield.svg)](https://pyup.io/repos/github/mauriciodoerr/pytools/)

Code samples regarding the module Pytools from DevPro Platform

Supported Python version 3

<h3>Implemented Libs:</h3>
- Requests: HTTP for Humans™

<h3>Installing</h3>
```console
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
```

Check for Code Quality following PEP8, execute:
```console
flake8
```

<h2>Useful Python commands</h2>
<h3>Create and activate venv</h3>
```console
python3 -m venv .venv
source .venv/bin/activate
```
---
<h3>Install PyPi local Lib[^1]</h3>
```console
pip install -e "path to setup.py inside the lib"
```
E.g.```pip install -e ./pytools```

Validate installation
```console
python
from libhttprequests.github_api import get_github_avatar
get_github_avatar('mauriciodoerr')
```

[^1]: List Classifiers for PyPi can be found at https://pypi.org/pypi?%3Aaction=list_classifiers