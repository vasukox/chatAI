"""
Capa de Interfaz: Interfaz de línea de comandos para el chatbot
"""
from ..services.ollama_service import OllamaService


class ChatbotCLI:
    """Interfaz de línea de comandos para el chatbot"""
    
    def __init__(self, model_name: str = 'llama2', language: str = 'es'):
        self.service = OllamaService(model_name=model_name, language=language)
        self.running = False
    
    def display_welcome(self):
        """Muestra el mensaje de bienvenida"""
        print("=" * 60)
        print("🤖 CHATBOT CON OLLAMA")
        print("=" * 60)
        print(f"Modelo: {self.service.model_name}")
        print(f"Idioma: {self.service.language.upper()}")
        print("\nComandos disponibles:")
        print("  - 'salir' o 'exit': Termina el chat")
        print("  - 'limpiar' o 'clear': Limpia el historial")
        print("  - 'historial': Muestra el número de mensajes")
        print("=" * 60)
        print()
    
    def setup(self) -> bool:
        """Configura el chatbot verificando el modelo"""
        print("Verificando disponibilidad del modelo...")
        
        if not self.service.check_model_availability():
            print(f"El modelo {self.service.model_name} no está disponible.")
            response = input("¿Deseas descargarlo? (s/n): ").lower()
            
            if response == 's':
                if not self.service.pull_model():
                    print("No se pudo descargar el modelo.")
                    return False
            else:
                print("No se puede continuar sin el modelo.")
                return False
        
        print(f"✓ Modelo {self.service.model_name} listo para usar.\n")
        return True
    
    def process_command(self, user_input: str) -> bool:
        """Procesa comandos especiales. Retorna True si debe continuar"""
        user_input_lower = user_input.lower().strip()
        
        if user_input_lower in ['salir', 'exit', 'quit']:
            print("\n👋 ¡Hasta luego!")
            return False
        
        elif user_input_lower in ['limpiar', 'clear']:
            self.service.clear_conversation()
            return True
        
        elif user_input_lower in ['historial', 'history']:
            count = self.service.get_conversation_length()
            print(f"📝 Mensajes en la conversación: {count}")
            return True
        
        return True
    
    def run(self):
        """Ejecuta el loop principal del chatbot"""
        self.display_welcome()
        
        if not self.setup():
            return
        
        self.running = True
        print("Puedes empezar a chatear...\n")
        
        while self.running:
            try:
                # Obtener entrada del usuario
                user_input = input("Tú: ").strip()
                
                if not user_input:
                    continue
                
                # Procesar comandos especiales
                if not self.process_command(user_input):
                    break
                
                # Si no es un comando, es un mensaje normal
                if user_input.lower() not in ['limpiar', 'clear', 'historial', 'history']:
                    print("\n🤖 Asistente: ", end="", flush=True)
                    
                    response = self.service.send_message(user_input)
                    
                    if response:
                        print(response)
                    else:
                        print("Lo siento, hubo un error al procesar tu mensaje.")
                    
                    print()  # Línea en blanco para separar
            
            except KeyboardInterrupt:
                print("\n\n👋 Interrupción detectada. ¡Hasta luego!")
                break
            
            except Exception as e:
                print(f"\n❌ Error inesperado: {e}")
                print("Intenta de nuevo.\n")