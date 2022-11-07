@echo off

::---------------------------------------------------
:: Custom Settings
::---------------------------------------------------

:: Required
set MAYA_VERSION=2023
set MAYA_UI_LANGUAGE=en_US

:: Optional
set REGION=Model

set MAYA_FORCE_PANEL_FOCUS=1
::set MAYA_ENABLE_LEGACY_VIEWPORT=1
::set MAYA_ENABLE_LEGACY_RENDER_LAYERS=1

set CUSTOM_MEL_PATH=
set CUSTOM_PYTHON_PATH=
set CUSTOM_PLUGIN_PATH=
set CUSTOM_MODULE_PATH=

set MAYA_PROJECT=
::---------------------------------------------------

call %~dp0launch.bat