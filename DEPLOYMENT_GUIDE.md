# 📚 Guide de Déploiement - Portail ConstructoAI

## 🚀 Déploiement sur GitHub et Render

### Étape 1: Préparation sur GitHub

1. **Créer un nouveau repository sur GitHub**
   - Allez sur [github.com](https://github.com)
   - Cliquez sur "New repository"
   - Nom suggéré: `portail-constructoai`
   - Description: "Portail centralisé pour les solutions IA ConstructoAI"
   - Public ou Private selon votre préférence
   - **NE PAS** initialiser avec README (vous en avez déjà un)

2. **Initialiser Git localement**
   ```bash
   cd E:\09. LOGICIELS\GITHUB\PORTAIL
   git init
   git add .
   git commit -m "Initial commit - Portail ConstructoAI"
   ```

3. **Connecter au repository GitHub**
   ```bash
   git remote add origin https://github.com/VOTRE-USERNAME/portail-constructoai.git
   git branch -M main
   git push -u origin main
   ```

### Étape 2: Déploiement sur Render

1. **Créer un compte Render** (si pas déjà fait)
   - Allez sur [render.com](https://render.com)
   - Inscrivez-vous ou connectez-vous

2. **Créer un nouveau Web Service**
   - Cliquez sur "New +"
   - Sélectionnez "Web Service"
   - Connectez votre compte GitHub si pas déjà fait
   - Sélectionnez le repository `portail-constructoai`

3. **Configuration du service**
   ```
   Name: portail-constructoai
   Region: Oregon (US West) ou Frankfurt (EU)
   Branch: main
   Root Directory: (laisser vide)
   Runtime: Python
   Build Command: pip install -r requirements.txt
   Start Command: streamlit run portal.py --server.port=$PORT --server.address=0.0.0.0
   ```

4. **Plan de service**
   - Sélectionnez "Free" pour commencer
   - Vous pouvez upgrader plus tard si nécessaire

5. **Variables d'environnement** (optionnel)
   Aucune variable requise pour le portail basique

6. **Cliquez sur "Create Web Service"**

### Étape 3: Configuration du domaine personnalisé

Une fois déployé, votre portail sera accessible à:
`https://portail-constructoai.onrender.com`

Pour ajouter un domaine personnalisé comme `portail.constructoai.ca`:

1. **Dans Render:**
   - Allez dans Settings > Custom Domains
   - Ajoutez `portail.constructoai.ca`
   - Notez les instructions DNS

2. **Dans GoDaddy:**
   - Ajoutez un enregistrement CNAME
   - Name: `portail`
   - Data: `portail-constructoai.onrender.com`
   - TTL: 1 Hour

3. **Vérification:**
   - Retournez dans Render
   - Cliquez "Verify" sur le domaine
   - Attendez la propagation DNS (5-30 minutes)

## 📝 Structure des fichiers pour le déploiement

```
portail-constructoai/
├── portal.py              # Application principale
├── style_portal.css       # Styles CSS
├── requirements.txt       # Dépendances Python
├── runtime.txt           # Version Python pour Render
├── render.yaml           # Configuration Render (optionnel)
├── Procfile              # Commandes de démarrage
├── setup.sh              # Script de configuration
├── .gitignore            # Fichiers à ignorer
├── .streamlit/
│   └── config.toml       # Configuration Streamlit
└── README.md             # Documentation
```

## 🔧 Commandes Git utiles

### Mise à jour du code
```bash
git add .
git commit -m "Description des changements"
git push origin main
```

### Vérifier le statut
```bash
git status
git log --oneline
```

### Créer une branche pour tests
```bash
git checkout -b dev
# Faire des changements
git add .
git commit -m "Test feature"
git push origin dev
```

## ⚙️ Configuration avancée

### Optimisation des performances sur Render

1. **Mise en cache des ressources**
   - Les fichiers CSS sont automatiquement mis en cache
   - Les images statiques sont servies efficacement

2. **Auto-scaling** (Plan payant)
   - Render peut automatiquement scaler votre app
   - Configurez dans Dashboard > Settings > Scaling

3. **Monitoring**
   - Render fournit des métriques automatiques
   - Dashboard > Metrics pour voir l'utilisation

## 🐛 Troubleshooting

### Problème: "Module not found"
**Solution:** Vérifiez que tous les modules sont dans requirements.txt

### Problème: "Port binding error"
**Solution:** Utilisez `$PORT` dans la commande de démarrage

### Problème: "Build failed"
**Solution:** Vérifiez les logs dans Render Dashboard

### Problème: CSS non chargé
**Solution:** Assurez-vous que `style_portal.css` est committé

## 🔄 Mise à jour automatique

Avec la configuration actuelle:
1. Chaque `git push` sur la branche `main`
2. Déclenche automatiquement un redéploiement sur Render
3. L'app est mise à jour en ~2-3 minutes

## 📊 Monitoring et Logs

### Sur Render:
- **Logs:** Dashboard > Logs
- **Metrics:** Dashboard > Metrics
- **Events:** Dashboard > Events

### Commandes utiles:
```bash
# Voir les logs en temps réel (si Render CLI installé)
render logs --tail

# Vérifier le statut
render status
```

## 🚨 Sécurité

1. **HTTPS automatique**
   - Render fournit SSL/TLS gratuit
   - Forcé sur tous les domaines

2. **Protection DDoS**
   - Protection basique incluse
   - Upgrade pour protection avancée

3. **Secrets** (si nécessaire)
   - Utilisez Environment Variables dans Render
   - Ne jamais committer de secrets dans Git

## 💰 Coûts

### Plan Free:
- ✅ 750 heures/mois
- ✅ SSL gratuit
- ✅ Déploiement automatique
- ⚠️ Spin down après 15 min d'inactivité
- ⚠️ Limité en ressources

### Plan Starter ($7/mois):
- ✅ Always-on
- ✅ Plus de ressources
- ✅ Support prioritaire
- ✅ Métriques avancées

## 📞 Support

### Render:
- Documentation: [render.com/docs](https://render.com/docs)
- Status: [status.render.com](https://status.render.com)
- Support: Dashboard > Help

### ConstructoAI:
- Email: info@constructoai.ca
- GitHub Issues: github.com/VOTRE-USERNAME/portail-constructoai/issues

## ✅ Checklist de déploiement

- [ ] Code pushé sur GitHub
- [ ] Service créé sur Render
- [ ] Build réussi
- [ ] Application accessible via .onrender.com
- [ ] Domaine personnalisé configuré (optionnel)
- [ ] SSL vérifié
- [ ] Tests de navigation effectués
- [ ] Monitoring activé

---

**Dernière mise à jour:** Décembre 2024
**Version:** 1.0.0