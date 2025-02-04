import streamlit as st
import requests
import json

# Configuración inicial
st.set_page_config(page_title="Generador de Contenidos de Marketing", layout="wide")

# Título de la aplicación
st.title("Generador de Contenidos de Marketing")

# Instrucciones
st.write("Selecciona un prompt en la barra lateral, proporciona detalles adicionales y genera contenido para tus campañas de marketing.")

# Prompts disponibles en la barra lateral
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
    "Marketing socialmente responsable": "Crea una campaña que destaque cómo tu marca contribuye a una causa social o ambiental, conectando con los valores de tu audiencia.",
    
    # Nuevos prompts de email marketing
    "Email de bienvenida": "Escribe un email de bienvenida amigable que agradezca al cliente por registrarse y le dé una introducción a los servicios o productos de la marca.",
    "Email promocional": "Crea un email promocional que anuncie una oferta especial, destacando el beneficio principal y generando urgencia para aprovecharla.",
    "Email de contenido educativo": "Escribe un email que ofrezca información útil o educativa sobre un tema relacionado con los intereses de la audiencia.",
    "Email de recuperación de carrito": "Redacta un email para clientes que han abandonado su carrito de compras, recordándoles los productos y ofreciendo un incentivo para completar la compra.",
    "Email de fidelización": "Desarrolla un email que premie la lealtad del cliente, ofreciendo beneficios exclusivos como descuentos, acceso anticipado o contenido especial."
}

# Selección de prompt
selected_prompt = st.sidebar.selectbox("Selecciona un prompt", list(prompts.keys()))
st.sidebar.write("Descripción del prompt seleccionado:")
st.sidebar.write(prompts[selected_prompt])

# Entrada del usuario
user_input = st.text_area("Proporciona detalles adicionales para el prompt seleccionado")

# Generar contenido
if st.button("Generar contenido"):
    if not user_input:
        st.warning("Por favor, proporciona detalles adicionales para generar contenido.")
    else:
        # Configuración de la API
        api_url = "https://openrouter.ai/api/v1/chat/completions"
        api_key = st.secrets["openrouter_api_key"]

        # Petición a la API
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }

        data = {
            "model": "qwen/qwen-turbo",
            "messages": [
                {"role": "user", "content": f"{prompts[selected_prompt]} {user_input}"}
            ]
        }

        try:
            response = requests.post(api_url, headers=headers, data=json.dumps(data), timeout=30)

            # Manejo de la respuesta
            if response.status_code == 200:
                result = response.json()
                generated_content = result["choices"][0]["message"]["content"]
                st.subheader("Contenido Generado")
                st.write(generated_content)
            else:
                st.error(f"Ocurrió un error al generar el contenido. Código de estado: {response.status_code}")
                st.write("Detalles del error:", response.json())
        except requests.RequestException as e:
            st.error(f"Error de conexión: {e}")

# Footer
st.markdown(
    """
    <hr style="margin-top: 50px;">
    <div style="text-align: center; font-size: 0.9em; color: gray;">
        &copy; 2025 <a href="https://hablemosbien.org" target="_blank" style="text-decoration: none; color: gray;">Hablemosbien</a>. Todos los derechos reservados.
    </div>
    """,
    unsafe_allow_html=True
)
