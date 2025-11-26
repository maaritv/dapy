import numpy as np
import pandas as pd

##Muunnetaan data pandas data frameksi 
## käsittelyä varten

def load_bookloan_data(file_path):
    # Load the data from a CSV file
    data = np.genfromtxt(file_path, delimiter=';', dtype=None, encoding=None, names=True)
    df = pd.DataFrame(data)
    return df

#~ tarkoittaa bitwise NOT -operaattoria. käännettään true falseksi tai 
# toisinpäin.
def remove_bookloans_with_unknown_return_date(data):
    #eli return date EI ole "not a number" (isna) JA return date ei ole tyhjä merkkijono 
    mask = (~data['return_date'].isna()) & (data['return_date'] != '')
    #Käytetään maskia
    filtered_data = data[mask]
    return filtered_data

def print_bookloans(data):
    print("Tulosrivien määrä:\t", len(data))
    print(data)

# Sample file path
file_path = './bookloans.csv'

# Load the data
bookloan_data = load_bookloan_data(file_path)

# Filter the data
filtered_bookloan_data = remove_bookloans_with_unknown_return_date(bookloan_data)

print_bookloans(filtered_bookloan_data)


