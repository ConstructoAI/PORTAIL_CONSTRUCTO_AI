#!/usr/bin/env python3
# test_assistant_integration.py - Test de l'intégration de l'assistant IA

import sys
import os

print("=" * 50)
print("TEST D'INTEGRATION - ASSISTANT IA CONSTRUCTO")
print("=" * 50)
print()

# Vérifier Python
print(f"[OK] Python version: {sys.version}")
print(f"[OK] Repertoire: {os.getcwd()}")
print()

# Vérifier les fichiers
files_to_check = [
    "portal_with_assistant.py",
    "style_portal.css",
    "requirements.txt"
]

print("Verification des fichiers:")
for file in files_to_check:
    if os.path.exists(file):
        print(f"  [OK] {file} trouve")
    else:
        print(f"  [X] {file} NON trouve")
print()

# Vérifier Streamlit
try:
    import streamlit as st
    print(f"[OK] Streamlit installe: version {st.__version__}")
except ImportError:
    print("[X] Streamlit NON installe")
    print("  -> Installez avec: pip install streamlit")
print()

# Instructions de lancement
print("=" * 50)
print("POUR LANCER LE PORTAIL AVEC ASSISTANT:")
print("=" * 50)
print()
print("1. Mode simple (sans API Claude):")
print("   streamlit run portal_with_assistant.py")
print()
print("2. Mode complet (avec API Claude):")
print("   - Créez un fichier .env avec:")
print("     ANTHROPIC_API_KEY=votre_clé_api")
print("   - Installez: pip install anthropic python-dotenv")
print("   - Lancez: streamlit run portal_with_assistant.py")
print()
print("L'assistant fonctionnera en mode démo sans clé API.")
print("Il répondra avec des réponses prédéfinies.")
print()
print("=" * 50)