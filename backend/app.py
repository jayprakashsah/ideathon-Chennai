from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai

app = Flask(__name__)
CORS(app)

# Configure your Gemini API key
genai.configure(api_key="AIzaSyD5MP1A9AQFaJmMa-JDfm9MakOmcmoLgBU")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_msg = data.get("message", "")

    try:
        # Use a supported model:
        model = genai.GenerativeModel("gemini-2.5-flash")  # or "gemini-2.5-pro"
        response = model.generate_content(user_msg)
        reply = response.text if response.text else "Sorry, I didn’t understand that."
    except Exception as e:
        reply = f"Error: {str(e)}"

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)