from flask import Blueprint, jsonify, request
from utils.generator import generate_response
from utils.retriever import retrieve_documents

api_routes = Blueprint("api", __name__)

# dictionary for storing conversation history with session ids as keys
session_history = {}


@api_routes.route("/chat", methods=["POST"])
def chat():
    """
    Accepts query and returns generated response

    Request :
    JSON : {"message" : "user query", "session_id" : "unique session id"}

    Response :
    JSON : {"response" : "chatbot reply"}
    """

    user_input = request.json.get("message")
    session_id = request.json.get("session_id")

    if not user_input or not session_id:
        return jsonify({"error": "Both, message and session id are required"}), 400

    history = session_history.get(session_id, [])
    documents = retrieve_documents(user_input)

    # join query with history
    history_text = "\n".join(history)
    enhanced_query = f"{history_text}\n{user_input}" if history_text else user_input

    response = generate_response(enhanced_query, documents)

    # update session history
    history.append(f"User: {user_input}")
    history.append(f"Bot: {response}")
    session_history[session_id] = history

    return jsonify({"response": response})
