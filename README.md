# climate-migration-project

## Overview

This project uses machine learning to predict **climate-induced migration outflows** in Somalia. It integrates data from **GDELT (news coverage), IOM/DTM (displacement tracking), weather sources, and development indicators** to build a region-month level dataset. The aim is to identify regional "hotspots"—areas likely to generate out-migration in response to environmental and human security stressors.

---

## Objective

The goal is to predict **migration outflows** from regions in Somalia, by:
- Aggregating multi-source data (climate, news (from GDELT), displacement, vulnerability)
- Creating a region-month panel dataset
- Constructing vulnerability indices
- Comparing the predictive value of news vs. real-world weather
- Evaluating ML model performance and generalizability

---

## Target Variable

- `migration_outflows`: Number of people leaving a region per month (main prediction target)

---

## Feature Set

| Feature                          | Description |
|----------------------------------|-------------|
| `region_id`, `region_name`       | Standardized administrative region or district |
| `month`                          | Time period (monthly, e.g. 2023-04) |
| `gdelt_article_count`            | GDELT article count |
| `gdelt_tone_avg`                 | Avg sentiment tone score |
| `gdelt_conflict_mentions`        | Number of articles mentioning conflict keywords |
| `gdelt_env_mentions`             | Number of articles mentioning environmental keywords |
| `weather_rainfall_mm`           | Monthly rainfall (optional for validation) |
| `human_vulnerability_index`      | Composite human security vulnerability index |
| `environmental_vulnerability_index` | Composite environmental vulnerability index |
| `population`                     | Regional population |
| `urban_rural`                    | Urban/Rural label |
| `infrastructure_score`           | Infrastructure access score |
| `region_type`                    | General location tag (North, South, etc.) |

---

## Source Datasets

### 1. **Mobility & Displacement (IOM/DTM)**
| File | Description |
|------|-------------|
| `iom_dtm_somalia_baseline2_round1_31012022_hdx.xlsx` | Baseline regional displacement |
| `mobility-tracking-b2-public-use.csv` | Historical flows data |
| `dtm_som_baseline_assessment_r2_sws_jl_hs_2023_0-1.csv` | Household-level vulnerability |
| `somalia-baseline-assessment-dataset_-round-3-february-september-2024_hdx.csv` | Neighbourhood-level data |
| `somalia_mobility_iom_2024.xlsx` | Newest inflow/outflow figures |
| `somalia_mobility_iom_2025.xlsx` | Latest projections for 2025 |

### 2. **GDELT Climate & Conflict News**
| File | Description |
|------|-------------|
| `gdelt_somalia_events.csv` | Monthly GDELT articles with location, tone, keywords |
| `gdelt_keywords_dict.json` | Dictionary of keywords for climate/conflict categories |

### 3. **Demographics / Socio-Economic (World Bank, IOM)**
| File | Description |
|------|-------------|
| `worldbank_population_by_district.csv` | Population estimates |
| `iom_socioeconomic_indicators.csv` | Education, literacy, poverty rates |
| `worldbank_access_to_services.csv` | Health, water, electricity access |

### 4. **Governance & Infrastructure**
| File | Description |
|------|-------------|
| `vdem_local_governance.csv` | Local governance indicators |
| `infrastructure_score_by_region.csv` | Road, market, and electricity coverage |

### 5. **Weather Data**
| File | Description |
|------|-------------|
| `chirps_monthly_rainfall.csv` | Monthly rainfall data (validation) |

---

## Dataset Granularity

- **Time**: Monthly (e.g., 2022-01, 2022-02, ...)
- **Location**: Administrative region or district level (we can alternatively make a larger district)

---

## Folder Structure

```
📂 data/
   ├── raw/                         # All original source files
   ├── processed/                   # Cleaned/aggregated regional monthly files
   ├── indices/                     # Constructed indices for vulnerability
   └── final_panel/                 # Final dataset used for modeling

📂 notebooks/
   ├── 01_dtm_cleaning.ipynb
   ├── 02_gdelt_processing.ipynb
   ├── 03_build_indices.ipynb
   ├── 04_model_training.ipynb
   └── 05_evaluation.ipynb

📂 models/
   └── trained_models/

README.md
requirements.txt
```


---

## Notes

- **Migration outflows** are prioritized to identify climate hotspots.
- **Regional Vulnerability Index** is built from **multiple separate CSVs**, including:
  - Demographics (IOM, World Bank)
  - Infrastructure
  - Political governance (V-Dem)
  - Socioeconomic indicators
- Each of these is cleaned and merged during feature engineering.

---
