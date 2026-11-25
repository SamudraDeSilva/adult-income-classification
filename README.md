# Adult Income Classification

**Exploratory data analysis, statistical modelling and comparative machine learning using a cleaned Adult Census Income dataset (45,222 observations).**

## Overview

This project investigates whether selected historical census attributes can distinguish between annual-income categories of **≤US$50,000** and **>US$50,000**. The analysis includes numerical and categorical exploration, visualisation, feature engineering, classification, clustering, model optimisation and subgroup diagnostics.

The main notebook, **`Adult Income Classification.ipynb`**, is the centrepiece of the repository and can be executed against the included CSV.

## Repository structure

```text
Adult_Income_Classification/
├── Adult Income Classification.ipynb
├── data/
│   ├── adult_income_classification_dataset.csv
│   └── README.md
├── figures/
│   ├── Income_Class_Distribution.png
│   ├── Numerical_Correlations.png
│   ├── Model_ROC_Curves.png
│   ├── Model_Precision_Recall_Curves.png
│   ├── Model_Precision_Recall_F1.png
│   └── Random_Forest_Feature_Importance.png
├── model_metrics.csv
├── MODEL_CARD.md
├── requirements.txt
├── tests/
│   └── test_data.py
├── VERIFICATION.md
└── .gitignore
```

## Dataset

The analysis uses **45,222 records and 14 columns**. The target distribution is **34,014 observations at `<=50K` (75.2%)** and **11,208 at `>50K` (24.8%)**. The dataset is derived from the UCI Adult/Census Income benchmark; its origin and licensing information are documented in [`data/README.md`](data/README.md).

## Analysis and methods

- Data quality, missing values and class balance
- Numerical distributions, descriptive statistics, category comparisons and correlation analysis
- Leakage-aware preprocessing and group-aware train/test partitioning
- Logistic Regression, Random Forest, Gaussian Naive Bayes, neural network (MLP), Gradient Boosting and a majority-class baseline
- Accuracy, balanced accuracy, precision, recall, F1, ROC-AUC and PR-AUC
- ROC and precision–recall curves, confusion matrices and model importance
- Exploratory K-Means clustering and training-only hyperparameter optimisation
- Error analysis, subgroup diagnostics, conclusions and future objectives

## Results

| Model | Accuracy | Precision | Recall | F1 | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| **Gradient Boosting** | **0.871** | **0.784** | **0.645** | **0.708** | **0.930** |
| Random Forest | 0.862 | 0.776 | 0.603 | 0.679 | 0.921 |
| Neural Network (MLP) | 0.854 | 0.744 | 0.602 | 0.665 | 0.913 |
| Logistic Regression | 0.850 | 0.736 | 0.593 | 0.657 | 0.908 |
| Gaussian Naive Bayes | 0.627 | 0.388 | 0.944 | 0.550 | 0.863 |
| Majority-class baseline | 0.758 | 0.000 | 0.000 | 0.000 | 0.500 |

**Gradient Boosting achieved the highest observed held-out F1-score** in this comparison (0.708). It also achieved an ROC-AUC of 0.930. However, its recall of 0.645 indicates that a meaningful share of the higher-income class was missed. Gaussian Naive Bayes showed the opposing trade-off: considerably higher recall but substantially lower precision. The results should be interpreted across multiple metrics rather than accuracy alone.

Full values, including balanced accuracy and PR-AUC, are available in [`model_metrics.csv`](model_metrics.csv) and [`MODEL_CARD.md`](MODEL_CARD.md).

## Reproduce the analysis

```bash
python -m venv .venv
# Activate your virtual environment, then install dependencies
pip install -r requirements.txt
jupyter notebook "Adult Income Classification.ipynb"
```

Open the notebook and select **Run All**. The data path is resolved relative to the notebook or repository directory. To validate the dataset file, run:

```bash
python -m unittest discover -s tests -v
```

## Conclusion

The analysis demonstrates an end-to-end process for assessing structured census data, exploring income-associated patterns and comparing predictive classifiers. Gradient Boosting performed best by held-out F1-score, but performance depends on the selected metric, the sample and the evaluation design. The results are best understood as evidence of sound analytical practice rather than as a ready-to-deploy income decision system.

## Future objectives

Priorities include stronger external and cross-validated evaluation, class-sensitive threshold analysis, advanced classification methods, explainable AI, fairness auditing, detailed error analysis and research-quality communication of uncertainty and limitations.

## Limitations and responsible use

The data describe a historical population and a nominal US$50,000 income threshold. Observed relationships are not necessarily causal. Class imbalance, possible social biases, proxy variables and the use of one held-out test set limit generalisation. **Do not use the project to make hiring, lending, welfare or other consequential decisions about individuals.**

## License and Citation

### Licence

The original source code and analytical implementation developed for this project are available under the [MIT licence](LICENSE), permitting reuse, modification and distribution in accordance with its terms. Third-party datasets remain subject to their respective licensing conditions.

### Citation

This research project was developed by Samudra Nimesh De Silva. Researchers and practitioners referencing this work are encouraged to cite the repository using the information provided in [CITATION.cff](CITATION.cff).
