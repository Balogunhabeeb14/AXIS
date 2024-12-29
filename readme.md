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

## Metadata Documentation

For a detailed description of the dataset features, please refer to the [metadata documentation](metadata.md).

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
