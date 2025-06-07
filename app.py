# app.py

import gradio as gr

def respond(message, chat_history):
    # Replace this with your real AI logic
    bot_response = f"Echo: {message}"
    chat_history.append((message, bot_response))
    return "", chat_history  # Return empty string for the textbox and updated chat history

with gr.Blocks() as demo:
    chatbot = gr.Chatbot(type="messages")  # Use 'messages' format for future compatibility
    msg = gr.Textbox(label="Type your message here")
    clear = gr.Button("Clear Chat")

    state = gr.State([])

    # Bind the submit event to the respond function
    msg.submit(fn=respond, inputs=[msg, state], outputs=[chatbot, state])
    clear.click(lambda: ([], []), outputs=[chatbot, state])

# Launch the app
if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=8000)