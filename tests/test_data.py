import unittest
from pathlib import Path
import pandas as pd

CSV = Path(__file__).resolve().parents[1] / 'data' / 'adult_income_classification_dataset.csv'

class TestDataset(unittest.TestCase):
    def test_attached_dataset_schema_and_counts(self):
        self.assertTrue(CSV.exists())
        d=pd.read_csv(CSV,skipinitialspace=True)
        self.assertEqual(d.shape,(45222,14))
        self.assertEqual(d['income'].value_counts().to_dict(),{'<=50K':34014,'>50K':11208})
        self.assertEqual(d.isna().sum().sum(),0)

if __name__ == '__main__': unittest.main()
