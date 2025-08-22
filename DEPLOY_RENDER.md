# 🚀 Guide de Déploiement sur Render - Portail Constructo AI avec Assistant

## 📋 Prérequis

- Compte GitHub avec le code
- Compte Render.com (gratuit)
- (Optionnel) Clé API Claude Anthropic

## 🎯 Étapes de Déploiement

### 1️⃣ Préparer le Repository GitHub

1. **Pusher le code sur GitHub:**
```bash
git add .
git commit -m "Ajout assistant Sylvain Leduc avec Claude API"
git push origin main
```

2. **Fichiers requis dans le repo:**
- ✅ `portal_with_claude_api.py` (application principale)
- ✅ `requirements_render.txt` (dépendances)
- ✅ `style_portal.css` (styles)
- ✅ `render_deploy.yaml` (config Render)

### 2️⃣ Configurer sur Render

1. **Créer un nouveau Web Service:**
   - Allez sur [dashboard.render.com](https://dashboard.render.com)
   - Cliquez sur "New +" → "Web Service"
   - Connectez votre repo GitHub

2. **Configuration de base:**
   ```
   Name: portail-constructoai-assistant
   Region: Oregon (US West) ou Frankfurt (Europe)
   Branch: main
   Runtime: Python 3
   Plan: Free (ou Starter pour $7/mois)
   ```

3. **Build Command:**
   ```bash
   pip install --upgrade pip && pip install -r requirements_render.txt
   ```

4. **Start Command:**
   ```bash
   streamlit run portal_with_claude_api.py --server.port=$PORT --server.address=0.0.0.0 --server.enableCORS=true --server.enableXsrfProtection=false
   ```

### 3️⃣ Variables d'Environnement

Dans Render Dashboard → Environment :

#### Obligatoires:
```
PYTHON_VERSION = 3.11.0
STREAMLIT_SERVER_HEADLESS = true
STREAMLIT_SERVER_ENABLE_CORS = true
STREAMLIT_SERVER_ENABLE_XSRF_PROTECTION = false
```

#### Optionnel (pour Claude API):
```
ANTHROPIC_API_KEY = sk-ant-api03-xxxxx
```

> ⚠️ **Sans clé API**, l'assistant fonctionne en **mode démo** avec réponses prédéfinies

### 4️⃣ Déployer

1. Cliquez sur "Create Web Service"
2. Attendez le build (5-10 minutes première fois)
3. URL générée: `https://portail-constructoai-assistant.onrender.com`

## 🔧 Dépannage

### Erreur "Application not found"
```bash
# Vérifier que le fichier principal existe
ls portal_with_claude_api.py

# Sinon, renommer:
mv portal_with_assistant.py portal_with_claude_api.py
git add . && git commit -m "Fix filename" && git push
```

### Erreur "Port binding"
Assurez-vous que Start Command contient: `--server.port=$PORT`

### Assistant ne répond pas
- Vérifiez les logs: Render Dashboard → Logs
- Mode démo activé si pas de clé API
- Limite de 10 échanges par session

### Performance lente (plan gratuit)
- Normal: Render Free ralentit après 15 min d'inactivité
- Solution: Upgrade vers Starter ($7/mois)

## 📊 Monitoring

### Métriques à surveiller:
- **Memory**: < 500MB normalement
- **CPU**: Pics lors des requêtes
- **Requests**: Limite 100k/mois (plan gratuit)
- **Bandwidth**: 100GB/mois (plan gratuit)

### Logs importants:
```
✅ Claude API initialisée = API active
💬 Mode Démo = Pas de clé API
```

## 🌐 URLs de Production

Après déploiement:
- **Portail**: `https://[votre-app].onrender.com`
- **Health Check**: `https://[votre-app].onrender.com/_stcore/health`

## 💰 Coûts

### Plan Gratuit Render:
- ✅ 750 heures/mois
- ✅ Auto-sleep après 15 min
- ✅ 100GB bandwidth
- ❌ Domaine custom

### Plan Starter ($7/mois):
- ✅ Always-on (pas de sleep)
- ✅ Domaine custom
- ✅ Performance garantie
- ✅ Support prioritaire

### Coûts Claude API (si utilisé):
- Sonnet 4: Tarification selon Anthropic
- Sonnet 3.5: ~$3/million tokens (fallback)
- Haiku: ~$0.25/million tokens (économique)
- Estimation: $5-10/mois usage normal

## 🔒 Sécurité

1. **Ne jamais commiter `.env` avec clés**
2. **Utiliser Environment Variables dans Render**
3. **Activer HTTPS (automatique sur Render)**
4. **Limiter les échanges (10 max configuré)**

## 📈 Optimisations

### Pour réduire les coûts:
1. Limiter tokens Claude à 300
2. Max 10 échanges par session
3. Cache les réponses fréquentes
4. Mode démo par défaut

### Pour améliorer performance:
1. Upgrade vers Starter
2. Utiliser CDN pour assets
3. Compresser images
4. Minifier CSS

## ✅ Checklist Finale

- [ ] Code pushé sur GitHub
- [ ] Render Web Service créé
- [ ] Build Command configuré
- [ ] Start Command configuré
- [ ] Variables environnement ajoutées
- [ ] Déploiement réussi
- [ ] URL accessible
- [ ] Assistant fonctionne (mode démo ou API)
- [ ] 7 applications accessibles
- [ ] Footer chat visible

## 🆘 Support

- **Render Status**: [status.render.com](https://status.render.com)
- **Render Docs**: [render.com/docs](https://render.com/docs)
- **Streamlit Deploy**: [docs.streamlit.io](https://docs.streamlit.io)
- **Contact**: info@constructoai.ca

---

**💡 Astuce:** Commencez sans clé API Claude. Une fois que tout fonctionne, ajoutez la clé pour activer l'IA complète.

**🎯 Succès:** Votre portail sera accessible mondialement avec l'assistant Sylvain Leduc intégré!