"""
Punto de entrada principal del Chatbot con Ollama
"""
from src.interface.cli import ChatbotCLI


def main():
    """Función principal"""
    # Usar Mistral con idioma español
    chatbot = ChatbotCLI(model_name='mistral', language='es')
    chatbot.run()


if __name__ == "__main__":
    main()