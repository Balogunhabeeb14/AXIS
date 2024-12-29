import pandas as pd
import numpy as np

def extract(file_path):
    """Extract data from a CSV file."""
    return pd.read_csv(file_path)

def transform(data):
    """Transform the data by cleaning and processing."""
    
    # Drop duplicates
    data = data.drop_duplicates()
    
    # Handle missing values for 'DayOfWeekClaimed' and 'MonthClaimed'
    data['DayOfWeekClaimed'].replace('0', np.nan, inplace=True)
    data['MonthClaimed'].replace('0', np.nan, inplace=True)
    data.fillna(method='ffill', inplace=True)
    
    # Convert 'Sex' to binary
    data['Sex'] = data['Sex'].map({'Male': 1, 'Female': 0})
    
    # Convert 'Fault' to binary
    data['Fault'] = data['Fault'].map({'Policy Holder': 1, 'Third Party': 0})
    
    # Convert 'PoliceReportFiled' and 'WitnessPresent' to binary
    data['PoliceReportFiled'] = data['PoliceReportFiled'].map({'Yes': 1, 'No': 0})
    data['WitnessPresent'] = data['WitnessPresent'].map({'Yes': 1, 'No': 0})
    
    return data

def load(data, output_path):
    """Load the transformed data into a new CSV file."""
    data.to_csv(output_path, index=False)

def etl_pipeline(input_file, output_file):
    """Run the ETL pipeline."""
    # Extract
    data = extract(input_file)
    
    # Transform
    transformed_data = transform(data)
    
    # Load
    load(transformed_data, output_file)

if __name__ == "__main__":
    input_file = 'Data/fraud_oracle.csv'
    output_file = 'Data/cleaned_fraud_data.csv'
    etl_pipeline(input_file, output_file) 