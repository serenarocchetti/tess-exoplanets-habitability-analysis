# Statistical Analysis of Exoplanet Habitability (TESS Mission)
### A Machine Learning Approach Using the ExoFOP-TESS Catalog

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-blue.svg)](https://scikit-learn.org/)
[![Statsmodels](https://img.shields.io/badge/Statistical%20Modeling-Statsmodels-red.svg)](https://www.statsmodels.org/)

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


## 🤖 Analytical Model

- Logistic Regression used as a statistical classification tool
- Feature-based analysis of planetary characteristics
- Exploration of relationships between physical variables and habitability indicators


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


## 📊 Key Impact

- Analyzed exoplanet populations using statistical indicators
- Developed a reproducible data analysis pipeline for astrophysical datasets
- Supported prioritization of exoplanet candidates for further scientific investigation

## 🚀 Author

Bachelor’s Degree in Statistics & Big Data  
Focus: Data Science, Statistical Modeling, Astrophysical Data Analysis


## ▶️ How to run

```bash
pip install -r requirements.txt
python regressione_logistica.py
