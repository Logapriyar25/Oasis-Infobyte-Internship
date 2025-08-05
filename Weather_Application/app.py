from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

API_KEY = "your_openweathermap_api_key"  # get one free from https://openweathermap.org/api

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/weather')
def weather():
    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'No city provided'}), 400

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data.get('cod') != 200:
        return jsonify({'error': data.get('message', 'Error fetching data')}), 404

    weather_data = {
        'city': data['name'],
        'temperature': data['main']['temp'],
        'description': data['weather'][0]['description'],
        'icon': data['weather'][0]['icon']
    }
    return jsonify(weather_data)

if __name__ == '__main__':
    app.run(debug=True)
