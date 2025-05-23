# climate-migration-project

## Overview

This project uses machine learning to predict **climate-induced migration outflows** in countries registered by IOM. It integrates data from the **World Bank, IMF,  IOM/DTM (displacement tracking), weather sources, and development indicators** to build a country-month level dataset. The aim is to identify regional "hotspots"—areas likely to generate out-migration in response to environmental and human security stressors.

---

## Objective

The goal is to predict **internally displaced people** from countries where the IOM has collected data, by:
- Aggregating multi-source data (climate, climate catastrophes, socio-economical vulnerability)
- Creating a region-month panel dataset
- Evaluating ML model performance and generalizability

---

## Target Variable

- `internally_displaced_persons`: Number of people leaving a country per month (main prediction target)


## Source Datasets

### 1. **Mobility & Displacement (IOM/DTM)**
| File | Description |
|------|-------------|
| `full_iom_dtm_data.csv` | Baseline regional displacement |

### 2. **EMDAT Climate Catastrophes**
| File | Description |
|------|-------------|
| `emdat_full.xslx` | Register of climate catastrophes per month, with total number of affected people and kind of catastrophe |

### 3. **Demographics / Socio-Economic (World Bank, IOM)**
| File | Description |
|------|-------------|
| `inflation_all_countries_sorted_cleaned.csv` | Inflation data from IMF |
| `environment_pop_data_all.csv` | Diverse country indicators from World Bank |

### 4. **Weather Data**
| File | Description |
|------|-------------|
| `ERA5_Monthly_Climate_Weather_FULL.csv` | Temperature in kelvin, rainfall and evaporation in meters |
---

## Dataset Granularity

- **Time**: Monthly (e.g., 2022-01, 2022-02, ...)
- **Location**: Country level

---

## Folder Structure

```
📂 CLIMATE-MIGRATION-PROJECT/
│
├── 📂 data/
├── merged_climate_iom_data.csv #final dataset
│ ├── 📂 climate_catastrophes/ # Disaster data (e.g., EM-DAT)
│ │ └── emdat_full.xlsx
│ │
│ ├── 📂 climate_data/ # Monthly climate and weather data
│ │ └── ERA5_Monthly_Climate_Weather_FULL.csv
│ │
│ ├── 📂 economic/ # Inflation and economic indicators
│ │ ├── inflation_all_countries_sorted_cleaned.csv
│ │ └── inflation_full.csv
│ │
│ ├── 📂 img/ # Visualization outputs
│ │ ├── alpha_optimization.png
│ │ ├── improved_distributions.png
│ │ └── model_comparison_results.png
│ │
│ ├── 📂 migration/ # Migration-related datasets
│ │ ├── full_iom_dtm_data.csv
│ │ ├── environment_pop_data_all.csv
│ │ ├── environment_som.csv
│ │ ├── Floods_Mastertable_2023.xlsx
│ │ ├── floods_mastertable_2024.xlsx
│ │ ├── merged_climate_iom_data.csv
│ │ ├── X_test.csv
│ │ └── y_test.csv
│
├── 📂 mlfp copy/ # Duplicate/backup of ML-related files (uncategorized)
│
├── 📂 models/ # Serialized trained models and results
│ ├── lasso_model.pkl
│ ├── ols_model.pkl
│ ├── rf_model.pkl
│ ├── ridge_model.pkl
│ └── model_comparison_results.csv
│
├── 📂 old/ # Archive of earlier notebooks
├── 000_prepro_inflation.ipynb
├── 001_merge_data.ipynb
├── 002_exploratory_data.ipynb
├── 003_crossval_log_transform.ipynb
└── 004_modeling_for_individual_country.ipynb
│
└── README.Rmd # Project overview and structure (this file)
```
---

## Credits & Contributions

This project was developed through a collaborative effort by the following team members:

- **Laia Domenech Burin** – Conceptualization and data analysis, modeling, integration of climate and migration datasets and documentation
- **Elena Mijares Lopez** – Modeling, feature engineering, documentation and results synthesis
- **Hanna Getachew** – Climate data wrangling, visualization, model evaluation and results synthesis  
- **Fanus Ghorjani** – Inflation data processing, model evaluation, and results synthesis
- **Matheus de Galiza** - Sociodemographic data processing, exploratory analysis, results synthesis 
