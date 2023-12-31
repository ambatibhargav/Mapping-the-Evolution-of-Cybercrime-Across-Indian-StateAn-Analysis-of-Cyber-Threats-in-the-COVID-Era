# -*- coding: utf-8 -*-
"""Final Project CU

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kXTqCNPMJOvpaTQMV6-oEnq4AyiZCT-g

#**Mapping the Evolution of Cybercrime Across Indian States and Union Territories:**
An Analysis of Cyber Threats in the COVID Era

## **Installing and Importing the Libraries**
"""

pip install tabula-py

pip install PyPDF2

"""## **Scrapping the data from PDF**"""

import tabula
import PyPDF2
import pandas as pd

# Function to extract text from a PDF
def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    return text

# Function to extract tables from a PDF in the specified page range
def extract_tables_from_pdf(pdf_path, start_page, end_page):
    pdf_text = extract_text_from_pdf(pdf_path)
    tables = tabula.read_pdf(pdf_path, pages=f'{start_page}-{end_page}', multiple_tables=True)
    return tables

# PDF file path
pdf_path = "Cyber.pdf"
# Page range to extract tables from
start_page = 332
end_page = 342

# Extract tables from the specified page range
tables = extract_tables_from_pdf(pdf_path, start_page, end_page)

# Convert the tables to Pandas DataFrames
dataframes = [pd.DataFrame(table) for table in tables]

# You can now access and work with the extracted tables as DataFrames, for example:
# dataframes[0] is the first table, dataframes[1] is the second table, and so on.

# Example: Display the first table
dataframes[0]

"""**Dataframe of a page**

"""

dataframes[0]

"""# **Data Cleaning**

**Dropping the columns**
"""

dataframes[0] = dataframes[0].drop(dataframes[0].index[0:14])

dataframes[0]

"""**Splitting the column**"""

# Split the 'A. Offences under I.T.Act' column based on spaces and create new columns in the first DataFrame (dataframes[0])
dataframes[0][['A) Computer Related Offences (Sec.66) (Total)', 'a1) Ransomware', 'a2) Offences other than Ransomware', 'B) Dishonestlyreceiving stolen computer resource or communication device (Sec.66B)']] = dataframes[0]['A. Offences under I.T.Act'].str.split(' ', expand=True)

# Drop the original 'A. Offences under I.T.Act' column in the first DataFrame (dataframes[0])
dataframes[0] = dataframes[0].drop('A. Offences under I.T.Act', axis=1)

# Now, the first DataFrame (dataframes[0]) will have separate columns for each value
print(dataframes[0])

dataframes[0]

"""**Renaming the columns**"""

dataframes[0].rename(columns={
    'Unnamed: 0': 'State/UT',
    'Unnamed: 2': 'Tampering computer source documents (Sec.65)',
    'Unnamed: 3': 'Computer Related Offences (Total)',
    'Unnamed: 4': 'C) IdentityTheft(Sec.66C)'
}, inplace=True)

dataframes[0]

"""**Dropping a row**"""

# Find the row index that contains the specified data
row_index_to_remove = dataframes[0][dataframes[0]['State/UT'] == 'UNION TERRITORIES:'].index

# Drop the row using the row index
dataframes[0] = dataframes[0].drop(row_index_to_remove)

# Delete the 'Unnamed: 1' column
dataframes[0] = dataframes[0].drop('Unnamed: 1', axis=1)

"""**Re-ordering the columns**"""

# Reorder the columns with 'C) IdentityTheft(Sec.66C)' in the 8th position
dataframes[0] = dataframes[0][['State/UT',
                               'Tampering computer source documents (Sec.65)',
                               'Computer Related Offences (Total)',
                               'A) Computer Related Offences (Sec.66) (Total)',
                               'a1) Ransomware',
                               'a2) Offences other than Ransomware',
                               'B) Dishonestlyreceiving stolen computer resource or communication device (Sec.66B)',
                                'C) IdentityTheft(Sec.66C)']]

"""**Cleaning the column State/Ut**"""

dataframes[0]['State/UT'] = dataframes[0]['State/UT'].str.replace(r'\d+', '').str.strip()

dataframes[0] = dataframes[0].reset_index(drop=True)

dataframes[0]

"""**Same process done for every dataframe**"""

dataframes[1]

dataframes[1] = dataframes[1].drop(dataframes[1].index[0:16])

dataframes[1]

# Split the 'A. Offences under I.T.Act' column based on spaces and create new columns in the first DataFrame (dataframes[0])
dataframes[1][[ 'E) Violation of Privacy (Sec.66E)', 'Cyber Terrorism (Sec.66 F)', 'Publication/ transmission of obscene / sexually explicit act in electronic form (Total)','A) Publishing ortransmitting obscene material in Electronic Form']] = dataframes[1]['A. Offences under I.T.Act'].str.split(' ', expand=True)

# Drop the original 'A. Offences under I.T.Act' column in the first DataFrame (dataframes[0])
dataframes[1] = dataframes[1].drop('A. Offences under I.T.Act', axis=1)

# Now, the first DataFrame (dataframes[0]) will have separate columns for each value
print(dataframes[1])

dataframes[1].rename(columns={
    'Unnamed: 0': 'State/UT',
    'Unnamed: 2': 'D) Cheating bypersonation by using computer resource (Sec.66D)'

}, inplace=True)

# Delete the 'Unnamed: 1' column
dataframes[1] = dataframes[1].drop('Unnamed: 1', axis=1)

dataframes[1]

# Find the row index that contains the specified data
row_index_to_remove = dataframes[1][dataframes[1]['State/UT'] == 'UNION TERRITORIES:'].index

# Drop the row using the row index
dataframes[1] = dataframes[1].drop(row_index_to_remove)

dataframes[1]['State/UT'] = dataframes[1]['State/UT'].str.replace(r'\d+', '').str.strip()

dataframes[1] = dataframes[1].reset_index(drop=True)

dataframes[1]

dataframes[2]

dataframes[2] = dataframes[2].drop(dataframes[2].index[0:18])

# Split the 'A. Offences under I.T.Act' column based on spaces and create new columns in the first DataFrame (dataframes[0])
dataframes[2][[ 'B) Publishing ortransmitting of material containing Sexually explicit act in electronic form (Sec.67A)', 'C) Publishing ortransmitting of material depicting children in Sexually explicit act in electronic form (Sec.67B)', 'D) Preservationand retention of information by intermediaries (Sec.67C)','E) Othersubsections of Sec. 67 IT Act']] = dataframes[2]['A. Offences under I.T.Act'].str.split(' ', expand=True)

# Drop the original 'A. Offences under I.T.Act' column in the first DataFrame (dataframes[0])
dataframes[2] = dataframes[2].drop('A. Offences under I.T.Act', axis=1)

# Now, the first DataFrame (dataframes[0]) will have separate columns for each value
print(dataframes[2])


dataframes[2].rename(columns={
    'Unnamed: 0': 'State/UT',
    'Unnamed: 2': 'Interception or Monitoring or decryption of Information (Sec.69)'

}, inplace=True)



# Find the row index that contains the specified data
row_index_to_remove = dataframes[2][dataframes[2]['State/UT'] == 'UNION TERRITORIES:'].index

# Drop the row using the row index
dataframes[2] = dataframes[2].drop(row_index_to_remove)


# Delete the 'Unnamed: 1' column
dataframes[2] = dataframes[2].drop('Unnamed: 1', axis=1)


# Reorder the columns with 'C) IdentityTheft(Sec.66C)' in the 8th position
dataframes[2] = dataframes[2][['State/UT',
                               'B) Publishing ortransmitting of material containing Sexually explicit act in electronic form (Sec.67A)',
                               'C) Publishing ortransmitting of material depicting children in Sexually explicit act in electronic form (Sec.67B)',
                               'D) Preservationand retention of information by intermediaries (Sec.67C)',
                               'E) Othersubsections of Sec. 67 IT Act',
                               'Interception or Monitoring or decryption of Information (Sec.69)']]


dataframes[2]['State/UT'] = dataframes[2]['State/UT'].str.replace(r'\d+', '').str.strip()

dataframes[2] = dataframes[2].reset_index(drop=True)

dataframes[2]

dataframes[3]

dataframes[3] = dataframes[3].drop(dataframes[3].index[0:10])

# Split the 'A. Offences under I.T.Act' column based on spaces and create new columns in the first DataFrame (dataframes[0])
dataframes[3][[ 'Abetment to Commit Offences (Sec.84 B)', 'Attempt to Commit Offences (Sec.84C)', 'Other Sections of IT Act ']] = dataframes[3]['A. Offences under I.T.Act'].str.split(' ', expand=True)

# Drop the original 'A. Offences under I.T.Act' column in the first DataFrame (dataframes[0])
dataframes[3] = dataframes[3].drop('A. Offences under I.T.Act', axis=1)

# Now, the first DataFrame (dataframes[0]) will have separate columns for each value
print(dataframes[3])

dataframes[3].rename(columns={
    'Unnamed: 0': 'State/UT',
    'Unnamed: 2': 'Un-authorized access/attempt to access to protected computer system (Sec.70)'

}, inplace=True)

# Find the row index that contains the specified data
row_index_to_remove = dataframes[3][dataframes[3]['State/UT'] == 'UNION TERRITORIES:'].index

# Drop the row using the row index
dataframes[3] = dataframes[3].drop(row_index_to_remove)

dataframes[3]

dataframes[3]['State/UT'] = dataframes[3]['State/UT'].str.replace(r'\d+', '').str.strip()

dataframes[3] = dataframes[3].reset_index(drop=True)

dataframes[3]

dataframes[3]['Total Offences under I.T. Act'] = dataframes[3]['Unnamed: 3'].fillna(dataframes[3]['Unnamed: 4'])

dataframes[3]

dataframes[3] = dataframes[3].drop(columns=['Unnamed: 3', 'Unnamed: 4'])

# Convert "Total Offences under I.T. Act" column to integers
dataframes[3]['Total Offences under I.T. Act'] = dataframes[3]['Total Offences under I.T. Act'].astype(int)

# Delete the 'Unnamed: 1' column
dataframes[3] = dataframes[3].drop('Unnamed: 1', axis=1)

dataframes[3]

dataframes[4]

dataframes[4] = dataframes[4].drop(dataframes[4].index[0:14])

# Split the 'A. Offences under I.T.Act' column based on spaces and create new columns in the first DataFrame (dataframes[0])
dataframes[4][[ 'Abetment of Suicide (Online) (Sec.305/306 IPC)', 'Cyber Stalking/ Bullying of Women/ Children (Sec.354D IPC)', 'Data theft (Sec.379 to 381)','Fraud (Sec.420 r/w Sec.465,468-471 IPC) (Total)','A) CreditCard/Debit Card']] = dataframes[4]['B. IPC Crimes(Involving Communication Devices as Medium/Target or r/w IT Act)'].str.split(' ', expand=True)

# Drop the original 'A. Offences under I.T.Act' column in the first DataFrame (dataframes[0])
dataframes[4] = dataframes[4].drop('B. IPC Crimes(Involving Communication Devices as Medium/Target or r/w IT Act)', axis=1)

# Now, the first DataFrame (dataframes[0]) will have separate columns for each value
print(dataframes[4])


dataframes[4].rename(columns={
    'Unnamed: 0': 'State/UT'


}, inplace=True)



# Find the row index that contains the specified data
row_index_to_remove = dataframes[4][dataframes[4]['State/UT'] == 'UNION TERRITORIES:'].index

# Drop the row using the row index
dataframes[4] = dataframes[4].drop(row_index_to_remove)


# Delete the 'Unnamed: 1' column
dataframes[4] = dataframes[4].drop('Unnamed: 1', axis=1)



dataframes[4]['State/UT'] = dataframes[4]['State/UT'].str.replace(r'\d+', '').str.strip()

dataframes[4] = dataframes[4].reset_index(drop=True)

dataframes[4]

dataframes[5]

dataframes[5] = dataframes[5].drop(dataframes[5].index[0:9])

# Split the 'A. Offences under I.T.Act' column based on spaces and create new columns in the first DataFrame (dataframes[0])
dataframes[5][[ 'B) ATMs', 'C) Online Banking Fraud ', 'D) OTP Frauds','E) Others','Cheating (Sec.420)']] = dataframes[5]['B. IPC Crimes(Involving Communication Devices as Medium/Target or r/w IT Act)'].str.split(' ', expand=True)

# Drop the original 'A. Offences under I.T.Act' column in the first DataFrame (dataframes[0])
dataframes[5] = dataframes[5].drop('B. IPC Crimes(Involving Communication Devices as Medium/Target or r/w IT Act)', axis=1)

# Now, the first DataFrame (dataframes[0]) will have separate columns for each value
print(dataframes[5])


dataframes[5].rename(columns={
    'Unnamed: 0': 'State/UT'


}, inplace=True)



# Find the row index that contains the specified data
row_index_to_remove = dataframes[5][dataframes[5]['State/UT'] == 'UNION TERRITORIES:'].index

# Drop the row using the row index
dataframes[5] = dataframes[5].drop(row_index_to_remove)


# Delete the 'Unnamed: 1' column
dataframes[5] = dataframes[5].drop('Unnamed: 1', axis=1)



dataframes[5]['State/UT'] = dataframes[5]['State/UT'].str.replace(r'\d+', '').str.strip()

dataframes[5] = dataframes[5].reset_index(drop=True)

dataframes[5]

dataframes[6]

dataframes[6] = dataframes[6].drop(dataframes[6].index[0:10])

# Split the 'A. Offences under I.T.Act' column based on spaces and create new columns in the first DataFrame (dataframes[0])
dataframes[6][[ 'Forgery (Sec.465, 468 & 471)', 'Defamation/ Morphing (Sec.469 IPC r/w IPC and Indecent representation of women Act) ', 'Fake Profile (r/w IPC/SLL)','Counterfeiting (Total)']] = dataframes[6]['B. IPC Crimes(Involving Communication Devices as Medium/Target or r/w IT Act)'].str.split(' ', expand=True)

# Drop the original 'A. Offences under I.T.Act' column in the first DataFrame (dataframes[0])
dataframes[6] = dataframes[6].drop('B. IPC Crimes(Involving Communication Devices as Medium/Target or r/w IT Act)', axis=1)

# Now, the first DataFrame (dataframes[0]) will have separate columns for each value
print(dataframes[6])


dataframes[6].rename(columns={
    'Unnamed: 0': 'State/UT',
    'Unnamed: 2':'A) Currency(Sec.489A to 489E)'


}, inplace=True)



# Find the row index that contains the specified data
row_index_to_remove = dataframes[6][dataframes[6]['State/UT'] == 'UNION TERRITORIES:'].index

# Drop the row using the row index
dataframes[6] = dataframes[6].drop(row_index_to_remove)


# Delete the 'Unnamed: 1' column
dataframes[6] = dataframes[6].drop('Unnamed: 1', axis=1)



dataframes[6]['State/UT'] = dataframes[6]['State/UT'].str.replace(r'\d+', '').str.strip()

dataframes[6] = dataframes[6].reset_index(drop=True)

dataframes[6]

# Convert "Total Offences under I.T. Act" column to integers
dataframes[6]['A) Currency(Sec.489A to 489E)'] = dataframes[6]['A) Currency(Sec.489A to 489E)'].astype(int)

dataframes[7]

dataframes[7] = dataframes[7].drop(dataframes[7].index[0:11])

# Split the 'A. Offences under I.T.Act' column based on spaces and create new columns in the first DataFrame (dataframes[0])
dataframes[7][[ 'B) Stamps(Sec.255))', 'Cyber Blackmailing/Threatening (Sec.506,503,384 IPC) ', 'Fake News on Social Media (Sec.505)','Other Offences ']] = dataframes[7]['B. IPC Crimes(Involving Communication Devices as Medium/Target or r/w IT'].str.split(' ', expand=True)

# Drop the original 'A. Offences under I.T.Act' column in the first DataFrame (dataframes[0])
dataframes[7] = dataframes[7].drop('B. IPC Crimes(Involving Communication Devices as Medium/Target or r/w IT', axis=1)

# Now, the first DataFrame (dataframes[0]) will have separate columns for each value
print(dataframes[7])


dataframes[7].rename(columns={
    'Unnamed: 0': 'State/UT',
    'Unnamed: 2':'Total Offences under IPC '


}, inplace=True)



# Find the row index that contains the specified data
row_index_to_remove = dataframes[7][dataframes[7]['State/UT'] == 'UNION TERRITORIES:'].index

# Drop the row using the row index
dataframes[7] = dataframes[7].drop(row_index_to_remove)


# Delete the 'Unnamed: 1' column
dataframes[7] = dataframes[7].drop('Unnamed: 1', axis=1)



dataframes[7]['State/UT'] = dataframes[6]['State/UT'].str.replace(r'\d+', '').str.strip()

dataframes[7] = dataframes[7].reset_index(drop=True)

dataframes[7]

dataframes[8]

dataframes[8] = dataframes[8].drop(dataframes[8].index[0:5])

# Split the 'A. Offences under I.T.Act' column based on spaces and create new columns in the first DataFrame (dataframes[0])
dataframes[8][[ 'Gambling Act (Online Gambling)', 'Lotteries Act (Online Lotteries)', "Copy Right Act, 1957'",'Trade Marks Act, 1999 ']] = dataframes[8]['C. SLL Crimes(Involving Communication Devices as Medium/Target or r/w IT Act)'].str.split(' ', expand=True)

# Drop the original 'A. Offences under I.T.Act' column in the first DataFrame (dataframes[0])
dataframes[8] = dataframes[8].drop('C. SLL Crimes(Involving Communication Devices as Medium/Target or r/w IT Act)', axis=1)

# Now, the first DataFrame (dataframes[0]) will have separate columns for each value
print(dataframes[8])


dataframes[8].rename(columns={
    'Unnamed: 0': 'State/UT'


}, inplace=True)



# Find the row index that contains the specified data
row_index_to_remove = dataframes[8][dataframes[8]['State/UT'] == 'UNION TERRITORIES:'].index

# Drop the row using the row index
dataframes[8] = dataframes[8].drop(row_index_to_remove)


# Delete the 'Unnamed: 1' column
dataframes[8] = dataframes[8].drop('Unnamed: 1', axis=1)



dataframes[8]['State/UT'] = dataframes[8]['State/UT'].str.replace(r'\d+', '').str.strip()

dataframes[8] = dataframes[8].reset_index(drop=True)

dataframes[8]

dataframes[9]

dataframes[9] = dataframes[9].drop(dataframes[9].index[0:6])

# Split the 'A. Offences under I.T.Act' column based on spaces and create new columns in the first DataFrame (dataframes[0])
dataframes[9][[ 'Other SLL Crimes', 'Total Offences under SLL']] = dataframes[9]['C. SLL Crimes(Involving Communication Devices as'].str.split(' ', expand=True)

# Drop the original 'A. Offences under I.T.Act' column in the first DataFrame (dataframes[0])
dataframes[9] = dataframes[9].drop('C. SLL Crimes(Involving Communication Devices as', axis=1)

# Now, the first DataFrame (dataframes[0]) will have separate columns for each value
print(dataframes[9])


dataframes[9].rename(columns={
    'Unnamed: 0': 'State/UT',
    'Unnamed: 2':'Total Cyber Crimes (IT Act+ IPC r/w IT Act + SLL r/w IT Act)'



}, inplace=True)



# Find the row index that contains the specified data
row_index_to_remove = dataframes[9][dataframes[9]['State/UT'] == 'UNION TERRITORIES:'].index

# Drop the row using the row index
dataframes[9] = dataframes[9].drop(row_index_to_remove)


# Delete the 'Unnamed: 1' column
dataframes[9] = dataframes[9].drop('Unnamed: 1', axis=1)



dataframes[9]['State/UT'] = dataframes[9]['State/UT'].str.replace(r'\d+', '').str.strip()

dataframes[9] = dataframes[9].reset_index(drop=True)

dataframes[9]

"""###**Concatinating all Dataframes into one Dataframe**"""

for i in range(1, 10):
    dataframes[i] = dataframes[i].drop('State/UT', axis=1)

df_final = pd.concat(dataframes[:10], axis=1)

df_final

"""## **Checking null value counts**"""

null_counts = df_final.isnull().sum()
print(null_counts)

"""##**Identifying missing values in the DataFrame:**"""

missing_values = df_final.isnull().sum()
print(missing_values)

"""##**Removing Duplicates**"""

df_final.drop_duplicates(inplace=True)

df_final

"""##**Checking the datatype of all the columns**

"""

column_data_types = df_final.dtypes
print(column_data_types)

"""##**Converting to numeric datatype**"""

import pandas as pd

# Replace 'df_final' with the actual name of your DataFrame
for column in df_final.columns[1:]:  # Start from the second column (excluding 'State/UT')
    df_final[column] = pd.to_numeric(df_final[column], errors='coerce')

column_data_types = df_final.dtypes
print(column_data_types)

"""### **Saving the cleaned data**"""

# Save the DataFrame as a CSV file
df_final.to_csv('finaldataframe.csv', index=False)

"""reading the saved final dataframe"""

# Replace 'your_saved_csv_file.csv' with the actual file path
file_path = 'finaldataframe.csv'

# Read the CSV file and store it in a DataFrame
import pandas as pd
df_final = pd.read_csv(file_path)

"""#**Exploratory Data Analysis**"""

import matplotlib.pyplot as plt
import seaborn as sns

"""## **Univariate Analysis**

**Summary Statistics:**
"""

summary_stats = df_final.describe()
print(summary_stats)

""" **Distribution Plots:**"""

plt.figure(figsize=(7, 5))
sns.histplot(df_final["Total Offences under I.T. Act"], kde=True)
plt.title("Distribution of Total Offences under I.T. Act")
plt.xlabel("Total Offences")
plt.ylabel("Frequency")
plt.show()

"""**Count Plots:**"""

plt.figure(figsize=(10, 6))
sns.countplot(x="State/UT", data=df_final)
plt.xticks(rotation=90)
plt.title("Count of States/UT")
plt.show()

"""**Count Plot for Categorical Columns**"""

plt.figure(figsize=(10, 6))
sns.countplot(data=df_final, x="Abetment of Suicide (Online) (Sec.305/306 IPC)")
plt.title("Count Plot for Abetment of Suicide (Online) (Sec.305/306 IPC)")
plt.xticks(rotation=90)
plt.show()

"""**Distribution of Total Cyber Crimes**"""

plt.figure(figsize=(10, 6))
sns.histplot(df_final["Total Cyber Crimes (IT Act+ IPC r/w IT Act + SLL r/w IT Act)"], kde=True)
plt.title("Distribution of Total Cyber Crimes")
plt.xlabel("Total Cyber Crimes")
plt.ylabel("Frequency")
plt.show()

"""**Bar Plot for Total Offences under SLL**"""

plt.figure(figsize=(12, 6))
sns.barplot(data=df_final, x="State/UT", y="Total Offences under SLL")
plt.title("Bar Plot for Total Offences under SLL")
plt.xticks(rotation=90)
plt.show()

"""**Histogram for Fraud Cases**"""

plt.figure(figsize=(10, 6))
sns.histplot(df_final["Fraud (Sec.420 r/w Sec.465,468-471 IPC) (Total)"], kde=True)
plt.title("Distribution of Fraud Cases")
plt.xlabel("Total Fraud Cases")
plt.ylabel("Frequency")
plt.show()

"""**Bar Plot for Identity Theft**"""

plt.figure(figsize=(12, 6))
sns.barplot(data=df_final, x="State/UT", y="C) IdentityTheft(Sec.66C)")
plt.title("Identity Theft Cases by State")
plt.xticks(rotation=90)
plt.show()

"""**Kernel Density Estimate Plot for Cheating Cases**"""

plt.figure(figsize=(10, 6))
sns.kdeplot(df_final["Cheating (Sec.420)"], fill=True)
plt.title("Distribution of Cheating Cases")
plt.xlabel("Total Cheating Cases")
plt.ylabel("Density")
plt.show()

"""## **Bivariate Analysis**

**Scatter Plots:**
"""

plt.figure(figsize=(7, 6))
sns.scatterplot(x="Total Offences under I.T. Act", y="Total Cyber Crimes (IT Act+ IPC r/w IT Act + SLL r/w IT Act)", data=df_final)
plt.title("Scatter Plot of Total I.T. Act Offences vs. Total Cyber Crimes")
plt.show()

"""**Scatter Plot for Total Cyber Crimes vs. Total Offences under I.T. Act**"""

plt.figure(figsize=(10, 6))
sns.scatterplot(data=df_final, x="Total Cyber Crimes (IT Act+ IPC r/w IT Act + SLL r/w IT Act)", y="Total Offences under I.T. Act")
plt.title("Total Cyber Crimes vs. Total Offences under I.T. Act")
plt.xlabel("Total Cyber Crimes")
plt.ylabel("Total Offences under I.T. Act")
plt.show()

"""**Correlation Heatmap:**"""

corr_matrix = df_final.iloc[:, 1:20].corr()
plt.figure(figsize=(12, 10))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap of Cybercrime Variables")
plt.show()

"""**Pairplot for Select Columns:**"""

sns.pairplot(df_final, vars=["Total Cyber Crimes (IT Act+ IPC r/w IT Act + SLL r/w IT Act)", "Total Offences under I.T. Act", "C) IdentityTheft(Sec.66C)"], hue="State/UT")
plt.title("Pairplot of Selected Variables")
plt.show()

"""**Bar Plot: Cyber Crimes by State**"""

plt.figure(figsize=(12, 6))
sns.barplot(data=df_final, x="State/UT", y="Total Cyber Crimes (IT Act+ IPC r/w IT Act + SLL r/w IT Act)", palette="viridis")
plt.title("Total Cyber Crimes by State")
plt.xticks(rotation=90)
plt.show()

"""**Joint Plot: Total Cyber Crimes vs. Total Offences under SLL**"""

sns.jointplot(data=df_final, x="Total Cyber Crimes (IT Act+ IPC r/w IT Act + SLL r/w IT Act)", y="Total Offences under SLL", kind="scatter")

"""**Regression Plot: Cyber Stalking/ Bullying vs. Total Cyber Crimes**"""

sns.lmplot(data=df_final, x="Cyber Stalking/ Bullying of Women/ Children (Sec.354D IPC)", y="Total Cyber Crimes (IT Act+ IPC r/w IT Act + SLL r/w IT Act)")

"""**Stacked Bar Plot: Cybercrime Types by State**"""

cybercrime_types = ["Tampering computer source documents (Sec.65)", "a1) Ransomware", "B) Dishonestlyreceiving stolen computer resource or communication device (Sec.66B)"]
df_cybercrime_types = df_final[cybercrime_types]

plt.figure(figsize=(12, 6))
df_cybercrime_types.plot(kind="bar", stacked=True, colormap="viridis", ax=plt.gca())
plt.title("Cybercrime Types by State")
plt.xticks(range(len(df_final["State/UT"])), df_final["State/UT"], rotation=90)
plt.legend(title="Cybercrime Type")
plt.show()

pip install geopandas pandas matplotlib

df_final

"""## **Multivariate Analysis:**

**Pairplot**
"""

import seaborn as sns

# Select a subset of states for the pair plot (e.g., the first 10 states)
subset_states = df_final['State/UT'].unique()[:10]

# Filter the DataFrame to include only these states
df_subset = df_final[df_final['State/UT'].isin(subset_states)]

# Create the pair plot
columns_to_plot = df_subset[['State/UT', 'Tampering computer source documents (Sec.65)', 'Cyber Terrorism (Sec.66 F)', 'Total Offences under SLL', 'Total Cyber Crimes (IT Act+ IPC r/w IT Act + SLL r/w IT Act)']]
sns.pairplot(columns_to_plot, hue='State/UT', markers=["o", "s", "D"])

"""**Scatterplot Matrix:**"""

import seaborn as sns
import matplotlib.pyplot as plt

# Select the columns from the last part of the DataFrame (adjust column selection as needed)
columns_to_plot = df_final.iloc[:, -4:]  # Select the last 4 columns or adjust as per your preference

# Create the scatterplot matrix
scatterplot_matrix = sns.pairplot(columns_to_plot, height=2, aspect=1.5)

# Add a title to the scatterplot matrix
plt.suptitle("Scatterplot Matrix", y=1.02)

# Show the plot
plt.show()

"""**Heatmap:**"""

import seaborn as sns
import matplotlib.pyplot as plt

# Select the middle 10 columns (adjust as needed)
middle_columns = df_final.iloc[:, 20:30]

# Calculate the correlation matrix for the selected columns
correlation_matrix = middle_columns.corr()

# Set the figure size
plt.figure(figsize=(12, 8))

# Create the heatmap
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")

# Display the plot
plt.show()

"""**3D Scatterplot:**"""

from mpl_toolkits.mplot3d import Axes3D

# Replace these column names with the ones you want to plot
x_column = 'Tampering computer source documents (Sec.65)'
y_column = 'Computer Related Offences (Total)'
z_column = 'A) Computer Related Offences (Sec.66) (Total)'

fig = plt.figure(figsize=(17,17))
ax = fig.add_subplot(111, projection='3d')
scatter = ax.scatter(df_final[x_column], df_final[y_column], df_final[z_column])

ax.set_xlabel(x_column, labelpad=10)
ax.set_ylabel(y_column, labelpad=10)
ax.set_zlabel(z_column, labelpad=10)

# Adjust the rotation of the labels for better visibility
ax.xaxis.label.set_rotation(15)
ax.yaxis.label.set_rotation(45)
ax.zaxis.label.set_rotation(45)

# Set additional customization options if needed

plt.show()

"""**Parallel Coordinates Plot:**"""

import matplotlib.pyplot as plt
import pandas as pd
from pandas.plotting import parallel_coordinates

# Define the columns to be used in the Parallel Coordinates Plot
columns_to_plot = [
    'A) Computer Related Offences (Sec.66) (Total)',
    'C) IdentityTheft(Sec.66C)',
    'Cyber Terrorism (Sec.66 F)',
    'Total Offences under I.T. Act',
    'Data theft (Sec.379 to 381)',
]

# Create a dummy class column with the same value for all rows
df_final['Class'] = 1

plt.figure(figsize=(12, 6))
parallel_coordinates(df_final[['Class'] + columns_to_plot], 'Class')

plt.title("Parallel Coordinates Plot")
plt.show()

# Remove the dummy class column from the DataFrame
df_final.drop('Class', axis=1, inplace=True)

"""**Radar Chart:**"""

from math import pi
import numpy as np

# Categories and values
categories = list(df_final.columns[1:6])
N = len(categories)

values = df_final.loc[0][1:6].values.tolist()
values += values[:1]

angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]

# Create a radar chart
plt.figure(figsize=(8, 8))
ax = plt.subplot(111, polar=True)
plt.xticks(angles[:-1], categories, color='Darkblue', size=12)
ax.set_rlabel_position(0)
plt.yticks(np.arange(0, 4001, 1000), ["0", "1000", "2000", "3000", "4000"], color="grey", size=10)
plt.ylim(0, 4000)
ax.fill(angles, values, 'b', alpha=0.1)

plt.show()

# Load your dataset (replace 'your_dataset.csv' with your data)
import pandas as pd
df_final = pd.read_csv(file_path)

df_final

"""# **Data Splitting**"""

# Split data into features and target variable
X = df_final.drop(['Total Cyber Crimes (IT Act+ IPC r/w IT Act + SLL r/w IT Act)'], axis=1)
y = df_final['Total Cyber Crimes (IT Act+ IPC r/w IT Act + SLL r/w IT Act)']

from sklearn.model_selection import train_test_split
# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

"""# **Data Preprocessing**"""

from sklearn.preprocessing import StandardScaler


from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

# Identify the categorical and numerical columns
categorical_cols = ['State/UT']  # Add more columns if needed
numerical_cols = X.columns.difference(categorical_cols)

# Use ColumnTransformer to apply transformations to the columns
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numerical_cols),  # Scale numerical columns
        ('cat', OneHotEncoder(), categorical_cols)  # One-hot encode categorical columns
    ])

# Apply the transformations to the feature matrix X
X = preprocessor.fit_transform(X)

# Make sure to do the same transformations to the training set
X_train = preprocessor.transform(X_train)

# Make sure to do the same transformations to the test set if applicable
X_test = preprocessor.transform(X_test)  # If you have a test set

"""# **Predicting Total Cyber Crimes in India**

## **Model Selection and Model Training:**

## **Multi Layered Perceptron**
"""

# Create and train a feedforward neural network
from sklearn.neural_network import MLPRegressor

model = MLPRegressor(hidden_layer_sizes=(100, 50), max_iter=1000, random_state=42)
model.fit(X_train, y_train)

"""## **Prediction:**"""

# Make predictions
y_pred = model.predict(X_test)

"""## **Model Evaluation:**"""

# Evaluate the model
from sklearn.metrics import mean_squared_error
import numpy as np

from sklearn.metrics import mean_absolute_error, r2_score
mse_mlp = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse_mlp}")

# Calculate Mean Absolute Error (MAE)
mae_mlp = mean_absolute_error(y_test, y_pred)
print(f"Mean Absolute Error: {mae_mlp}")

# Calculate Root Mean Squared Error (RMSE)
rmse_mlp = np.sqrt(mean_squared_error(y_test, y_pred))
print(f"Root Mean Squared Error: {rmse_mlp}")

"""## **Deep Neural Network (DNN) for regression:**"""

import tensorflow as tf
from sklearn.metrics import mean_squared_error

from sklearn.metrics import mean_absolute_error, r2_score

# Define your DNN model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(1)  # Output layer for regression
])

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
model.fit(X_train, y_train, epochs=100, batch_size=32)
from sklearn.metrics import mean_squared_error

# Assuming you already have your model and have trained it

# Generate predictions
y_pred = model.predict(X_test)

# Calculate Mean Squared Error (MSE)
mseDNN = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error (MSE): {mseDNN}")


# Calculate Mean Absolute Error (MAE)
maeDNN = mean_absolute_error(y_test, y_pred)
print(f"Mean Absolute Error: {maeDNN}")

# Calculate RMSE (Root Mean Squared Error)
rmseDNN = np.sqrt(mseDNN)
print(f"Root Mean Squared Error (RMSE): {rmseDNN}")

"""## **Machine Learning Approaches**

## **Random Forest**
"""

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import numpy as np



# Create a Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model using Mean Squared Error (MSE)
mse_rf = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse_rf}")

# Calculate Mean Absolute Error (MAE)
mae_rf = mean_absolute_error(y_test, y_pred)
print(f"Mean Absolute Error: {mae_rf}")

# Calculate Root Mean Squared Error (RMSE)
rmse_rf = np.sqrt(mean_squared_error(y_test, y_pred))
print(f"Root Mean Squared Error: {rmse_rf}")

"""## **Support Vector Machine (SVM) Regression:**"""

from sklearn.svm import SVR

# Create an SVR model
svm_model = SVR()

# Train the model
svm_model.fit(X_train, y_train)

# Make predictions
y_svm_pred = svm_model.predict(X_test)

# Evaluate the model using the same metrics
mse_svm = mean_squared_error(y_test, y_svm_pred)
print(f"SVM Mean Squared Error: {mse_svm}")

mae_svm = mean_absolute_error(y_test, y_svm_pred)
print(f"SVM Mean Absolute Error: {mae_svm}")

rmse_svm = np.sqrt(mean_squared_error(y_test, y_svm_pred))
print(f"SVM Root Mean Squared Error: {rmse_svm}")



"""## **Gradient Boosting Regression:**"""

from sklearn.ensemble import GradientBoostingRegressor

# Create a Gradient Boosting model
gb_model = GradientBoostingRegressor()

# Train the model
gb_model.fit(X_train, y_train)

# Make predictions
y_gb_pred = gb_model.predict(X_test)

# Evaluate the model using the same metrics
mse_gb = mean_squared_error(y_test, y_gb_pred)
print(f"Gradient Boosting Mean Squared Error: {mse_gb}")

mae_gb = mean_absolute_error(y_test, y_gb_pred)
print(f"Gradient Boosting Mean Absolute Error: {mae_gb}")

rmse_gb = np.sqrt(mean_squared_error(y_test, y_gb_pred))
print(f"Gradient Boosting Root Mean Squared Error: {rmse_gb}")

"""## **LinearRegression**"""

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import numpy as np

# Create a Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model using Mean Squared Error (MSE)
mse_lr = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse_lr}")

# Calculate Mean Absolute Error (MAE)
mae_lr = mean_absolute_error(y_test, y_pred)
print(f"Mean Absolute Error: {mae_lr}")

# Calculate Root Mean Squared Error (RMSE)
rmse_lr = np.sqrt(mean_squared_error(y_test, y_pred))
print(f"Root Mean Squared Error: {rmse_lr}")

"""## **Visualizing the best Model**"""

import matplotlib.pyplot as plt
import numpy as np

# List of model names
models = ["MLP", "DNN", "Random Forest", "Gradient Boost", "Linear Regression", "SVM"]

# List of corresponding MSE, RMSE, MAE, and R-squared scores
mse_scores = [mse_mlp, mseDNN, mse_rf, mse_gb, mse_lr, mse_svm]
rmse_scores = [rmse_mlp, rmseDNN, rmse_rf, rmse_gb, rmse_lr, rmse_svm]
mae_scores = [mae_mlp, maeDNN, mae_rf, mae_gb, mae_lr, mae_svm]


# Set the width of the bars
bar_width = 0.2

# Create an array of positions for each group of bars
index = range(len(models))

# Define a color map for the bars
colors = plt.cm.viridis(np.linspace(0, 1, len(models)))

# Create the subplots
fig, ax = plt.subplots()

# Create the bars for each metric with different colors
for i, (metric, scores) in enumerate(zip(["MSE", "RMSE", "MAE", "R-squared"], [mse_scores, rmse_scores, mae_scores])):
    plt.bar([x + i * bar_width for x in index], scores, bar_width, label=metric, alpha=0.7, color=colors)

# Rotate the X-axis labels
plt.xticks([i + bar_width for i in index], models, rotation=45, ha="right")

# Set the Y-axis label and title
plt.ylabel('Scores')
plt.title('Comparison of Evaluation Metrics')

# Add a legend
plt.legend(loc='best')

# Display the plot
plt.tight_layout()
plt.show()

"""### **Random Forest and Linear Regression appeared to be best model for predicting Total Cyber Crimes**"""