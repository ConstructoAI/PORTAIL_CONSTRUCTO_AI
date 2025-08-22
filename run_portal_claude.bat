@echo off
echo ==========================================
echo   PORTAIL CONSTRUCTO AI + CLAUDE API
echo   Assistant IA Sylvain Leduc
echo ==========================================
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
pause
exit /b 1

:found_python
echo Python trouve: %PYTHON_CMD%
%PYTHON_CMD% --version

echo.
echo ==========================================
echo   VERIFICATION CONFIGURATION CLAUDE API
echo ==========================================
echo.

REM Vérifier si .env existe
if exist ".env" (
    echo [OK] Fichier .env trouve
    findstr /C:"ANTHROPIC_API_KEY" .env >nul
    if %errorlevel% equ 0 (
        echo [OK] Cle API Claude configuree
        echo.
        echo MODE: Claude API Active
    ) else (
        echo [!] Cle API non trouvee dans .env
        echo MODE: Demo (sans Claude API)
    )
) else (
    echo [!] Fichier .env non trouve
    echo.
    echo Pour activer Claude API:
    echo 1. Copiez .env.example vers .env
    echo 2. Ajoutez votre cle ANTHROPIC_API_KEY
    echo.
    echo MODE: Demo (sans Claude API)
)

echo.
echo ==========================================
echo   INSTALLATION DES DEPENDANCES
echo ==========================================
echo.

echo Installation des packages de base...
%PYTHON_CMD% -m pip install --upgrade pip
%PYTHON_CMD% -m pip install -r requirements.txt

echo.
echo Installation des packages Claude (optionnel)...
%PYTHON_CMD% -m pip install anthropic python-dotenv 2>nul

echo.
echo ==========================================
echo   DEMARRAGE DU PORTAIL AVEC CLAUDE API
echo ==========================================
echo.
echo Interface accessible sur: http://localhost:8501
echo.
echo FONCTIONNALITES:
echo - Portail complet avec 7 applications
echo - Assistant Sylvain Leduc integre
echo - Support Claude API si configure
echo - Mode demo si pas de cle API
echo.
echo MODELES CLAUDE DISPONIBLES:
echo - claude-sonnet-4-20250514 (configure - derniere version)
echo - claude-3-5-sonnet-20241022 (fallback automatique)
echo - claude-3-haiku-20240307 (economique)
echo.
echo Appuyez sur CTRL+C pour arreter
echo ==========================================
echo.

REM Attendre 3 secondes puis ouvrir le navigateur
timeout /t 3 /nobreak >nul
start http://localhost:8501

REM Lancer Streamlit avec le portail Claude API
%PYTHON_CMD% -m streamlit run portal_with_claude_api.py --server.headless=false --theme.base="light" --theme.primaryColor="#3B82F6"

echo.
echo Application fermee.
pause