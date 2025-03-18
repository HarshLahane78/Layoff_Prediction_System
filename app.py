from flask import Flask, request, jsonify,send_from_directory,send_file,render_template
import pickle
import numpy as np

app = Flask(__name__)

model_path = "layoff_logistic_regression_model.pkl"  # Update with your actual model file name

try:
    with open(model_path, "rb") as file:
        model = pickle.load(file)  # Load the trained model
    print("Model loaded successfully!")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None  # Handle failure to load the model

# Now you can use the model or save it again if needed
with open("updated_model.pkl", "wb") as file:
    pickle.dump(model, file, protocol=pickle.HIGHEST_PROTOCOL)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory('static', 'favicon.webp', mimetype='image/vnd.microsoft.icon')

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json  # Expecting input as JSON
        features = np.array(data["features"]).reshape(1, -1)  # Convert to 2D array
        prediction = model.predict(features)
        return jsonify({"prediction": int(prediction[0])})
    except Exception as e:
        return jsonify({"error": str(e)})



@app.route('/download_model')
def download_model():
    return send_file("layoff_logistic_regression_model.pkl", as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)  # Render requires a specified port
