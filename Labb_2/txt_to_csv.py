import pandas as pd

txt_files = ['pichu','pikachu']

for file in txt_files:
    read_file = pd.read_csv (f'{file}.txt')
    read_file.to_csv (f'{file}.csv', index=None)

