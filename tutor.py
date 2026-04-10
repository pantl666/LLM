import os
from dotenv import load_dotenv
from openai import OpenAI  

# 1. CARGAMOS LA CONFIGURACIÓN
load_dotenv()

# Configuramos el cliente para que use Groq aunque usemos la librería de OpenAI
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

def tutor_virtual():
    # 2. DEFINIMOS LA PERSONALIDAD (EL ADN)
    instrucciones_mentor = (
        "Eres un tutor experto en tecnología, con una personalidad como la de Gemini. "
        "Eres empático, ingenioso y alentador. No das respuestas directas; usas el "
        "método socrático para que el alumno piense. Usa analogías sencillas y "
        "siempre termina con una pregunta para motivar al estudiante."
    )

    historial = [{"role": "system", "content": instrucciones_mentor}]

    print("\n--- [SISTEMA]: Tutor Virtual Iniciado Correctamente ---")
    print("🤖 Mentor AI: ¡Hola! Me emociona acompañarte en este camino para orientarte. ¿Qué concepto quieres que exploremos hoy?\n")

    while True:
        usuario = input("Estudiante (tú): ")

        if usuario.lower() in ["salir", "exit", "adiós", "bye"]:
            print("\n🤖 Mentor AI: ¡Gran sesión hoy! Sigue practicando y recuerda que el código no muerde. ¡Hasta pronto!")
            break

        # Guardamos lo que dijo el usuario
        historial.append({"role": "user", "content": usuario})

        try:
            # 3. LLAMADA REAL A LA API
            print("--- [LOG]: Generando respuesta educativa personalizada... ---\n")
            
            completion = client.chat.completions.create(
                model="llama-3.1-8b-instant", 
                messages=historial
            )

            respuesta = completion.choices[0].message.content

            # Mostramos la respuesta del tutor
            print(f"🤖 Mentor AI: {respuesta}\n")

            # Guardamos la respuesta en el historial para que no pierda el hilo
            historial.append({"role": "assistant", "content": respuesta})

        except Exception as e:
            print(f"❌ Error en la API: {e}")
            break

if __name__ == "__main__":
    tutor_virtual()