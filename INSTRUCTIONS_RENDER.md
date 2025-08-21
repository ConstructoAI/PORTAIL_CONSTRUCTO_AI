# 🚀 Instructions pour corriger le déploiement sur Render

## ❌ Fichiers à SUPPRIMER de votre repository GitHub :
- `setup.sh`
- `render.yaml` 
- `runtime.txt`

## ✅ Fichiers à GARDER :
- `portal.py`
- `style_portal.css`
- `requirements.txt`
- `Procfile`
- `.streamlit/config.toml`
- `README.md`
- `DEPLOYMENT_GUIDE.md`

## 📝 Configuration sur Render :

### Dans les Settings de votre service Render :

**Build Command :**
```
pip install --upgrade pip && pip install -r requirements.txt
```

**Start Command :**
```
streamlit run portal.py --server.port=$PORT --server.address=0.0.0.0 --server.enableCORS=true --server.enableXsrfProtection=false
```

## 🔄 Étapes pour corriger :

1. **Sur GitHub :**
```bash
# Supprimer les fichiers problématiques
git rm setup.sh render.yaml runtime.txt
git add .
git commit -m "Fix Render deployment - remove conflicting files"
git push origin main
```

2. **Sur Render :**
- Le redéploiement devrait se faire automatiquement
- Si non, cliquez sur "Manual Deploy" > "Deploy latest commit"

3. **Attendez 2-3 minutes** que le build se termine

4. **Testez** : https://portail-constructo-ai.onrender.com

## 🐛 Si le problème persiste :

### Option 1 - Recréer le service :
1. Supprimez le service actuel sur Render
2. Créez un nouveau Web Service
3. Utilisez les commandes ci-dessus

### Option 2 - Clear Build Cache :
1. Dans Render Dashboard > Settings
2. Cliquez sur "Clear build cache"
3. Redéployez

## ✅ Le site devrait maintenant fonctionner !

L'application Streamlit devrait s'afficher correctement avec toutes les cartes des applications Constructo AI.