#!/bin/bash
# setup.sh - Script de configuration pour Render

# Créer le dossier .streamlit si nécessaire
mkdir -p ~/.streamlit/

# Créer le fichier config.toml
echo "\
[general]\n\
email = \"info@constructoai.ca\"\n\
\n\
[server]\n\
headless = true\n\
enableCORS = false\n\
port = \$PORT\n\
\n\
[theme]\n\
primaryColor = \"#3B82F6\"\n\
backgroundColor = \"#FFFFFF\"\n\
secondaryBackgroundColor = \"#F0F9FF\"\n\
textColor = \"#1F2937\"\n\
font = \"sans serif\"\n\
" > ~/.streamlit/config.toml

# Créer le fichier credentials.toml vide
echo "\
[general]\n\
" > ~/.streamlit/credentials.toml