# 02_data_sources_identification.py

import pandas as pd
import requests
import datetime
import os

# Create data directories if they don't exist
os.makedirs("data/climate", exist_ok=True)
os.makedirs("data/environmental", exist_ok=True)
os.makedirs("data/socioeconomic", exist_ok=True)
os.makedirs("data/migration", exist_ok=True)

# Current date for reference
current_date = datetime.datetime.now().strftime("%Y-%m-%d")

# Dictionary of data sources with their metadata
data_sources = {
    # CLIMATE DATA
    "chirps_rainfall": {
        "category": "climate",
        "description": "CHIRPS rainfall data for Somalia (1981-present)",
        "url": "https://data.chc.ucsb.edu/products/CHIRPS-2.0/",
        "time_range": "1981-present",
        "spatial_resolution": "0.05 degrees",
        "temporal_resolution": "daily/monthly",
        "api_available": True,
        "download_method": "ftp/http",
        "notes": "Precipitation data with long historical record"
    },
    
    "spei_drought_index": {
        "category": "climate",
        "description": "Standardized Precipitation-Evapotranspiration Index",
        "url": "https://spei.csic.es/database.html",
        "time_range": "1950-present",
        "spatial_resolution": "0.5 degrees",
        "temporal_resolution": "monthly",
        "api_available": True,
        "download_method": "http",
        "notes": "Drought index accounting for both precipitation and temperature effects"
    },
    
    # ENVIRONMENTAL DATA
    "modis_ndvi": {
        "category": "environmental",
        "description": "MODIS Vegetation Index Products (NDVI)",
        "url": "https://lpdaac.usgs.gov/products/mod13q1v006/",
        "time_range": "2000-present",
        "spatial_resolution": "250m",
        "temporal_resolution": "16-day",
        "api_available": True,
        "download_method": "api",
        "notes": "Vegetation health indicator, proxy for agricultural conditions"
    },
    
    "fao_crop_production": {
        "category": "environmental",
        "description": "FAO crop production statistics for Somalia",
        "url": "http://www.fao.org/faostat/en/#data/QC",
        "time_range": "1961-present",
        "spatial_resolution": "national/subnational",
        "temporal_resolution": "annual",
        "api_available": True,
        "download_method": "api/csv",
        "notes": "Crop yield data indicating agricultural performance"
    },
    
    # SOCIOECONOMIC DATA
    "fews_net": {
        "category": "socioeconomic",
        "description": "Famine Early Warning Systems Network - Food Security Classification",
        "url": "https://fews.net/east-africa/somalia",
        "time_range": "~2000-present",
        "spatial_resolution": "admin regions",
        "temporal_resolution": "quarterly",
        "api_available": False,
        "download_method": "manual/scrape",
        "notes": "Historical food security assessments and forecasts"
    },
    
    "wfp_food_prices": {
        "category": "socioeconomic",
        "description": "World Food Programme - Food Prices Database",
        "url": "https://data.humdata.org/dataset/wfp-food-prices",
        "time_range": "~2000-present",
        "spatial_resolution": "market locations",
        "temporal_resolution": "monthly",
        "api_available": True,
        "download_method": "api/csv",
        "notes": "Food price data as indicator of economic stress"
    },
    
    # MIGRATION DATA
    "unhcr_displacement": {
        "category": "migration",
        "description": "UNHCR Somalia Internal Displacement",
        "url": "https://data.unhcr.org/en/situations/horn",
        "time_range": "varies",
        "spatial_resolution": "admin regions",
        "temporal_resolution": "monthly",
        "api_available": True,
        "download_method": "api/csv",
        "notes": "Historical displacement patterns and numbers"
    },
    
    "iom_dtm": {
        "category": "migration",
        "description": "IOM Displacement Tracking Matrix",