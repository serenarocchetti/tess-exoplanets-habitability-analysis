# Statistical Analysis of Exoplanet Habitability (TESS Mission)
### A Machine Learning Approach Using the ExoFOP-TESS Catalog


## 📌 Project Overview

This project is part of a Bachelor's thesis in *Statistics and Big Data* (Universitas Mercatorum).

The goal is to analyze and classify the habitability potential of exoplanets discovered by NASA’s TESS mission using statistical methods and machine learning.

The study is based on real astrophysical data from the **ExoFOP-TESS catalog**.


## 🎯 Objectives

- Analyze physical and orbital properties of exoplanets
- Compute key habitability-related astrophysical metrics
- Apply machine learning for planetary classification
- Evaluate model performance using statistical validation techniques


## 🛠️ Data Science & Technical Skills

### 📊 Data Preparation
- Data cleaning and missing value imputation
- Feature engineering from raw astrophysical signals

### 🌍 Astrophysical Feature Engineering
- **Equilibrium Temperature (Tₑq)** — thermal balance modeling
- **Transmission Spectroscopy Metric (TSM)** — atmospheric characterization potential
- **Emission Spectroscopy Metric (ESM)** — thermal emission detectability
- **Mean Density (ρ)** — derived from mass-radius relationships


## 🤖 Machine Learning Model

- Logistic Regression classifier
- Probability estimation of planetary habitability
- Feature-based classification pipeline


## 📈 Model Evaluation

- ROC Curve analysis
- AUC (Area Under the Curve) metric
- Performance assessment for classification separability


## 🪐 Planet Classification (by Density)

- **Super-Earth / Iron-rich** → ρ > 5.5 g/cm³  
- **Rocky planets** → 4.0 – 5.5 g/cm³  
- **Ocean / Hybrid worlds** → 2.0 – 4.0 g/cm³  
- **Gas giants** → ρ < 2.0 g/cm³  


## 📁 Repository Structure

- `regressione_logistica.py` → main ML pipeline (data processing + model training)
- `README.md` → project documentation


## 📊 Key Insight

Machine learning techniques applied to astrophysical datasets enable efficient filtering of exoplanet candidates, supporting future observational prioritization for missions such as **JWST (James Webb Space Telescope)**.


## 🚀 Author

Bachelor’s Degree in Statistics & Big Data  
Focus: Data Science, Statistical Modeling, Astrophysical Data Analysis
