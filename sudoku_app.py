import streamlit as st
import random
import time
import streamlit as st

# =============================================
# CONFIGURACIÓN PWA (PROGRESSIVE WEB APP)
# =============================================
pwa_html = """
<link rel="manifest" href="pwa/manifest.json">
<link rel="icon" href="pwa/icon-192.png">
<meta name="theme-color" content="#4B0082">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="SudokuMath">
<link rel="apple-touch-icon" href="pwa/icon-192.png">

<script>
// Registrar Service Worker
if ('serviceWorker' in navigator) {
  window.addEventListener('load', () => {
    navigator.serviceWorker.register('pwa/service-worker.js')
      .then(reg => console.log('Service Worker registrado: ', reg))
      .catch(err => console.error('Error registrando SW: ', err));
  });
}

// Detectar si es móvil para mejor experiencia
function isMobile() {
  return /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent);
}

// Optimizar interfaz para móviles
if (isMobile()) {
  document.body.style.zoom = "80%";
  document.querySelectorAll('.stButton > button').forEach(btn => {
    btn.style.padding = "12px 20px";
    btn.style.fontSize = "16px";
  });
}
</script>
"""

st.markdown(pwa_html, unsafe_allow_html=True)
# =============================================

st.set_page_config(page_title="🧠 Sudoku Numérico", layout="centered")

banco_preguntas = [
    ("√49", "7"),
    ("2x + 3 = 11", "4"),
    ("3² + 4²", "25"),
    ("(18 ÷ 3) + 2", "8"),
    ("log10(100)", "2"),
    ("5! ÷ 10", "12"),
    ("2³ + 3²", "17"),
    ("12 % 5", "2"),
    ("√81", "9"),
    ("x = (10 - 4)/2", "3"),
    ("√64 + 3", "11"),
    ("5² - 3²", "16"),
    ("x² = 49", "7"),
    ("3x - 6 = 3", "3"),
    ("9 * 2 - 5", "13"),
    ("log10(1000)", "3"),
    ("7 + 2 * 3", "13")
]

if "preguntas" not in st.session_state or st.button("🔄 Nueva Partida"):
    random.shuffle(banco_preguntas)
    st.session_state.preguntas = banco_preguntas[:9]
    st.session_state.respuestas = ["" for _ in range(9)]
    st.session_state.inicio_tiempo = time.time()

st.title("🧠 Sudoku Numérico Universitario")
tiempo_transcurrido = int(time.time() - st.session_state.inicio_tiempo)
st.write(f"⏱️ Tiempo: {tiempo_transcurrido} segundos")

puntos = 0
cols = st.columns(3)

for i in range(3):
    for j in range(3):
        idx = i * 3 + j
        pregunta, solucion = st.session_state.preguntas[idx]
        with cols[j]:
            st.markdown(f"**{pregunta} =**")
            entrada = st.text_input("", key=f"input_{idx}", value=st.session_state.respuestas[idx])
            st.session_state.respuestas[idx] = entrada
            if entrada.strip() == solucion:
                st.success("✔️ Correcto")
                puntos += 1
            elif entrada:
                st.error("❌ Incorrecto")

st.markdown(f"### 🎯 Puntaje: {puntos} / 9")

streamlit

# Sudoku Numérico Duke

st.markdown("Una app educativa tipo Sudoku en Streamlit que presenta operaciones matemáticas universitarias para resolver en una grilla 3x3.")

## 🧩 Funcionalidades

st.markdown("""
- Operaciones y validación automática
* Sistema de verificación integrado
""")

## ⚙️ Instalación
# Alrededor de la línea 70
st.header("Instalación y Uso")
st.markdown("### Clonar el repositorio:")
st.code("git clone https://github.com/CTU_USUARIO/sudoku-numerico-duke.git", language='bash')
st.markdown("* Ejecuta este comando en tu terminal")

st.markdown("### Instalar dependencias:")
st.code("pip install -r requirements.txt", language='bash')

st.markdown("### Ejecutar la aplicación:")
st.code("streamlit run sudoku_app.py", language='bash')
