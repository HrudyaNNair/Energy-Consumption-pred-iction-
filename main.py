from flask import Flask, render_template, request,jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    microwave = request.form['Microwave']
    humidity = request.form['Humidity']
    windspeed = request.form['Windspeed']
    home_office = request.form['HomeOffice']
    precipitation_intensity = request.form['PrecipitationIntensity']
    fridge = request.form['Fridge']
    solar = request.form['Solar']
    living_room = request.form['Living_room']
    temperature = request.form['Temperature']

    # Perform calculations or predictions based on the inputs
    # Replace the code below with your own logic
    total = int(microwave) + int(humidity) + int(windspeed) + int(home_office) + int(precipitation_intensity) + int(fridge) + int(solar) + int(living_room) + int(temperature)

    response = {'result': total}
    return response

if __name__ == '__main__':
    app.run(debug=True)
