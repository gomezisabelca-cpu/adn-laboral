import streamlit as st
import google.generativeai as genai

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Mapeador de ADN Laboral", layout="wide")

# --- ESTILO PERSONALIZADO (CSS) ---
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stButton>button { border-radius: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- CONFIGURACIÓN DE IA ---
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("⚠️ Falta la API Key en los Secrets de Streamlit.")

# --- SIDEBAR (MENÚ DE NAVEGACIÓN) ---
with st.sidebar:
    st.title("🧬 ADN Laboral")
    mode = st.radio("Selecciona el Módulo:", ["👤 Personas", "🏢 Empresas"])
    st.info("Creado por Isabel Gómez | Ing. Civil & SEO")

# --- LÓGICA DE CEREBRO (PROMPTS) ---
if mode == "👤 Personas":
    st.header("Tu valor no es un cargo, es tu esencia")
    system_instr = "Eres el Mapeador de ADN Laboral para personas. Tu meta es extraer habilidades reales de historias de vida."
else:
    st.header("Un cargo no es una lista, es un propósito")
    system_instr = "Eres el Mapeador de ADN Laboral para empresas. Ayuda a diseñar cargos basados en problemas reales a resolver."

# --- CHAT INTERFACE ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar mensajes
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Entrada de usuario
if prompt := st.chat_input("Escribe aquí..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

# Respuesta de Gemini simplificada
    model = genai.GenerativeModel('gemini-1.5-flash', system_instruction=system_instr)
    
    with st.chat_message("assistant"):
        # En lugar de usar start_chat, vamos a enviarlo directo para probar
        response = model.generate_content(prompt)
        st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
