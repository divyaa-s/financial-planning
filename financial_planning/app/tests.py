
import joblib

def load_model(model_path):
    try:
        # Load the model from the specified path
        model = joblib.load(model_path)
        # Check if the loaded object has a 'predict' attribute
        if hasattr(model, 'predict'):
            return model
        else:
            raise AttributeError("Loaded object does not have a 'predict' attribute.")
    except Exception as e:
        print("Error loading the model:", str(e))
        return None

# Example usage:
model_path = 'D:\Programs\model.pkl'
loaded_model = load_model(model_path)
if loaded_model:
    # Now you can use the loaded model for prediction
    # Assuming 'data' is your input data
    prediction = loaded_model.predict("On the last trading day of the week, the BSE Sensex and Nifty50 extended their losing streak amidst global turmoil fueled by the Iran-Israel conflict. The BSE Sensex plummeted by 600 points, breaching the 72,000 mark, while the Nifty50 approached 21,800. At 9:19 AM, the BSE Sensex was trading at 71,897.78, marking a decline of 591 points or 0.82 per cent, with the Nifty50 at 21,802.75, down by 193 points or 0.88 per cent. Here are five reasons behind the market bloodbath.")
    print("Prediction:", prediction)
