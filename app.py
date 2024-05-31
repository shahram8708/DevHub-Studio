from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

JDoodle_CLIENT_ID = '3812e25af18bdbbbb9819073b7e083e6'
JDoodle_CLIENT_SECRET = 'de219f6ad96a4c727aecede1834977e7daf28cc769d0bec4e58e5fbe97f1a0a5'

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
