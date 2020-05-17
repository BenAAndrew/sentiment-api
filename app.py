from flask import Flask, request, jsonify
from sentiment import getSentiment

app = Flask(__name__)
DEFAULT_SENTIMENT_THRESHOLD = 0.1


@app.route("/", methods=["POST"])
def index():
    text = request.form.get("text")
    sentiment_threshold = float(request.form.get("sentiment_threshold", DEFAULT_SENTIMENT_THRESHOLD))
    return jsonify({"words": getSentiment(text, sentiment_threshold)})


if __name__ == "__main__":
    app.run(debug=False)
