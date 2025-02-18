import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Replace this with your Hugging Face API key
HUGGINGFACE_API_KEY = "your_huggingface_api_key"

# Hugging Face API URL (for a free text generation model)
HUGGINGFACE_API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    question = data.get("question")

    if not question:
        return jsonify({"error": "No question provided"}), 400

    # Call Hugging Face API
    headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}
    payload = {"inputs": question}

    response = requests.post(HUGGINGFACE_API_URL, json=payload, headers=headers)

    if response.status_code == 200:
        answer = response.json()[0].get("generated_text", "No response received.")
        return jsonify({"answer": answer})
    else:
        return jsonify({"error": f"Failed to get response: {response.text}"}), 500

if __name__ == "__main__":
    app.run(port=5000, debug=True)
