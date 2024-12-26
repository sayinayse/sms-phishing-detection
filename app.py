from flask import Flask, request, jsonify, render_template
import re
import rule_based

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
    is_spam_rule_based = rule_based.is_phishing_sms(sms_text)
    if not is_spam_rule_based:
        is_spam_ML = is_phishing_sms(sms_text)

    is_spam = (is_spam_rule_based or is_spam_ML)
    result = {'is_spam' : is_spam}

    # Send back a JSON response
    return render_template("index.html", result=result)


@app.route('/presentation')
def presentation():
    return render_template("presentation.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)