# AXIS - AI for eXposing Insurance Scams

## Project Overview

The **AXIS** project aims to implement the latest advancements in **Artificial Intelligence (AI)** to create a novel **Intelligent Insurance Fraud Detection System (IIFDS)**. By identifying high-risk behaviors and patterns, AXIS enables the early detection of potentially fraudulent activity, transforming **Industry**'s approach to insurance fraud.

This system will help improve the efficiency of the insurance claims process and ensure a proactive approach to fraud detection. Key focus areas include:

- **Risk Scoring Models-RSM**: Building predictive models based on both internal and external data sources to flag high-risk individuals and/or claims early, enabling the potential refusal of sales or charging higher premiums.
  
- **Network Analytics-NTA**: Developing models that connect individual and device details to identify duplicate accounts, often used to mask fraudulent activity.
  
- **Call Transcript Analytics-CTA**: Leveraging NLP and Generative AI (Gen-AI) models to analyze customer phone call transcripts, identifying key fraud indicators and flagging them for review.

- **Fraud Detection Ecosystem-FDE**: Creating an ecosystem that enhances the work of operational teams by automating fraud detection processes, improving both speed and accuracy.

The AXIS system applies **state-of-the-art AI techniques** to mitigate risk and fraud, improving operational efficiency and setting a new standard for the insurance industry.

---

## Key Features

### 1. **Risk Scoring Models - RSM**
- **Objective**: To flag high-risk individuals and claims early.
- **Tech**: Machine Learning, Predictive Analytics, Data Fusion (internal & external data sources).
  
### 2. **Network Analytics - NTA**
- **Objective**: To identify and link fraudulent accounts using device and account details.
- **Tech**: Graph Theory, Network Analysis, Entity Resolution.

### 3. **Call Transcript Analytics- CTA**
- **Objective**: To identify fraud indicators from phone calls and use **Generative AI** to flag these patterns in transcripts.
- **Tech**: NLP, Generative AI (Gen-AI), Speech-to-Text, Text Classification.

### 4. **Fraud Detection Ecosystem - FDE**
- **Objective**: To expedite and automate the process of fraud detection for operational teams.
- **Tech**: AI-powered workflow automation, Real-time alerts, Data visualization.

---

## Data Source

The dataset used in this project is sourced from Kaggle, specifically the "Vehicle Claim Fraud Detection" dataset. It is derived from a real-world fraud detection case study originally used by Oracle for machine learning purposes. The dataset contains:

- **33 columns** and **15,420 rows**.
- **8 continuous features** and **24 categorical features**.
- A binary label, `FraudFound_P` (0,1), indicating whether a claim is fraudulent (1) or not (0).

This dataset provides a comprehensive basis for training and evaluating the fraud detection models within the AXIS system.

## Metadata Brief:

| **Feature**                | **Type**    | **Description**                                                                                       | **Values/Notes**                                                                                                          |
|----------------------------|-------------|-------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| **Month**                  | `object`    | 3-letter abbreviation for the month when the accident occurred.                                        | Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec                                                                 |
| **WeekOfMonth**            | `int64`     | The week number within the month when the accident occurred.                                           | Integer value (1, 2, 3, 4)                                                                                                 |
| **DayOfWeek**              | `object`    | Day of the week the accident occurred.                                                                  | Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday                                                            |
| **Make**                   | `object`    | Car manufacturer involved in the accident.                                                             | List of 19 car manufacturers (e.g., Ford, Chevrolet, Toyota)                                                               |
| **AccidentArea**           | `object`    | Area classification of the accident (Urban or Rural).                                                   | Urban, Rural                                                                                                              |
| **DayOfWeekClaimed**       | `object`    | Day of the week when the claim was filed.                                                              | Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday                                                            |
| **MonthClaimed**           | `object`    | 3-letter abbreviation for the month when the claim was filed.                                           | Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec (contains "0" which may indicate missing data)                |
| **WeekOfMonthClaimed**     | `int64`     | Week number within the month when the claim was filed.                                                 | Integer value (1, 2, 3, 4)                                                                                                 |
| **Sex**                    | `object`    | Gender of the individual making the claim.                                                             | Male (1), Female (0)                                                                                                      |
| **MaritalStatus**          | `object`    | Marital status of the individual making the claim.                                                     | Single, Married, Divorced, Widowed                                                                                         |
| **Age**                    | `int64`     | Age of the individual making the claim.                                                                | Integer value (e.g., 25, 40, etc.)                                                                                        |
| **Fault**                  | `object`    | Whether the individual was at fault for the accident.                                                  | Policy Holder (1), Third Party (0)                                                                                        |
| **PolicyType**             | `object`    | Type of insurance and vehicle category.                                                                | Liability, All Perils, Collision (with vehicle categories: Sport, Sedan, Utility)                                        |
| **VehicleCategory**        | `object`    | Vehicle categorization (as described in `PolicyType`).                                                  | Sport, Sedan, Utility                                                                                                     |
| **VehiclePrice**           | `object`    | Price range of the vehicle involved in the accident.                                                  | Low, Medium, High                                                                                                         |
| **FraudFound_P**           | `int64`     | Indicates if the claim was fraudulent (1) or not (0).                                                  | 1 (fraudulent), 0 (non-fraudulent)                                                                                         |
| **PolicyNumber**           | `int64`     | Masked policy number, appears to be the same as the row number minus 1.                               | Integer values                                                                                                            |
| **RepNumber**              | `int64`     | Number of the representative handling the claim.                                                      | Integer values between 1 and 16                                                                                           |
| **Deductible**             | `int64`     | Deductible amount associated with the policy.                                                          | Integer values (e.g., 100, 500, etc.)                                                                                      |
| **DriverRating**           | `int64`     | Rating scale from 1 to 4 for the driver.                                                              | Integer values (1 to 4)                                                                                                   |
| **Days_Policy_Accident**   | `object`    | Days between policy purchase and the accident.                                                        | Numeric or categorical (e.g., "10", "Unknown")                                                                            |
| **Days_Policy_Claim**      | `object`    | Days between policy purchase and claim filing.                                                        | Numeric or categorical (e.g., "5", "Unknown")                                                                             |
| **PastNumberOfClaims**     | `object`    | Number of previous claims filed by the policyholder.                                                  | Numeric or categorical values                                                                                             |
| **AgeOfVehicle**           | `object`    | Age of the vehicle at the time of the accident.                                                       | Integer value or range (e.g., "1-3", "4-6")                                                                                |
| **AgeOfPolicyHolder**      | `object`    | Age of the policyholder at the time of the claim.                                                     | Integer value (e.g., 30, 45, etc.)                                                                                        |
| **PoliceReportFiled**      | `object`    | Whether a police report was filed for the accident.                                                    | Yes (1), No (0)                                                                                                           |
| **WitnessPresent**         | `object`    | Whether a witness was present during the accident.                                                     | Yes (1), No (0)                                                                                                           |
| **AgentType**              | `object`    | Classifies the agent handling the claim as internal or external.                                       | Internal, External                                                                                                        |
| **NumberOfSuppliments**    | `object`    | Likely refers to supplementary claims or documents.                                                    | Numeric or categorical (unclear, needs investigation)                                                                     |
| **AddressChange_Claim**    | `object`    | Time between claim filing and address change (if applicable).                                         | Numeric or categorical (e.g., "30 days", "Unknown")                                                                       |
| **NumberOfCars**           | `object`    | Number of cars involved in the accident or covered under the policy.                                  | Numeric or categorical values (e.g., "1", "2", etc.)                                                                      |
| **Year**                   | `int64`     | Year the accident occurred.                                                                            | Numeric values (e.g., 2019, 2020)                                                                                         |
| **BasePolicy**             | `object`    | Type of insurance coverage.                                                                             | Likely corresponds to `PolicyType` (e.g., Liability, Collision, etc.)                                                      |


---

## Folder Structure

The project is organized into the following directories:

- **Data**: Contains all data-related files and scripts.
  - **EDA**: Exploratory Data Analysis scripts and notebooks.
  - **utilities**: Utility scripts for data processing.
    - **ETL.py**: Script for Extract, Transform, Load processes.
    - **__init__.py**: Initialization file for the utilities module.

- **Models**: Contains model training and evaluation scripts.

- **Notebooks**: Jupyter notebooks for experimentation and analysis.

- **Scripts**: Standalone scripts for various tasks.

- **Docs**: Documentation files and resources.

---

## Installation

To set up the project on your local machine:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/AXIS.git
   ```
2. Go to the repository:
   ```bash
   cd AXIS
   ```
3. Install the requirements:
   ```bash
   pip install -r requirements.txt
   ```

This project was inspired by a job advert by Domestic and General (D&G).
