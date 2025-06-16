import streamlit as st
import random
import time

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

Una app educativa tipo Sudoku en Streamlit que presenta operaciones matemáticas universitarias para resolver en una grilla 3X3.

## 🧩 Funcionalidades

- Operaciones y validación automática.
- Temporizador y puntaje.
- Botón de "Nueva partida" para rejugar.
- Accesible desde navegador o móvil.

## ⚙️ Instalación

```bash
git clone https://github.com/<TU_USUARIO>/sudoku-numerico-duke.git
cd sudoku-numerico-duke
pip install -r requirements.txt
streamlit run sudoku_app.py

