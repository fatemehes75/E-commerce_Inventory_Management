from flask import Flask, request, render_template
import numpy as np
import pickle

app = Flask(__name__)
# Load the trained model (before the routes)
with open('/Users/fati/PycharmProjects/inventory_management/models/model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get user input from the form
    year = int(request.form['year'])
    month = int(request.form['month'])
    day = int(request.form['day'])
    inventory_level = int(request.form['inventory_level'])

    # Make a prediction using the trained model
    input_data = np.array([year, month, day, inventory_level]).reshape(1, -1)
    prediction = model.predict(input_data)

    return f'Recommended restocking quantity: {prediction[0]:.2f} units'

if __name__ == '__main__':
    app.run(debug=True)