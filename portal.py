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
        "description": "Système d'estimation et de métrés automatisé pour projets de construction",
        "features": ["Calculs automatiques", "Métrés précis", "Estimations détaillées", "Rapports Excel"],
        "status": "production",
        "category": "estimation",
        "color": "#10B981",
        "gradient": "linear-gradient(135deg, #10B981 0%, #059669 100%)",
        "badge": "🚀 POPULAIRE"
    },
    {
        "id": "erp-ai",
        "name": "ERP AI",
        "icon": "💼",
        "url": "https://erp-ai.constructoai.ca/",
        "description": "Système de gestion intégré pour entreprises de construction",
        "features": ["Gestion projets", "Suivi budgétaire", "Planning ressources", "Tableaux de bord"],
        "status": "production",
        "category": "gestion",
        "color": "#8B5CF6",
        "gradient": "linear-gradient(135deg, #8B5CF6 0%, #7C3AED 100%)",
        "badge": "💎 ENTERPRISE"
    },
    {
        "id": "seaop",
        "name": "SEAOP",
        "icon": "🌊",
        "url": "https://seaop.constructoai.ca/",
        "description": "Optimisation des opérations et processus de construction",
        "features": ["Optimisation workflow", "Analyse performance", "Automatisation", "KPIs temps réel"],
        "status": "production",
        "category": "optimisation",
        "color": "#06B6D4",
        "gradient": "linear-gradient(135deg, #06B6D4 0%, #0891B2 100%)",
        "badge": "⚡ EFFICACITÉ"
    },
    {
        "id": "b2b-pbr8",
        "name": "B2B PBR8",
        "icon": "🤝",
        "url": "https://b2b-pbr8.constructoai.ca/",
        "description": "Plateforme B2B pour collaboration inter-entreprises construction",
        "features": ["Réseau professionnel", "Échange documents", "Appels d'offres", "Partenariats"],
        "status": "production",
        "category": "collaboration",
        "color": "#F59E0B",
        "gradient": "linear-gradient(135deg, #F59E0B 0%, #D97706 100%)",
        "badge": "🔗 RÉSEAU"
    },
    {
        "id": "c2b-cs4p",
        "name": "C2B CS4P",
        "icon": "👥",
        "url": "https://c2b-cs4p.constructoai.ca/",
        "description": "Interface client-entreprise pour services de construction",
        "features": ["Portail clients", "Suivi projets", "Communication directe", "Satisfaction client"],
        "status": "production",
        "category": "client",
        "color": "#EC4899",
        "gradient": "linear-gradient(135deg, #EC4899 0%, #DB2777 100%)",
        "badge": "💬 CLIENT"
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
            <div class="logo-container">
                <div class="logo-icon">🏗️</div>
                <div class="logo-ring"></div>
            </div>
            <h1 class="main-title">Portail Constructo AI</h1>
            <p class="main-subtitle">Centre de Solutions IA pour la Construction au Québec</p>
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
        "optimisation": "⚡ Optimisation",
        "collaboration": "🤝 Collaboration",
        "client": "👥 Client",
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
            # Carte d'application avec style premium
            st.markdown(f"""
                <div class="app-card" style="background: {app['gradient']};">
                    <div class="app-card-inner">
                        <div class="app-badge">{app['badge']}</div>
                        <div class="app-icon">{app['icon']}</div>
                        <h3 class="app-name">{app['name']}</h3>
                        <p class="app-description">{app['description']}</p>
                        <div class="app-features">
                            {''.join([f'<span class="feature-tag">✓ {feature}</span>' for feature in app['features'][:2]])}
                        </div>
                        <a href="{app['url']}" target="_blank" class="app-button">
                            <span>Accéder</span>
                            <span class="button-arrow">→</span>
                        </a>
                        <div class="app-status">
                            <span class="status-dot"></span>
                            <span>En ligne</span>
                        </div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            
            # Espacement entre les cartes
            st.markdown("<div style='margin-bottom: 2rem;'></div>", unsafe_allow_html=True)

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
    <div class="footer">
        <div class="footer-content">
            <div class="footer-section">
                <h4>🏗️ Constructo AI</h4>
                <p>Leader en solutions IA pour la construction au Québec</p>
            </div>
            <div class="footer-section">
                <h4>Contact</h4>
                <p>📧 info@constructoai.ca<br>
                📞 1-888-CONSTRUCT<br>
                📍 Montréal, Québec</p>
            </div>
            <div class="footer-section">
                <h4>Ressources</h4>
                <p><a href="#" style="color: #93C5FD;">Documentation</a><br>
                <a href="#" style="color: #93C5FD;">Support</a><br>
                <a href="#" style="color: #93C5FD;">API</a></p>
            </div>
            <div class="footer-section">
                <h4>Suivez-nous</h4>
                <p>LinkedIn | Twitter | YouTube</p>
            </div>
        </div>
        <div class="footer-bottom">
            <p>© 2025 Constructo AI - Tous droits réservés | Développé avec ❤️ au Québec</p>
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