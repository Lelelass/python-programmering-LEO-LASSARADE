import pandas as pd

def read_and_format(csv_file) -> pd.DataFrame:
        '''
        The function cleans the csv file (previously created by running txt_to_csv.py) from parenthesis,
        transforms it's values to float and store them in a dataframe with Height and Width columns
        '''
        df = pd.read_csv(csv_file)
        df.columns.values[0] = "Width"# Manuellt nämning av kolumner
        df.columns.values[1] = "Height"
        df.iloc[:, 0] = df.iloc[:, 0].str.replace(r'(', '', regex=True)# 2 rad kod för att ersätta värden i celler med värden utan parenthes
        df.iloc[:, 1] = df.iloc[:, 1].str.replace(r')', '', regex=True)
        df['Width'] = df['Width'].astype(float)# 2 rad kod för att byta strings som finns i varje kolumn (original datatyp) till float
        df['Height'] = df['Height'].astype(float)
        return df

def sample_randomization(dataframe : pd.DataFrame) -> tuple: # koden har jag fått reda på från https://www.geeksforgeeks.org/pandas-how-to-shuffle-a-dataframe-rows/
        '''
        The function shuffles the index of the imported dataframes so the data is randomized.
        it then slices the data in proportion 95 - 5 and returns two dataframes, one train, one test, as a tuple.
        '''
        random_df = dataframe.sample(frac = 1)# Blandar raderna
        train_data = random_df[0:44]
        test_data = random_df[45:]
        return train_data, test_data

def sort_and_list(dataframe : pd.DataFrame) -> list:
        """
        The function sorts the dataframe by distances in ascending order and returns the 5 smallest distances of the dataframe into a list
        """
        dataframe = dataframe.sort_values('distance')
        min_five = dataframe.iloc[:5,2].tolist()
        return min_five

def test_df_to_coordinates_list(dataframe1: pd.DataFrame, dataframe2: pd.DataFrame) -> list:
        """
        Returns coordinates from test dataframes by first turning each row's width and height into a coordinate as a list.
        The function then adds up the coordinates in a new list (list of lists)
        """
        dataframe1['coordinates'] = dataframe1.values.tolist()# Creates a new list from two separate values in columns height, width
        dataframe2['coordinates'] = dataframe2.values.tolist()
        test_points = dataframe1.iloc[:5,2].tolist() + dataframe2.iloc[:5,2].tolist()
        return test_points


