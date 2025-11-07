"""
Capa de Servicio: Lógica de negocio para interactuar con Ollama
"""
import ollama
from typing import Optional
from ..domain.models import Conversation


class OllamaService:
    """Servicio para manejar la comunicación con Ollama"""
    
    def __init__(self, model_name: str = 'llama2', language: str = 'es'):
        self.model_name = model_name
        self.language = language
        
        # Prompt del sistema según el idioma
        system_prompts = {
            'es': 'Eres un asistente útil que SIEMPRE responde en español. Todas tus respuestas deben estar completamente en español, sin importar el idioma de la pregunta.',
            'en': 'You are a helpful assistant.',
        }
        
        system_prompt = system_prompts.get(language, system_prompts['es'])
        self.conversation = Conversation(model_name=model_name, system_prompt=system_prompt)
    
    def check_model_availability(self) -> bool:
        """Verifica si el modelo está disponible"""
        try:
            models = ollama.list()
            model_list = models.get('models', [])
            
            # Extraer nombres de modelos de forma segura
            available_models = []
            for model in model_list:
                if isinstance(model, dict):
                    if 'name' in model:
                        available_models.append(model['name'])
                    elif 'model' in model:
                        available_models.append(model['model'])
            
            # Verificar si nuestro modelo está en la lista
            for available in available_models:
                if self.model_name in available or available.startswith(self.model_name + ':'):
                    return True
            
            return False
            
        except Exception as e:
            print(f"Error verificando modelos: {e}")
            return False
    
    def pull_model(self) -> bool:
        """Descarga el modelo si no está disponible"""
        try:
            print(f"Descargando modelo {self.model_name}...")
            ollama.pull(self.model_name)
            print(f"Modelo {self.model_name} descargado correctamente.")
            return True
        except Exception as e:
            print(f"Error descargando modelo: {e}")
            return False
    
    def send_message(self, user_message: str) -> Optional[str]:
        """Envía un mensaje y obtiene la respuesta"""
        try:
            # Agregar mensaje del usuario al historial
            self.conversation.add_message('user', user_message)
            
            # Obtener respuesta de Ollama
            response = ollama.chat(
                model=self.model_name,
                messages=self.conversation.get_history()
            )
            
            # Extraer el contenido de la respuesta
            assistant_message = response['message']['content']
            
            # Agregar respuesta al historial
            self.conversation.add_message('assistant', assistant_message)
            
            return assistant_message
            
        except Exception as e:
            print(f"Error al enviar mensaje: {e}")
            return None
    
    def clear_conversation(self):
        """Limpia el historial de la conversación"""
        self.conversation.clear()
        print("Conversación limpiada.")
    
    def get_conversation_length(self) -> int:
        """Retorna el número de mensajes en la conversación"""
        return len(self.conversation.messages)