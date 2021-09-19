import pandas as pd
#Seed

def read_and_format(csv_file):
        df = pd.read_csv(csv_file)
        df.columns.values[0] = "Width"# Manuellt nämning av kolumner
        df.columns.values[1] = "Height"
        df.iloc[:, 0] = df.iloc[:, 0].str.replace(r'(', '', regex=True)# 2 rad kod för att erätta värden i celler med värden utan parenthes
        df.iloc[:, 1] = df.iloc[:, 1].str.replace(r')', '', regex=True)
        df['Width'] = df['Width'].astype(float)# 2 rad kod för att byta strings som finns i varje kolumn (original datatyp) till float
        df['Height'] = df['Height'].astype(float)
        return df

def sample_randomization(dataframe): # koden har jag fått reda på från https://www.geeksforgeeks.org/pandas-how-to-shuffle-a-dataframe-rows/
        random_df = dataframe.sample(frac = 1)# Blandar raderna
        train_data = random_df[0:44]
        test_data = random_df[45:]
        return train_data, test_data

def sort_and_list(dataframe): # Returns a list of the 5 minimal distances calculated within the dataframe
        dataframe = dataframe.sort_values('distance')
        min_five = dataframe.iloc[:5,2].tolist()
        return min_five

def test_df_to_coordinates_list(dataframe1, dataframe2):
        dataframe1['coordinates'] = dataframe1.values.tolist()
        dataframe2['coordinates'] = dataframe2.values.tolist()
        test_points = dataframe1.iloc[:5,2].tolist() + dataframe2.iloc[:5,2].tolist()
        return test_points


