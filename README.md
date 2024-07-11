# IBM Attrition Prediction

## Overview
This project is using a dataset found on kaggle.com. All resources obtained can be found inside the code (e.g. URL).
The purpose of the project is to make IBM employee attrition prediction. Why am I doing this project? In professional settings, such data could serve as a useful insight especially in knowing what factors are affecting the model the most and what we could do regarding these factors. What are the company goals? What demographics of employees do they want to keep or allow a higher turnover cycle? Many of these questions can be simply answered once we know the model that could predict well.

## Steps breakdown
The processes include 3 main steps:
1. Data Mining - grabbing publicly available dataset from kaggle.com and accessing the data
2. Data Processing / Exploration - analyze dataset using statistical methods (boxplots, heatmaps, histograms of different hiring-related variables)
3. Data Transformation & Modeling - make necessary changes in order to create statistical models and make predictions based on these models.
Note: Data visualization is a potential future update for this personal project.

## What analytical methods are used
We are dealing with categorical data types and are not time series data, thus we could use the following statistical methods to generate our models:
- Regression Tree
- Random Forest
- Log Regression
- Support Vector Machine (SVM)
- KNN clustering 

## Metrics explained
Model qualities are then calculated by the following metrics, as the following:
- Accuracy (accuracy_score), refers to the ratio of correctly predicted instances to the total instances. High accuracy means that the model correctly predicts most of the cases. However, we must keep in mind that in the presence of imbalanced dataset, accuracy along can be misleading.
- Precision (precision_score), refers to the ratio of true positive predictions to the sum of true positive + false positive. False positive is a situation where employees are predicted to leave but they end up staying. High precision indicates low false positive rate. This is important to note especially when the cost of false positive is high. An example of this is allocating unnecessary resources such as retention bonuses, training programs, etc., that may lead to increased overall company costs.
- Sensitivity / Recall (recall_score), refers to ratio of true positive predictions to the sum of true positive + false negative. False negative is a situation where employees are predicted to stay but they end up leaving. High sensitivity indicates low false negative rate. This is important to note when the cost of false negative is high. An example of this cost, as common as we may find, is disruption in existing projects, increased hiring and training costs, and loss of organizational knowledge. Some of which may have intangible values.
- F1 (f1_score), refers to the harmonic mean of precision of recall. High F1 score indicates balance between precision and sensitivity, useful when we want the two of them to be balanced.
- F2 (fbeta_score), refers to a weighted average of precision and recall where sensitivity is given more importance (beta = 2). High F2 score indicates model is sensitive to sensitivity, which is useful when we want to prioritize miniming false negative.

## Conclusion
Once you got through the project, you will find the results of the metrics above and sample prediction output comparing results of the actual (from dataset) vs predicted attrition. This means that the model can be effectively used to predict future datasets and it's attrition possibilities, in which then could lead the company to better decision making (e.g. in budget allocations, project timelines and turnovers that may be affected by employee attritions, and many more). Ultimately, this may help the company save costs and/or generate more revenue.

# Thank you for tuning in
