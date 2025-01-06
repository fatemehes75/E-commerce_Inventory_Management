from flask import Flask, request, render_template
import numpy as np
import pickle

app = Flask(__name__)

# Load the trained model
model_path = '/Users/fatemeheslaminasab/E-commerce_Inventory_Management/models/model.pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def index():
    return render_template('index.html')  # Ensure you have an `index.html` file in your templates folder

@app.route('/predict', methods=['POST'])
def predict():
    # Get user input from the form
    year = int(request.form['year'])
    month = int(request.form['month'])
    day = int(request.form['day'])
    inventory_level = int(request.form['inventory_level'])
    product_name = request.form['product_name']  # Get the product name

    # List of product columns from training data (same columns as used for training)
    product_columns = [
        'Alcatel', 'BlackBerry', 'Google Pixel', 'HTC','Huawei', 'LG', 'Lenovo', 'Motorola', 
        'Nokia', 'OnePlus', 'Samsung Galaxy', 'Sony Xperia', 'Xiaomi', 'ZTE', 'iPhone'
    ]
    
    # Convert the product name to one-hot encoding
    # Check if the product_name is one of the possible options
    product_vector = [1 if product_name.lower() in col.lower() else 0 for col in product_columns]
    
    # Prepare input data for prediction (4 base features + product vector)
    input_data = np.array([year, month, day, inventory_level] + product_vector).reshape(1, -1)

    # Check the shape of input_data to ensure it has the correct number of features (19 in total)
    print("Input data shape:", input_data.shape)  # This should print (1, 19)

    # Make a prediction using the trained model
    prediction = model.predict(input_data)
    
    # Calculate the restocking quantity (ensure no negative values)
    recommended_restocking_quantity = max(0, prediction[0] - inventory_level)

    # Return the restocking recommendation
    return f'Recommended restocking quantity: {recommended_restocking_quantity:} units'

if __name__ == '__main__':
    app.run(debug=True)
