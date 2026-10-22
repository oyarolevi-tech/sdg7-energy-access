# SDG 7: Affordable and Clean Energy — Electricity Access Analysis

## 1. Project Overview

This project explores electricity access across countries in relation to Sustainable Development Goal 7 (SDG 7): Affordable and Clean Energy.

The project uses data analysis, visualisation, and machine learning to investigate patterns in electricity access and its relationship with economic development, urbanisation, and energy-related indicators.

The project follows the CRISP-DM (Cross-Industry Standard Process for Data Mining) methodology.

## 2. Problem Statement

Access to reliable and affordable electricity is important for economic development, education, healthcare, and improved living standards.

This project examines differences in electricity access across countries and explores how selected economic, demographic, and energy indicators relate to electricity access.

## 3. Project Objectives

* Analyse electricity access across countries and over time.
* Perform descriptive statistics and exploratory data analysis.
* Investigate relationships between electricity access and selected socioeconomic and energy indicators.
* Develop an interactive Power BI dashboard to communicate key patterns.
* Build and evaluate Linear Regression and Ridge Regression models for predicting electricity access.
* Apply the CRISP-DM methodology throughout the project.

## 4. Sustainable Development Goal

**SDG 7: Affordable and Clean Energy**

The project relates to the goal of ensuring access to affordable, reliable, sustainable, and modern energy for all.

Official SDG information: https://sdgs.un.org/goals/goal7

## 5. Dataset and Data Preparation

The project uses country-level data containing electricity access, population, economic indicators, urbanisation, and energy-related variables.

The preparation process includes:

* Inspecting the dataset structure and data types.
* Examining missing values and data quality.
* Cleaning and preparing variables for analysis.
* Performing exploratory analysis and descriptive statistics.
* Preparing appropriate features for regression modelling.

**Data source:** Add the original dataset provider and source link here.

## 6. Methodology: CRISP-DM

### Phase 1: Business Understanding

Define the project objectives and investigate factors associated with electricity access.

### Phase 2: Data Understanding

Explore the dataset using descriptive statistics, correlation analysis, and visualisations.

### Phase 3: Data Preparation

Clean the data, handle missing values, prepare features, and define the target variable.

### Phase 4: Modelling

Train Linear Regression and Ridge Regression models to estimate electricity access using selected features.

### Phase 5: Evaluation

Evaluate the models using R², Mean Squared Error (MSE), and Root Mean Squared Error (RMSE). Examine regression diagnostics and compare model performance.

### Phase 6: Deployment

Present the analytical findings through a Power BI dashboard and document the workflow and results for further use.

## 7. Machine Learning

The target variable is `access_electricity_pct`.

The project compares:

* **Linear Regression:** A baseline model for estimating electricity access.
* **Ridge Regression:** A regularised linear model that can help manage multicollinearity and reduce the impact of large coefficients.

Model performance is evaluated using:

* **R²:** Indicates how much variation in the target variable is explained by the model.
* **MSE:** Measures the average squared prediction error.
* **RMSE:** Expresses prediction error in the same units as the target variable.

The model results and diagnostic findings should be interpreted before drawing conclusions about predictive performance.

## 8. Dashboard

The Power BI dashboard presents key patterns and insights from the electricity access dataset.

## 9. Key Findings

Add the actual findings from the completed analysis here, including:

Major patterns in electricity access across countries and years.
Relationships between electricity access and selected indicators.
Linear Regression and Ridge Regression evaluation results.
The selected model and the reasons for selecting it.
## 10. Limitations
Observational relationships do not establish causation.
Missing data and differences in data coverage may affect the analysis.
Model performance depends on the available features and the evaluation method.
Predictions should be interpreted with caution when applied to countries or periods not adequately represented in the training data.
## 11. Project Structure
sdg7-energy-access/
├── notebooks/
│   └── 01_sdg7_crisp_dm.ipynb
├── data/
├── app/
├── README.md
└── ...

The structure above is illustrative. Update it to match the files and folders actually present in the repository.

## 12. Running the Notebook
Clone or download the repository.
Install the required Python packages.
Open notebooks/01_sdg7_crisp_dm.ipynb in Jupyter Notebook or VS Code.
Ensure the dataset is available at the path expected by the notebook.
Run the notebook cells in order.

Add a requirements.txt file if you want to document the project's Python dependencies.

## 13. Conclusion

This project applies data analysis and machine learning to investigate electricity access in the context of SDG 7. It combines exploratory analysis, regression modelling, model evaluation, and dashboard visualisation to support a better understanding of patterns associated with electricity access.