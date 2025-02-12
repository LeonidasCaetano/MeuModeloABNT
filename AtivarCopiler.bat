@echo off
setlocal

:: Obtém o caminho do diretório onde o script está localizado
set "PENDRIVE_PATH=%~d0"
set "PASTA=%~dp0"

:: Define os caminhos para MinGW, Lua e Python
set "PATH=%PENDRIVE_PATH%\Apps\AppC\bin\;%PATH%"
set "PATH=%PENDRIVE_PATH%\Apps\AppLua\5.1\;%PATH%"
set "PATH=%PENDRIVE_PATH%\Apps\AppPython\Scripts\;%PATH%"
set "PATH=%PENDRIVE_PATH%\Apps\AppPython\;%PATH%"

:: Move para a pasta de códigos (opcional, ajuste conforme necessário)
cd /d "%PASTA%"

:: Exibe uma mensagem e abre o CMD já configurado
echo Ambiente configurado!

echo %PENDRIVE_PATH%Apps\AppC\bin\
echo %PENDRIVE_PATH%Apps\AppLua\5.1\
echo %PENDRIVE_PATH%Apps\AppPython\
echo %PASTA%

cmd
