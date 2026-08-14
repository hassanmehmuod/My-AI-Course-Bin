Task 1: Heart Disease Classification

Dataset
Heart Disease Cleveland dataset (UCI) — 303 patients, 14 clinical features, binary target (0 = no disease, 1 = disease).

Objective
Predict presence of heart disease using classification and ensemble learning techniques.

Steps
- Loaded data and performed descriptive statistics (`.info()`, `.describe()`, null checks)
- Handled missing values in `ca` and `thal` using median imputation (preserves data, avoids invalid category values)
- Performed EDA using Seaborn: target distribution, correlation heatmap, age distribution, chest pain type, cholesterol by target, pairplot
- Split data 80/20 (stratified), scaled features for distance-based models
- Trained 5 models: Logistic Regression, Decision Tree, Random Forest, SVM, KNN
- Evaluated using accuracy, classification report, confusion matrix, feature importance

Results
Random Forest achieved the best overall performance (88.5% accuracy), chosen as the final model for its balanced precision/recall and because it satisfies the ensemble learning requirement. Top predictive features: maximum heart rate (thalach), chest pain type (cp), thalassemia result (thal), and number of major vessels (ca).

Limitation
Dataset is limited to 303 patients from a single institution (Cleveland), so results may not generalize to broader populations.