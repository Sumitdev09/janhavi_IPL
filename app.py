from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import os

# Try to load model if it exists, otherwise create a dummy one
model = None
# Use repository-relative path for the model file so it works in containers
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'IPL_Prediction_Model.pkl')
if os.path.exists(MODEL_PATH):
    try:
        import joblib
        model = joblib.load(MODEL_PATH)
    except Exception as e:
        # If model fails to load, log and fall back to dummy predictions
        print(f"⚠️  Failed loading model: {e}. Using dummy predictions for demo purposes.")
        model = None
else:
    print("⚠️  Model file not found. Using dummy predictions for demo purposes.")
    print("📝 To create the actual model, run the Prediction.ipynb notebook.")

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/health')
def health():
    # Simple health check for PaaS health endpoints
    return 'OK', 200

def calculate_crr(target_runs, runs_left, balls_left):
    total_runs = target_runs - runs_left
    total_overs = balls_left / 6
    return total_runs / total_overs

def calculate_rrr(target_runs, runs_left, balls_left):
    remaining_runs = target_runs - runs_left
    remaining_overs = balls_left / 6
    return remaining_runs / remaining_overs


@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        
        batting_team = request.form.get('batting_team')
        bowling_team = request.form.get('bowling_team')
        city = request.form.get('city')
        runs_left = float(request.form.get('runs_left'))
        balls_left = float(request.form.get('balls_left'))
        wickets_left = float(request.form.get('wickets_left'))
        target = float(request.form.get('target'))
        
        current_run_rate = calculate_crr(target,runs_left,balls_left)
        required_run_rate = calculate_rrr(target, runs_left,balls_left)

        # Create a DataFrame with the input values
        data = [[batting_team, bowling_team, city, runs_left, balls_left, wickets_left,
             current_run_rate, required_run_rate, target]]
        columns = ['BattingTeam', 'BowlingTeam', 'City', 'runs_left', 'balls_left',
               'wickets_left', 'current_run_rate', 'required_run_rate', 'target']
        input_df = pd.DataFrame(data, columns=columns)

        team1 = batting_team
        team2 = bowling_team

        # Make the prediction using the loaded model or dummy prediction
        if model is not None:
            prediction = model.predict_proba(input_df)
        else:
            # Dummy prediction for demo purposes
            # This creates realistic-looking probabilities based on current game state
            if required_run_rate > 12:
                # High required rate - bowling team favored
                prob1, prob2 = 0.25, 0.75
            elif required_run_rate > 9:
                # Moderate required rate
                prob1, prob2 = 0.45, 0.55
            elif required_run_rate < 6:
                # Low required rate - batting team favored
                prob1, prob2 = 0.75, 0.25
            else:
                # Close match
                prob1, prob2 = 0.6, 0.4
                
            # Add some randomness and adjust based on wickets
            wicket_factor = wickets_left / 10
            prob1 *= (0.8 + wicket_factor * 0.4)
            prob2 = 1 - prob1
            
            prediction = np.array([[prob1, prob2]])

        return render_template('prediction.html',
                           team1=team1,
                           team2=team2,
                           probability1=int(prediction[0, 0] * 100),
                           probability2=int(prediction[0, 1] * 100))
 

    else:
        return render_template("prediction.html") 


if __name__ == '__main__':
    # When running directly (python app.py) pick up PORT from environment so PaaS can set it.
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
