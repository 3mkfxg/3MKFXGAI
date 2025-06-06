import requests

# Change this to Groq or another hosted model API
API_URL = "https://api-inference.huggingface.co/models/meta-llama/Meta-Llama-3-8B" 
headers = {"Authorization": "Bearer YOUR_HUGGINGFACE_API_KEY"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

def chat(message, chat_history):
    # Custom rule
    if message.lower() == "who is my uncle":
        return "3MKFXG (FAWZI MOHAZIA / Fawzi Mohazia)"

    # Otherwise ask Llama 3
    output = query({
        "inputs": message,
    })
    
    return output.get("generated_text", "Sorry, I couldn't understand that.")

# Gradio chat interface
from gradio_netlify import mount_gradio_app
import gradio as gr

app = mount_gradio_app()
demo = gr.ChatInterface(fn=chat, additional_inputs=[])

if __name__ == "__main__":
    demo.launch()