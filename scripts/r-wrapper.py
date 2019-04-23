# Title: Wrapper for running R code in Python
# Institution: Oregon State University
# Author: Brian Katz
# Date: 2019-04-22

# Import dependencies
from rpy2 import robjects
import rpy2.robjects.packages as rpackages
from rpy2.robjects.packages import importr
from rpy2.robjects.vectors import StrVector

# Load R packages
base = importr('base')
utils = importr('utils')
utils.chooseCRANmirror(ind=1)
packnames = ('pastecs', 'janitor', 'bindrcpp')  # add list of package names here
names_to_install = [x for x in packnames if not rpackages.isinstalled(x)]
if len(names_to_install) > 0:
    utils.install_packages(StrVector(names_to_install))

# Wrapper to run R commands:
robjects.r('''
input_data <- read.csv("../assets/input_data.csv")
print('Successfully loaded data in R through Python')
''')
