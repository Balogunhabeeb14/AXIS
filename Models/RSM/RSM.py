import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import classification_report
from sklearn.impute import SimpleImputer
import joblib

def preprocess_and_engineer(data):
    """
    Preprocesses and performs feature engineering for risk scoring.
    """
    # Handle missing values
    data['DayOfWeekClaimed'].replace('0', np.nan, inplace=True)
    data['MonthClaimed'].replace('0', np.nan, inplace=True)
    data.fillna(method='ffill', inplace=True)
    
    # Binary Encoding for categorical features
    data['Sex'] = data['Sex'].map({'Male': 1, 'Female': 0})
    data['Fault'] = data['Fault'].map({'Policy Holder': 1, 'Third Party': 0})
    data['PoliceReportFiled'] = data['PoliceReportFiled'].map({'Yes': 1, 'No': 0})
    data['WitnessPresent'] = data['WitnessPresent'].map({'Yes': 1, 'No': 0})
    
    # Feature Engineering
    data['DriverRating_Scaled'] = (data['DriverRating'] - data['DriverRating'].min()) / \
                                   (data['DriverRating'].max() - data['DriverRating'].min())
    data['PolicyAccident_Delay'] = data['Days_Policy_Accident'].apply(lambda x: 1 if x == '30+' else 0)
    data['HighClaimHistory'] = data['PastNumberOfClaims'].apply(lambda x: 1 if pd.to_numeric(x, errors='coerce') > 2 else 0)
    data['NoPoliceReport'] = data['PoliceReportFiled'].apply(lambda x: 1 if x == 0 else 0)
    vehicle_price_map = {'less than 20,000': 1, '20,000 to 29,000': 2, '30,000 to 39,000': 3, 
                         '40,000 to 59,000': 4, '60,000 to 69,000': 5, 'more than 69,000': 6}
    data['VehiclePrice_Category'] = data['VehiclePrice'].map(vehicle_price_map)
    data['UrbanArea'] = data['AccidentArea'].map({'Urban': 1, 'Rural': 0})
    data['NoWitness'] = data['WitnessPresent'].apply(lambda x: 1 if x == 0 else 0)
    rep_claims = data.groupby('RepNumber')['FraudFound_P'].mean()
    data['Rep_FraudRate'] = data['RepNumber'].map(rep_claims)
    
    return data

def train_risk_model(data):
    """
    Trains a classification model to validate the risk scoring system.
    """
    # Define features and target
    features = [
        'DriverRating_Scaled', 'PolicyAccident_Delay', 'HighClaimHistory', 'NoPoliceReport',
        'VehiclePrice_Category', 'UrbanArea', 'NoWitness', 'Rep_FraudRate'
    ]
    X = data[features]
    y = data['FraudFound_P']
    
    # Impute missing values
    imputer = SimpleImputer(strategy='median')
    X = imputer.fit_transform(X)
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    # Train model
    model = RandomForestClassifier(random_state=42, n_estimators=100)
    model.fit(X_train, y_train)
    
    # Evaluate model
    y_pred = model.predict(X_test)
    print("Model Evaluation Report:\n", classification_report(y_test, y_pred))
    
    # Save model
    joblib.dump(model, 'models/risk_scoring_model.pkl')
    
    return model

if __name__ == "__main__":
    # Load and preprocess data
    data = pd.read_csv('Data/cleaned_fraud_data.csv')
    data = preprocess_and_engineer(data)
    
    # Train and save model
    train_risk_model(data)
