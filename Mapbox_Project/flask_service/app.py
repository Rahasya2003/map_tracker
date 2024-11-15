from flask import Flask, jsonify, request
import requests

app = Flask(__name__)
MAPBOX_API_KEY = "your_mapbox_api_key"

@app.route('/geocode', methods=['GET'])
def geocode():
    address = request.args.get('address')
    url = f"https://api.mapbox.com/geocoding/v5/mapbox.places/{address}.json?access_token={MAPBOX_API_KEY}"
    response = requests.get(url)
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(port=5001)
