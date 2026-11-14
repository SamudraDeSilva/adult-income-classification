# Model Card — Adult Income Classification

## Purpose

Educational comparative classification of whether an annual-income label is above US$50,000 in historical U.S. census-derived data. **Not for hiring, credit, welfare, or any consequential decisions about individuals.**

## Data and evaluation

- Input: 45,222 cleaned observations, 14 columns.
- Target: `income`, labels `<=50K` and `>50K`.
- Split: 36,061 training observations and 9,161 held out using `GroupShuffleSplit`, preventing identical predictor rows from crossing sets.
- Preprocessing: training-only median numeric imputation/scaling and categorical one-hot encoding.
- `race`, `sex`, `education_level` excluded from model features; the first two retained for descriptive error-rate checks. Proxy discrimination remains possible.
- The base model suite uses a fixed default classification threshold (0.5). The hyperparameter exercise is a separately tuned Logistic Regression using training-only group CV.

## Held-out performance

| Model                   |   Accuracy |   Balanced_Accuracy |   Precision |   Recall |    F1 |   ROC_AUC |   PR_AUC |
|:------------------------|-----------:|--------------------:|------------:|---------:|------:|----------:|---------:|
| Gradient Boosting       |      0.871 |               0.794 |       0.784 |    0.645 | 0.708 |     0.93  |    0.829 |
| Random Forest           |      0.862 |               0.774 |       0.776 |    0.603 | 0.679 |     0.921 |    0.807 |
| Neural Network (MLP)    |      0.854 |               0.768 |       0.744 |    0.602 | 0.665 |     0.913 |    0.779 |
| Logistic Regression     |      0.85  |               0.763 |       0.736 |    0.593 | 0.657 |     0.908 |    0.768 |
| Gaussian Naive Bayes    |      0.627 |               0.735 |       0.388 |    0.944 | 0.55  |     0.863 |    0.637 |
| Majority-class baseline |      0.758 |               0.5   |       0     |    0     | 0     |     0.5   |    0.242 |

The best F1 model in this comparison is **Gradient Boosting**, with held-out accuracy **0.871**, F1 **0.708**, recall **0.645**, ROC-AUC **0.930** and PR-AUC **0.829**. The reported metrics are computed from the included dataset using the documented evaluation procedure.

## Limitations

- Historic sample and non-inflation-adjusted threshold.
- Unequal class sizes; positive-class recall is materially lower than overall accuracy.
- Repeated model comparison on one held-out set can cause selection bias; external validation is absent.
- Clustering results are descriptive, not income predictions.
- The dataset may reflect inequities, even after excluding explicit demographic inputs; subgroup error reports require cautious interpretation.
- Model performance cannot be generalized to present-day incomes or applications without independent validation.

