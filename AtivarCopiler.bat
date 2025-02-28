@echo off
setlocal

set "PENDRIVE_PATH=%~d0"
set "PASTA=%~dp0"

set "PATH=%PENDRIVE_PATH%\Apps\AppC\bin\;%PATH%"
set "PATH=%PENDRIVE_PATH%\Apps\AppLua\5.1\;%PATH%"
set "PATH=%PENDRIVE_PATH%\Apps\AppPython\;%PATH%"
set "PATH=%PENDRIVE_PATH%\Apps\AppTex\texmfs\install\miktex\bin\x64\;%PATH%"
set "PATH=%PENDRIVE_PATH%\Scripts\;%PATH%"
set "PATH=%PENDRIVE_PATH%\Apps\AppGit\bin\;%PATH%"
set "PATH=%PENDRIVE_PATH%\Apps\AppOpera\;%PATH%"

cd /d "%PASTA%"

echo Ambiente configurado!

echo Diretórios adicionados
echo %PENDRIVE_PATH%Apps\AppC\bin\
echo %PENDRIVE_PATH%Apps\AppLua\5.1\
echo %PENDRIVE_PATH%Apps\AppPython\
echo %PENDRIVE_PATH%\Apps\AppTex\texmfs\install\miktex\bin\x64\
echo %PENDRIVE_PATH%\Scripts\
echo %PENDRIVE_PATH%\Apps\AppGit\bin\
echo %PENDRIVE_PATH%\Apps\AppOpera\
echo Pasta atual: %PASTA%

cmd
