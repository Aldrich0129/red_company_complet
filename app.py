import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

# =========================
# 页面基础配置
# =========================

st.set_page_config(
    page_title="Red Dinámica de Empresas",
    page_icon="🕸️",
    layout="wide"
)

# =========================
# 自定义样式（极简高端风格）
# =========================

CUSTOM_CSS = """
<style>
/* 整体背景与字体 */
body {
    background-color: #f6f7fb;
    font-family: -apple-system, BlinkMacSystemFont, "SF Pro Text", system-ui, sans-serif;
}

/* 主容器宽度 */
.block-container {
    padding-top: 1rem;
    padding-bottom: 2rem;
    max-width: 1400px;
}

/* 标题区 */
h1, h2, h3 {
    font-weight: 600;
    letter-spacing: 0.02em;
}

/* 去掉默认的 Streamlit 边框感 */
.css-18e3th9, .css-1d391kg {
    padding-top: 0rem;
}

/* 卡片样式 */
.network-card {
    background-color: #ffffff;
    border-radius: 18px;
    padding: 1.2rem 1.5rem 1.5rem 1.5rem;
    box-shadow: 0 14px 30px rgba(15, 23, 42, 0.08);
    border: 1px solid rgba(148, 163, 184, 0.20);
}

/* 小标签 */
.badge {
    display: inline-block;
    padding: 0.15rem 0.55rem;
    border-radius: 999px;
    font-size: 0.68rem;
    letter-spacing: 0.04em;
    text-transform: uppercase;
    background: rgba(37, 99, 235, 0.06);
    color: #1d4ed8;
    border: 1px solid rgba(37, 99, 235, 0.25);
    margin-right: 0.4rem;
}

/* 副标题说明文本 */
.subtle {
    font-size: 0.85rem;
    color: #6b7280;
}

/* 让嵌入的 iframe 占满卡片宽度 */
iframe {
    width: 100% !important;
    border-radius: 12px;
    border: none;
}
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# =========================
# 文件路径映射
# =========================

HTML_MAP_YEARS = {
    "Red Global (por años)": "global_dynamic_years.html",
    "Red de Riesgo (por años)": "risk_dynamic_years.html",
    "Red de Rentabilidad (por años)": "return_dynamic_years.html",
}

HTML_VARIABLES = "global_dynamic_variables.html"


# =========================
# 工具函数
# =========================

@st.cache_data(show_spinner=False)
def load_html_file(path: str) -> str:
    """读取本地 HTML 文件为字符串。"""
    file_path = Path(path)
    if not file_path.exists():
        return f"<h3 style='color:#b91c1c;'>Archivo no encontrado: {path}</h3>"
    return file_path.read_text(encoding="utf-8")


# =========================
# 侧边栏
# =========================

with st.sidebar:
    st.markdown("### 🕸️ Red de Empresas Mineras")
    st.markdown(
        "<span class='subtle'>Visualización interactiva de redes basadas en "
        "indicadores de rentabilidad y riesgo (2006–2024).</span>",
        unsafe_allow_html=True,
    )
    st.markdown("---")

    # 选择年份网络的数据集
    dataset_choice = st.radio(
        "Vista principal por años",
        list(HTML_MAP_YEARS.keys()),
        index=0
    )

    st.markdown("---")
    st.markdown(
        "<span class='subtle'>Use la pestaña superior para cambiar entre "
        "la vista por años y la vista por variables.</span>",
        unsafe_allow_html=True,
    )

    st.markdown("---")
    st.caption("Autor: Tu nombre\n\nVersión para uso académico.")


# =========================
# 顶部标题区
# =========================

st.markdown(
    "<span class='badge'>Network Analytics</span>",
    unsafe_allow_html=True,
)

st.markdown(
    "<h1>Red dinámica de empresas mineras</h1>",
    unsafe_allow_html=True,
)

st.markdown(
    "<p class='subtle'>Exploración de la estructura de red basada en "
    "indicadores financieros de rentabilidad y riesgo, "
    "tanto a lo largo del tiempo como por tipo de ratio.</p>",
    unsafe_allow_html=True,
)

st.write("")  # 一点间隔

# =========================
# 主体：Tabs 视图
# =========================

tab_years, tab_vars = st.tabs(["🔁 Vista por años", "📊 Vista por variables"])

# ---------- Tab 1: 按年份 ----------
with tab_years:
    st.markdown(
        "<div class='network-card'>",
        unsafe_allow_html=True,
    )

    st.markdown(
        f"<h3 style='margin-top:0;'> {dataset_choice}</h3>",
        unsafe_allow_html=True,
    )

    st.markdown(
        "<p class='subtle'>Desplácese en el control temporal del gráfico para "
        "observar cómo evoluciona la red año a año. "
        "Las posiciones de los nodos se basan en un layout de fuerzas "
        "y el tamaño del nodo refleja la centralidad (eigenvector).</p>",
        unsafe_allow_html=True,
    )

    html_file = HTML_MAP_YEARS[dataset_choice]
    html_data = load_html_file(html_file)

    components.html(html_data, height=900, scrolling=True)

    st.markdown("</div>", unsafe_allow_html=True)


# ---------- Tab 2: 按变量 ----------
with tab_vars:
    st.markdown(
        "<div class='network-card'>",
        unsafe_allow_html=True,
    )

    st.markdown(
        "<h3 style='margin-top:0;'>Red Global por variables</h3>",
        unsafe_allow_html=True,
    )

    st.markdown(
        "<p class='subtle'>En esta vista, cada red se construye a partir de "
        "un único ratio financiero (p. ej., ROE, margen operativo) y "
        "muestra cómo se agrupan las empresas según la trayectoria temporal "
        "de ese indicador. Use el control del gráfico para seleccionar la "
        "variable de interés.</p>",
        unsafe_allow_html=True,
    )

    html_data_vars = load_html_file(HTML_VARIABLES)
    components.html(html_data_vars, height=900, scrolling=True)

    st.markdown("</div>", unsafe_allow_html=True)
