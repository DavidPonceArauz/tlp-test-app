import streamlit as st

# ---------------- CONFIGURACIÓN ---------------- #

st.set_page_config(
    page_title="Test emocional (orientativo)",
    page_icon="💙",
    layout="centered"
)

ESCALA = [
    "Nunca",
    "Rara vez",
    "A veces",
    "Frecuentemente",
    "Casi siempre"
]

CRITERIOS = {
    "Miedo al abandono": [
        (
            "Siento mucho miedo de que las personas importantes se vayan de mi vida.",
            "Ejemplo: Como cuando un niño piensa que sus padres lo van a dejar solo si se enojan."
        ),
        (
            "Me pongo muy nervioso cuando alguien tarda en responderme.",
            "Ejemplo: Mandas un mensaje y, si no contestan rápido, piensas que ya no te quieren."
        ),
        (
            "Hago cosas desesperadas para que no me dejen.",
            "Ejemplo: Rogar, insistir mucho o hacer algo que no quieres solo para que se quede."
        ),
        (
            "Pequeños cambios me hacen pensar que me van a abandonar.",
            "Ejemplo: Si alguien habla menos, sientes que ya no le importas."
        )
    ],
    "Relaciones inestables": [
        (
            "Al inicio veo a las personas como perfectas y luego me decepcionan mucho.",
            "Ejemplo: Pensar que alguien es increíble y luego sentir que es horrible."
        ),
        (
            "Mis relaciones suelen ser muy intensas.",
            "Ejemplo: Amistades o parejas donde todo se siente muy fuerte."
        ),
        (
            "Puedo pasar de querer mucho a alguien a rechazarlo.",
            "Ejemplo: Un día quieres estar siempre con alguien y al otro no soportarlo."
        ),
        (
            "Mis relaciones terminan con conflictos fuertes.",
            "Ejemplo: Peleas grandes, bloqueos o rupturas dolorosas."
        )
    ],
    "Identidad inestable": [
        (
            "A veces no sé bien quién soy.",
            "Ejemplo: Sentir que cambias dependiendo con quién estés."
        ),
        (
            "Mi forma de verme cambia mucho.",
            "Ejemplo: Un día sentirte capaz y otro sentirte inútil."
        ),
        (
            "No siento que tenga una identidad clara.",
            "Ejemplo: No saber qué te define como persona."
        ),
        (
            "Mis metas cambian seguido.",
            "Ejemplo: Querer una cosa hoy y otra mañana."
        )
    ],
    "Impulsividad": [
        (
            "Hago cosas sin pensar y luego me arrepiento.",
            "Ejemplo: Gastar dinero o decir algo sin pensar."
        ),
        (
            "He hecho cosas arriesgadas sin medir consecuencias.",
            "Ejemplo: Decisiones que podrían hacerte daño."
        ),
        (
            "Cuando estoy mal emocionalmente, me cuesta controlarme.",
            "Ejemplo: Actuar solo para calmar lo que sientes."
        ),
        (
            "Actúo antes de pensar.",
            "Ejemplo: Reaccionar rápido y reflexionar después."
        )
    ],
    "Conductas autodestructivas": [
        (
            "Cuando me siento muy mal, pienso en hacerme daño.",
            "Ejemplo: Pensar que lastimarte podría calmar lo que sientes."
        ),
        (
            "A veces pienso que sería mejor desaparecer.",
            "Ejemplo: Desear no existir por un momento."
        ),
        (
            "Uso cosas dañinas para aliviar emociones.",
            "Ejemplo: Hacer algo que sabes que te hace mal."
        ),
        (
            "Siento alivio después de dañarme.",
            "Ejemplo: Calmarte por poco tiempo."
        )
    ],
    "Inestabilidad emocional": [
        (
            "Mis emociones cambian muy rápido.",
            "Ejemplo: Estar bien y luego muy mal sin razón clara."
        ),
        (
            "Mis emociones son muy intensas.",
            "Ejemplo: Sentir todo exageradamente fuerte."
        ),
        (
            "Me cuesta volver a la calma.",
            "Ejemplo: Tardar mucho en tranquilizarte."
        ),
        (
            "Siento que mis emociones me controlan.",
            "Ejemplo: No poder manejarlas."
        )
    ],
    "Vacío emocional": [
        (
            "Siento un vacío dentro de mí.",
            "Ejemplo: Como si algo faltara aunque todo esté bien."
        ),
        (
            "Nada parece llenarme.",
            "Ejemplo: Las cosas no te hacen sentir completo."
        ),
        (
            "Me siento desconectado.",
            "Ejemplo: Como lejos de todos."
        ),
        (
            "Siento que algo importante falta en mí.",
            "Ejemplo: No saber qué es, pero sentirlo."
        )
    ],
    "Ira intensa": [
        (
            "Me enojo muy fuerte.",
            "Ejemplo: Enojos grandes por cosas pequeñas."
        ),
        (
            "Me cuesta controlar mi enojo.",
            "Ejemplo: Decir cosas que luego lamentas."
        ),
        (
            "Luego me siento culpable.",
            "Ejemplo: Pensar “no debía reaccionar así”."
        ),
        (
            "Mi enojo afecta mis relaciones.",
            "Ejemplo: Personas que se alejan."
        )
    ],
    "Pensamiento extremo": [
        (
            "Veo las cosas como todo o nada.",
            "Ejemplo: Algo es perfecto o terrible."
        ),
        (
            "Me cuesta ver puntos medios.",
            "Ejemplo: Solo blanco o negro."
        ),
        (
            "Cambio rápido de opinión sobre las personas.",
            "Ejemplo: Admirar y luego despreciar."
        ),
        (
            "Mis pensamientos son extremos.",
            "Ejemplo: Amar u odiar sin grises."
        )
    ]
}

# ---------------- ESTADO ---------------- #

if "indice" not in st.session_state:
    st.session_state.indice = -1
    st.session_state.respuestas = []

# ---------------- PANTALLAS ---------------- #

st.title("💙 Test emocional (orientativo)")

if st.session_state.indice == -1:
    st.warning("""
    ⚠️ **Aviso importante**

    Este test **NO es un diagnóstico**.
    Sirve solo como una herramienta de orientación emocional.

    Responde pensando en **cómo eres en general**, no en un mal día.
    Si alguna pregunta te incomoda, puedes cerrar la app.
    """)
    if st.button("👉 Comenzar"):
        st.session_state.indice = 0
        st.experimental_rerun()

else:
    preguntas = []
    for criterio, items in CRITERIOS.items():
        for p, e in items:
            preguntas.append((criterio, p, e))

    if st.session_state.indice < len(preguntas):
        criterio, pregunta, ejemplo = preguntas[st.session_state.indice]

        st.subheader(f"Pregunta {st.session_state.indice + 1} de {len(preguntas)}")
        st.caption(f"Criterio: {criterio}")

        st.markdown(f"**{pregunta}**")
        st.info(ejemplo)

        respuesta = st.radio(
            "Elige una opción:",
            list(range(5)),
            format_func=lambda x: ESCALA[x],
            key=f"preg_{st.session_state.indice}"
        )

        if st.button("Siguiente ➡️"):
            st.session_state.respuestas.append(respuesta)
            st.session_state.indice += 1
            st.experimental_rerun()

    else:
        total = sum(st.session_state.respuestas)
        max_total = len(st.session_state.respuestas) * 4

        criterios_activados = 0
        i = 0
        for items in CRITERIOS.values():
            puntos = sum(st.session_state.respuestas[i:i+len(items)])
            if puntos >= len(items) * 4 * 0.6:
                criterios_activados += 1
            i += len(items)

        prob = min((total / max_total) * 100 + criterios_activados * 5, 100)

        st.success("✅ Test finalizado")
        st.metric("Probabilidad estimada", f"{prob:.1f}%")

        if prob < 30:
            st.write("🔹 Probabilidad baja.")
        elif prob < 60:
            st.write("🟡 Probabilidad moderada.")
        else:
            st.write("🔴 Probabilidad alta. Se recomienda hablar con un profesional.")

        st.caption("Este resultado no te define como persona 💙")
