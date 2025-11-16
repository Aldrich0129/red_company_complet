import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

# ======================================================
# CONFIG – 页面布局为全宽
# ======================================================

st.set_page_config(
    page_title="Red Dinámica de Empresas",
    page_icon="🕸️",
    layout="wide"
)

# ======================================================
# CSS：让内容真正全屏展现
# ======================================================

FULLSCREEN_CSS = """
<style>
/* 整个页面填充满 */
.block-container {
    padding: 0 !important;
    margin: 0 !important;
    max-width: 100% !important;
}

/* 主区域全宽 */
.css-ffhzg2 {   /* 适配部分 streamlit 版本 */
    padding: 0 !important;
    max-width: 100% !important;
}

/* iframe 100% 宽度，95% 屏幕高度 */
.fullscreen-iframe iframe {
    width: 100% !important;
    height: 95vh !important;
    border: none !important;
}

/* 左侧 sidebar 更窄，让主屏最大化 */
section[data-testid="stSidebar"] {
    width: 260px !important;
}

/* 主内容区无 padding */
div[data-testid="stAppViewContainer"] {
    padding: 0 !important;
}
</style>
"""

st.markdown(FULLSCREEN_CSS, unsafe_allow_html=True)

# ======================================================
# 文件映射
# ======================================================

HTML_MAP_YEARS = {
    "Red Global (por años)": "global_dynamic_years.html",
    "Red de Riesgo (por años)": "risk_dynamic_years.html",
    "Red de Rentabilidad (por años)": "return_dynamic_years.html",
}

HTML_VARIABLES = "global_dynamic_variables.html"

# ======================================================
# 缓存 HTML 文件读取
# ======================================================

@st.cache_data
def load_html(path: str) -> str:
    p = Path(path)
    if not p.exists():
        return f"<h3 style='color:red;'>Archivo no encontrado: {path}</h3>"
    return p.read_text(encoding="utf-8")

# ======================================================
# Sidebar
# ======================================================

with st.sidebar:
    st.markdown("### 🕸️ Red Dinámica – Control Panel")
    choice_year = st.radio(
        "Seleccione una red (por años):",
        list(HTML_MAP_YEARS.keys())
    )
    st.markdown("---")
    st.markdown("📊 **Vista por variables** está en la pestaña superior.")
    st.markdown("---")
    st.caption("© 2025 – Visualización académica")

# ======================================================
# 主界面 Tabs
# ======================================================

tab1, tab2 = st.tabs(["🔁 Vista por años (Máxima pantalla)", "📈 Vista por variables"])

# ======================================================
# TAB 1：按年动态 red（全屏）
# ======================================================

with tab1:
    st.markdown("### 🔁 Red dinámica por años (Pantalla completa)")
    html_file = HTML_MAP_YEARS[choice_year]
    html = load_html(html_file)

    st.markdown('<div class="fullscreen-iframe">', unsafe_allow_html=True)
    components.html(html, height=900, scrolling=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ======================================================
# TAB 2：按变量动态 red（全屏）
# ======================================================

with tab2:
    st.markdown("### 📈 Red dinámica por variables (Pantalla completa)")
    html = load_html(HTML_VARIABLES)

    st.markdown('<div class="fullscreen-iframe">', unsafe_allow_html=True)
    components.html(html, height=900, scrolling=True)
    st.markdown('</div>', unsafe_allow_html=True)
