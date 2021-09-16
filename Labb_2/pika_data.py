import pandas as pd

def read_and_format(csv_file):
        df = pd.read_csv(csv_file)
        df.columns.values[0] = "Width"# Manuellt nämning av kolumner
        df.columns.values[1] = "Height"
        df.iloc[:, 0] = df.iloc[:, 0].str.replace(r'(', '', regex=True)# 2 rad kod för att erätta värden i celler med värden utan parenthes
        df.iloc[:, 1] = df.iloc[:, 1].str.replace(r')', '', regex=True)
        df['Width'] = df['Width'].astype(float)# 2 rad kod för att byta strings som finns i varje kolumn (original datatyp) till float
        df['Height'] = df['Height'].astype(float)
        return df