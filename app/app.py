from flask import Flask, jsonify
import requests

app = Flask(__name__)

cat_facts = []

@app.route('/collect-cat-fact', methods=['GET'])
def collect_cat_fact():
    response = requests.get('https://catfact.ninja/fact')
    data = response.json()
    cat_facts.append(data['fact'])  # Save only the 'fact' part
    return jsonify({"message": "Cat fact collected!"}), 200

@app.route('/cat-facts', methods=['GET'])
def get_collected_facts():
    return jsonify({"cat_facts": cat_facts})

# Endpoint to fetch a random cat fact

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Flask runs on port 5000 by default


