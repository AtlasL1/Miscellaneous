# Learn Data Analysis & Science
# NEO Earth Close Approaches
# With Numpy and Pandas

# IMPORTING LIBRARIES
import numpy as np
import pandas as pd

# READ CSV FILE
df = pd.read_csv(r'NEO Earth Close Approaches.csv')

# SET THE NUMBERS OF ROWS AND COLUMNS TO BE DISPLAYED
pd.set_option('display.min_rows', 10)  # 10 IS THE DEFAULT
pd.set_option('display.max_columns', 20)
print('\n.........................................................................................\n')
print('\nNEO EARTH CLOSE APPROACHES\n')
print(df)

# LOADING CSV FILE WITH SKIP FIRST 2 ROWS WITHOUT HEADER
df_csv = pd.read_csv(r'NEO Earth Close Approaches.csv', skiprows=2, header=None)
df_csv.head(3)
print('\n.........................................................................................\n')
print('\nLOADING CSV FILE WITH SKIP FIRST 2 ROWS WITHOUT HEADER\n')
print(df_csv)

# DISPLAY FIRST 3 ROWS
print('\n.........................................................................................\n')
print('\nDISPLAY FIRST 3 ROWS\n')
print(df.head(3))

# DISPLAY LAST 3 ROWS
print('\n.........................................................................................\n')
print('\nDISPLAY LAST 3 ROWS\n')
print(df.tail(6))

# DISPLAY DATAFRAME INFO
print('\n.........................................................................................\n')
print('\nDISPLAY DATAFRAME INFO\n')
print(df.info())

# DISPLAY DATATYPES
print('\n.........................................................................................\n')
print('\nDISPLAY DATATYPES\n')
print(df.dtypes)

# DISPLAY VALUES OF EACH DATATYPE
print('\n.........................................................................................\n')
print('\nDISPLAY VALUES OF EACH DATATYPE\n')
print(df.dtypes.value_counts())

# DISPLAY THE NUMBER OF ROWS AND COLUMNS
print('\n.........................................................................................\n')
print('\nDISPLAY THE NUMBER OF ROWS AND COLUMNS\n')
print(df.shape)

# DISPLAY COLUMNS NAME AND DATA
print('\n.........................................................................................\n')
print('\nDISPLAY COLUMNS NAME AND DATA\n')
print(df.columns)

# DISPLAY DIAMETER COLUMNS (FIRST 3 ROWS)
print('\n.........................................................................................\n')
print('\nDISPLAY DIAMETER COLUMNS (FIRST THREE ROWS)\n')
print(df['Diameter'].head(3))

# DISPLAY OBJECT, DIAMETER & RARITY COLUMNS (FIRST 4 ROWS)
print('\n.........................................................................................\n')
print('\nDISPLAY OBJECT, DIAMETER & RARITY COLUMNS (FIRST 4 ROWS)\n')
print(df[['Object', 'Diameter', 'Rarity']].head(4))

# DISPLAY A SPECIFIC RANGE OF ROWS
print('\n.........................................................................................\n')
print('\nDISPLAY A SPECIFIC RANGE OF ROWS')
print('\n2nd to 6th: \n', df[2:7])  # 2ND TO 6TH
print('\nStarting to 10th: \n', df[:11])  # STARTING TO 10TH
print('\nLast two: \n', df[-2:])  # LAST TWO

# DROP UNWANTED COLUMNS
print('\n.........................................................................................\n')
print('\nDROP UNWANTED COLUMNS - DIAMETER\n')
df_dropped = df.drop(['Diameter'], axis=1)
print(df_dropped)

# CREATE NEW DF_COL DATAFRAME FROM DF.COPY() METHOD
df_col = df.copy()

# RENAME COLUMNS NAME
print('\n.........................................................................................\n')
print('\nRENAME COLUMNS:')
print('"CLOSE-APPROACH (CA) DATE" TO "CA DATE",')
print('"CA DISTANCENOMINAL (AU)" TO "CA NOMINAL DIST. (AU)",')
print('"CA DISTANCEMINIMUM (AU)" TO "CA MIN. DIST. (AU)"\n')
df_col.rename(columns={"Close-Approach (CA) Date": "CA Date", "CA DistanceNominal (au)": "CA Nominal Dist. (au)",
                       "CA DistanceMinimum (au)": "CA Min. Dist. (au)"}, inplace=True)
print(df_col.head(3))

# ADD A NEW COLUMN (USELESS COLUMN: FOR LEARNING PURPOSES ONLY)
print('\n.........................................................................................\n')
print('\nADD A COLUMN\n')
df_col['Useless Column'] = df_col['Rarity'] * 0
print(df_col.head(3))

# CHANGE STRING VALUE
print('\n.........................................................................................\n')
print('\nCHANGING STRING VALUE:\n')
print('STRINGS IN "USELESS COLUMN" TO 0\n')
df_col.loc[df_col['Useless Column'] == 0.0, 'Useless Column'] = "0"
print(df_col.head(3))

# DISPLAY NEW DATASET INFO
print('\n.........................................................................................\n')
print('\nDISPLAY NEW DATASET INFO\n')
df_col.info()

# CHANGE DATATYPE OF "USELESS COLUMN"
print('\n.........................................................................................\n')
print('\nCHANGE DATATYPE OF "USELESS COLUMN"\n')
df_col['Useless Column'] = df_col['Useless Column'].astype('float64')
df_col.info()

# DELETE ENTIRE COLUMNS
print('\n.........................................................................................\n')
print('\nDELETE "USELESS COLUMN"\n')
df_new = df_col.copy()
df_new.drop(columns=['Useless Column'], inplace=True)
print(df_new)

# COUNTS OF UNIQUE VALUES
print('\n.........................................................................................\n')
print('\nCOUNT VALUES OF CA DATE\n')
print(df_new['CA Date'].value_counts())

# SORT SMALLEST (ONLY AVAILABLE FOR FLOAT TYPES)
print('\n.........................................................................................\n')
print('\nSORT ACCORDING TO SMALLEST RARITY\n')
print(df_new.nsmallest(4, 'Rarity').head(9))

# SORT LARGEST (ONLY AVAILABLE FOR FLOAT TYPES)
print('\n.........................................................................................\n')
print('\nSORT ACCORDING TO LARGEST RARITY\n')
print(df_new.nlargest(4, 'Rarity').head(9))

# SAVE MEMORY BY CHANGING DATATYPE
print('\n.........................................................................................\n')
print('\nSAVE MEMORY BY CHANGING DATATYPE\n')
df_memory = df_new.copy()
memory_usage = df_memory.memory_usage(deep=True)
memory_usage_in_mbs = round(np.sum(memory_usage / 1024 ** 2), 3)
print(f"Total memory taking df_memory dataframe is: {memory_usage_in_mbs:.2f} MB")

# CHANGE OBJECT TO CATEGORY DATA TYPES
print('\n.........................................................................................\n')
print('\nCHANGE OBJECT TO CATEGORY DATA TYPES\n')
df_memory[df_memory.select_dtypes(['object']).columns] = df_memory.select_dtypes(['object']).apply(lambda x: x.astype('category'))
df_memory.info(memory_usage="deep")