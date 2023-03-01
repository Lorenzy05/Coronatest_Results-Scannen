import pandas as pd
from pandas import DataFrame

File = "D:\WPS\Excel\Coronatest_Resultaten.xlsx"

dataframe = pd.read_excel(File)

RESULTATEN = [
               'Onbekend', 'Positief', 'Onbekend', 'Onbekend', 'Negatief', 'Negatief', 'Positief', 'Positief', 'Positief', 'Positief',
               'Positief', 'Negatief', 'Negatief', 'Onbekend', 'Positief', 'Positief', 'Positief', 'Positief', 'Positief', 'Onbekend',
               'Onbekend', 'Negatief', 'Negatief', 'Negatief', 'Negatief', 'Negatief', 'Negatief', 'Positief', 'Negatief', 'Negatief'
             ]

dataframe['Resultaten'] = RESULTATEN

DataFrame(dataframe).to_excel(File, index=False, header=True)


