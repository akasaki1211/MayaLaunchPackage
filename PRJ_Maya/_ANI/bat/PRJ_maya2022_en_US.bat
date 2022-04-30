@echo off

::---------------------------------------------------
::パス取得
::---------------------------------------------------
set BAT_PATH=%~dp0
set REGION_PATH=%BAT_PATH:bat\=%
set REGION=%REGION_PATH:~-5,4%
set ROOT_PATH=%REGION_PATH:~0,-5%

::---------------------------------------------------
::Python設定
::---------------------------------------------------
set PYTHONDONTWRITEBYTECODE=1


::---------------------------------------------------
::Maya設定
::---------------------------------------------------
set MAYA_VERSION=2022
set MAYA_UI_LANGUAGE=en_US

::起動が早くなるおまじない
set MAYA_DISABLE_CIP=1
set MAYA_DISABLE_CLIC_IPM=1
set MAYA_DISABLE_CER=1

set MAYA_SHOW_OUTPUT_WINDOW=1
::set MAYA_ENABLE_LEGACY_VIEWPORT=1
::set MAYA_ENABLE_LEGACY_RENDER_LAYERS=1


::icon Path
set XBMLANGPATH_PRJ=%ROOT_PATH%\icons
::Python Path
set PYTHONPATH_PRJ=%ROOT_PATH%\scripts
set PYTHONPATH_REGION=%REGION_PATH%\scripts
::Plug-in Path
set PLUGINPATH_PRJ=%ROOT_PATH%\plug-ins
set PLUGINPATH_REGION=%REGION_PATH%\plug-ins
::Module Path
set MODULEPATH_PRJ=%ROOT_PATH%\modules
set MODULEPATH_MGEAR=%ROOT_PATH%\mgear_4.0.7\release

::Set
set XBMLANGPATH=%XBMLANGPATH_PRJ%
set PYTHONPATH=%PYTHONPATH_PRJ%;%PYTHONPATH_REGION%
set MAYA_PLUG_IN_PATH=%PLUGINPATH_PRJ%;%PLUGINPATH_REGION%
set MAYA_MODULE_PATH=%MODULEPATH_PRJ%;%MODULEPATH_MGEAR%



::Mayaプロジェクト
set MAYA_PROJECT=D:\Projects\PRJ\Works

::---------------------------------------------------
::Maya起動
::---------------------------------------------------
set MAYA_EXE="%ProgramFiles%\Autodesk\Maya%MAYA_VERSION%\bin\maya.exe"
start "" %MAYA_EXE%

exit