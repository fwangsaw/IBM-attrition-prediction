from DataMining import df_new, df
from sklearn.preprocessing import LabelEncoder
import seaborn as sns
import matplotlib.pyplot as plt


# -------- Data Transformation --------- #
print(df_new.info())
print(df_new['Over18'].value_counts())
df_new.drop(columns=['Over18'], inplace=True)  # Remove age since all are above 18

# Change attrition to integer
df_new['Attrition'] = df_new['Attrition'].astype('int64')

# Replace BusinessTravel & Department into numbers/integer
print(df_new['BusinessTravel'].value_counts())
print(df_new['Department'].value_counts())
df_new['BusinessTravel'] = df_new['BusinessTravel'].replace({'Travel_Rarely': 0, 'Travel_Frequently': 1, 'Non-Travel': 3})
df_new['BusinessTravel'] = df_new['BusinessTravel'].astype('int64')
df_new['Department'] = df_new['Department'].replace({'Research & Development': 0, 'Sales': 1, 'Human Resources': 3})
df_new['Department'] = df_new['Department'].astype('int64')

# Using encoder and fit_transform from sklearn to automatically change variables into integer
# Categorical variables and those without specific orders won't need to be manually replaced as above
# Changes are based on findings from data exploration, using variables we found conclusions from
print(df_new['EducationField'].value_counts())  # Check
df_new['EducationField'] = LabelEncoder().fit_transform(df_new['EducationField'])
df_new['Gender'] = LabelEncoder().fit_transform(df_new['Gender'])
df_new['JobRole'] = LabelEncoder().fit_transform(df_new['JobRole'])
df_new['MaritalStatus'] = LabelEncoder().fit_transform(df_new['MaritalStatus'])
df_new['OverTime'] = LabelEncoder().fit_transform(df_new['OverTime'])
df_new.info()
# All variables needed should now be integer form

# Heatmap to show relationship of correlation among variables
plt.figure(figsize=(12, 8))
sns.heatmap(df_new.corr())  # brighter = positive corr, darker = negative corr
plt.show()
