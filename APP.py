import streamlit as st

# -----------------------------
# CONFIGURACIÓN INICIAL
# -----------------------------
st.set_page_config(
    page_title="Test Orientativo de TLP",
    page_icon="🧠",
    layout="centered"
)

# -----------------------------
# ADVERTENCIA LEGAL
# -----------------------------
st.title("🧠 Test Orientativo de Trastorno Límite de la Personalidad (TLP)")

st.warning("""
⚠️ **IMPORTANTE – LEE ANTES DE CONTINUAR**

Este test:
- ❌ NO es un diagnóstico médico
- ❌ NO reemplaza a un psicólogo o psiquiatra
- ✅ Es solo una herramienta **orientativa y educativa**

Si el resultado te preocupa, **habla con un profesional de salud mental**.
""")

st.markdown("---")

# -----------------------------
# INICIALIZAR ESTADO
# -----------------------------
if "pregunta_actual" not in st.session_state:
    st.session_state.pregunta_actual = 0

if "respuestas" not in st.session_state:
    st.session_state.respuestas = []

# -----------------------------
# PREGUNTAS DEL TEST
# -----------------------------
preguntas = [
    {
        "pregunta": "¿Tus emociones cambian muy rápido?",
        "explicacion": (
            "Por ejemplo:\n\n"
            "Un momento estás muy feliz porque alguien te habló bonito, "
            "y poco después estás muy triste o enojado sin saber exactamente por qué."
        )
    },
    {
        "pregunta": "¿Sientes miedo intenso a que las personas te abandonen?",
        "explicacion": (
            "Por ejemplo:\n\n"
            "Si alguien no responde un mensaje, piensas que ya no te quiere "
            "o que se va a ir de tu vida."
        )
    },
    {
        "pregunta": "¿Cambias mucho la forma en que te ves a ti mismo?",
        "explicacion": (
            "Por ejemplo:\n\n"
            "Un día piensas que eres una buena persona y al otro día sientes "
            "que no vales nada o que no sabes quién eres."
        )
    },
    {
        "pregunta": "¿Tomas decisiones impulsivas que luego lamentas?",
        "explicacion": (
            "Por ejemplo:\n\n"
            "Gastar dinero sin pensar, decir cosas hirientes cuando estás molesto "
            "o hacer algo peligroso solo para sentir algo."
        )
    },
    {
        "pregunta": "¿Sientes un vacío interno difícil de explicar?",
        "explicacion": (
            "Por ejemplo:\n\n"
            "Aunque todo esté bien afuera, por dentro sientes como si algo faltara "
            "y nada te llena completamente."
        )
    },
    {
        "pregunta": "¿Te enojas muy fuerte y te cuesta controlarlo?",
        "explicacion": (
            "Por ejemplo:\n\n"
            "Te molestas tanto que gritas, rompes cosas o dices cosas que luego te arrepientes."
        )
    },
    {
        "pregunta": "¿Idealizas mucho a las personas y luego te decepcionan?",
        "explicacion": (
            "Por ejemplo:\n\n"
            "Alguien te parece perfecto y muy importante, pero luego un pequeño error "
            "hace que lo veas como alguien malo."
        )
    },
    {
        "pregunta": "¿Sientes emociones muy intensas por mucho tiempo?",
        "explicacion": (
            "Por ejemplo:\n\n"
            "Cuando estás triste o enojado, esa emoción dura horas o días y se siente muy fuerte."
        )
    },
    {
        "pregunta": "¿Te cuesta estar solo contigo mismo?",
        "explicacion": (
            "Por ejemplo:\n\n"
            "Cuando estás solo te sientes muy incómodo, triste o ansioso."
        )
    },
    {
        "pregunta": "¿Sientes que reaccionas más fuerte que otras personas?",
        "explicacion": (
            "Por ejemplo:\n\n"
            "Algo pequeño te afecta muchísimo más que a los demás."
        )
    }
]

# -----------------------------
# ESCALA DE RESPUESTAS
# -----------------------------
opciones = {
    "Nunca": 0,
    "Rara vez": 1,
    "A veces": 2,
    "Casi siempre": 3,
    "Siempre": 4
}

# -----------------------------
# MOSTRAR PREGUNTAS
# -----------------------------
if st.session_state.pregunta_actual < len(preguntas):
    p = preguntas[st.session_state.pregunta_actual]

    st.subheader(f"Pregunta {st.session_state.pregunta_actual + 1} de {len(preguntas)}")
    st.markdown(f"### {p['pregunta']}")
    st.info(p["explicacion"])

    respuesta = st.radio(
        "Elige la opción que más se parezca a ti:",
        list(opciones.keys()),
        key=st.session_state.pregunta_actual
    )

    if st.button("➡️ Siguiente"):
        st.session_state.respuestas.append(opciones[respuesta])
        st.session_state.pregunta_actual += 1
        st.rerun()

# -----------------------------
# RESULTADOS
# -----------------------------
else:
    st.title("📊 Resultado del Test")

    puntaje_total = sum(st.session_state.respuestas)
    puntaje_maximo = len(preguntas) * 4
    probabilidad = round((puntaje_total / puntaje_maximo) * 100, 1)

    st.write(f"**Puntaje obtenido:** {puntaje_total} / {puntaje_maximo}")
    st.write(f"**Probabilidad orientativa:** {probabilidad}%")

    if probabilidad < 30:
        st.success("🔵 Probabilidad baja de rasgos TLP")
        st.write("Tus respuestas muestran pocos rasgos compatibles con TLP.")
    elif 30 <= probabilidad < 60:
        st.warning("🟡 Probabilidad moderada de rasgos TLP")
        st.write("Podrías tener algunos rasgos emocionales intensos. Observar y reflexionar puede ayudar.")
    else:
        st.error("🔴 Probabilidad alta de rasgos TLP")
        st.write("Sería muy recomendable hablar con un profesional de salud mental.")

    if st.button("🔄 Reiniciar test"):
        st.session_state.clear()
        st.rerun()

