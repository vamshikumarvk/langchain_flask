from flask import Flask, request, jsonify
from langchain_integration.chain import ask_llm

app = Flask(__name__)  # Create Flask app instance

@app.route("/chat", methods=["POST"])
def chat():
    """
    API endpoint to handle chat requests.
    Expects JSON with a 'question' field.
    """
    data = request.get_json()
    question = data.get("question", "")
    if not question:
        return jsonify({"error": "No question provided"}), 400

    # Call the LLM chain to get an answer
    answer = ask_llm(question)
    return jsonify({"answer": answer})
