# [JoeBot](https://github.com/LouisMeMyself/JoeFeeCollector)

Fee collector for XJoe.

Iterate over all pairs on the farm and exclude reflective tokens (at least for now).

Installation
-------

### Use Virtualenv

This repo uses virtualenv. Follow the instructions for Linux:

Create a virtual env:
```bash
... $> python3 -m venv /path/to/new/virtual/environment
```

Installation of the dependencies required for the project:
```bash
# activation of the virtual environment
... $> source /path/to/new/virtual/environment/venv/bin/activate

# installation of dependencies (only after having activated the virtual environment!)
(venv) ... $> pip3 install -r requirements.txt
```

Then, to launch the fee collector simply type:
```bash
# launch the fee collector
(venv) ... $> python3 main.py
```