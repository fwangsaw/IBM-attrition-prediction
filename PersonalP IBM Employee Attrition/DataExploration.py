from DataMining import df_new, df
import seaborn as sns
import matplotlib.pyplot as plt


# Print all column names
for i in range(len(df.columns)):
    print(df.columns[i])

# These are variables/data I believe are important to explore
# Age count
plt.figure(figsize=(10, 6))
sns.histplot(df_new['Age'], kde=True,)
plt.title('Histogram and Kde plot of Age')
plt.show()
# Result shows somewhat normality, with a bit of right skewness

# Gender histogram & group with attrition count
df_new['Gender'].value_counts().plot(kind='bar')
plt.show()  # More male staff in the dataset
df_new.groupby('Gender').Attrition.value_counts().plot(kind='bar')
plt.show()  # Also more male staff in both attrition attribute

# Age vs monthly income
plt.figure(figsize=(10, 6))
sns.regplot(x=df_new['Age'], y=df_new['MonthlyIncome'])
plt.show()  # Steady increase overall but cannot assume linearity

# Job role vs attrition count
(df_new.groupby('JobRole').Attrition.value_counts().
 sort_values(ascending=False).plot(kind='bar'))
plt.show()  # Can't draw definite conclusion, may need to do ratio between attrition for each job role

# Job satisfaction vs attrition count
(df_new.groupby('JobSatisfaction').Attrition.value_counts().
 sort_values(ascending=False).plot(kind='bar'))
plt.show()  # Higher satisfaction tends to show no attrition.
# Among attrition, 3 and 1 satisfaction point show most attrition.

# Marital status vs attrition count
df_new.groupby('Attrition').MaritalStatus.value_counts().plot(kind='bar')
plt.show()  # Married people tend to show less attrition, while single people tend to show higher attrition

# Environment satisfaction vs attrition count
(df_new.groupby('EnvironmentSatisfaction').Attrition.value_counts().
 sort_values(ascending=False).plot(kind='bar'))
plt.show()  # May not contribute as much, as different level of satisfaction show similar amount of attrition

# Year since last promotion vs attrition count
df_new.groupby('YearsSinceLastPromotion').Attrition.value_counts().plot(kind='bar')
plt.show()  # Lower year of last promotion tend to show attrition, as well as long year
# (above 5 years, starting to rise up)

# Number of companies worked (mean) vs attrition
df_new.groupby('Attrition')['NumCompaniesWorked'].mean().plot(kind='bar')
plt.show()  # People who tend to have worked in more places also tend to leave the company

# Work-life balance vs attrition
(df_new.groupby('WorkLifeBalance').Attrition.value_counts().
 sort_values(ascending=False).plot(kind='bar'))
plt.show()  # higher work-life balance tend to show no attrition,
# but also satisfaction point 3 show attrition as highest
# Maybe because one may be looking for something more challenging

# Age (mean) vs attrition count
df_new.groupby('Attrition')['Age'].mean().plot(kind='bar')
plt.show()  # Age mean are closely related maybe due to age range and quantity. Can't tell any conclusion other than
# no attrition have higher age mean -> Older people are less prone to leave the company, while younger ones do

# Overtime count vs attrition count
df_new.groupby('OverTime').Attrition.value_counts().plot(kind='bar')
plt.show()  # No overtime exhibit most reason to stay, but overtime and attrition is the 2nd lowest number.

# Business travel vs attrition count
df_new.groupby('BusinessTravel').Attrition.value_counts().plot(kind='bar')
plt.show()  # Lower number of travel seem to exhibit less attrition, maybe related to work-life balance?
