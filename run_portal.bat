@echo off
echo ========================================
echo   PORTAIL CONSTRUCTO AI
echo   Centre de Solutions IA
echo ========================================
echo.

echo Recherche de Python...

REM Essayer py launcher (priorité)
py --version 2>nul
if %errorlevel% equ 0 (
    set "PYTHON_CMD=py"
    goto :found_python
)

REM Essayer python dans le PATH
python --version 2>nul
if %errorlevel% equ 0 (
    set "PYTHON_CMD=python"
    goto :found_python
)

REM Essayer python3
python3 --version 2>nul
if %errorlevel% equ 0 (
    set "PYTHON_CMD=python3"
    goto :found_python
)

echo.
echo ========================================
echo ERREUR: Python n'est pas trouve
echo ========================================
echo.
echo SOLUTIONS:
echo 1. Installez Python depuis https://python.org
echo 2. Cochez "Add Python to PATH" pendant l'installation
echo 3. Redemarrez votre ordinateur
echo.
echo OU desactivez les alias Microsoft Store:
echo Parametres Windows ^> Applications ^> Aliases d'execution
echo Desactivez python.exe et python3.exe
echo.
pause
exit /b 1

:found_python
echo Python trouve: %PYTHON_CMD%
%PYTHON_CMD% --version

echo.
echo Installation des dependances...
%PYTHON_CMD% -m pip install --upgrade pip
%PYTHON_CMD% -m pip install -r requirements.txt

echo.
echo ========================================
echo   DEMARRAGE DU PORTAIL CONSTRUCTO AI
echo ========================================
echo.
echo Interface accessible sur: http://localhost:8501
echo.
echo Appuyez sur CTRL+C pour arreter l'application
echo ========================================
echo.

REM Attendre 3 secondes puis ouvrir le navigateur automatiquement
timeout /t 3 /nobreak >nul
start http://localhost:8501

REM Lancer Streamlit
%PYTHON_CMD% -m streamlit run portal.py --server.headless=false --theme.base="light" --theme.primaryColor="#3B82F6"

echo.
echo Application fermee.
pause