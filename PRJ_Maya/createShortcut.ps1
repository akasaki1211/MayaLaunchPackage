if ($args[0] -eq $null) {
    exit
}

$currentDir = Split-Path -Parent $MyInvocation.MyCommand.Path
#$currentDir = (Get-Location).Path

#$filename = Join-Path $currentDir ((Split-Path $args[0] -Leaf) + '.lnk')
$targetName = [System.IO.Path]::GetFileNameWithoutExtension($args[0])
$filename = Join-Path $currentDir ($targetName + '.lnk')
$icons = (Get-ChildItem -Path ($currentDir + "\icons\*.ico"))

$wsh = New-Object -com WScript.Shell
$shortcut = $wsh.CreateShortcut($filename)
$shortcut.Arguments = "/c " + $args[0]
$shortcut.TargetPath = "C:\WINDOWS\system32\cmd.exe"
$shortcut.WorkingDirectory = $currentDir
if ($icons -ne $null){
    $shortcut.IconLocation = $icons[0].FullName
}
$shortcut.Save()

echo $filename