

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

def read_json_file(file_name):
    # Lue JSON tiedostosta
    with open(file_name, "r") as f:
        data_list = json.load(f)  

        # Muunna NumPy arrayksi
        data_array = np.array(data_list)
        return data_array

# -------------------------------------------------------------------
#   Eruptiotietojen käsittelyfunktiot
# -------------------------------------------------------------------

def prepare_eruptions(pandasDataFrame: pd.DataFrame) -> pd.DataFrame:
    """
    Varmistaa, että päivämääräsarake on datetime-tyyppiä.
    """
    pandasDataFrameCopy = pandasDataFrame.copy()
    try:
        pandasDataFrameCopy["edate"] = pd.to_datetime(pandasDataFrameCopy["edate"], errors="coerce")
    except KeyError:
        print(f"Saraketta 'edate' ei löydy. Saatavilla olevat sarakkeet: {pandasDataFrameCopy.columns}")
    except Exception as e:
        print(f"Tapahtui virhe: {e}")
    return pandasDataFrameCopy


def filter_eruptions_by_years(from_year: int, eruptions_df: pd.DataFrame) -> pd.DataFrame:
    """
    Palauttaa purkaukset, jotka ovat tapahtuneet after from_year.
    """
    df = prepare_eruptions(eruptions_df)
    return df[df["edate"].dt.year > from_year]


def filter_eruptions_by_name(name: str, eruptions_df: pd.DataFrame) -> pd.DataFrame:
    """
    Suodattaa purkaukset, joiden nimi alkaa tietyllä merkkijonolla.
    Vastaa JS:n filterEruptionsByName.
    """
    return eruptions_df[eruptions_df["volcanoName"].str.startswith(name)]


# -------------------------------------------------------------------
#   Esimerkinomainen ajettava kokonaisuus (voit poistaa tai muokata)
# -------------------------------------------------------------------

if __name__ == "__main__":
    eruptions = read_csv_file("eruptions.csv")
    print("=== Alkuperäinen data ===")
    print(eruptions, "\n")

    # Suodatus vuosiluvun mukaan
    after_2000 = filter_eruptions_by_years(2000, eruptions)
    print("=== Purkaukset vuoden 2000 jälkeen ===")
    print(after_2000, "\n")

    # Suodatus nimen perusteella
    etna_only = filter_eruptions_by_name("Etna", eruptions)
    print("=== Purkaukset joiden nimi alkaa 'Etna' ===")
    print(etna_only, "\n")

