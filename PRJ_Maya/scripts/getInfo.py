# -*- coding: utf-8 -*-
# *********************************************
# Don't edit this file
# *********************************************

import os
import sys

# get environment variables
ROOT_PATH = os.environ.get("ROOT_PATH")
REGION_PATH = os.environ.get("REGION_PATH")
REGION = os.environ.get("REGION")

# get info
PROJECT_NAME = os.path.basename(ROOT_PATH).replace('_Maya', '')
PYTHON_VER = 'Python {}.{}.{}'.format(sys.version_info.major, sys.version_info.minor, sys.version_info.micro)

print('\n\n========================================================')
print("PROJECT_NAME     : {}".format(PROJECT_NAME))
print("PYTHON_VER       : {}".format(PYTHON_VER))
print('-----------------------------')
print("ROOT_PATH        : {}".format(ROOT_PATH))
print("REGION_PATH      : {}".format(REGION_PATH))
print("REGION           : {}".format(REGION))
print('========================================================\n\n')