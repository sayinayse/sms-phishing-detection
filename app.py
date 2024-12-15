from flask import Flask, request, jsonify, render_template
import random

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def classify_sms():
    # Get sms texe from the form
    sms_text = request.form.get('sms', '').strip()

    if not sms_text:
        return jsonify({'error': 'SMS text is required'}), 400

        # Example logic for spam detection
    is_spam = random.choice([True, False])
    result = {'is_spam' : is_spam}

    # Send back a JSON response
    return render_template("index.html", result=result)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)