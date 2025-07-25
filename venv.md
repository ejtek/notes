
# Venv

- You can run a Python script that is outside your virtual environment by specifying its absolute path-you do not need to copy the script into the virtual environment. What matters is which Python interpreter you use to run the script.

- If you want the script to run using the packages and environment of your virtual environment, you should invoke the Python interpreter from the virtual environment and pass it the path to your script, like this:

`python -m venv (.venv)`
`/path/to/venv/bin/python /absolute/path/to/your_script.py`

**Organization/Structure**
my_project/
│
├── .venv/                - Virtual environment (excluded from version control)
├── src/                  - Source code
├── data/                 - Data files
├── tests/                - Test scripts
├── requirements.txt      - Dependency list
└── README.md
