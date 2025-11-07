# 🤖 Ollama Chat AI

Un chatbot interactivo de línea de comandos (CLI) construido con Python que utiliza [Ollama](https://ollama.ai/) para interactuar con modelos de IA de forma local.

## ✨ Características

- **Interfaz CLI interactiva**: Conversaciones fluidas directamente desde tu terminal
- **Arquitectura limpia**: Diseño modular con capas de dominio, servicios e interfaz
- **Gestión de conversación**: Mantiene el contexto del chat con historial de mensajes
- **Soporte multimodelo**: Compatible con diferentes modelos de Ollama (Mistral, Llama2, etc.)
- **Comandos integrados**: Controles para limpiar historial, ver estadísticas y más
- **Multiidioma**: Configuración de idioma personalizable

## 📋 Requisitos Previos

Antes de comenzar, asegúrate de tener instalado:

- **Python 3.8+**
- **Ollama**: Instala Ollama desde [ollama.ai](https://ollama.ai/)

### Instalación de Ollama

#### Windows
```bash
# Descarga el instalador desde https://ollama.ai/download
```

#### macOS
```bash
brew install ollama
```

#### Linux
```bash
curl -fsSL https://ollama.ai/install.sh | sh
```

Una vez instalado, inicia el servicio de Ollama:
```bash
ollama serve
```

## 🚀 Instalación

1. **Clona el repositorio**
```bash
git clone https://github.com/vasukox/chatAI.git
cd chatAI
```

2. **Crea un entorno virtual** (recomendado)
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

3. **Instala las dependencias**
```bash
pip install -r requirements.txt
```

4. **Descarga un modelo de Ollama** (si no lo tienes)
```bash
# Mistral (recomendado, usado por defecto)
ollama pull mistral

# O Llama2
ollama pull llama2
```

## 💻 Uso

### Iniciar el chatbot

```bash
python main.py
```

### Comandos disponibles

Una vez iniciado el chatbot, puedes usar los siguientes comandos:

| Comando | Descripción |
|---------|-------------|
| `salir` o `exit` | Termina la sesión del chat |
| `limpiar` o `clear` | Limpia el historial de conversación |
| `historial` o `history` | Muestra el número de mensajes en la conversación |

### Ejemplo de uso

```
============================================================
🤖 CHATBOT CON OLLAMA
============================================================
Modelo: mistral
Idioma: ES

Comandos disponibles:
  - 'salir' o 'exit': Termina el chat
  - 'limpiar' o 'clear': Limpia el historial
  - 'historial': Muestra el número de mensajes
============================================================

Verificando disponibilidad del modelo...
✓ Modelo mistral listo para usar.

Puedes empezar a chatear...

Tú: Hola, ¿cómo estás?

🤖 Asistente: ¡Hola! Estoy bien, gracias por preguntar. Soy un asistente de IA y estoy aquí para ayudarte. ¿En qué puedo ayudarte hoy?

Tú: salir

👋 ¡Hasta luego!
```

## 📁 Estructura del Proyecto

```
chatAI/
├── main.py                      # Punto de entrada de la aplicación
├── requirements.txt             # Dependencias del proyecto
├── src/
│   ├── __init__.py
│   ├── domain/                  # Capa de dominio
│   │   ├── __init__.py
│   │   └── models.py           # Modelos de datos (Message, Conversation)
│   ├── services/               # Capa de servicios
│   │   ├── __init__.py
│   │   └── ollama_service.py  # Servicio de integración con Ollama
│   └── interface/              # Capa de interfaz
│       ├── __init__.py
│       └── cli.py              # Interfaz de línea de comandos
└── README.md
```

### Descripción de las capas

- **Domain**: Contiene las entidades y modelos de datos del negocio
  - `Message`: Representa un mensaje en la conversación
  - `Conversation`: Gestiona el historial de mensajes

- **Services**: Implementa la lógica de negocio y la integración con servicios externos
  - `OllamaService`: Maneja la comunicación con la API de Ollama

- **Interface**: Capa de presentación para interactuar con el usuario
  - `ChatbotCLI`: Interfaz de línea de comandos interactiva

## 🔧 Configuración

### Cambiar el modelo de IA

Edita [main.py](main.py) para cambiar el modelo:

```python
def main():
    # Cambiar 'mistral' por otro modelo disponible
    chatbot = ChatbotCLI(model_name='llama2', language='es')
    chatbot.run()
```

### Modelos populares disponibles en Ollama

- `mistral` - Modelo potente y rápido (recomendado)
- `llama2` - Modelo de Meta AI
- `codellama` - Especializado en código
- `phi` - Modelo ligero de Microsoft
- `gemma` - Modelo de Google

Para ver todos los modelos disponibles:
```bash
ollama list
```

## 🛠️ Desarrollo

### Requisitos para desarrollo

```bash
pip install -r requirements.txt
```

### Ejecutar en modo desarrollo

```bash
python main.py
```

## 🤝 Contribuir

Las contribuciones son bienvenidas. Si deseas contribuir:

1. Haz un Fork del proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

## 🙏 Agradecimientos

- [Ollama](https://ollama.ai/) - Por proporcionar una forma sencilla de ejecutar LLMs localmente
- [Mistral AI](https://mistral.ai/) - Por el excelente modelo Mistral
- [Meta AI](https://ai.meta.com/) - Por Llama2

## 📧 Contacto

Si tienes preguntas o sugerencias, no dudes en abrir un issue en el repositorio.

---

**Desarrollado con ❤️ usando Python y Ollama**
