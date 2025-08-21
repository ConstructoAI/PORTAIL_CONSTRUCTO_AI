# 🏗️ Portail Constructo AI

[![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-FF6B6B.svg)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://python.org)
[![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen.svg)]()

> **Vos Assistant AI pour la construction**

## 🎯 Description

**Constructo AI** est votre point d'accès unique à l'écosystème complet de solutions IA dédiées au secteur de la construction au Québec. Cette plateforme intelligente révolutionne vos projets de construction en vous permettant d'estimer et vérifier vos projets 4x plus vite.

## 🚀 Applications Disponibles

### 🏗️ **EXPERTS IA** - [experts-ai.constructoai.ca](https://experts-ai.constructoai.ca/)
Assistant IA avec 60+ experts spécialisés en construction
- 60+ profils d'experts métiers
- Analyse de documents avancée
- Recherche web intégrée
- Export professionnel

### 📐 **TAKEOFF AI** - [takeoff-ai.constructoai.ca](https://takeoff-ai.constructoai.ca/)
Système d'estimation de construction avec IA Claude
- Visualisation et annotation de plans PDF
- 5 modes de mesure (distance, surface, périmètre, angle, calibration)
- Assistant IA Claude intégré pour conseils experts
- Export rapports CSV/JSON/PDF

### 🏭 **ERP AI** - [erp-ai.constructoai.ca](https://erp-ai.constructoai.ca/)
Solution ERP industrielle complète
- 61 postes de travail configurés (Soudage, CNC, Assemblage)
- TimeTracker intégré avec synchronisation temps réel
- CRM et RH avec gestion des compétences
- Multi-vues: Dashboard, Kanban, Gantt, Calendrier

### 📊 **SEAOP** - [seaop.constructoai.ca](https://seaop.constructoai.ca/)
Système Électronique d'Appel d'Offres Public
- Plateforme de mise en relation clients-entrepreneurs
- Chat en temps réel intégré
- Système d'évaluations 5 étoiles
- Dashboard analytics avec KPIs

### 🏗️ **B2B** - [b2b.constructoai.ca](https://b2b.constructoai.ca/)
Plateforme B2B de gestion des soumissions pour entreprises RBQ
- Workflow d'approbation intelligent en 5 étapes
- Évaluation multi-critères automatisée
- Validation RBQ et certifications
- Dashboard analytique avec KPIs B2B

### 🏢 **C2B** - [c2b.constructoai.ca](https://c2b.constructoai.ca/)
Portail Client à Entreprise mono-entreprise
- Réception automatique des demandes clients
- Création de soumissions personnalisées
- Dashboard entreprise propriétaire
- Suivi temps réel et notifications

### 📋 **Feuille de Soumission** - [constructoai.github.io/FEUILLE_SOUMISSION/](https://constructoai.github.io/FEUILLE_SOUMISSION/)
Générateur de soumissions professionnelles
- Templates personnalisés
- Calculs automatiques
- Export PDF professionnel
- Suivi des soumissions

## 💻 Installation

### Prérequis
- Python 3.9 ou supérieur
- pip (gestionnaire de packages Python)

### Installation rapide

1. **Cloner le repository**
```bash
git clone https://github.com/constructoai/portail.git
cd portail
```

2. **Installer les dépendances**
```bash
pip install -r requirements.txt
```

3. **Lancer l'application**
```bash
streamlit run portal.py
```

Ou utilisez le script batch fourni (Windows) :
```bash
run_portal.bat
```

## 🎨 Fonctionnalités

### Interface Moderne
- ✨ Design professionnel épuré avec cartes blanches et ombres subtiles
- 🎯 Navigation intuitive et responsive avec effets de survol
- 🔍 Recherche et filtrage intelligent des applications
- 📊 Statistiques en temps réel (2,500+ utilisateurs, 15,000+ projets)
- 🎨 Animations CSS fluides et transitions professionnelles

### Modes d'Affichage
- **Vue Cartes** : Affichage en grille avec design professionnel blanc
- **Vue Liste** : Affichage détaillé avec descriptions complètes

### Filtres Intelligents
- Par catégorie (Expertise, Estimation, Gestion, Appels d'Offres, etc.)
- Par recherche textuelle
- Par statut de production

## 📁 Structure du Projet

```
portail/
├── portal.py              # Application principale Streamlit
├── style_portal.css       # Styles CSS professionnels
├── requirements.txt       # Dépendances Python (streamlit>=1.48.0)
├── Procfile              # Configuration déploiement Render
├── run_portal.bat        # Script de lancement Windows
├── INSTRUCTIONS_RENDER.md # Guide de déploiement Render
└── README.md             # Documentation complète
```

## 🔧 Configuration

### Variables d'environnement (optionnel)
Créez un fichier `.env` pour configurer :
```env
# Port personnalisé (défaut: 8501)
STREAMLIT_SERVER_PORT=8501

# Thème (light/dark)
STREAMLIT_THEME_BASE="light"
```

### Personnalisation
Modifiez les applications dans `portal.py` :
```python
APPLICATIONS = [
    {
        "name": "Nouvelle App",
        "url": "https://nouvelle-app.constructoai.ca",
        "description": "Description",
        # ...
    }
]
```

## 🚀 Déploiement

### Option 1: Streamlit Cloud
1. Push vers GitHub
2. Connectez à [share.streamlit.io](https://share.streamlit.io)
3. Déployez automatiquement

### Option 2: Render.com (Production - Recommandé)
1. Créez un nouveau Web Service sur [render.com](https://render.com)
2. Connectez votre repository GitHub
3. **Build Command:**
   ```bash
   pip install --upgrade pip && pip install -r requirements.txt
   ```
4. **Start Command:**
   ```bash
   streamlit run portal.py --server.port=$PORT --server.address=0.0.0.0 --server.enableCORS=true --server.enableXsrfProtection=false
   ```
5. Déploiement automatique à chaque push sur `main`

### Option 3: Docker
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8501
CMD ["streamlit", "run", "portal.py"]
```

## 🔧 Dépannage Déploiement

### Problèmes courants sur Render
Si vous obtenez une erreur "Not Found" :

1. **Supprimer les fichiers conflictuels :**
   ```bash
   git rm setup.sh render.yaml runtime.txt
   git commit -m "Fix deployment - remove conflicting files"
   git push origin main
   ```

2. **Vérifier la configuration Render :**
   - Build Command : `pip install --upgrade pip && pip install -r requirements.txt`
   - Start Command : `streamlit run portal.py --server.port=$PORT --server.address=0.0.0.0 --server.enableCORS=true --server.enableXsrfProtection=false`

3. **Clear Build Cache :**
   - Dashboard Render > Settings > "Clear build cache"
   - Redéployer manuellement

Consultez `INSTRUCTIONS_RENDER.md` pour plus de détails.

## 📊 Statistiques

Le portail affiche en temps réel :
- 👥 **2,500+** Utilisateurs actifs
- 📁 **15,000+** Projets gérés
- 🏢 **350+** Entreprises clientes
- 💰 **3.5M$** Économies réalisées

## 🛡️ Sécurité

- ✅ Connexions HTTPS sécurisées
- 🔒 Chiffrement SSL/TLS
- 🛡️ Protection contre les injections
- 📝 Logs d'accès détaillés

## 🤝 Support

### Documentation
- Manuel complet : [docs.constructoai.ca](https://docs.constructoai.ca)
- API Reference : [api.constructoai.ca](https://api.constructoai.ca)

### Contact
- 📧 Email : info@constructoai.ca
- 📞 Téléphone : 514-820-1972
- 📍 Localisation : Farnham, Québec
- 💬 Chat : Disponible sur chaque application

## 📝 Licence

© 2025 Constructo AI - Tous droits réservés | Développé par Sylvain Leduc

---

## 🎯 Roadmap

### Version 1.1 (Q1 2025)
- [ ] Dashboard analytique intégré
- [ ] Système de notifications
- [ ] Mode sombre/clair

### Version 1.2 (Q2 2025)
- [ ] Authentification SSO
- [ ] API REST publique
- [ ] Mobile responsive amélioré

### Version 2.0 (Q3 2025)
- [ ] Intelligence artificielle prédictive
- [ ] Intégrations tierces
- [ ] Multi-langue (FR/EN)

---

## 🏆 Équipe

**Sylvain Leduc**
📧 info@constructoai.ca
📞 514-820-1972
📍 Farnham, Québec

Leader en solutions IA pour la construction au Québec
- Innovation continue depuis 2023
- Support technique personnalisé

---

**Pour toute question ou suggestion, n'hésitez pas à nous contacter !**