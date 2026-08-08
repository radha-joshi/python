import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split

# 1. Generate synthetic data
np.random.seed(0)
n = 500
class0 = np.random.multivariate_normal([30, 60], [[30, 5], [5, 100]], n)
class1 = np.random.multivariate_normal([45, 90], [[30, 5], [5, 100]], n)

X = np.vstack((class0, class1))
y = np.hstack((np.zeros(n), np.ones(n)))

# 2. Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# 3. Train logistic regression
model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

# 4. Evaluate performance
acc = accuracy_score(y_test, y_pred)
prec = precision_score(y_test, y_pred)
rec = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print("=== Logistic Regression Performance ===")
print(f"Accuracy:  {acc:.3f}")
print(f"Precision: {prec:.3f}")
print(f"Recall:    {rec:.3f}")
print(f"F1-Score:  {f1:.3f}")