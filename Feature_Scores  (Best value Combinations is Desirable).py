import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import LabelEncoder

# Load dataset
url = 'database name.csv'
column_names = [
    'age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status', 
    'occupation', 'relationship', 'income'
]
df = pd.read_csv(url, names=column_names, sep=',\s', engine='python')

# Handle missing values, since we used clean datasets so this step can be ommitted.
df.replace(' ?', pd.NA, inplace=True)
df.dropna(inplace=True)


label_encoder = LabelEncoder()
categorical_columns = df.select_dtypes(include=['object']).columns.tolist()
for col in categorical_columns:
    df[col] = label_encoder.fit_transform(df[col])

# Split data
X = df.drop('income', axis=1)
y = df['income']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Define the model basic structure.
rf_model = RandomForestClassifier(random_state=42)

# Set up the parameter grid for tuning/analysis
param_grid = {
    'n_estimators': [50, 100, 200],  # ntree values (first very important paramter)
    'max_features': ['auto', 'sqrt', 'log2'],  # mtry values (max_features in RandomForestClassifier) (second very important paramter)
    'min_samples_split': [2, 5, 10],  # Additional  hyper-parameters
    'min_samples_leaf': [1, 2, 4]
}

# Use GridSearchCV for model tuning
grid_search = GridSearchCV(estimator=rf_model, param_grid=param_grid, 
                           cv=5, n_jobs=-1, verbose=2, scoring='accuracy')

grid_search.fit(X_train, y_train)

# Print the best parameters, and use them in training the model next time.
print(f"Best parameters: {grid_search.best_params_}")

# predictions based on best paramters.
best_rf_model = grid_search.best_estimator_

# Predict and evaluate
y_pred = best_rf_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.4f}')
print('\nClassification Report:\n', classification_report(y_test, y_pred))

# QIDs scores from the best model
feature_importances = pd.Series(best_rf_model.feature_importances_, index=X.columns)
print("\nFeature scores:")
print(feature_importances.sort_values(ascending=False))
