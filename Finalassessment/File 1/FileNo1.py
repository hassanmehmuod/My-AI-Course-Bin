import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

df = pd.read_csv('D:\\Work\\Github\\My-AI-Course-Bin\\Finalassessment\\File 1\\heart_disease_cleveland.csv')
df.head()
df.info()
print(df.describe())
print(df.isnull().sum())
print(df['target'].value_counts())

df['ca']= df['ca'].fillna(df['ca'].median())
df['thal']= df['thal'].fillna(df['thal'].median())

print(df.isnull().sum())

#Target distribution
plt.figure(figsize=(6,4))
sns.countplot(x='target', data=df)
plt.title('Distribution of Heart Disease (0 = No Disease, 1 = Disease)')
plt.show()

#Correlation heatmap
plt.figure(figsize=(12,8))
sns.heatmap(df.corr(), annot=True, fmt='.2f', cmap='coolwarm')
plt.title('Feature Correlation Heatmap')
plt.show()

#Age distribution by target
plt.figure(figsize=(8,5))
sns.histplot(data=df, x='age', hue='target', kde=True, multiple='stack')
plt.title('Age Distribution by Heart Disease Status')
plt.show()

#Chest pain type vs target
plt.figure(figsize=(7,5))
sns.countplot(x='cp', hue='target', data=df)
plt.title('Chest Pain Type vs Heart Disease')
plt.show()

#Boxplot - cholesterol by target 
plt.figure(figsize=(6,5))
sns.boxplot(x='target', y='chol', data=df)
plt.title('Cholesterol Levels by Heart Disease Status')
plt.show()

#Pairplot for key numeric features
sns.pairplot(df[['age','trestbps','chol','thalach','oldpeak','target']], hue='target')
plt.show()

X = df.drop('target', axis=1)
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("Train shape:", X_train.shape)
print("Test shape:", X_test.shape)

models = {
    'Logistic Regression': LogisticRegression(max_iter=1000),
    'Decision Tree': DecisionTreeClassifier(random_state=42),
    'Random Forest': RandomForestClassifier(random_state=42),
    'SVM': SVC(),
    'KNN': KNeighborsClassifier()
}

results = {}

for name, model in models.items():
    # Logistic Regression, SVM, and KNN benefit from scaled data
    if name in ['Logistic Regression', 'SVM', 'KNN']:
        model.fit(X_train_scaled, y_train)
        y_pred = model.predict(X_test_scaled)
    else:
        # Tree-based models don't need scaling
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
    
    acc = accuracy_score(y_test, y_pred)
    results[name] = acc
    
    
    print(f"Model: {name}")
    print(f"Accuracy: {acc:.4f}")
    print(classification_report(y_test, y_pred))

best_model = models['Random Forest']
y_pred_best = best_model.predict(X_test)

cm = confusion_matrix(y_test, y_pred_best)

plt.figure(figsize=(6,5))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=['No Disease', 'Disease'],
            yticklabels=['No Disease', 'Disease'])
plt.title('Confusion Matrix - Random Forest')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()

plt.figure(figsize=(8,5))
sns.barplot(x=list(results.keys()), y=list(results.values()))
plt.title('Model Accuracy Comparison')
plt.ylabel('Accuracy')
plt.ylim(0, 1)
plt.xticks(rotation=30)
plt.show()


importances = pd.Series(best_model.feature_importances_, index=X.columns)
importances = importances.sort_values(ascending=False)

plt.figure(figsize=(8,5))
sns.barplot(x=importances.values, y=importances.index)
plt.title('Feature Importance - Random Forest')
plt.xlabel('Importance')
plt.show()

print(importances)
print("I chose Random Forest as my final model because it had the highest accuracy (88.5%) and performed more consistently than the other models. A single Decision Tree only got 73.8% accuracy, but Random Forest — which combines many decision trees together — improved a lot on that, showing how combining models (ensemble learning) gives better results than using just one. KNN got the same accuracy (88.5%), but its results were less balanced — it was very good at detecting healthy patients but missed more actual disease cases, so Random Forest is the more reliable choice. Looking at feature importance, the four factors that mattered most for predicting heart disease were: maximum heart rate (thalach), chest pain type (cp), thalassemia test result (thal), and number of major vessels blocked (ca). These make sense medically, since they're all common indicators doctors use. One limitation of this analysis is that the dataset only has 303 patients, all from one hospital (Cleveland), so the model might not work as well on patients from other hospitals or regions.")