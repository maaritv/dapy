import numpy as np

def load_bookloan_data(file_path):
    # Load the data from a CSV file
    data = np.genfromtxt(file_path, delimiter=';', dtype=None, encoding=None, names=True)
    return data

def remove_bookloans_with_unknown_return_date(data):
    filtered_data = data[data['return_date'] != '']
    return filtered_data

def print_bookloans(data):
    print("Tulosrivien määrä:\t", len(data))
    for row in data:
        print(row)

# Sample file path
file_path = './bookloans.csv'

# Load the data
bookloan_data = load_bookloan_data(file_path)

# Filter the data
filtered_bookloan_data = remove_bookloans_with_unknown_return_date(bookloan_data)

print_bookloans(filtered_bookloan_data)


