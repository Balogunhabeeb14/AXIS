import logging
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import joblib

# Configure logging
logging.basicConfig(level=logging.INFO)

# Define the input data model
class InputData(BaseModel):
    DriverRating: float
    Days_Policy_Accident: str
    PastNumberOfClaims: str
    PoliceReportFiled: int
    VehiclePrice: str
    AccidentArea: str
    WitnessPresent: int
    RepNumber: int

app = FastAPI()

# Load the trained model
model = joblib.load('models/risk_scoring_model.pkl')

# Define the expected feature order
expected_features = [
    'DriverRating', 'Days_Policy_Accident', 'PastNumberOfClaims', 
    'PoliceReportFiled', 'VehiclePrice', 'AccidentArea', 
    'WitnessPresent', 'RepNumber'
]

def preprocess_input(data: pd.DataFrame) -> pd.DataFrame:
    # Ensure the input data has the correct feature order
    data = data[expected_features]
    # Implement any additional preprocessing steps here
    return data

@app.post("/rsm")
async def predict_risk(data: InputData):
    """
    API endpoint to calculate risk score for incoming data.
    """
    try:
        # Convert input data to DataFrame
        input_df = pd.DataFrame([data.dict()])
        
        # Log received data
        logging.info(f"Received data: {data.dict()}")
        
        # Preprocess input data
        processed_data = preprocess_input(input_df)
        
        # Predict risk score
        risk_score = model.predict(processed_data)
        
        return {"prediction": risk_score[0]}
    except Exception as e:
        logging.error(f"Error during prediction: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)