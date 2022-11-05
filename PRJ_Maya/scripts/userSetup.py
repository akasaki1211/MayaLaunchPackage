# -*- coding: utf-8 -*-
import getInfo


# ====================================================
# Common Custom Settings
# ====================================================
import maya.utils
import maya.cmds as cmds
import maya.api.OpenMaya as om2
import sys
import os

def drawHUD(*args):
    HUD_name = 'MayaRunningMode1'
    str = 'Running in {}{} ({})'.format(getInfo.PROJECT_NAME, getInfo.REGION, getInfo.PYTHON_VER)
    cmds.headsUpDisplay(HUD_name, s=6, b=0, lfs="large" ,l=str)
maya.utils.executeDeferred(drawHUD)

def loadPlugin(*args):
    # load
    cmds.loadPlugin('fbxmaya.mll',qt=True)
    cmds.loadPlugin('matrixNodes.mll',qt=True)
    # unload
    cmds.unloadPlugin("Mayatomr", f=True)
    cmds.unloadPlugin('lookdevKit.mll',f=True)
maya.utils.executeDeferred( loadPlugin )

def sceneSettings(*args):
    print('==== Set {} Settings ===='.format(getInfo.PROJECT_NAME))
    # fps, unit
    cmds.currentUnit(t='ntsc', l='cm', a='deg')
    # timerange
    cmds.playbackOptions(min=1, max=90, ast=1, aet=90)
    # current time
    cmds.currentTime(1)
om2.MSceneMessage.addCallback(om2.MSceneMessage.kAfterNew, sceneSettings)
om2.MSceneMessage.addCallback(om2.MSceneMessage.kAfterOpen, sceneSettings)

def autoSetProject(*args):
    currentProjectPath = os.path.normpath(cmds.workspace(q=True, active=True))
    filePath = os.path.normpath(cmds.file(query=True, expandName=True))
    dirPath = os.path.dirname(filePath)
    
    for i in range(len(dirPath.split(os.sep))):
        workspace_mel = os.path.join(dirPath, 'workspace.mel')
        if os.path.isfile(workspace_mel):
            print('Find Project Path: {}'.format(dirPath))
            if os.path.normpath(dirPath) != currentProjectPath:
                conf = cmds.confirmDialog(title='Set Project', message='Do you want to set project?\n{}'.format(dirPath), button=['Yes', 'No'], defaultButton='Yes', cancelButton='No', dismissString='No')
                if conf == 'Yes':
                    cmds.workspace(dirPath, openWorkspace=True)
            break
        else:
            dirPath = os.path.dirname(dirPath)
om2.MSceneMessage.addCallback(om2.MSceneMessage.kBeforeFileRead, autoSetProject)