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

**Data sources:**
* [Our World in Data energy dataset](https://github.com/owid/energy-data): electricity mix, per-capita energy, population
* [World Bank Open Data](https://data.worldbank.org): electricity access, renewable share of final energy, GDP per capita, urban population

**Size:** 5,040 raw country-year rows (220 countries, 2000–2022), reduced to 4,338 rows (194 countries) after cleaning.

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
The dashboard design has three pages (screenshots in `reports/`):
1. Global overview: average access, countries below 90%, people without access, trend
2. What is linked to access: lowest-access countries, renewables vs access, income vs access
3. Kenya spotlight

![Page 1](reports/page1_global_overview.png)
![Page 2](reports/page2_links_to_access.png)
![Page 3](reports/page3_kenya_spotlight.png)

## 9. Key Findings
* Average electricity access rose from 72.5% (2000) to 87.1% (2022), but 52 of 191 countries are still below 90%.
* Kenya rose from 15.2% to 76.0%, with 87.8% of its electricity from renewables in 2022.
* Income is the strongest predictor (correlation 0.73 with log GDP per capita), followed by urbanisation (0.63).
* Linear and Ridge Regression perform almost identically: R² about 0.60, RMSE about 19 percentage points. Ridge is kept for stability because predictors are correlated.
* Capping predictions to the 0–100% range improves R² to about 0.63.
## 10. Limitations
* Observational relationships do not establish causation.
* Missing data and differences in coverage may affect the analysis.
* Uneven error variance and dependence between years of the same country mean coefficient significance should not be over-interpreted.
* The lowest-access ranking excludes countries removed during cleaning (for example South Sudan).
## 11. Project Structure
```
final Power BI/
├── notebooks/
│   └── 01_sdg7_crisp_dm.ipynb
├── data/
│   └── processed/        # cleaned dataset
├── powerbi/              # dashboard files
├── reports/              # dashboard screenshots
├── app/
├── requirements.txt
└── readme.md
```

## 12. Running the Notebook
1. Clone or download the repository.
2. Create a virtual environment and install packages: `pip install -r requirements.txt`
3. Open `notebooks/01_sdg7_crisp_dm.ipynb` in VS Code or Jupyter.
4. Run all cells in order. The notebook downloads the raw data itself.

## 13. Conclusion

This project applies data analysis and machine learning to investigate electricity access in the context of SDG 7. It combines exploratory analysis, regression modelling, model evaluation, and dashboard visualisation to support a better understanding of patterns associated with electricity access.