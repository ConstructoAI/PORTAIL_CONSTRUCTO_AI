#!/usr/bin/env python3
# test_local.py - Test de l'application en local

import sys
import os

print("=== Test de l'environnement ===")
print(f"Python version: {sys.version}")
print(f"Répertoire actuel: {os.getcwd()}")
print(f"Fichiers présents: {os.listdir('.')}")

# Vérifier les imports
try:
    import streamlit as st
    print(f"✓ Streamlit version: {st.__version__}")
except ImportError as e:
    print(f"✗ Erreur Streamlit: {e}")

# Vérifier le fichier principal
if os.path.exists("portal.py"):
    print("✓ portal.py trouvé")
else:
    print("✗ portal.py NON trouvé")

# Vérifier le CSS
if os.path.exists("style_portal.css"):
    print("✓ style_portal.css trouvé")
else:
    print("✗ style_portal.css NON trouvé")

print("\n=== Pour tester localement ===")
print("Exécutez: streamlit run portal.py")