import streamlit as st
import re
import os

# Configuración de página
st.set_page_config(
    page_title="ARRIENDAIA — Asistente Legal",
    page_icon="⚖️",
    layout="centered"
)

# ---------------------------------------------------------
# SALVAGUARDA ÉTICA OBLIGATORIA (VISIBLE ARRIBA)
# ---------------------------------------------------------
st.warning(
    "⚠️ **ADVERTENCIA LEGAL:** Esta herramienta es un ejercicio académico que no constituye "
    "asesoría legal ni sustituye la consulta con un abogado profesional. "
    "No ingrese ni almacene datos personales reales."
)

st.title("⚖️ ARRIENDAIA")
st.markdown("#### *“Entiende tu contrato. Conoce tus derechos.”*")
st.caption("Pontificia Universidad Javeriana · Derecho e Inteligencia Artificial (2026-II) · Estudiante: Mariana Perez Correal")

st.divider()

# ---------------------------------------------------------
# CORPUS NORMATIVO INTEGRADO (Ley 820 de 2003 y Código Civil)
# ---------------------------------------------------------
CORPUS_KNOWLEDGE = {
    "incremento": {
        "titulo": "Reajuste del canon de arrendamiento",
        "norma": "Ley 820 de 2003, Artículo 20",
        "cita": (
            "«Cada doce (12) meses de ejecución del contrato bajo un mismo precio, el arrendador "
            "podrá incrementar el canon hasta en una proporción que no sea superior al ciento por ciento (100%) "
            "del incremento que haya tenido el índice de precios al consumidor (IPC) en el año calendario "
            "inmediatamente anterior a aquél en que se efectúe el reajuste del canon, siempre y cuando el nuevo "
            "canon no supere el límite máximo del uno por ciento (1%) del valor comercial del inmueble.»"
        ),
        "explicacion": (
            "1. El canon solo puede incrementarse cuando hayan transcurrido al menos 12 meses desde la firma o el último aumento.\n"
            "2. El porcentaje máximo de aumento es el IPC (inflación oficial) del año anterior.\n"
            "3. En ningún caso el canon mensual resultante puede superar el 1% del valor comercial del inmueble.\n"
            "4. El arrendador debe notificar por escrito al arrendatario el monto y la fecha del incremento."
        )
    },
    "terminacion_arrendador": {
        "titulo": "Terminación unilateral por el arrendador",
        "norma": "Ley 820 de 2003, Artículo 22",
        "cita": (
            "«Son causales para que el arrendador pueda pedir unilateralmente la terminación del contrato...\n"
            "Numeral 7: El arrendador podrá dar por terminado unilateralmente el contrato durante las prórrogas, "
            "previo aviso escrito dirigido al arrendatario con una antelación no menor de tres (3) meses "
            "y el pago de una indemnización equivalente al precio de tres (3) meses de arrendamiento.»"
        ),
        "explicacion": (
            "1. Si el inquilino ha cumplido, el arrendador solo puede pedir el inmueble durante una prórroga avisando con mínimo tres (3) meses de anticipación.\n"
            "2. Además, debe pagar una indemnización equivalente a tres (3) meses de arriendo.\n"
            "3. En la fecha de vencimiento inicial o prórrogas, puede no renovar invocando causales específicas (demoler, habitar el inmueble o venta) con preaviso de 3 meses."
        )
    },
    "terminacion_arrendatario": {
        "titulo": "Terminación unilateral por el arrendatario (inquilino)",
        "norma": "Ley 820 de 2003, Artículo 24",
        "cita": (
            "«Son causales para que el arrendatario pueda pedir unilateralmente la terminación del contrato...\n"
            "Numeral 4: El arrendatario podrá dar por terminado unilateralmente el contrato dentro del término inicial "
            "o durante sus prórrogas, previo aviso escrito dirigido al arrendador con una antelación no menor de tres (3) meses "
            "y el pago de una indemnización equivalente al precio de tres (3) meses de arrendamiento.»"
        ),
        "explicacion": (
            "1. Si el inquilino quiere irse antes de tiempo sin justa causa, debe avisar con al menos tres (3) meses de anticipación y pagar 3 meses de indemnización.\n"
            "2. Si es para el día exacto en que termina el contrato, avisa con tres (3) meses de anticipación y NO paga ninguna indemnización.\n"
            "3. Si el dueño incumple (corta servicios o la casa se vuelve inhabitable), el inquilino puede terminarlo de inmediato sin pagar nada."
        )
    },
    "depositos": {
        "titulo": "Prohibición de depósitos y garantías en efectivo",
        "norma": "Ley 820 de 2003, Artículo 16",
        "cita": (
            "«En los contratos de arrendamiento para vivienda urbana no se podrán exigir depósitos en dinero efectivo "
            "u otra clase de cauciones reales, para garantizar el cumplimiento de las obligaciones que conforme a dichos "
            "contratos hayan asumido los arrendatarios. Una cláusula en este sentido no producirá efecto alguno.»"
        ),
        "explicacion": (
            "1. En Colombia está expresamente PROHIBIDO que el arrendador exija depósitos en efectivo o letras de cambio en garantía para vivienda urbana.\n"
            "2. Si el contrato incluye una cláusula pidiendo depósito en efectivo, esa cláusula es nula y no tiene valor."
        )
    },
    "reparaciones": {
        "titulo": "Reparaciones necesarias y locativas",
        "norma": "Código Civil Colombiano, Artículo 1985 y Ley 820 de 2003, Artículo 8",
        "cita": (
            "«El arrendador es obligado a mantener la cosa arrendada en estado de servir para el fin a que ha sido arrendada; "
            "y en consecuencia a hacer en ella, durante el arriendo, todas las reparaciones necesarias, a excepción de las locativas...»"
        ),
        "explicacion": (
            "1. Reparaciones necesarias (daños de techos, goteras, tuberías principales, estructura): Las paga el arrendador (dueño).\n"
            "2. Reparaciones locativas (mantenimiento del uso diario, bombillos, pintura por desgaste ordinario): Corresponden al arrendatario (inquilino)."
        )
    },
    "servicios": {
        "titulo": "Servicios públicos domiciliarios",
        "norma": "Ley 820 de 2003, Artículo 15",
        "cita": (
            "«Cuando un inmueble se entregue en arrendamiento a través de contrato verbal o escrito, y el pago de los servicios "
            "públicos corresponda al arrendatario, el arrendador podrá exigir la prestación de garantías o fianzas...»"
        ),
        "explicacion": (
            "1. El pago corresponde a quien se haya comprometido en el contrato.\n"
            "2. Si el arrendador debía pagarlos y los cortan por su culpa, el arrendatario puede pagarlos y descontarlos del canon mensual."
        )
    }
}

# ---------------------------------------------------------
# MOTOR DE RESPUESTA Y PREVENCIÓN DE ALUCINACIONES
# ---------------------------------------------------------
def consultar_arriendaia(pregunta: str) -> dict:
    pregunta_lower = pregunta.lower()

    # Detección de temas ajenos (salvaguarda anti-alucinación)
    temas_fuera = ["despido", "laboral", "salario", "divorcio", "penal", "delito", "cárcel", "comercial", "herencia"]
    for tema in temas_fuera:
        if tema in pregunta_lower:
            return {
                "tipo": "fuera",
                "mensaje": (
                    f"⚠️ **Consulta fuera del corpus:** Su pregunta trata sobre temas ajenos al arrendamiento de vivienda urbana ('{tema}'). "
                    "Por política ética de prevención de alucinaciones, ARRIENDAIA solo responde sobre vivienda urbana en Colombia (Ley 820 de 2003)."
                )
            }

    if any(p in pregunta_lower for p in ["subir", "incremento", "aumento", "ipc", "canon", "precio"]):
        return {"tipo": "exito", "data": CORPUS_KNOWLEDGE["incremento"]}
    elif any(p in pregunta_lower for p in ["pedir", "desalojo", "arrendador terminar", "preaviso arrendador", "irse el dueño"]):
        return {"tipo": "exito", "data": CORPUS_KNOWLEDGE["terminacion_arrendador"]}
    elif any(p in pregunta_lower for p in ["entregar", "irme", "terminar contrato", "terminacion inquilino", "preaviso"]):
        return {"tipo": "exito", "data": CORPUS_KNOWLEDGE["terminacion_arrendatario"]}
    elif any(p in pregunta_lower for p in ["deposito", "depósito", "garantia", "garantía", "plata adelantada"]):
        return {"tipo": "exito", "data": CORPUS_KNOWLEDGE["depositos"]}
    elif any(p in pregunta_lower for p in ["reparacion", "reparación", "arreglo", "humedad", "tuberia", "daño", "gotera"]):
        return {"tipo": "exito", "data": CORPUS_KNOWLEDGE["reparaciones"]}
    elif any(p in pregunta_lower for p in ["servicio", "agua", "luz", "gas", "factura"]):
        return {"tipo": "exito", "data": CORPUS_KNOWLEDGE["servicios"]}
    else:
        return {
            "tipo": "no_encontrado",
            "mensaje": (
                "🔍 **Información no suficiente en el corpus:** La situación consultada no se encuentra contemplada en los artículos delimitados "
                "de la Ley 820 de 2003. Para evitar inventar información, ARRIENDAIA se abstiene de responder sin una fuente directa."
            )
        }

# ---------------------------------------------------------
# PANTALLA Y FORMULARIO
# ---------------------------------------------------------
st.write("Escribe tu duda o haz clic en un botón de prueba:")

col1, col2 = st.columns(2)
ejemplo = None

with col1:
    if st.button("📈 ¿Cuánto pueden subirme el arriendo?"):
        ejemplo = "¿Cuánto me pueden subir el canon de arrendamiento este año?"
    if st.button("🛠️ ¿Quién paga las reparaciones?"):
        ejemplo = "¿Quién debe pagar las reparaciones de la casa?"

with col2:
    if st.button("🚪 ¿Cómo me pueden pedir la casa?"):
        ejemplo = "¿Con cuánta anticipación debe avisarme el dueño para pedirme el inmueble?"
    if st.button("🛑 Pregunta fuera de tema (Prueba ética)"):
        ejemplo = "¿Cómo liquido a un trabajador despedido en mi empresa?"

consulta = st.text_input("Tu duda sobre arrendamiento:", value=ejemplo if ejemplo else "")

if st.button("Consultar en ARRIENDAIA ⚖️", type="primary"):
    if not consulta.strip():
        st.info("Escribe una duda o presiona uno de los botones de arriba.")
    else:
        res = consultar_arriendaia(consulta)
        st.divider()
        if res["tipo"] == "exito":
            info = res["data"]
            st.success(f"### 📋 {info['titulo']}")
            st.markdown("#### 💡 Orientación en lenguaje claro:")
            st.markdown(info["explicacion"])
            st.markdown("---")
            st.info(f"**Norma y artículo oficial:** {info['norma']}\n\n{info['cita']}")
        else:
            st.warning(res["mensaje"])

with st.sidebar:
    st.header("📚 Marco Jurídico")
    st.write("• Ley 820 de 2003 (Vivienda Urbana)\n• Código Civil Colombiano")
    st.divider()
    st.header("🛡️ Salvaguardas Éticas")
    st.write("• No inventa leyes ni artículos.\n• Sin almacenamiento de datos personales.")
