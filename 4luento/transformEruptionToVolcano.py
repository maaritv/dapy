

import pandas as pd
import numpy as np
import json

##Käytetty data osoitteesta:
##Global Volcanism Program, 2025. [Database] 
## Volcanoes of the World (v. 5.3.2; 30 Sep 2025). 
# Distributed by Smithsonian Institution, 
# compiled by Venzke, E. https://doi.org/10.5479/si.GVP.VOTW5-2025.5.3

def read_csv_file(file_name):
    # Load CSV into a NumPy array
    data = np.genfromtxt(file_name, delimiter=';', skip_header=0, names=True, dtype=None, encoding=None)
    df = pd.DataFrame(data)
    return df

def transform_eruptions_to_volcanos(eruptions_df: pd.DataFrame) -> pd.DataFrame:
    """
    Luodaan volcanos-dataframe eruptions-datasta.
    Mukaan otetaan volcanoNumber (1. sarake) ja volcanoName,
    poistetaan duplikaatit ja lisätään keinotekoinen avain.
    """
    print(eruptions_df.columns)
    eruptions_df.columns = eruptions_df.columns.str.strip()
    volcanos_df = (
        eruptions_df[[eruptions_df.columns[0], 'volcanoName']]
        .drop_duplicates()
        .reset_index(drop=True)
    )

    # Keinotekoinen avain, alkaa arvosta 1
    volcanos_df["volcanoId"] = range(1, len(volcanos_df) + 1)
    #Vaihda sarakkeen nimi
    volcanos_df = volcanos_df.rename(columns={
        volcanos_df.columns[0]: "volcanonumber",
        "volcanoName": "volcanoname"
    })
    return volcanos_df

def save_to_file(pandasDataFrame, fileName):
    filePath=f"./output/{fileName}"
    pandasDataFrame.to_csv(filePath, index=False)


# -------------------------------------------------------------------
#   Esimerkinomainen ajettava kokonaisuus (voit poistaa tai muokata)
# -------------------------------------------------------------------

if __name__ == "__main__":
    eruptions = read_csv_file("eruptions.csv")
    print("=== Alkuperäinen data ===")
    print(eruptions, "\n")

    # Suodatus vuosiluvun mukaan
    volcanos = transform_eruptions_to_volcanos(eruptions)
    print("=== Tulivuoret ===")
    print(volcanos, "\n")
    save_to_file(volcanos, "myvolcanos.csv")


   
