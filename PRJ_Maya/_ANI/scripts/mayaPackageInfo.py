# -*- coding: utf-8 -*-
import os

def getScriptPath():
    return os.path.dirname(os.path.abspath(__file__))

def getPakageRootPath():
    return os.sep.join(getScriptPath().split(os.sep)[:-2])

def getBatPath():
    return os.sep.join(getScriptPath().split(os.sep)[:-1] + ['bat'])

def getProjectName():
    return os.path.basename(getPakageRootPath()).replace('_Maya','')

def getRegion():
    return getScriptPath().split(os.sep)[-2]