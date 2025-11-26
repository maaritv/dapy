

import pandas as pd
import numpy as np
import json

##Käytetty data osoitteesta:
##Global Volcanism Program, 2025. [Database] 
## Volcanoes of the World (v. 5.3.2; 30 Sep 2025). 
# Distributed by Smithsonian Institution, 
# compiled by Venzke, E. https://doi.org/10.5479/si.GVP.VOTW5-2025.5.3



def read_json_file(file_name):
    with open(file_name, "r") as f:
        data_list = json.load(f)

    df = pd.DataFrame(data_list)
    return df



def filter_volcanoes_by_country(country: str, volcano_df: pd.DataFrame) -> pd.DataFrame:
    """
    Palauttaa tietyn valtion tulivuoret.
    """
    
    return volcano_df[volcano_df["country"].str.startswith(country)]


# -------------------------------------------------------------------
#   Esimerkinomainen ajettava kokonaisuus (voit poistaa tai muokata)
# -------------------------------------------------------------------

if __name__ == "__main__":
    country="Japan"
    volcanos = read_json_file("volcanos.json")
    print("=== Alkuperäinen data ===")
    print(volcanos, "\n")

    # Suodatus nimen perusteella
    country_volcanos = filter_volcanoes_by_country(country, volcanos)
    print(f"=== Tulivuoret '{country}:ssa' ===")
    print(country_volcanos, "\n")

