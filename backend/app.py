from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests from React frontend

# Define the main chatbot route
@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    # Basic logic for chatbot response
    if "hello" in user_message.lower():
        bot_response = "Hi there! How can I help you today?"
    elif "bye" in user_message.lower():
        bot_response = "Goodbye! Have a nice day."
    else:
        bot_response = "I'm not sure how to respond to that."

    return jsonify({"response": bot_response})

if __name__ == '__main__':
    app.run(debug=True)
