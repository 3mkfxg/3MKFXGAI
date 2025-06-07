# app.py

import gradio as gr

# Example chatbot logic
def respond(message, chat_history):
    # Replace this with your real AI model or logic
    bot_response = f"Echo: {message}"
    chat_history.append((message, bot_response))
    return chat_history, chat_history

# Create the chatbot UI
with gr.Blocks(theme="default") as demo:
    chatbot = gr.Chatbot()
    msg = gr.Textbox(label="Type your message here")
    clear = gr.Button("Clear Chat")

    state = gr.State([])

    msg.submit(fn=respond, inputs=[msg, state], outputs=[chatbot, state])
    clear.click(fn=lambda: ([], []), inputs=[], outputs=[chatbot, state])

# Launch the app
if __name__ == "__main__":
    demo.launch()