# 🏗️ Portail ConstructoAI

[![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-FF6B6B.svg)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://python.org)
[![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen.svg)]()

> **Centre de Solutions IA pour la Construction au Québec**

## 🎯 Description

Le **Portail ConstructoAI** est votre point d'accès unique à l'écosystème complet de solutions IA dédiées au secteur de la construction au Québec. Cette interface élégante centralise l'accès à toutes nos applications spécialisées.

## 🚀 Applications Disponibles

### 🏗️ **EXPERTS IA** - [experts-ai.constructoai.ca](https://experts-ai.constructoai.ca/)
Assistant IA avec 60+ experts spécialisés en construction
- 60+ profils d'experts métiers
- Analyse de documents avancée
- Recherche web intégrée
- Export professionnel

### 📐 **TAKEOFF AI** - [takeoff-ai.constructoai.ca](https://takeoff-ai.constructoai.ca/)
Système d'estimation et de métrés automatisé
- Calculs automatiques précis
- Métrés détaillés
- Estimations professionnelles
- Rapports Excel

### 💼 **ERP AI** - [erp-ai.constructoai.ca](https://erp-ai.constructoai.ca/)
Système de gestion intégré pour entreprises
- Gestion de projets complète
- Suivi budgétaire en temps réel
- Planning des ressources
- Tableaux de bord dynamiques

### 🌊 **SEAOP** - [seaop.constructoai.ca](https://seaop.constructoai.ca/)
Optimisation des opérations et processus
- Optimisation des workflows
- Analyse de performance
- Automatisation intelligente
- KPIs temps réel

### 🤝 **B2B PBR8** - [b2b-pbr8.constructoai.ca](https://b2b-pbr8.constructoai.ca/)
Plateforme B2B pour collaboration inter-entreprises
- Réseau professionnel
- Échange de documents sécurisé
- Gestion d'appels d'offres
- Partenariats stratégiques

### 👥 **C2B CS4P** - [c2b-cs4p.constructoai.ca](https://c2b-cs4p.constructoai.ca/)
Interface client-entreprise pour services
- Portail clients intuitif
- Suivi de projets en direct
- Communication directe
- Satisfaction client

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
- ✨ Design professionnel avec animations fluides
- 🎯 Navigation intuitive et responsive
- 🔍 Recherche et filtrage des applications
- 📊 Statistiques en temps réel

### Modes d'Affichage
- **Vue Cartes** : Affichage en grille avec aperçu visuel
- **Vue Liste** : Affichage détaillé avec descriptions complètes

### Filtres Intelligents
- Par catégorie (Expertise, Gestion, Collaboration, etc.)
- Par recherche textuelle
- Par statut de production

## 📁 Structure du Projet

```
portail/
├── portal.py           # Application principale Streamlit
├── style_portal.css    # Styles CSS professionnels
├── requirements.txt    # Dépendances Python
├── run_portal.bat      # Script de lancement Windows
└── README.md          # Documentation
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

### Option 2: Render.com
1. Créez un nouveau Web Service
2. Connectez votre repo GitHub
3. Build command: `pip install -r requirements.txt`
4. Start command: `streamlit run portal.py --server.port=$PORT`

### Option 3: Docker
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8501
CMD ["streamlit", "run", "portal.py"]
```

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
- 📞 Téléphone : 1-888-CONSTRUCT
- 💬 Chat : Disponible sur chaque application

## 📝 Licence

© 2025 ConstructoAI - Tous droits réservés

Développé avec ❤️ au Québec

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

**Développé par ConstructoAI**
- Leader en solutions IA pour la construction au Québec
- Innovation continue depuis 2023
- Support technique 24/7

---

**Pour toute question ou suggestion, n'hésitez pas à nous contacter !**