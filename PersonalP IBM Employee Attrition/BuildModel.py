from DataTransform import df_new
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, fbeta_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB


# Our goal is to make prediction on attrition
# Scale all dataset df_new
df_new[df_new.columns] = MinMaxScaler().fit_transform(df_new[df_new.columns])
print(df_new.head())

X = df_new.drop('Attrition', axis=1)  # Create feature matrix X
y = df_new['Attrition']  # Create response variable
y = LabelEncoder().fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=50)
# We are dealing with binary, we use classification methods
classifiers = {
    "Decision Tree": DecisionTreeClassifier(),
    "Random Forest": RandomForestClassifier(),
    "Logistic Regression": LogisticRegression(),
    "SVM": SVC(),
    "KNN": KNeighborsClassifier()
}

for classify_name, classify in classifiers.items():
    classify.fit(X_train, y_train)
    y_prediction = classify.predict(X_test)
    model_acc = accuracy_score(y_test, y_prediction)
    model_precision = precision_score(y_test, y_prediction)
    model_sensitivity = recall_score(y_test, y_prediction)
    model_F1 = f1_score(y_test, y_prediction)
    model_F2 = fbeta_score(y_test, y_prediction, beta=2)
    print(f"Classifier method: {classify_name}")
    print(f"Model Accuracy: {model_acc: .2f}")
    print(f"Model Precision: {model_precision: .2f}")
    print(f"Model Sensitivity: {model_sensitivity: .2f}")
    print(f"Model F1 score: {model_F1: .2f}")
    print(f"Model F2 score: {model_F2: .2f}")
    # print few sample predictions
    print("Sample prediction comparison:")
    for i in range(5):
        print(f"Actual: {y_test[i]}, Predicted: {y_prediction[i]}")
    print("--------------------------------------------------")

