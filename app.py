from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def get_address():
    # Set the API endpoint
    url = 'https://maps.googleapis.com/maps/api/geocode/json'

    # Set the parameters for the API request
    params = {
        'key': 'AIzaSyD7w-GA5fp8_Dq7denlBlW3zhhDBTKDKIQ',
        'address': 'Georgian College, Barrie, ON, Canada'
    }

    # Make the API request
    response = requests.get(url, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response JSON to get the address of Georgian College
        response_json = response.json()
        address = response_json['results'][0]['formatted_address']
        
        return jsonify({"address": address}), 200
    else:
        return jsonify({"error": "Request failed."}), 500

if __name__ == "__main__":
    app.run(port=5001)