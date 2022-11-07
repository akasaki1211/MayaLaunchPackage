# -*- coding: utf-8 -*-
# *********************************************
# Don't edit this file
# *********************************************

import os
import sys

# get environment variables
ROOT_PATH = os.environ.get("ROOT_PATH")

REGION = os.environ.get("REGION")
REGION_PATH = os.environ.get("REGION_PATH")
REGION_SCRIPT_PATH = os.environ.get("REGION_SCRIPT_PATH")
REGION_PLUGIN_PATH = os.environ.get("REGION_PLUGIN_PATH")
REGION_MODULE_PATH = os.environ.get("REGION_MODULE_PATH")

# get info
PROJECT_NAME = os.path.basename(ROOT_PATH).split('_')[0]
PYTHON_VER = 'Python {}.{}.{}'.format(sys.version_info.major, sys.version_info.minor, sys.version_info.micro)

print('\n\n========================================================')
print("PROJECT_NAME        : {}".format(PROJECT_NAME))
print("REGION              : {}".format(REGION))
print("PYTHON_VER          : {}".format(PYTHON_VER))
print('-------------------------------------')
print("ROOT_PATH           : {}".format(ROOT_PATH))
print("REGION_PATH         : {}".format(REGION_PATH))
print("REGION_SCRIPT_PATH  : {}".format(REGION_SCRIPT_PATH))
print("REGION_PLUGIN_PATH  : {}".format(REGION_PLUGIN_PATH))
print("REGION_MODULE_PATH  : {}".format(REGION_MODULE_PATH))
print('========================================================\n\n')