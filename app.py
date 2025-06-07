# app.py

from flask import Flask, request, jsonify, send_from_directory
from llama_cpp import Llama

app = Flask(__name__)

# Load LLaMA 3 GGUF model (make sure path is correct)
llm = Llama(
    model_path="./models/llama3-instruct.Q4_K_M.gguf",  # Update this path
    n_ctx=2048,      # Context length
    n_threads=4,     # CPU threads
    verbose=False    # Don't print debug output
)

@app.route('/')
def home():
    return send_from_directory('templates', 'index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '').strip()

    if not user_message:
        return jsonify({'response': 'Please say something.'})

    # Build prompt (you can customize this)
    prompt = f"<|start_header_id|>user<|end_header_id|>\n{user_message}<|start_header_id|>assistant<|end_header_id|>\n"

    # Generate response
    output = llm(prompt, max_tokens=256, stop=["<|start_header_id|>"])
    bot_response = output["choices"][0]["text"].strip()

    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)