import streamlit as st

# --------------------------------
# CONFIGURACIÓN
# --------------------------------
st.set_page_config(
    page_title="Test Avanzado de TLP",
    page_icon="🧠",
    layout="centered"
)

# --------------------------------
# ADVERTENCIA
# --------------------------------
st.title("🧠 Test Avanzado Orientativo de TLP")

st.warning("""
⚠️ **ATENCIÓN**

Este test:
- ❌ NO diagnostica
- ❌ NO sustituye terapia o psiquiatría
- ✅ Es solo una herramienta **orientativa**

Si el resultado te preocupa, busca ayuda profesional.
""")

st.markdown("---")

# --------------------------------
# ESTADO
# --------------------------------
if "i" not in st.session_state:
    st.session_state.i = 0
if "respuestas" not in st.session_state:
    st.session_state.respuestas = []
if "control" not in st.session_state:
    st.session_state.control = []

# --------------------------------
# ESCALA
# --------------------------------
escala = {
    "Nunca": 0,
    "Rara vez": 1,
    "A veces": 2,
    "Casi siempre": 3,
    "Siempre": 4
}

# --------------------------------
# PREGUNTAS (40)
# type = "core" | "trap"
# --------------------------------
preguntas = [
    # ----- CORE (TLP) -----
    {"p": "¿Tus emociones cambian muy rápido?", "e": "Ejemplo: pasas de feliz a triste en minutos.", "t": "core"},
    {"p": "¿Tienes miedo intenso a que te abandonen?", "e": "Ejemplo: alguien no responde y piensas que se irá.", "t": "core"},
    {"p": "¿Reaccionas de forma muy intensa emocionalmente?", "e": "Ejemplo: algo pequeño te afecta muchísimo.", "t": "core"},
    {"p": "¿Te cuesta controlar el enojo?", "e": "Ejemplo: gritas o dices cosas que luego lamentas.", "t": "core"},
    {"p": "¿Sientes un vacío interno frecuente?", "e": "Ejemplo: nada te llena por dentro.", "t": "core"},
    {"p": "¿Cambias mucho tu forma de verte a ti mismo?", "e": "Ejemplo: hoy te valoras, mañana no.", "t": "core"},
    {"p": "¿Tus relaciones son muy intensas?", "e": "Ejemplo: amar mucho y luego odiar.", "t": "core"},
    {"p": "¿Te cuesta estar solo?", "e": "Ejemplo: la soledad te genera ansiedad.", "t": "core"},
    {"p": "¿Idealizas y luego te decepcionas mucho?", "e": "Ejemplo: alguien pasa de perfecto a terrible.", "t": "core"},
    {"p": "¿Sientes emociones muy duraderas?", "e": "Ejemplo: tristeza o enojo duran días.", "t": "core"},
    {"p": "¿Te afecta demasiado la crítica?", "e": "Ejemplo: un comentario te hunde.", "t": "core"},
    {"p": "¿Te cuesta regular lo que sientes?", "e": "Ejemplo: sabes que exageras, pero no puedes parar.", "t": "core"},
    {"p": "¿Te sientes incomprendido?", "e": "Ejemplo: sientes que nadie te entiende.", "t": "core"},
    {"p": "¿Cambias de opinión sobre las personas fácilmente?", "e": "Ejemplo: hoy confías, mañana no.", "t": "core"},
    {"p": "¿Te sientes emocionalmente agotado?", "e": "Ejemplo: sentir tanto te cansa.", "t": "core"},
    {"p": "¿Te culpas mucho después de reaccionar?", "e": "Ejemplo: te castigas mentalmente.", "t": "core"},
    {"p": "¿Necesitas a otros para sentirte bien?", "e": "Ejemplo: sin alguien cerca te sientes vacío.", "t": "core"},
    {"p": "¿Te afecta mucho el rechazo?", "e": "Ejemplo: sentir que no te quieren duele demasiado.", "t": "core"},
    {"p": "¿Sientes que todo es muy intenso?", "e": "Ejemplo: nada es neutral.", "t": "core"},
    {"p": "¿Te cuesta mantener estabilidad emocional?", "e": "Ejemplo: subidas y bajadas constantes.", "t": "core"},
    {"p": "¿Te sientes diferente a los demás?", "e": "Ejemplo: no encajas.", "t": "core"},
    {"p": "¿Sientes ansiedad cuando alguien se aleja?", "e": "Ejemplo: distancia = desesperación.", "t": "core"},
    {"p": "¿Te cuesta perdonarte errores emocionales?", "e": "Ejemplo: sigues castigándote.", "t": "core"},
    {"p": "¿Reaccionas antes de pensar?", "e": "Ejemplo: actúas por impulso emocional.", "t": "core"},
    {"p": "¿Tus emociones te controlan?", "e": "Ejemplo: no decides cómo sentirte.", "t": "core"},
    {"p": "¿Te sientes vacío incluso con gente?", "e": "Ejemplo: acompañado pero solo.", "t": "core"},
    {"p": "¿Te cuesta confiar?", "e": "Ejemplo: esperas que te fallen.", "t": "core"},
    {"p": "¿Te sientes emocionalmente inestable?", "e": "Ejemplo: montaña rusa emocional.", "t": "core"},
    {"p": "¿Sientes culpa intensa con frecuencia?", "e": "Ejemplo: te juzgas duramente.", "t": "core"},
    {"p": "¿Te afecta demasiado lo que piensan de ti?", "e": "Ejemplo: un comentario cambia tu día.", "t": "core"},

    # ----- TRAMPA / CONTROL -----
    {"p": "¿Siempre te sientes perfectamente estable emocionalmente?", "e": "Ejemplo: nunca te alteras.", "t": "trap"},
    {"p": "¿Nunca has sentido enojo en tu vida?", "e": "Ejemplo: jamás.", "t": "trap"},
    {"p": "¿Tus emociones nunca cambian?", "e": "Ejemplo: siempre iguales.", "t": "trap"},
    {"p": "¿Nunca te afecta lo que otros piensan?", "e": "Ejemplo: cero impacto.", "t": "trap"},
    {"p": "¿Jamás reaccionas impulsivamente?", "e": "Ejemplo: siempre perfecto control.", "t": "trap"},
    {"p": "¿Nunca te has sentido triste?", "e": "Ejemplo: tristeza inexistente.", "t": "trap"},
    {"p": "¿Siempre entiendes exactamente lo que sientes?", "e": "Ejemplo: total claridad emocional.", "t": "trap"},
    {"p": "¿Nunca te contradices emocionalmente?", "e": "Ejemplo: siempre coherente.", "t": "trap"},
    {"p": "¿Tus relaciones nunca tienen conflictos?", "e": "Ejemplo: todo es perfecto.", "t": "trap"},
    {"p": "¿Siempre respondes con total calma?", "e": "Ejemplo: jamás pierdes control.", "t": "trap"},
]

# --------------------------------
# MOSTRAR PREGUNTA
# --------------------------------
if st.session_state.i < len(preguntas):
    q = preguntas[st.session_state.i]

    st.subheader(f"Pregunta {st.session_state.i + 1} de {len(preguntas)}")
    st.markdown(f"### {q['p']}")
    st.info(q["e"])

    r = st.radio(
        "Selecciona la opción:",
        list(escala.keys()),
        key=st.session_state.i
    )

    if st.button("➡️ Siguiente"):
        valor = escala[r]

        if q["t"] == "core":
            st.session_state.respuestas.append(valor)
        else:
            st.session_state.control.append(valor)

        st.session_state.i += 1
        st.rerun()

# --------------------------------
# RESULTADOS
# --------------------------------
else:
    st.title("📊 Resultado Final")

    core_total = sum(st.session_state.respuestas)
    core_max = len(st.session_state.respuestas) * 4
    prob = (core_total / core_max) * 100

    # Evaluar trampas
    incoherencia = sum(1 for x in st.session_state.control if x >= 3)

    if incoherencia >= 5:
        ajuste = 15
        advertencia = "⚠️ Se detectaron respuestas poco coherentes."
    else:
        ajuste = 0
        advertencia = None

    prob_final = max(0, min(100, prob - ajuste))

    st.write(f"**Probabilidad orientativa:** {round(prob_final, 1)}%")

    if advertencia:
        st.warning(advertencia + " El resultado fue ajustado.")

    if prob_final < 30:
        st.success("🔵 Probabilidad baja de rasgos TLP")
    elif prob_final < 60:
        st.warning("🟡 Probabilidad moderada de rasgos TLP")
    else:
        st.error("🔴 Probabilidad alta de rasgos TLP")

    if st.button("🔄 Reiniciar"):
        st.session_state.clear()
        st.rerun()
