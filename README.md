# Phishing URL Detector

A supervised machine learning model that classifies URLs as safe or phishing using logistic regression and character-level TF-IDF features.

## Overview

This project demonstrates AI-assisted threat detection by combining URL structural analysis with text-based feature extraction. The model uses a dual-feature pipeline: manual URL heuristics (length, special characters, suspicious keywords) and character n-gram TF-IDF vectors from the raw URL string.

## Features

•⁠  ⁠Character-level TF-IDF vectorization (3-5 grams)
•⁠  ⁠Manual feature extraction: URL length, domain length, dot/hyphen/digit counts, HTTPS presence, and keyword flags (login, verify, security, free, password)
•⁠  ⁠ColumnTransformer pipeline combining both feature sets
•⁠  ⁠Logistic regression classifier with probability outputs

## Requirements

•⁠  ⁠Python 3.8+
•⁠  ⁠pandas
•⁠  ⁠scikit-learn

Install dependencies:

⁠ bash
pip install pandas scikit-learn
 ⁠

## Usage

⁠ python
from phishing_detector import model, extract_url_features
import pandas as pd

test_url = "https://example.com"
test_df = pd.DataFrame([extract_url_features(test_url)])
test_df["url"] = [test_url]

prediction = model.predict(test_df)
probability = model.predict_proba(test_df)

print(f"Prediction: {prediction[0]}")
print(f"Confidence: {probability[0]}")
 ⁠

## Dataset

The current model is trained on a small demonstration dataset of 10 URLs (4 safe, 6 phishing). This is intentionally minimal for learning purposes.
