from flask import Flask, request, render_template
import pandas as pd
import numpy as np
import altair as alt
import joblib

app = Flask(__name__)

# Load the model
pipe_lr = joblib.load(open("model/text_emotion.pkl", "rb"))

# Define the emotion-emoji dictionary
emotions_emoji_dict = {
    "anger": "😠", "disgust": "🤮", "fear": "😨😱", "happy": "🤗", "joy": "😂",
    "neutral": "😐", "sad": "😔", "sadness": "😔", "shame": "😳", "surprise": "😮"
}

# Prediction functions
def predict_emotions(docx):
    results = pipe_lr.predict([docx])
    return results[0]

def get_prediction_proba(docx):
    results = pipe_lr.predict_proba([docx])
    return results

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        raw_text = request.form["raw_text"]
        
        # Predictions
        prediction = predict_emotions(raw_text)
        probability = get_prediction_proba(raw_text)
        
        # Preparing results for display
        emoji_icon = emotions_emoji_dict[prediction]
        confidence = np.max(probability)
        
        # Prediction probabilities as DataFrame
        proba_df = pd.DataFrame(probability, columns=pipe_lr.classes_)
        proba_df_clean = proba_df.T.reset_index()
        proba_df_clean.columns = ["emotions", "probability"]

        return render_template(
            "index.html",
            raw_text=raw_text,
            prediction=prediction,
            emoji_icon=emoji_icon,
            confidence=confidence,
            proba_df_clean=proba_df_clean.to_dict(orient="records")
        )
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

