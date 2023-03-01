import pandas as pd
from pandas import DataFrame

True_Resultaten = [
               'Onbekend', 'Positief', 'Onbekend', 'Onbekend', 'Negatief', 'Negatief', 'Positief', 'Positief', 'Positief', 'Positief',
               'Positief', 'Negatief', 'Negatief', 'Onbekend', 'Positief', 'Positief', 'Positief', 'Positief', 'Positief', 'Onbekend',
               'Onbekend', 'Negatief', 'Negatief', 'Negatief', 'Negatief', 'Negatief', 'Negatief', 'Positief', 'Negatief', 'Negatief'
             ]
File = "D:\WPS\Excel\Coronatest_Resultaten.xlsx"

df = pd.read_excel(File)

df['Resultaten'] = True_Resultaten

DataFrame(df).to_excel(File, index=False, header=True)



def Add_Info(file, r):
    Excel_file = File
    resultaat  = r

    df = pd.read_excel(Excel_file)
    df['Resultaten'] = resultaat

    DataFrame(df).to_excel(Excel_file, index=False, header=True)

    print("-----Saved to " + str(Excel_file))
