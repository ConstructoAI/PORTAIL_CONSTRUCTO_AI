# portal.py - Portail Constructo AI
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

# CSS Responsive pour mobile
st.markdown("""
<style>
    /* Responsive Design pour Mobile */
    @media (max-width: 768px) {
        /* Ajustement des colonnes pour mobile */
        .stColumns > div {
            flex: 0 0 100% !important;
            max-width: 100% !important;
        }
        
        /* Header responsive */
        .header-container {
            padding: 20px 10px !important;
        }
        
        /* Cartes en pleine largeur sur mobile */
        [data-testid="column"] {
            width: 100% !important;
            flex: 1 0 100% !important;
        }
        
        /* Texte adaptatif */
        h1, h2, h3 {
            word-wrap: break-word !important;
        }
        
        /* Boutons et inputs responsive */
        .stTextInput > div > div > input {
            font-size: 16px !important;
        }
        
        .stSelectbox > div > div {
            font-size: 16px !important;
        }
    }
    
    @media (max-width: 480px) {
        /* Encore plus petit pour très petits écrans */
        .main-title {
            font-size: 1.8rem !important;
        }
        
        /* Padding réduit */
        .block-container {
            padding: 1rem !important;
        }
    }
</style>
""", unsafe_allow_html=True)

# Données des applications
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
        "description": "Solution ERP complète de gestion industrielle avec 61 postes de travail et TimeTracker intégré",
        "features": ["61 postes de travail configurés", "TimeTracker temps réel", "CRM et RH intégrés", "Multi-vues: Dashboard, Kanban, Gantt"],
        "status": "production",
        "category": "gestion",
        "color": "#8B5CF6",
        "gradient": "linear-gradient(135deg, #8B5CF6 0%, #7C3AED 100%)",
        "badge": "🏭 INDUSTRIE 4.0"
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

# Statistiques globales (simulées ou récupérables d'une API)
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
if 'show_details' not in st.session_state:
    st.session_state.show_details = {}

# Header principal avec animation
st.markdown("""
    <div class="header-container">
        <div class="header-glow"></div>
        <div class="header-content">
            <style>
                @media (max-width: 768px) {
                    .title-container { flex-direction: column !important; gap: 10px !important; }
                    .title-line { width: 100px !important; margin: 10px auto !important; }
                    .main-title { font-size: 2rem !important; letter-spacing: 4px !important; }
                    .main-subtitle { font-size: 1.2rem !important; }
                    .main-description { font-size: 0.95rem !important; padding: 0 20px !important; }
                    .header-stats { flex-wrap: wrap !important; gap: 15px !important; }
                    .stat-item { flex: 0 0 45% !important; }
                }
                @media (max-width: 480px) {
                    .main-title { font-size: 1.5rem !important; letter-spacing: 2px !important; }
                    .stat-item { flex: 0 0 100% !important; }
                }
            </style>
            <div class="title-container" style="display: flex; align-items: center; justify-content: center; gap: 15px; margin-bottom: 2rem;">
                <div class="title-line" style="width: 60px; height: 2px; background: linear-gradient(to right, transparent, rgba(255,255,255,0.8));"></div>
                <h1 class="main-title" style="
                    font-size: 3.5rem; 
                    font-weight: 500; 
                    color: white; 
                    margin: 0;
                    letter-spacing: 8px; 
                    text-transform: uppercase;
                    font-family: 'Helvetica Neue', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
                    text-shadow: 0 2px 10px rgba(0,0,0,0.2);
                ">CONSTRUCTO<span style="font-weight: 700; color: #1a1a1a;"> AI</span></h1>
                <div class="title-line" style="width: 60px; height: 2px; background: linear-gradient(to left, transparent, rgba(255,255,255,0.8));"></div>
            </div>
            <p class="main-subtitle" style="font-size: 1.5rem; font-weight: 500; margin-bottom: 1rem;">Vos Assistant AI pour la construction</p>
            <p class="main-description" style="color: rgba(255, 255, 255, 0.9); font-size: 1.1rem; max-width: 800px; margin: 0 auto;">Estimez et vérifiez vos projets 4x plus vite. Constructo AI est la plateforme intelligente qui révolutionne vos projets de construction.</p>
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

# Footer
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

# JavaScript pour animations supplémentaires
st.markdown("""
    <script>
    // Animation des cartes au survol
    document.addEventListener('DOMContentLoaded', function() {
        const cards = document.querySelectorAll('.app-card');
        cards.forEach(card => {
            card.addEventListener('mouseenter', function() {
                this.style.transform = 'translateY(-10px) scale(1.02)';
            });
            card.addEventListener('mouseleave', function() {
                this.style.transform = 'translateY(0) scale(1)';
            });
        });
    });
    </script>
""", unsafe_allow_html=True)