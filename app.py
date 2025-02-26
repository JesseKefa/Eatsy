from Flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    msg = request.form.get('Body', 'Hello, World!')
    response = {
        "messages": [
            {"text": f"Echo: {msg}"}
        ]
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, port=5000)  , 