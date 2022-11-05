::*********************************************
:: Don't edit this file
::*********************************************

@echo off

:: Get Path
set ROOT_PATH=%~dp0
set ROOT_PATH=%ROOT_PATH:~0,-1%

IF DEFINED REGION (
    set REGION_PATH=%ROOT_PATH%\region\%REGION%
    set REGION_SCRIPT_PATH=%REGION_PATH%\scripts
    set REGION_PLUGIN_PATH=%REGION_PATH%\plug-ins
    set REGION_MODULE_PATH=%REGION_PATH%\modules
)

:: Maya Settings
set MAYA_DISABLE_CIP=1
set MAYA_DISABLE_CLIC_IPM=1
set MAYA_DISABLE_CER=1
set MAYA_SHOW_OUTPUT_WINDOW=1

:: Python Settings
set PYTHONDONTWRITEBYTECODE=1

:: Maya Path
set XBMLANGPATH=%ROOT_PATH%\icons
set MAYA_SCRIPT_PATH=%ROOT_PATH%\scripts;%REGION_SCRIPT_PATH%;%CUSTOM_MEL_PATH%
set PYTHONPATH=%ROOT_PATH%\scripts;%REGION_SCRIPT_PATH%;%CUSTOM_PYTHON_PATH%
set MAYA_PLUG_IN_PATH=%ROOT_PATH%\plug-ins;%REGION_PLUGIN_PATH%;%CUSTOM_PLUGIN_PATH%
set MAYA_MODULE_PATH=%ROOT_PATH%\modules;%REGION_MODULE_PATH%;%CUSTOM_MODULE_PATH%

:: Start Maya
start "" "%ProgramFiles%\Autodesk\Maya%MAYA_VERSION%\bin\maya.exe"

exit