from flask import Flask, request, jsonify, render_template
import rule_based
import ml_based

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

    print(sms_text)
    # rule based detection
    is_spam = rule_based.is_phishing_sms(sms_text)
    print("rule: ", is_spam)
    if is_spam == False:
        is_spam = ml_based.is_phishing_sms(sms_text)
        print("ml: ", is_spam)

    print("is_spam", is_spam)
    result = {'is_spam' : is_spam}

    # TO DO: Show an informative result evaluation.
    # Why is it evaluated as spam, because of the rule_based? Which rule?
    # Because of ML classification? Which model, present the related model evaluation results.
    # Send back a JSON response
    return render_template("index.html", result=result)


@app.route('/presentation')
def presentation():
    return render_template("presentation.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)