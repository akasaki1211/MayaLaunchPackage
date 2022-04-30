# -*- coding: utf-8 -*-
import maya.utils
import maya.cmds as cmds
import maya.api.OpenMaya as om2
import sys

#----------------------------------------------------------------------
import mayaPackageInfo

print("==== {} Maya ====".format(mayaPackageInfo.getProjectName()))
print("Maya Package path : {}".format(mayaPackageInfo.getPakageRootPath()))
print("Startup bat path  : {}".format(mayaPackageInfo.getBatPath()))
print("Scripts path      : {}".format(mayaPackageInfo.getScriptPath()))
print("""
 _____  _____      _ 
|  __ \|  __ \    | |
| |__) | |__) |   | |
|  ___/|  _  /_   | |
| |    | | \ \ |__| |
|_|    |_|  \_\____/ {}
""".format(mayaPackageInfo.getRegion())
)

#----------------------------------------------------------------------

def loadPlugin(*args):
    cmds.loadPlugin('fbxmaya.mll',qt=True)
    cmds.loadPlugin('matrixNodes.mll',qt=True)
maya.utils.executeDeferred( loadPlugin )

def setfps(*args):
    print('set fps!')
    cmds.currentUnit( time='ntsc')
    cmds.playbackOptions(min=1, max=100, ast=0, aet=100)
    cmds.currentTime(1)
om2.MSceneMessage.addCallback(om2.MSceneMessage.kAfterNew, setfps)

def drawHUD(*args):
    HUD_name = 'MayaRunningMode1'
    str = 'Running in {}{} mode (PY{})'.format(mayaPackageInfo.getProjectName(), mayaPackageInfo.getRegion(), sys.version_info[0])
    cmds.headsUpDisplay(HUD_name, s=6, b=0, lfs="large" ,l=str)
maya.utils.executeDeferred(drawHUD)