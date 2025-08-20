@echo off
setlocal

set "PENDRIVE_PATH=%~d0"
set "PASTA=%~dp0"

set "PATH=%PENDRIVE_PATH%\Portable\PortableApps\AppC\bin\;%PATH%"
set "PATH=%PENDRIVE_PATH%\Portable\PortableApps\AppLua\5.1\;%PATH%"
set "PATH=%PENDRIVE_PATH%\Portable\PortableApps\AppPython\;%PATH%"
set "PATH=%PENDRIVE_PATH%\Portable\PortableApps\AppTex\texmfs\install\miktex\bin\x64\;%PATH%"
set "PATH=%PENDRIVE_PATH%\Portable\PortableApps\AppGit\bin\;%PATH%"
set "PATH=%PENDRIVE_PATH%\Portable\PortableApps\OperaPortable\;%PATH%"
set "PATH=%PENDRIVE_PATH%\Portable\PortableApps\DrMemory\bin\;%PATH%"
set "PATH=%PENDRIVE_PATH%\Portable\PortableApps\AppVs\;%PATH%"
set "PATH=%PENDRIVE_PATH%\Portable\PortableApps\.elan\toolchains\leanprover--lean4---v4.19.tmp\bin\;%PATH%"
set "PATH=%PENDRIVE_PATH%\Scripts\;%PATH%"

cd /d "%PASTA%"

echo Ambiente configurado!

cmd
