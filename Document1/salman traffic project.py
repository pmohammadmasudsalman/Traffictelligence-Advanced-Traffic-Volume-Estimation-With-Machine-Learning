from flask import Flask, render_template, request
import pickle
 # only if you're using os.path.join below

app = Flask(__name__)

print("✅ app.py has started running")

# Load model
model = pickle.load(open(r"C:\Users\key\Downloads\Traffic_Telligence_Project\Flask\model.pkl", 'rb'))
encoder = pickle.load(open(r"C:\Users\key\Downloads\Traffic_Telligence_Project\Flask\encoder.pkl",'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # Collect form data
        temp = float(request.form['temp'])
        rain = int(request.form['rain'])
        snow = float(request.form['snow'])
        weather = int(request.form['weather'])
        holiday = int(request.form['holiday'])
        year = int(request.form['year'])
        month = int(request.form['month'])
        day = int(request.form['day'])
        hours = int(request.form['hours'])
        minutes = int(request.form['minutes'])
        seconds = int(request.form['seconds'])

        # Form the input array for prediction
        input_data = [[temp, rain, snow, weather, holiday, year, month, day, hours, minutes, seconds]]

        # Prediction
        predicted_value = model.predict(input_data)[0]

        # Pass prediction to HTML
        return render_template('index.html', prediction_text=f"Predicted Traffic Volume: {int(predicted_value)}")
    
    return render_template('index.html', prediction_text='')


if __name__ == "__main__":
    print("🚀 Starting Flask server...")
    app.run(debug=True)