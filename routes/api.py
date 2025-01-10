from flask import Blueprint, jsonify, request
from utils.generator import generate_response
from utils.retriever import retrieve_documents

api_routes = Blueprint("api", __name__)


@api_routes.route("/chat", methods=["POST"])
def chat():
    """
    Accepts query and returns generated response

    Request :
    JSON : {"messaage" : "user query"}

    Response :
    JSON : {"response" : "chatbot reply"}
    """

    user_input = request.json.get("message")
    if not user_input:
        return jsonify({"error": "Message is required"}), 400

    documents = retrieve_documents(user_input)

    reponse = generate_response(user_input, documents)

    return jsonify({"response": reponse})
