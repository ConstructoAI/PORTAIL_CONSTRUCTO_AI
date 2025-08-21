#!/bin/bash
# setup.sh - Script de configuration pour Render

# Créer le dossier .streamlit si nécessaire
mkdir -p ~/.streamlit/

# Créer le fichier config.toml
cat > ~/.streamlit/config.toml <<EOF
[server]
headless = true
port = \$PORT
enableCORS = false
enableXsrfProtection = true

[browser]
gatherUsageStats = false
serverAddress = "0.0.0.0"

[theme]
primaryColor = "#3B82F6"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F9FF"
textColor = "#1F2937"
font = "sans serif"
EOF

# Créer le fichier credentials.toml vide
cat > ~/.streamlit/credentials.toml <<EOF
[general]
EOF

echo "Configuration Streamlit créée avec succès"