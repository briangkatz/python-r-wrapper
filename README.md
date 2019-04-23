# Run R Code in Python
###### Brian Katz | Oregon State University | Spring 2019

### Purpose

The purpose of this script is to serve as a wrapper for running R code in Python.

`robjects.r(```YOUR R CODE HERE```)`

### Requirements

- Python 3.5 (Anaconda venv)
- R
- IDE (e.g. PyCharm)

### Instructions

- Make sure R and Python are installed on your computer

- Add the list of R packages needed to run your R code in the `packnames` variable

  - e.g. `packnames = ('pastecs', 'janitor', 'bindrcpp')`

- Add R code within the wrapper

  ```python
  # Wrapper to run R commands:
  robjects.r('''
  YOUR R CODE HERE
  ''')
  ```

- Run the `r-wrapper.py` script in your IDE
- If successful, the script should execute your R code from within Python