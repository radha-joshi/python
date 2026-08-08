import pandas as pd
from sklearn.datasets import load_iris

# 1. Load Iris dataset as a pandas DataFrame
iris = load_iris(as_frame=True)
df = iris.frame  # Automatically includes both features and target
df.rename(columns={'target': 'species'}, inplace=True)

# (Optional) Map species numbers to actual names for readability
# df['species'] = pd.Categorical.from_codes(df['species'], iris.target_names)

# 2. Display first few rows
print("=== First 5 rows ===")
print(df.head(), "\n")

# 3. DataFrame summary: shape, column types, and non-null counts
print("=== Dataset Info ===")
df.info()
print() # Added an empty print() for spacing instead of "\n"

# 4. Check for missing values in each column
print("=== Missing Values per Column ===")
print(df.isnull().sum(), "\n")

# 5. Basic statistics (only numerical features)
print("=== Descriptive Statistics ===")
print(df.describe(), "\n")

# 6. Species value counts
print("=== Species Counts ===")
print(df['species'].value_counts())