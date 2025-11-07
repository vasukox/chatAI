"""
Capa de Dominio: Modelos de datos del chatbot
"""
from dataclasses import dataclass
from typing import List, Literal
from datetime import datetime


@dataclass
class Message:
    """Representa un mensaje en la conversación"""
    role: Literal['user', 'assistant', 'system']
    content: str
    timestamp: datetime = None
    
    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = datetime.now()
    
    def to_dict(self):
        """Convierte el mensaje al formato de Ollama"""
        return {
            'role': self.role,
            'content': self.content
        }


@dataclass
class Conversation:
    """Representa una conversación completa"""
    messages: List[Message]
    model_name: str
    
    def __init__(self, model_name: str = 'llama2', system_prompt: str = None):
        self.messages = []
        self.model_name = model_name
        
        # Agregar prompt del sistema si se proporciona
        if system_prompt:
            self.add_message('system', system_prompt)
    
    def add_message(self, role: str, content: str):
        """Añade un mensaje a la conversación"""
        message = Message(role=role, content=content)
        self.messages.append(message)
    
    def get_history(self):
        """Obtiene el historial en formato Ollama"""
        return [msg.to_dict() for msg in self.messages]
    
    def clear(self):
        """Limpia la conversación (mantiene el system prompt si existe)"""
        system_messages = [msg for msg in self.messages if msg.role == 'system']
        self.messages = system_messages