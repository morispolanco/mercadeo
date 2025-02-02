import streamlit as st
import requests
import os

# Configuración de la página
st.set_page_config(page_title="Aplicación de Mercadeo", layout="wide")

# Título de la aplicación
st.title("Aplicación de Mercadeo con Streamlit")

# Obtener la API Key desde los secrets de Streamlit
api_key = st.secrets["OPENROUTER_API_KEY"]

# Función para enviar una solicitud a la API de OpenRouter
def get_openrouter_response(prompt):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "model": "google/gemini-2.0-flash-thinking-exp:free",
        "messages": [{"role": "user", "content": prompt}]
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()

# Prompts de mercadeo
prompts = {
    "Contenido de valor": "Crea una guía paso a paso sobre [tema relevante para tu audiencia] que resuelva un problema común y posicione a tu marca como una autoridad en el sector.",
    "Testimonios y casos de éxito": "Diseña una campaña que muestre testimonios reales de clientes satisfechos, destacando cómo tu producto o servicio transformó su experiencia.",
    "Marketing de influencers": "Desarrolla una estrategia para colaborar con influencers que compartan los valores de tu marca y puedan llegar a tu público objetivo de manera auténtica.",
    "Contenido interactivo": "Crea un quiz, encuesta o calculadora interactiva relacionada con tu industria que genere engagement y permita captar leads.",
    "Email marketing personalizado": "Diseña una serie de correos electrónicos automatizados que ofrezcan contenido personalizado basado en el comportamiento del usuario en tu sitio web.",
    "Descuentos y promociones": "Lanza una campaña de marketing que ofrezca un descuento exclusivo por tiempo limitado, creando urgencia y aumentando las conversiones.",
    "Storytelling emocional": "Desarrolla una narrativa emocional que conecte con tu audiencia, mostrando cómo tu marca puede ser parte de su historia de éxito.",
    "Contenido visual atractivo": "Crea una serie de gráficos, infografías o videos cortos que expliquen de manera visual los beneficios de tu producto o servicio.",
    "Marketing de contenidos SEO": "Escribe un artículo de blog optimizado para SEO que responda a una pregunta frecuente de tu audiencia y atraiga tráfico orgánico.",
    "Experiencias de marca": "Organiza un evento virtual o presencial que permita a los clientes interactuar con tu producto o servicio de manera memorable.",
    "Gamificación": "Diseña una campaña que incluya elementos de gamificación, como desafíos o recompensas, para aumentar la participación y fidelización de los clientes.",
    "Marketing socialmente responsable": "Crea una campaña que destaque cómo tu marca contribuye a una causa social o ambiental, conectando con los valores de tu audiencia."
}

# Barra lateral con los prompts
st.sidebar.title("Selecciona un Prompt de Mercadeo")
selected_prompt = st.sidebar.selectbox("Prompts", list(prompts.keys()))

# Mostrar el prompt seleccionado y su descripción
st.write(f"## {selected_prompt}")
st.write(prompts[selected_prompt])

# Botón para generar respuesta
if st.button("Generar Respuesta"):
    with st.spinner("Generando respuesta..."):
        response = get_openrouter_response(prompts[selected_prompt])
        st.write(response)
