# app.py

from flask import Flask, request, jsonify
import gradio as gr

app = Flask(__name__)

# === YOUR CHATBOT FUNCTION ===
def respond(message, chat_history):
    # Replace this with your real AI logic
    bot_response = f"Echo: {message}"
    chat_history.append((message, bot_response))
    return "", chat_history

# === GRADIO CHAT INTERFACE (for internal use) ===
chat_interface = gr.ChatInterface(fn=respond)

# === CUSTOM FLASK ROUTE FOR YOUR FRONTEND ===
@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message")
    history = data.get("history", [])

    # Call Gradio function directly
    response, new_history = respond(user_message, history)
    return jsonify({"response": response, "history": new_history})

# === SERVE CUSTOM HTML PAGE ===
@app.route("/")
def home():
    return open("templates/index.html").read()

# === MOUNT GRADIO INTO FLASK APP ===
app = DispatcherMiddleware(app, {
    "/gradio": chat_interface.app
})

if __name__ == "__main__":
    from werkzeug.serving import run_simple
    run_simple("0.0.0.0", 8000, app, use_reloader=False)