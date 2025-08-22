# portal_with_claude_api.py - Portail Constructo AI avec Assistant Claude API
import streamlit as st
import time
from datetime import datetime
import json
import os

# Configuration de la page
st.set_page_config(
    page_title="Portail Constructo AI - Centre de Solutions IA",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Tentative d'import de l'API Claude
try:
    from anthropic import Anthropic
    ANTHROPIC_AVAILABLE = True
except ImportError:
    ANTHROPIC_AVAILABLE = False

# Tentative de chargement des variables d'environnement
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# Classe Assistant IA avec profil Sylvain Leduc et support Claude API
class AssistantIA:
    """Assistant IA Sylvain Leduc avec support Claude API optionnel"""
    
    def __init__(self):
        self.max_exchanges = 10
        self.exchange_count = 0
        self.profile = "Sylvain Leduc - Créateur de Constructo AI"
        self.api_key = os.getenv("ANTHROPIC_API_KEY", "")
        self.client = None
        self.mode = "Mode Démo 🎯"
        
        # Initialiser Claude si disponible
        if ANTHROPIC_AVAILABLE and self.api_key:
            try:
                self.client = Anthropic(api_key=self.api_key)
                self.mode = "Claude API ✅"
                print(f"✅ Claude API initialisée avec succès - Mode intelligent activé")
                print(f"✅ Clé API détectée: {self.api_key[:10]}...")
            except Exception as e:
                print(f"⚠️ Erreur d'initialisation Claude: {e}")
                self.client = None
                self.mode = "Mode Démo 🎯"
        else:
            print(f"⚠️ Mode démo - ANTHROPIC_AVAILABLE: {ANTHROPIC_AVAILABLE}, API_KEY présente: {bool(self.api_key)}")
    
    def get_system_prompt(self):
        """Retourne le prompt système pour Claude"""
        return """Tu es Sylvain Leduc, créateur et développeur principal de l'écosystème Constructo AI.

INSTRUCTIONS:
1. Tu es expert en construction et en IA, spécialisé dans les 7 applications Constructo AI (+ le portail)
2. Tu peux discuter de sujets connexes à la construction tout en ramenant vers tes solutions
3. Réponses détaillées et utiles (200-300 mots selon le besoin)
4. Tu parles à la première personne en tant que créateur passionné et accessible

TES 7 APPLICATIONS (+ LE PORTAIL):
1. EXPERTS AI - 60+ experts IA spécialisés révolutionnaires, 2,400+ années expérience cumulative, architecture 6,000+ lignes, valorisation 36-55M$ CAD, impossible reproduire 5-10 ans
2. TAKEOFF AI - 5 outils mesure PDF professionnels, mode orthogonal 8 directions (0°-315°), 18 viewers optimisés, accrochage intelligent, catalogue produits prix 2025
3. ERP AI - 120 postes construction (charpentier, électricien, plombier, etc.), TimeTracker granulaire, CRM/RH intégrés, 25 phases construction, conformité RBQ/CCQ/CNESST
4. B2B - Workflow d'approbation 5 étapes, validation RBQ, évaluation multi-critères, 10 tables métier, chiffrement SHA-256, 20+ types projets Québec
5. SEAOP - Système appels d'offres publics, calcul urgence automatique 🟢🟡🟠🔴 intelligent, chat Facebook-style avec likes, badges RBQ, 3,000+ lignes
6. C2B - Portail mono-entreprise dédié, configuration 3 clics, workflow Client→Entreprise→Notification, 7,200+ lignes code, modèle d'affaires portails individuels
7. FEUILLE SOUMISSION - Générateur HTML autonome 5,190 lignes, calculateur interactif temps réel, export JSON/HTML, impression PDF
8. PORTAIL - Hub central unifié

MÉTRIQUES CLÉS:
- ROI moyen: 30 jours
- Productivité: +30-45%
- Économies: 20h/semaine (1,000$/semaine)
- 3.5M$ économisés collectivement
- 2,500+ utilisateurs, 15,000+ projets

CONTACT:
- Téléphone: 514-820-1972
- Email: info@constructoai.ca
- Localisation: Farnham, Québec

Pour questions hors-sujet, réponds: "Je me spécialise exclusivement dans Constructo AI. Quelle application vous intéresse?"
"""
    
    def get_response_from_claude(self, user_message: str, conversation_history: list = None):
        """Obtient une réponse de Claude API"""
        if not self.client:
            return None
            
        try:
            # Construire l'historique
            messages = []
            if conversation_history:
                # Limiter à 6 derniers messages pour économiser
                recent = conversation_history[-6:]
                for msg in recent:
                    role = "user" if msg["role"] == "user" else "assistant"
                    messages.append({
                        "role": role,
                        "content": msg["content"]
                    })
            
            # Ajouter le message actuel
            messages.append({
                "role": "user",
                "content": user_message
            })
            
            # Appel à Claude avec le modèle Sonnet le plus récent
            response = self.client.messages.create(
                model="claude-3-5-sonnet-20241022",  # Modèle Sonnet 3.5 le plus récent
                system=self.get_system_prompt(),
                messages=messages,
                max_tokens=500,  # Augmenté pour des réponses plus complètes
                temperature=0.7
            )
            
            return response.content[0].text
            
        except Exception as e:
            print(f"Erreur Claude API: {e}")
            # Si le modèle demandé n'existe pas, essayer avec des modèles de fallback
            if "model" in str(e).lower() or "does not exist" in str(e).lower():
                fallback_models = [
                    "claude-3-5-sonnet-20241022",  # Fallback vers Sonnet 3.5
                    "claude-3-sonnet-20240229",    # Fallback vers Sonnet 3
                    "claude-3-haiku-20240307"      # Fallback final vers Haiku
                ]
                
                for fallback_model in fallback_models:
                    try:
                        print(f"Tentative avec modèle de fallback: {fallback_model}")
                        response = self.client.messages.create(
                            model=fallback_model,
                            system=self.get_system_prompt(),
                            messages=messages,
                            max_tokens=300,
                            temperature=0.7
                        )
                        return response.content[0].text
                    except:
                        continue
                        
                return None
            return None
    
    def get_response(self, user_message: str, conversation_history: list = None) -> str:
        """Génère une réponse (Claude API si disponible, sinon mode démo)"""
        user_msg_lower = user_message.lower()
        
        # Essayer d'abord avec Claude API si disponible (PRIORITÉ ABSOLUE)
        if self.client:
            try:
                claude_response = self.get_response_from_claude(user_message, conversation_history)
                if claude_response:
                    return claude_response
            except Exception as e:
                print(f"Erreur API, passage au mode démo: {e}")
        
        # Vérifier le compteur d'échanges SEULEMENT en mode démo
        self.exchange_count += 1
        if self.exchange_count > self.max_exchanges:
            return ("🎯 **Nous avons bien couvert Constructo AI!**\n\n"
                   "Pour une démonstration personnalisée ou plus de détails:\n"
                   "📞 Appelez-moi au 514-820-1972\n"
                   "📧 info@constructoai.ca\n\n"
                   "À bientôt pour transformer votre entreprise! - Sylvain Leduc")
        
        # ===== MODE DÉMO - Réponses prédéfinies =====
        
        # Détecter les questions hors-sujet et rediriger
        offtopic_keywords = ["météo", "sport", "politique", "cuisine", "voyage", "film", "musique", "jeu"]
        if any(word in user_msg_lower for word in offtopic_keywords):
            return ("💡 **Je comprends votre question, mais en tant que créateur de Constructo AI,** "
                   "je me spécialise exclusivement dans nos 7 applications pour la construction.\n\n"
                   "Revenons à comment Constructo AI peut transformer votre entreprise! "
                   "Quelle application vous intéresse le plus?")
        
        # Réponses spécifiques aux applications
        if "experts" in user_msg_lower or "expert" in user_msg_lower:
            return ("🏗️ **EXPERTS IA - Mon chef-d'œuvre avec 60+ profils spécialisés!**\n\n"
                   "**Révolution unique au monde:**\n"
                   "• 60+ experts IA spécialisés vs 1-3 concurrents\n"
                   "• 2,400+ années d'expérience cumulative\n"
                   "• Impossible à reproduire en moins de 5-10 ans!\n\n"
                   "**Architecture 6,000+ lignes:**\n"
                   "• app.py (1,089 lignes), expert_logic.py (659 lignes)\n"
                   "• conversation_manager.py persistance SQLite\n"
                   "• 60+ profils experts détaillés avec prix 2025\n"
                   "• Recherche web contextuelle + analyse documents\n\n"
                   "**Valorisation estimée: 36-55M$ CAD** - c'est notre joyau!")
        
        elif "takeoff" in user_msg_lower:
            return ("📐 **TAKEOFF AI - Mon système de mesure PDF révolutionnaire!**\n\n"
                   "**5 outils de mesure professionnels:**\n"
                   "• Distance linéaire, Surface (polygones), Périmètre\n"
                   "• Angle (3 points), Calibration d'échelle\n\n"
                   "**Mode orthogonal 8 directions intelligent:**\n"
                   "• Angles: 0°, 45°, 90°, 135°, 180°, 225°, 270°, 315°\n"
                   "• Accrochage automatique aux lignes et points\n"
                   "• Guides visuels pointillés en temps réel\n\n"
                   "**18 viewers PDF optimisés** (fast, smooth, reactive, ultra_fast...)\n"
                   "**Catalogue produits** avec prix 2025 intégrés!")
        
        elif "erp" in user_msg_lower:
            return ("🏭 **ERP AI - J'ai conçu 120 postes de travail pour la construction!**\n\n"
                   "**Structure complète:**\n"
                   "• 12 postes INGÉNIERIE (architecte, ingénieurs, BIM)\n"
                   "• 7 postes DÉMOLITION (décontamination, excavation)\n"
                   "• 6 postes BÉTON (coffreur, ferrailleur, cimentier)\n"
                   "• 8 postes ISOLATION (uréthane, cellulose, acoustique)\n"
                   "• 13 postes EXTÉRIEUR (paysagiste, paveur, piscine)\n\n"
                   "**TimeTracker Québec** avec pointage granulaire et mapping automatique!\n"
                   "25 phases construction + conformité RBQ/CCQ native!")
        
        elif "b2b" in user_msg_lower:
            return ("🤝 **B2B CONSTRUCTION - Ma plateforme d'approbation révolutionnaire!**\n\n"
                   "**Workflow intelligent 5 étapes:**\n"
                   "1. 📥 Réception automatique\n"
                   "2. 🔍 Évaluation technique RBQ\n"
                   "3. 💰 Évaluation financière pondérée\n"
                   "4. 📊 Synthèse globale multi-critères\n"
                   "5. ✅ Décision finale automatisée\n\n"
                   "**Architecture complète:**\n"
                   "• 10 tables métier optimisées\n"
                   "• 20+ types projets construction Québec\n"
                   "• Validation RBQ instantanée\n"
                   "• Chiffrement SHA-256 sécurisé\n"
                   "• Audit trail complet\n\n"
                   "Plus de 350+ entreprises RBQ certifiées!")
        
        elif "seaop" in user_msg_lower or "appel" in user_msg_lower and "offre" in user_msg_lower:
            return ("🏛️ **SEAOP - Mon système d'appels d'offres publics révolutionnaire!**\n\n"
                   "**Calcul automatique d'urgence intelligent:**\n"
                   "• 🟢 Faible: 14+ jours (délai confortable)\n"
                   "• 🟡 Normal: 7-14 jours (dans les temps)\n"
                   "• 🟠 Élevé: 3-7 jours (assez urgent)\n"
                   "• 🔴 Critique: <3 jours ou échéance dépassée\n\n"
                   "**Chat communautaire Facebook-style:**\n"
                   "• Messages instantanés + likes\n"
                   "• Badges utilisateurs (Premium, RBQ Vérifié)\n"
                   "• Indicateurs temps réel + notifications\n\n"
                   "**3,000+ lignes optimisées** pour projets publics Québec!")
        
        elif "c2b" in user_msg_lower:
            return ("🏢 **C2B PORTAIL - Ma solution mono-entreprise révolutionnaire!**\n\n"
                   "**Concept unique Client-to-Business:**\n"
                   "• UN portail dédié = UNE entreprise propriétaire\n"
                   "• Configuration en 3 clics avec assistant Windows\n"
                   "• Personnalisation complète (nom, RBQ, couleurs)\n"
                   "• Workflow direct Client → Entreprise → Notification\n\n"
                   "**7 étapes simplifiées:**\n"
                   "📝 Demande client → 📥 Réception → 📋 Soumission → 👀 Évaluation → ✅ Acceptation → 🔔 Notification → 📞 Suivi\n\n"
                   "**Modèle d'affaires:** Créez des portails individuels pour chaque entreprise!\n"
                   "Plus de 7,200 lignes de code optimisées!")
        
        elif "workflow" in user_msg_lower or "approbation" in user_msg_lower or "étape" in user_msg_lower:
            return ("⚙️ **Mon workflow d'approbation B2B révolutionnaire!**\n\n"
                   "**5 étapes automatisées:**\n"
                   "1. **📥 Réception**: Soumission reçue et enregistrée\n"
                   "2. **🔍 Évaluation technique**: Analyse proposition RBQ\n"
                   "3. **💰 Évaluation financière**: Analyse budget pondéré\n"
                   "4. **📊 Évaluation globale**: Synthèse multi-critères\n"
                   "5. **✅ Décision finale**: Approbation/rejet automatisé\n\n"
                   "**Statuts intelligents:**\n"
                   "📝 Brouillon → 📤 Soumise → 📥 Reçue → 🔍 En évaluation → ⏳ En approbation → ✅ Approuvée\n\n"
                   "Chaque étape avec audit trail complet et notifications temps réel!")
        
        elif "rbq" in user_msg_lower or "validation" in user_msg_lower or "critère" in user_msg_lower:
            return ("🏗️ **Validation RBQ et critères d'évaluation B2B!**\n\n"
                   "**Validation RBQ instantanée:**\n"
                   "• Vérification numéro RBQ en temps réel\n"
                   "• Domaines d'expertise certifiés\n"
                   "• Statut licence actuel\n"
                   "• Conformité CCQ automatique\n\n"
                   "**10 critères d'évaluation pondérés:**\n"
                   "• Prix et rapport qualité-prix (30%)\n"
                   "• Expérience et références (25%)\n"
                   "• Qualité proposition technique (20%)\n"
                   "• Délais de livraison (15%)\n"
                   "• Innovation et créativité (10%)\n\n"
                   "**20+ types projets Québec** supportés!\n"
                   "Système de notation 1-5 avec justifications obligatoires!")
        
        elif "mono" in user_msg_lower or "configuration" in user_msg_lower or "personnalis" in user_msg_lower:
            return ("🎨 **Configuration mono-entreprise C2B personnalisée!**\n\n"
                   "**Assistant automatique Windows:**\n"
                   "• config_nouvelle_entreprise.bat pour setup instant\n"
                   "• Modification config_entreprise_unique.py\n"
                   "• Validation automatique des paramètres\n"
                   "• Initialisation base de données dédiée\n\n"
                   "**Éléments personnalisables:**\n"
                   "• Nom entreprise, RBQ, domaines expertise\n"
                   "• Contact, téléphone, adresse complète\n"
                   "• Description entreprise et certifications\n"
                   "• Zones de service, tarification horaire\n"
                   "• Couleurs thème (bleu/vert/violet corporate)\n\n"
                   "**Modèle unique:** 1 portail = 1 entreprise propriétaire!")
        
        elif "profil" in user_msg_lower or "architectur" in user_msg_lower or "6000" in user_msg_lower:
            return ("👥 **Architecture EXPERTS IA de niveau industriel!**\n\n"
                   "**60+ Profils Experts Spécialisés:**\n"
                   "• 8 Experts principaux (entrepreneur, portes/fenêtres, électricien, plombier, architecte)\n"
                   "• 12 Spécialistes techniques (ingénieur, maçonnerie, fondations, toiture, CVC)\n"
                   "• 15 Experts réglementaires (RBQ/CCQ, urbaniste, avocat, inspecteur)\n"
                   "• 15 Support business (comptable, agent immobilier, courtier)\n"
                   "• 10+ Calculs spécialisés (poutres, colonnes, linteaux, pentes)\n\n"
                   "**Code 6,000+ lignes optimisées:**\n"
                   "• Gestionnaire profils dynamique + persistance SQLite\n"
                   "• IA adaptative qui sélectionne l'expert optimal\n"
                   "**Barrière entrée insurmontable!**")
        
        elif "urgence" in user_msg_lower or "🟢" in user_msg_lower or "🟡" in user_msg_lower or "🟠" in user_msg_lower or "🔴" in user_msg_lower:
            return ("⚡ **Système d'urgence SEAOP automatique intelligent!**\n\n"
                   "**Calcul automatique basé sur délais:**\n"
                   "• 🟢 **Faible**: Plus de 14 jours (délai confortable)\n"
                   "• 🟡 **Normal**: 7-14 jours (dans les temps)\n"
                   "• 🟠 **Élevé**: 3-7 jours (assez urgent)\n"
                   "• 🔴 **Critique**: Moins de 3 jours ou échéance dépassée\n\n"
                   "**Fonctionnalités avancées:**\n"
                   "• Priorisation automatique projets urgents\n"
                   "• Notifications automatiques changement urgence\n"
                   "• Badges visuels sur tous les projets\n"
                   "• Escalade automatique en cas de dépassement\n\n"
                   "**Algorithme:** `min(jours_soumissions, jours_debut)` optimisé!")
        
        elif "mesur" in user_msg_lower or "accrochage" in user_msg_lower or "viewer" in user_msg_lower:
            return ("📏 **Système de mesure TAKEOFF AI ultra-précis!**\n\n"
                   "**5 outils professionnels complets:**\n"
                   "• **Distance**: Calcul linéaire entre 2 points\n"
                   "• **Surface**: Formule du lacet (shoelace) pour polygones\n"
                   "• **Périmètre**: Contour fermé ou ouvert\n"
                   "• **Angle**: Calcul 3 points avec produit scalaire\n"
                   "• **Calibration**: Pixel vers unité réelle\n\n"
                   "**18 viewers optimisés:**\n"
                   "fast, ultra_fast, smooth, reactive, streamlined, enhanced, instant, final...\n\n"
                   "**Catalogue intégré:** Béton (150-180$/m³), Acier, Gypse, Isolation prix 2025!")
        
        elif "feuille" in user_msg_lower or "soumission" in user_msg_lower and "feuille" in user_msg_lower:
            return ("📄 **FEUILLE SOUMISSION - Mon générateur HTML autonome révolutionnaire!**\n\n"
                   "**Application complète en 1 seul fichier HTML de 5,190 lignes!**\n\n"
                   "**Fonctionnalités avancées:**\n"
                   "• Calculs automatiques temps réel (sous-total, taxes, total)\n"
                   "• Taux personnalisables: Profit (0-50%), Admin (0-10%), Contingences (0-25%)\n"
                   "• Sauvegarde automatique localStorage toutes les 30 secondes\n"
                   "• Export/Import JSON pour archivage\n"
                   "• Export HTML complet avec données intégrées\n"
                   "• Impression PDF directe depuis navigateur\n\n"
                   "**Templates intégrés:** Construction Héritage, Bâtir Excellence Inc.\n"
                   "**Zéro dépendance** - Fonctionne offline!")
        
        elif "prix" in user_msg_lower or "coût" in user_msg_lower or "tarif" in user_msg_lower:
            return ("💰 **ROI moyen en moins de 30 jours!**\n\n"
                   "• Économies moyennes: 20h/semaine (1,000$/semaine)\n"
                   "• Productivité: +30-45% dès le premier mois\n"
                   "• 3.5M$ économisés collectivement par nos utilisateurs\n"
                   "• Garantie satisfaction 30 jours\n\n"
                   "L'investissement se rembourse en moins d'une semaine! "
                   "Contactez-moi pour un calcul de ROI personnalisé: 514-820-1972")
        
        elif "sécur" in user_msg_lower or "donnée" in user_msg_lower:
            return ("🔒 **Sécurité de niveau bancaire!**\n\n"
                   "• Chiffrement SSL/TLS pour toutes les données\n"
                   "• Conformité Loi 25 (protection renseignements personnels)\n"
                   "• Sauvegardes automatiques quotidiennes\n"
                   "• Hébergement sécurisé Render.com\n"
                   "• Vos données vous appartiennent à 100%\n\n"
                   "J'ai conçu le système avec la sécurité comme priorité!")
        
        elif "formation" in user_msg_lower or "support" in user_msg_lower or "aide" in user_msg_lower:
            return ("🎓 **Formation et support inclus!**\n\n"
                   "• Formation personnalisée gratuite (valeur 2,500$)\n"
                   "• Assistant IA disponible 24/7\n"
                   "• Opérationnel en moyenne en 2 heures\n"
                   "• Support email prioritaire (plans Pro)\n"
                   "• Documentation complète en français\n\n"
                   "Je m'assure personnellement que vous réussissiez!")
        
        elif "concurrent" in user_msg_lower or "compar" in user_msg_lower:
            return ("🏆 **Constructo AI se distingue par:**\n\n"
                   "• 54 experts IA vs 0-5 chez les concurrents\n"
                   "• Prix 2025 Québec actualisés vs données génériques\n"
                   "• 7 applications intégrées (+ portail) vs solutions fragmentées\n"
                   "• Conformité RBQ/CCQ native vs adaptations\n"
                   "• Moins cher que 2-3 logiciels séparés\n\n"
                   "Quelle fonctionnalité recherchez-vous précisément?")
        
        elif "contact" in user_msg_lower or "appel" in user_msg_lower or "démo" in user_msg_lower:
            return ("📞 **Contactez-moi directement!**\n\n"
                   "**Sylvain Leduc** - Créateur de Constructo AI\n"
                   "📱 514-820-1972\n"
                   "📧 info@constructoai.ca\n"
                   "🌐 www.constructoai.ca\n"
                   "📍 Farnham, Québec\n\n"
                   "Démonstration personnalisée gratuite disponible!")
        
        elif "sylvain" in user_msg_lower or "vous" in user_msg_lower and any(word in user_msg_lower for word in ["qui", "parlez", "présent"]):
            return ("👨‍💼 **Je suis Sylvain Leduc, créateur de Constructo AI!**\n\n"
                   "Passionné par l'innovation dans la construction, j'ai développé personnellement "
                   "cet écosystème complet de 7 applications (+ portail) pour transformer l'industrie québécoise.\n\n"
                   "**Mon expertise:**\n"
                   "• Concepteur de solutions IA pour la construction\n"
                   "• Expert en technologies Streamlit et Claude API\n"
                   "• Spécialiste des normes RBQ/CCQ québécoises\n\n"
                   "**Ma mission:** Permettre aux entreprises de construction d'économiser "
                   "20h/semaine et d'augmenter leur productivité de 30-45%!\n\n"
                   "Quelle solution puis-je vous présenter?")
        
        elif any(word in user_msg_lower for word in ["bonjour", "salut", "hello", "allo"]):
            return self.get_greeting()
        
        elif any(word in user_msg_lower for word in ["merci", "parfait", "super", "excellent", "bye", "aurevoir", "à bientôt"]):
            return ("😊 **Parfait! Ce fut un plaisir!**\n\n"
                   "Si vous avez d'autres questions sur Constructo AI, je suis là.\n"
                   "Pour une démonstration personnalisée: 514-820-1972\n\n"
                   "Bonne journée et au plaisir de vous accompagner dans votre "
                   "transformation numérique! 🏗️\n\n- Sylvain Leduc")
        
        # Questions sur TimeTracker ou pointage
        elif "timetracker" in user_msg_lower or "pointage" in user_msg_lower or "temps" in user_msg_lower:
            return ("⏰ **TimeTracker ERP AI - Pointage construction intelligent!**\n\n"
                   "• Pointage granulaire sur 120 postes de travail\n"
                   "• Mapping automatique postes → phases construction\n"
                   "• Fuseau horaire Québec (America/Montreal)\n"
                   "• Mode superviseur et mode employé\n"
                   "• Export rapports détaillés temps/coûts\n\n"
                   "Suivi précis des heures par poste et par phase de construction!")
        
        # Questions sur CRM ou clients
        elif "crm" in user_msg_lower or "client" in user_msg_lower and not "c2b" in user_msg_lower:
            return ("📊 **Module CRM intégré dans ERP AI!**\n\n"
                   "• Gestion contacts et entreprises construction\n"
                   "• 14 types d'entreprises (entrepreneur, sous-traitant, architecte)\n"
                   "• 18 secteurs spécialisés (résidentiel, commercial, industriel)\n"
                   "• Suivi opportunités avec Kanban visuel\n"
                   "• Intégration complète avec devis et bons de travail\n\n"
                   "CRM adapté à la réalité construction québécoise!")
        
        # Questions sur RH ou employés
        elif "rh" in user_msg_lower or "employé" in user_msg_lower or "ressource" in user_msg_lower:
            return ("👥 **Module RH complet dans ERP AI!**\n\n"
                   "• Gestion 120 profils métiers construction\n"
                   "• 106 compétences spécialisées (CCQ, CNESST, techniques)\n"
                   "• Suivi formations et certifications obligatoires\n"
                   "• Départements construction (chantier, structure, finition)\n"
                   "• Conformité normes travail Québec\n\n"
                   "Gestion complète des ressources humaines construction!")
        
        # Questions sur postes de travail
        elif "poste" in user_msg_lower or "métier" in user_msg_lower:
            return ("🔨 **120 postes de travail préconfigurés!**\n\n"
                   "**Exemples par catégorie:**\n"
                   "• CHARPENTE: Charpentier-menuisier (48$/h)\n"
                   "• ÉLECTRICITÉ: Électricien (55$/h), Câbleur (48$/h)\n"
                   "• PLOMBERIE: Plombier (55$/h), Gaz (58$/h)\n"
                   "• BÉTON: Coffreur (48$/h), Cimentier (45$/h)\n"
                   "• TOITURE: Couvreur (45-52$/h), Ferblantier (50$/h)\n\n"
                   "Tous avec coûts horaires québécois actualisés!")
        
        # Questions techniques construction -> rediriger vers EXPERTS AI
        construction_keywords = ["béton", "fondation", "structure", "électri", "plomb", "toiture", "isolation", "code", "norme"]
        if any(word in user_msg_lower for word in construction_keywords):
            return ("🔧 **Excellente question technique!**\n\n"
                   f"Notre module EXPERTS AI a justement un expert qui peut vous aider avec ça. "
                   f"Avec 54 profils spécialisés, vous aurez une réponse détaillée et conforme aux normes québécoises.\n\n"
                   f"Voulez-vous en savoir plus sur EXPERTS AI?")
        
        # Réponse par défaut
        else:
            return ("💡 **Je suis Sylvain Leduc, créateur de Constructo AI!**\n\n"
                   "J'ai développé 7 applications (+ ce portail) pour révolutionner la construction:\n\n"
                   "• **EXPERTS AI** - 54 experts IA spécialisés\n"
                   "• **TAKEOFF AI** - Mesure et estimation sur PDF\n"
                   "• **ERP AI** - 120 postes de travail configurés\n"
                   "• **B2B** - Marketplace avec validation RBQ\n"
                   "• **SEAOP** - Appels d'offres publics\n"
                   "• **C2B** - Portail mono-entreprise\n"
                   "• **FEUILLE SOUMISSION** - Générateur de devis\n"
                   "• **PORTAIL** - Hub central unifié\n\n"
                   "Quelle solution vous intéresse pour votre entreprise?")
    
    def get_greeting(self) -> str:
        """Message d'accueil de Sylvain Leduc"""
        return ("🏗️ **Bonjour! Je suis Sylvain Leduc, créateur de Constructo AI!**\n\n"
                "J'ai développé personnellement cet écosystème de 7 applications "
                "(plus ce portail central) pour révolutionner l'industrie de la construction québécoise.\n\n"
                "**Comment puis-je vous aider aujourd'hui?**\n"
                "• 📊 Découvrir EXPERTS AI (54 experts IA)\n"
                "• 📐 Explorer TAKEOFF AI (mesure PDF)\n"
                "• 🏭 Comprendre ERP AI (gestion complète)\n"
                "• 💰 Calculer votre ROI personnalisé\n"
                "• 📞 Planifier une démonstration\n\n"
                "Quelle application vous intéresse le plus?")

# Initialisation de l'assistant
if 'assistant' not in st.session_state:
    st.session_state.assistant = AssistantIA()
    st.session_state.chat_messages = []
    st.session_state.chat_expanded = False

# Fonction pour charger le CSS local
def load_css(file_name):
    """Charge les styles CSS depuis un fichier local."""
    try:
        if os.path.exists(file_name):
            with open(file_name, "r", encoding="utf-8") as f:
                st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        else:
            print(f"Warning: CSS file {file_name} not found")
    except Exception as e:
        print(f"Error loading CSS: {e}")

# Chargement du CSS
load_css("style_portal.css")

# CSS supplémentaire pour l'assistant dans le footer
st.markdown("""
<style>
    /* Assistant Chat Button */
    .chat-button {
        position: fixed;
        bottom: 20px;
        right: 20px;
        width: 60px;
        height: 60px;
        background: linear-gradient(135deg, #3B82F6 0%, #1E40AF 100%);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.4);
        z-index: 1000;
        transition: all 0.3s ease;
    }
    
    .chat-button:hover {
        transform: scale(1.1);
        box-shadow: 0 6px 20px rgba(59, 130, 246, 0.6);
    }
    
    .chat-button-icon {
        font-size: 28px;
        filter: brightness(0) invert(1);
    }
    
    /* Chat Container dans le footer */
    .footer-chat-container {
        background: linear-gradient(135deg, #F0F9FF 0%, #E0F2FE 100%);
        border-top: 3px solid #3B82F6;
        border-radius: 20px 20px 0 0;
        padding: 30px;
        margin-top: 50px;
        box-shadow: 0 -10px 30px rgba(0, 0, 0, 0.1);
    }
    
    .chat-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 20px;
        padding-bottom: 15px;
        border-bottom: 2px solid #E0F2FE;
    }
    
    .chat-title {
        font-size: 24px;
        font-weight: 700;
        color: #1E40AF;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    
    .chat-status {
        display: flex;
        align-items: center;
        gap: 8px;
        color: #10B981;
        font-weight: 500;
    }
    
    .status-dot {
        width: 10px;
        height: 10px;
        background: #10B981;
        border-radius: 50%;
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0% { opacity: 1; }
        50% { opacity: 0.5; }
        100% { opacity: 1; }
    }
    
    /* Messages */
    .chat-message {
        margin: 15px 0;
        animation: slideIn 0.3s ease;
    }
    
    @keyframes slideIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .user-message {
        background: white;
        border-left: 4px solid #3B82F6;
        padding: 12px 16px;
        border-radius: 8px;
        margin-left: 20%;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    }
    
    .assistant-message {
        background: linear-gradient(135deg, #FFFFFF 0%, #F0F9FF 100%);
        border-left: 4px solid #10B981;
        padding: 12px 16px;
        border-radius: 8px;
        margin-right: 20%;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    }
    
    /* Quick Actions */
    .quick-actions {
        display: flex;
        gap: 10px;
        flex-wrap: wrap;
        margin: 20px 0;
    }
    
    .quick-action-btn {
        background: white;
        border: 2px solid #E0F2FE;
        padding: 8px 16px;
        border-radius: 20px;
        color: #3B82F6;
        font-weight: 500;
        transition: all 0.3s;
        cursor: pointer;
    }
    
    .quick-action-btn:hover {
        background: #3B82F6;
        color: white;
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3);
    }
    
    /* API Status Indicator */
    .api-status {
        display: inline-flex;
        align-items: center;
        gap: 5px;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 500;
    }
    
    .api-status.active {
        background: #D1FAE5;
        color: #065F46;
    }
    
    .api-status.demo {
        background: #FEF3C7;
        color: #92400E;
    }
    
    /* Responsive */
    @media (max-width: 768px) {
        .footer-chat-container {
            padding: 20px 15px;
        }
        
        .user-message, .assistant-message {
            margin-left: 0;
            margin-right: 0;
        }
        
        .chat-title {
            font-size: 20px;
        }
    }
</style>
""", unsafe_allow_html=True)

# CSS Responsive pour mobile (existant)
st.markdown("""
<style>
    /* Responsive Design pour Mobile */
    @media (max-width: 768px) {{
        /* Ajustement des colonnes pour mobile */
        .stColumns > div {{
            flex: 0 0 100% !important;
            max-width: 100% !important;
        }}
        
        /* Header responsive */
        .header-container {{
            padding: 20px 10px !important;
        }}
        
        /* Cartes en pleine largeur sur mobile */
        [data-testid="column"] {{
            width: 100% !important;
            flex: 1 0 100% !important;
        }}
        
        /* Texte adaptatif */
        h1, h2, h3 {{
            word-wrap: break-word !important;
        }}
        
        /* Boutons et inputs responsive */
        .stTextInput > div > div > input {{
            font-size: 16px !important;
        }}
        
        .stSelectbox > div > div {{
            font-size: 16px !important;
        }}
    }}
    
    @media (max-width: 480px) {{
        /* Encore plus petit pour très petits écrans */
        .main-title {{
            font-size: 1.8rem !important;
        }}
        
        /* Padding réduit */
        .block-container {{
            padding: 1rem !important;
        }}
    }}
</style>
""", unsafe_allow_html=True)

# Données des applications (existantes)
APPLICATIONS = [
    {
        "id": "experts-ai",
        "name": "EXPERTS IA",
        "icon": "🏗️",
        "url": "https://experts-ai.constructoai.ca/",
        "description": "Assistant IA avec 60+ experts spécialisés en construction au Québec",
        "features": ["60+ profils d'experts", "Analyse documents", "Recherche web intégrée", "Export professionnel"],
        "status": "production",
        "category": "expertise",
        "color": "#3B82F6",
        "gradient": "linear-gradient(135deg, #3B82F6 0%, #1E40AF 100%)",
        "badge": "⭐ FLAGSHIP"
    },
    {
        "id": "takeoff-ai",
        "name": "TAKEOFF AI",
        "icon": "📐",
        "url": "https://takeoff-ai.constructoai.ca/",
        "description": "Système d'estimation de construction avec IA Claude - Visualisation PDF et mesures avancées",
        "features": ["Visualisation PDF avec annotations", "5 modes de mesure", "Assistant IA Claude intégré", "Export CSV/JSON/PDF"],
        "status": "production",
        "category": "estimation",
        "color": "#10B981",
        "gradient": "linear-gradient(135deg, #10B981 0%, #059669 100%)",
        "badge": "🚀 POPULAIRE"
    },
    {
        "id": "erp-ai",
        "name": "ERP AI",
        "icon": "🏭",
        "url": "https://erp-ai.constructoai.ca/",
        "description": "Solution ERP construction avec 120 postes de travail, TimeTracker Québec et modules CRM/RH complets",
        "features": ["120 postes construction préconfigurés", "TimeTracker fuseau Québec", "CRM/RH avec 106 compétences", "Dashboard, Kanban, Gantt, Calendrier"],
        "status": "production",
        "category": "gestion",
        "color": "#8B5CF6",
        "gradient": "linear-gradient(135deg, #8B5CF6 0%, #7C3AED 100%)",
        "badge": "🏭 CONSTRUCTION 4.0"
    },
    {
        "id": "seaop",
        "name": "SEAOP",
        "icon": "📊",
        "url": "https://seaop.constructoai.ca/",
        "description": "Système Électronique d'Appel d'Offres Public - Plateforme de mise en relation clients-entrepreneurs",
        "features": ["Appels d'offres publics", "Chat temps réel", "Évaluations 5 étoiles", "Dashboard analytics"],
        "status": "production",
        "category": "appels-offres",
        "color": "#06B6D4",
        "gradient": "linear-gradient(135deg, #06B6D4 0%, #0891B2 100%)",
        "badge": "🏆 APPELS D'OFFRES"
    },
    {
        "id": "b2b-pbr8",
        "name": "B2B",
        "icon": "🏗️",
        "url": "https://b2b.constructoai.ca/",
        "description": "Plateforme B2B de gestion des soumissions avec workflow d'approbation intelligent pour entreprises RBQ",
        "features": ["Workflow d'approbation 5 étapes", "Évaluation multi-critères", "Validation RBQ automatique", "Dashboard analytique B2B"],
        "status": "production",
        "category": "collaboration",
        "color": "#F59E0B",
        "gradient": "linear-gradient(135deg, #F59E0B 0%, #D97706 100%)",
        "badge": "🏗️ B2B CONSTRUCTION"
    },
    {
        "id": "c2b-cs4p",
        "name": "C2B",
        "icon": "🏢",
        "url": "https://c2b.constructoai.ca/",
        "description": "Portail Client à Entreprise - Solution mono-entreprise pour recevoir et gérer les demandes de soumissions",
        "features": ["Réception demandes clients", "Soumissions personnalisées", "Suivi temps réel", "Dashboard propriétaire"],
        "status": "production",
        "category": "portail-entreprise",
        "color": "#EC4899",
        "gradient": "linear-gradient(135deg, #EC4899 0%, #DB2777 100%)",
        "badge": "🏢 PORTAIL C2B"
    },
    {
        "id": "feuille-soumission",
        "name": "Feuille de Soumission",
        "icon": "📋",
        "url": "https://constructoai.github.io/FEUILLE_SOUMISSION/",
        "description": "Générateur de soumissions professionnelles pour projets de construction",
        "features": ["Templates personnalisés", "Calculs automatiques", "Export PDF", "Suivi soumissions"],
        "status": "production",
        "category": "documentation",
        "color": "#14B8A6",
        "gradient": "linear-gradient(135deg, #14B8A6 0%, #0D9488 100%)",
        "badge": "📄 DOCUMENTS"
    }
]

# Statistiques globales
STATS = {
    "users": "2,500+",
    "projects": "15,000+",
    "companies": "350+",
    "savings": "3.5M$"
}

# Initialisation session state
if 'selected_category' not in st.session_state:
    st.session_state.selected_category = "all"
if 'search_query' not in st.session_state:
    st.session_state.search_query = ""

# Header principal avec animation
st.markdown("""
    <div class="header-container">
        <div class="header-glow"></div>
        <div class="header-content">
            <style>
                .title-wrapper {{
                    display: flex;
                    align-items: baseline;
                    justify-content: center;
                    gap: 10px;
                }}
                @media (max-width: 768px) {{
                    .title-container {{ flex-direction: column !important; gap: 10px !important; }}
                    .title-line {{ display: none !important; }}
                    .title-wrapper {{ 
                        flex-direction: column !important; 
                        gap: 0 !important;
                        align-items: center !important;
                        text-align: center !important;
                    }}
                    .title-wrapper h1:first-child {{ 
                        font-size: 2.2rem !important; 
                        letter-spacing: 3px !important; 
                        margin-bottom: -5px !important;
                    }}
                    .title-wrapper h1:last-child {{ 
                        font-size: 2.2rem !important; 
                        letter-spacing: 3px !important; 
                    }}
                    .main-subtitle {{ font-size: 1.1rem !important; margin-top: 0.5rem !important; }}
                    .main-description {{ font-size: 0.9rem !important; padding: 0 15px !important; line-height: 1.5 !important; }}
                    .header-stats {{ flex-wrap: wrap !important; gap: 15px !important; padding: 0 10px !important; }}
                    .stat-item {{ flex: 0 0 45% !important; padding: 0.8rem !important; }}
                }}
                @media (max-width: 480px) {{
                    .title-wrapper {{ 
                        flex-direction: column !important; 
                        gap: 0 !important;
                        align-items: center !important;
                    }}
                    .title-wrapper h1:first-child {{ 
                        font-size: 1.8rem !important; 
                        letter-spacing: 2px !important;
                        margin-bottom: -5px !important;
                    }}
                    .title-wrapper h1:last-child {{ 
                        font-size: 1.8rem !important; 
                        letter-spacing: 2px !important; 
                    }}
                    .main-subtitle {{ font-size: 1rem !important; }}
                    .main-description {{ font-size: 0.85rem !important; }}
                    .stat-item {{ flex: 0 0 100% !important; }}
            </style>
            <div class="title-container" style="display: flex; align-items: center; justify-content: center; gap: 15px; margin-bottom: 2rem;">
                <div class="title-line" style="width: 60px; height: 2px; background: linear-gradient(to right, transparent, rgba(255,255,255,0.8));"></div>
                <div class="title-wrapper">
                    <h1 style="
                        font-size: 3.5rem; 
                        font-weight: 500; 
                        color: white; 
                        margin: 0;
                        letter-spacing: 8px; 
                        text-transform: uppercase;
                        font-family: 'Helvetica Neue', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
                        text-shadow: 0 2px 10px rgba(0,0,0,0.2);
                    ">CONSTRUCTO</h1>
                    <h1 style="
                        font-size: 3.5rem; 
                        font-weight: 700; 
                        color: #000000; 
                        margin: 0;
                        letter-spacing: 8px; 
                        text-transform: uppercase;
                        font-family: 'Helvetica Neue', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
                    ">AI</h1>
                </div>
                <div class="title-line" style="width: 60px; height: 2px; background: linear-gradient(to left, transparent, rgba(255,255,255,0.8));"></div>
            </div>
            <p class="main-subtitle" style="font-size: 1.5rem; font-weight: 500; margin-bottom: 1rem;">Vos Assistant AI pour la construction</p>
            <p class="main-description" style="color: rgba(255, 255, 255, 0.9); font-size: 1.1rem; max-width: 800px; margin: 0 auto;">Estimez et vérifiez vos projets 4x plus rapidement. Constructo AI est la plateforme intelligente qui révolutionne vos projets de construction.</p>
            <div class="header-stats">
                <div class="stat-item">
                    <span class="stat-value">{users}</span>
                    <span class="stat-label">Utilisateurs</span>
                </div>
                <div class="stat-item">
                    <span class="stat-value">{projects}</span>
                    <span class="stat-label">Projets</span>
                </div>
                <div class="stat-item">
                    <span class="stat-value">{companies}</span>
                    <span class="stat-label">Entreprises</span>
                </div>
                <div class="stat-item">
                    <span class="stat-value">{savings}</span>
                    <span class="stat-label">Économies</span>
                </div>
            </div>
        </div>
    </div>
""".format(**STATS), unsafe_allow_html=True)

# Barre de recherche et filtres
col1, col2, col3 = st.columns([2, 1, 1])

with col1:
    search = st.text_input(
        "🔍 Rechercher une application", 
        placeholder="Ex: estimation, experts, gestion...",
        key="search_input",
        label_visibility="collapsed"
    )
    st.session_state.search_query = search.lower()

with col2:
    categories = ["Toutes"] + list(set([app["category"] for app in APPLICATIONS]))
    category_labels = {
        "all": "🎯 Toutes",
        "expertise": "🏗️ Expertise",
        "estimation": "📐 Estimation",
        "gestion": "💼 Gestion",
        "appels-offres": "📊 Appels d'Offres",
        "collaboration": "🤝 Collaboration",
        "portail-entreprise": "🏢 Portail Entreprise",
        "documentation": "📄 Documentation"
    }
    
    selected_cat = st.selectbox(
        "Catégorie",
        categories,
        format_func=lambda x: category_labels.get(x.lower(), x),
        label_visibility="collapsed"
    )
    
    if selected_cat == "Toutes":
        st.session_state.selected_category = "all"
    else:
        st.session_state.selected_category = selected_cat.lower()

with col3:
    view_mode = st.radio(
        "Vue",
        ["Cartes", "Liste"],
        horizontal=True,
        label_visibility="collapsed"
    )

# Filtrage des applications
filtered_apps = APPLICATIONS.copy()

# Filtre par recherche
if st.session_state.search_query:
    filtered_apps = [
        app for app in filtered_apps
        if st.session_state.search_query in app["name"].lower() or
           st.session_state.search_query in app["description"].lower() or
           any(st.session_state.search_query in feature.lower() for feature in app["features"])
    ]

# Filtre par catégorie
if st.session_state.selected_category != "all":
    filtered_apps = [
        app for app in filtered_apps
        if app["category"] == st.session_state.selected_category
    ]

# Section d'accès rapide
st.markdown("""
    <div class="quick-access-container">
        <h2 class="section-title">⚡ Accès Rapide</h2>
        <p class="section-subtitle">Cliquez sur une application pour y accéder directement</p>
    </div>
""", unsafe_allow_html=True)

# Affichage des applications
if view_mode == "Cartes":
    # Vue en cartes (grille)
    cols = st.columns(3)
    for idx, app in enumerate(filtered_apps):
        with cols[idx % 3]:
            # Utilisation de st.container pour éviter les conflits CSS
            with st.container():
                st.markdown(f"""
                    <div style="background: white; border: 1px solid #ddd; border-radius: 10px; padding: 20px; margin-bottom: 20px;">
                        <div style="text-align: center; font-size: 40px; margin-bottom: 10px;">
                            {app['icon']}
                        </div>
                        <h3 style="color: #1a1a1a; font-size: 18px; margin: 10px 0; text-align: center; font-weight: bold;">
                            {app['name']}
                        </h3>
                        <p style="color: #666; font-size: 14px; line-height: 1.4; margin: 10px 0; text-align: center;">
                            {app['description'][:100]}...
                        </p>
                        <div style="margin: 15px 0; text-align: center;">
                            <span style="background: #f0f0f0; padding: 4px 8px; border-radius: 4px; font-size: 12px; color: #333; margin: 0 2px;">
                                {app['features'][0]}
                            </span>
                        </div>
                        <div style="text-align: center; margin-top: 15px;">
                            <a href="{app['url']}" target="_blank" style="
                                background: #007bff; 
                                color: white; 
                                padding: 10px 20px; 
                                border-radius: 5px; 
                                text-decoration: none; 
                                display: inline-block;
                                font-weight: bold;
                            ">
                                Accéder →
                            </a>
                        </div>
                        <div style="text-align: center; margin-top: 10px;">
                            <span style="color: #28a745; font-size: 12px;">● En ligne</span>
                        </div>
                    </div>
                """, unsafe_allow_html=True)

else:
    # Vue en liste détaillée
    for app in filtered_apps:
        with st.expander(f"{app['icon']} **{app['name']}** - {app['description'][:60]}...", expanded=False):
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.markdown(f"""
                    ### {app['icon']} {app['name']}
                    
                    **Description:** {app['description']}
                    
                    **Fonctionnalités principales:**
                    {chr(10).join([f"- ✅ {feature}" for feature in app['features']])}
                    
                    **Catégorie:** {app['category'].capitalize()}  
                    **Statut:** 🟢 En production
                """)
            
            with col2:
                st.markdown(f"""
                    <div style="text-align: center; padding: 2rem;">
                        <div style="font-size: 4rem; margin-bottom: 1rem;">{app['icon']}</div>
                        <a href="{app['url']}" target="_blank" style="
                            display: inline-block;
                            padding: 12px 24px;
                            background: {app['gradient']};
                            color: white;
                            text-decoration: none;
                            border-radius: 8px;
                            font-weight: 600;
                            transition: transform 0.3s;
                        ">
                            Accéder à l'application →
                        </a>
                    </div>
                """, unsafe_allow_html=True)

# Section informations supplémentaires
st.markdown("<br><br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class="info-card">
            <h3>🚀 Innovation Continue</h3>
            <p>Nos solutions IA évoluent constamment pour répondre aux besoins du secteur de la construction québécois.</p>
            <ul>
                <li>Mises à jour régulières</li>
                <li>Nouvelles fonctionnalités</li>
                <li>Support technique 24/7</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="info-card">
            <h3>🔒 Sécurité & Conformité</h3>
            <p>Toutes nos applications respectent les normes de sécurité les plus strictes.</p>
            <ul>
                <li>Chiffrement SSL/TLS</li>
                <li>Conformité RGPD</li>
                <li>Sauvegarde automatique</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="info-card">
            <h3>🤝 Support & Formation</h3>
            <p>Une équipe dédiée pour vous accompagner dans votre transformation numérique.</p>
            <ul>
                <li>Formation personnalisée</li>
                <li>Documentation complète</li>
                <li>Assistance prioritaire</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

# SECTION ASSISTANT IA DANS LE FOOTER
# Obtenir le mode actuel
current_mode = st.session_state.assistant.mode if hasattr(st.session_state.assistant, 'mode') else "Mode Démo 🎯"

st.markdown(f"""
    <div class="footer-chat-container">
        <div class="chat-header">
            <div class="chat-title">
                💬 Chat avec Sylvain Leduc - Créateur de Constructo AI
            </div>
            <div class="chat-status">
                <span class="status-dot"></span>
                En ligne - {current_mode}
            </div>
        </div>
        <p style="color: #6B7280; margin-bottom: 20px;">
            Bonjour! Je suis Sylvain Leduc, créateur de Constructo AI. Comment puis-je vous aider avec nos 7 applications?
        </p>
    </div>
""", unsafe_allow_html=True)

# Indicateur de statut API
api_status = "active" if st.session_state.assistant.client else "demo"
api_text = "🤖 Claude API Active" if st.session_state.assistant.client else "💬 Mode Démo"
api_color = "#10B981" if st.session_state.assistant.client else "#F59E0B"

st.markdown(f"""
    <div style="text-align: center; margin-bottom: 20px;">
        <span class="api-status {api_status}" style="background: {'#D1FAE5' if api_status == 'active' else '#FEF3C7'}; color: {'#065F46' if api_status == 'active' else '#92400E'}; padding: 4px 12px; border-radius: 20px; font-size: 12px; font-weight: 500;">
            {api_text}
        </span>
    </div>
""", unsafe_allow_html=True)

# Container pour le chat
with st.container():
    # Colonnes pour le chat
    col_chat, col_actions = st.columns([2, 1])
    
    with col_chat:
        # Zone des messages
        st.markdown("#### 💬 Conversation")
        
        # Afficher le message d'accueil si c'est la première fois
        if not st.session_state.chat_messages:
            greeting = st.session_state.assistant.get_greeting()
            st.session_state.chat_messages.append({"role": "assistant", "content": greeting})
        
        # Container pour les messages avec scroll
        messages_container = st.container(height=300)
        with messages_container:
            for message in st.session_state.chat_messages:
                if message["role"] == "user":
                    st.markdown(f"""
                        <div class="user-message">
                            <strong style="color: #3B82F6;">Vous:</strong><br>
                            {message["content"]}
                        </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                        <div class="assistant-message">
                            <strong style="color: #10B981;">Sylvain Leduc:</strong><br>
                            {message["content"]}
                        </div>
                    """, unsafe_allow_html=True)
        
        # Zone de saisie
        user_input = st.text_input(
            "Tapez votre message...",
            placeholder="Ex: Qu'est-ce que EXPERTS AI?",
            key="user_chat_input"
        )
        
        col_send, col_clear = st.columns([1, 1])
        with col_send:
            if st.button("📤 Envoyer", type="primary", use_container_width=True):
                if user_input and user_input.strip():
                    # Ajouter le message utilisateur
                    st.session_state.chat_messages.append({"role": "user", "content": user_input})
                    
                    # Obtenir la réponse avec historique
                    response = st.session_state.assistant.get_response(
                        user_input, 
                        st.session_state.chat_messages[:-1]  # Passer l'historique sans le dernier message
                    )
                    st.session_state.chat_messages.append({"role": "assistant", "content": response})
                    
                    # Rafraîchir la page
                    st.rerun()
        
        with col_clear:
            if st.button("🔄 Nouvelle conversation", use_container_width=True):
                st.session_state.chat_messages = []
                st.session_state.assistant = AssistantIA()
                st.rerun()
    
    with col_actions:
        st.markdown("#### ⚡ Questions rapides")
        
        # Questions suggérées adaptées au profil Sylvain Leduc
        quick_questions = [
            "Qu'est-ce que EXPERTS AI avec 54 experts?",
            "Comment TAKEOFF mesure sur PDF?",
            "Quel est le ROI moyen?",
            "Démonstration personnalisée",
            "Parlez-moi de vous Sylvain"
        ]
        
        for question in quick_questions:
            if st.button(f"💡 {question}", key=f"quick_{question}", use_container_width=True):
                # Ajouter la question et obtenir la réponse
                st.session_state.chat_messages.append({"role": "user", "content": question})
                response = st.session_state.assistant.get_response(
                    question,
                    st.session_state.chat_messages[:-1]
                )
                st.session_state.chat_messages.append({"role": "assistant", "content": response})
                st.rerun()
        
        st.markdown("---")
        st.markdown("#### 📞 Contact direct")
        st.info("""
            **Téléphone:** 514-820-1972  
            **Email:** info@constructoai.ca  
            **Horaires:** 24/7
        """)
        
        # Instructions pour activer Claude API
        if not st.session_state.assistant.client:
            st.markdown("---")
            st.markdown("##### 🔑 Activer Claude API")
            st.caption("""
                1. Créez `.env` avec:  
                   `ANTHROPIC_API_KEY=sk-...`
                2. Installez:  
                   `pip install anthropic python-dotenv`
                3. Relancez l'application
            """)

# Footer final
st.markdown("""
    <div style="background: white; border-top: 2px solid #e5e7eb; margin-top: 60px; padding: 40px 20px 20px 20px;">
        <div style="max-width: 1200px; margin: 0 auto; display: flex; flex-wrap: wrap; justify-content: space-between; gap: 40px;">
            <div style="flex: 1; min-width: 200px;">
                <h4 style="color: #1a1a1a; font-size: 18px; margin-bottom: 15px;">À propos</h4>
                <p style="color: #666; font-size: 14px; line-height: 1.6;">Leader en solutions IA pour la construction au Québec</p>
            </div>
            <div style="flex: 1; min-width: 200px;">
                <h4 style="color: #1a1a1a; font-size: 18px; margin-bottom: 15px;">Contact</h4>
                <p style="color: #666; font-size: 14px; line-height: 1.8;">
                    📧 info@constructoai.ca<br>
                    📞 514-820-1972<br>
                    📍 Farnham, Québec
                </p>
            </div>
            <div style="flex: 1; min-width: 200px;">
                <h4 style="color: #1a1a1a; font-size: 18px; margin-bottom: 15px;">Ressources</h4>
                <p style="color: #666; font-size: 14px; line-height: 1.8;">
                    <a href="#" style="color: #007bff; text-decoration: none;">Documentation</a><br>
                    <a href="#" style="color: #007bff; text-decoration: none;">Support</a><br>
                    <a href="#" style="color: #007bff; text-decoration: none;">API</a>
                </p>
            </div>
            <div style="flex: 1; min-width: 200px;">
                <h4 style="color: #1a1a1a; font-size: 18px; margin-bottom: 15px;">Suivez-nous</h4>
                <p style="color: #666; font-size: 14px; line-height: 1.6;">LinkedIn | Twitter | YouTube</p>
            </div>
        </div>
        <div style="text-align: center; margin-top: 30px; padding-top: 20px; border-top: 1px solid #e5e7eb;">
            <p style="color: #666; font-size: 14px;">© 2025 Constructo AI - Tous droits réservés | Développé par Sylvain Leduc</p>
        </div>
    </div>
""", unsafe_allow_html=True)

# Animation de chargement initial
placeholder = st.empty()
with placeholder.container():
    st.markdown("""
        <div class="loading-animation">
            <div class="loading-spinner"></div>
            <p>Chargement du portail...</p>
        </div>
    """, unsafe_allow_html=True)
    time.sleep(0.5)
placeholder.empty()