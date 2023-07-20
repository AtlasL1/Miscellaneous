# Data Analysis
# Titanic Survivors
# With Numpy and Pandas

# IMPORT LIBRARIES
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# READ CSV FILE
df = pd.read_csv(r'Titanic Passengers.csv')

# RENAME COLUMN, CHANGE INDEX, DISPLAY DATASET
df.rename(columns={'PassengerId': 'ID'}, inplace=True)
df = df.set_index('ID')
pd.set_option('display.min_rows', 10)  # 10 IS THE DEFAULT
pd.set_option('display.max_columns', 20)
print(df)

# RETRIEVE COLUMNS INFORMATION
print()
print(df.columns)
print()

# DISPLAY THE NUMBER OF PEOPLE WHO SURVIVED AND DID NOT
print('0 = Did Not Survive, 1 = Survived')
print(df['Survived'].value_counts())

# DATA VISUALISATION WITH SEABORN
# COMPARISON OF NUMBER OF SURVIVORS BETWEEN MALE AND FEMALE
sns.set_theme()
sns.catplot(
    data=df,
    x='Survived',
    kind='count',
    hue='Gender',
)
plt.title('Comparison of Number of Survivors Between Male and Female')
plt.show()

# SHORT CONCLUSION
# GENDER AND SURVIVAL
def gender(analysis):
    print('\nAn Analysis: \nComparison of Number of Survivors Between Male and Female\n')
    print(analysis)
    print()
gender('For those of whom did not survive the disaster, males top over 400 whereas females top under 100. \n'
       'On the other hand, for those whom survived, females top over 200 whereas males were barely over 100. \n'
       'It can be concluded that the passengers\' gender have an impact on survival. The main factor of this \n'
       'is likely because of order given on the ship after its fateful collision with the iceberg, "women and \n'
       'children first". The meaning of this order is that males stay back and allow females and children younger \n'
       'than 12 to board the lifeboats. Due to the limited time on the ship, most males did not manage to survive.')

# DATA VISUALISATION WITH SEABORN
# NUMBER OF SURVIVORS BETWEEN DIFFERENT AGES
sns.set_theme()
g = sns.FacetGrid(df, col='Survived')
g.map(plt.hist, 'Age', bins=20)
g.set_axis_labels('Age', 'Count')
plt.show()

# SHORT CONCLUSION
# AGE AND SURVIVAL
def age(analysis):
    print('\nAn Analysis: \nComparison of Number of Survivors Between Different Ages')
    print(analysis)
    print()
age('For those of whom did not survive the disaster, passengers around the age of 20 to 30 are  \n'
    '')

# DATA VISUALISATION WITH SEABORN
# NUMBER OF SURVIVORS BETWEEN DIFFERENT PASSENGER CLASSES
sns.set_theme()
sns.catplot(
    data=df,
    x='Survived',
    kind='count',
    hue='Pclass',
)
plt.title('Comparison of Number of Survivors Among Different Passenger Classes')
plt.show()