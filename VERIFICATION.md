# Project verification

This document records the checks performed on the release package.

- Main notebook: `Adult Income Classification.ipynb`
- Dataset: `data/adult_income_classification_dataset.csv`
- Dataset dimensions: **45,222 observations × 14 columns**
- Target counts: **34,014 `<=50K`** and **11,208 `>50K`**
- Notebook markdown, code and saved outputs reference the included dataset.
- Notebook JSON and code-cell syntax validated.
- Dataset integrity test: `python -m unittest discover -s tests -v`
- Model comparison values in the notebook, README and model card agree with `model_metrics.csv`.

The reported model results were generated in the executed notebook. The current editing pass modified narrative markdown and repository documentation, without changing model code, data or cached numeric results.
