# SDG 7: Affordable and Clean Energy — Electricity Access Analysis

**Course project:** Power BI dashboard + CRISP-DM data science notebook
**Author:** Levi (<your full name / course / institution>)

## About the project
This project looks at SDG 7 ("Ensure access to affordable, reliable, sustainable
and modern energy for all") using real country-level data from 2000 to 2022.
It follows the CRISP-DM methodology from business understanding through to
modeling, with a Kenya spotlight.

## Business questions
1. Which countries lag on electricity access, and how has that changed since 2000?
2. Does a cleaner (more renewable) electricity mix go together with higher access?
3. What drives electricity access (income, urbanisation, energy mix)?

## Data sources
| Source | What it provides |
|---|---|
| [Our World in Data energy dataset](https://github.com/owid/energy-data) | Electricity mix, per-capita energy figures |
| [World Bank Open Data](https://data.worldbank.org) | Electricity access (SDG 7.1.1), renewable share (SDG 7.2.1), GDP per capita, urban population |

## CRISP-DM progress
- [x] 1. Business Understanding
- [x] 2. Data Understanding
- [x] 3. Data Preparation
- [ ] 4. Modeling (linear regression, Ridge)
- [ ] 5. Evaluation (R² and MSE)
- [ ] 6. Deployment (Power BI dashboard, Streamlit app)

## Project structure
```
sdg7-energy-access/
├── data/
│   ├── raw/          # downloaded data (not tracked by git)
│   └── processed/    # cleaned datasets
├── notebooks/        # CRISP-DM notebook
├── app/              # Streamlit app
├── powerbi/          # Power BI dashboard file
├── reports/          # figures and write-ups
└── requirements.txt
```

## How to run
```powershell
git clone https://github.com/<your-username>/sdg7-energy-access.git
cd sdg7-energy-access
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```
Then open `notebooks/01_sdg7_crisp_dm.ipynb` in VS Code and run it top to bottom.
The notebook downloads the raw data itself.

## Key findings
<leave this for now, we fill it in after the dashboard and model>

## Tools
Python, pandas, scikit-learn, statsmodels, Streamlit, Power BI