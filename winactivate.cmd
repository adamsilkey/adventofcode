@ECHO OFF

REM --- Activate.cmd -----------------------------------------------------------

SET VENV_NAME=adventofcode
PUSHD %~dp0
IF NOT EXIST venv\windows\%VENV_NAME% (
  ECHO Virtual Environment not detected... 
  ECHO Installing virtual environment...
  MKDIR venv\windows\%VENV_NAME% >NUL 2>&1
  CD venv\windows
  py -m venv %VENV_NAME%
  CD %~dp0
  ECHO Installing requirements from Requirements.txt...
  CALL venv\windows\%VENV_NAME%\Scripts\activate.bat
  pip install -r Requirements.txt
)
CALL venv\windows\%VENV_NAME%\Scripts\activate.bat
