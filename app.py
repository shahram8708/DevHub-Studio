from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

JDoodle_CLIENT_ID = 'JDoodle_CLIENT_ID'
JDoodle_CLIENT_SECRET = 'JDoodle_CLIENT_SECRET'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/run', methods=['POST'])
def run_code():
    data = request.json
    code = data.get('code')
    language = data.get('language')

    url = "https://api.jdoodle.com/v1/execute"
    payload = {
        'clientId': JDoodle_CLIENT_ID,
        'clientSecret': JDoodle_CLIENT_SECRET,
        'script': code,
        'language': language,
        'versionIndex': '0'
    }

    response = requests.post(url, json=payload)
    result = response.json()

    return jsonify(output=result.get('output'))

if __name__ == '__main__':
    app.run(debug=True)
