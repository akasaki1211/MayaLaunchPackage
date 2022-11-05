# MayaLaunchPackage

This folder contains bat files, configuration files, additional plug-ins, scripts, etc. to start Maya.

Rather than using this folder as is, it is intended as a base folder for modification.

The minimal configuration and third-party tools used in the project can be contained in this package. It easy to have someone outside your team build the same environment.

> Tested with Maya 2023

## Key design of this package
* There is nothing for users to do other than install the package folder. (Maya must be already installed.)  
* Use relative paths whenever possible, so that package folder can be placed anywhere.  
* It has common settings and unique settings for each region(Model, Anim, etc). 
* This package does not modify local configuration files(`C:\Users\<username>\Documents\maya`).  
> package folder = `PRJ_Maya` folder

## How to use
1. Place `PRJ_Maya` folder somewhere.
1. Replace `PRJ` in the folder name with your project name.
1. Create a batchfile with any file name while referencing `PRJ_Maya2023.bat`. Be sure to specify `MAYA_VERSION` and `MAYA_UI_LANGUAGE`.
1. Write the script you want to run at startup in userSetup.py.
    * Common settings : `PRJ_Maya\scripts\userSetup.py`
    * Region settings : `PRJ_Maya\region\***\scripts\userSetup.py`
1. Place the third-party tools, etc. in each scripts, plug-ins, and modules folder.
    * Common settings : `PRJ_Maya\scripts`, `PRJ_Maya\plug-ins`, `PRJ_Maya\modules`
    * Region settings : `PRJ_Maya\region\***\scripts`, `PRJ_Maya\region\***\plug-ins`, `PRJ_Maya\region\***\modules`   
1. Place any image file named `MayaStartupImage.png` in `PRJ_Maya\icons` to affect the splash screen. (if necessary)

## About the samples in `PRJ_Maya\scripts\userSetup.py` 
|||
|---|---|
|drawHUD|Displays the following HUD in the lower left corner of viewport.<br>e.g. "Running in PRJ_Model (Python 3.9.7)"|
|loadPlugin|Loads/Unloads the plug-ins|
|sceneSettings|Set the unit, time-range, framerate, etc. when NewScene is executed (including at startup Maya).|
|autoSetProject|Display a confirmation dialog asking if you want to Set Project when you open a scene from a different Maya-Project than a current Maya-Project.|