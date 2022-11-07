# -*- coding: utf-8 -*-
import getInfo


# ====================================================
# Region Custom Settings
# ====================================================
import maya.cmds as cmds
import maya.api.OpenMaya as om2

def sceneSettings(*args):
    print('==== Set {}_{} Settings ===='.format(getInfo.PROJECT_NAME, getInfo.REGION))
    # playback
    cmds.playbackOptions(ps=0, mps=0)
om2.MSceneMessage.addCallback(om2.MSceneMessage.kAfterNew, sceneSettings)
om2.MSceneMessage.addCallback(om2.MSceneMessage.kAfterOpen, sceneSettings)