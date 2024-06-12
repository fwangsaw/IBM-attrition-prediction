import pandas as pd
import opendatasets as od
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import seaborn as sns
import os
# Guide obtained from:
# https://ravi-chan.medium.com/how-to-download-any-data-set-from-kaggle-7e2adc152d7f


# -------- Data Mining = Using opendatasets --------- #
# Assign the kaggle dataset URL into variable
dataset = 'https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset/data'

# Using opendatasets to download data
# Requires API token from kaggle.com, need to login to kaggle.com and go to account settings
od.download(dataset)
data_dir = './ibm-hr-analytics-attrition-dataset'

# Checking if data direction exists
if os.path.exists(data_dir):
    for root, dirs, files in os.walk(data_dir):
        print(f'Found directory: {root}')
        for file in files:
            print(f'\t{file}')
else:
    print(f'Directory {data_dir} does not exist')
os.listdir(data_dir)  # Somehow not returning list of files in the folder???


# -------- Access Data --------- #
# Combine file path name to make a complete location/dir name
csv_file_path = os.path.join(data_dir, 'WA_Fn-UseC_-HR-Employee-Attrition.csv')
df = pd.read_csv(csv_file_path)
# check if file has been assigned properly
print(df.head(10))
df.info()

# Checking data column "EmployeeCount"
print("Checking data in column 'EmployeeCount':")
print(df.EmployeeCount.value_counts())
# We confirm that the value of column "EmployeeCount" is only 1, we can remove
df.drop(columns=['EmployeeCount', 'EmployeeNumber'], inplace=True)
# Replace Attrition column into numerical type
df['Attrition'] = df['Attrition'].replace({'Yes': 1, 'No': 0})
# Checking if there's any duplicated values in the dataset
print("Checking if any duplicated values: " + str(df.duplicated().sum()))
# Checking if there's any null values in the dataset
print("Checking if any null values: " + "\n" + str(df.isna().sum()))
print(df.head(10))


# -------- Data Cleaning = Using boxplot --------- #
def generate_boxplot_report(df, output_filename='Boxplot_report.pdf'):
    with PdfPages('Boxplot_report.pdf') as pdf:
        # Creating loop for boxplot of each variable / column header
        for column in df.select_dtypes(include='number').columns:
            plt.figure(figsize=(10, 6))
            sns.boxplot(y=df[column])
            plt.title(f'Box plot for {column}')
            pdf.savefig()  # Save the current figure to the PDF
            plt.close()  # Close the figure
    print(f"Report saved as '{output_filename}'")


def remove_outliers(dff):
    for col in dff.select_dtypes(include='number').columns:
        q1 = dff[col].quantile(0.25)
        q3 = dff[col].quantile(0.75)
        iqr = q3 - q1
        lower_bound = q1 - 2 * iqr
        upper_bound = q3 + 2 * iqr
        dff = dff[(dff[col] >= lower_bound) | (dff['Attrition'] == 1)]
        dff = dff[(dff[col] <= upper_bound) | (dff['Attrition'] == 1)]
    return dff


# Generating boxplot PDF after removing outliers
df_new = remove_outliers(df)  # Remove outliers using IQR method via function
generate_boxplot_report(df_new)  # Create boxplot report
