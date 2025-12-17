import pyarrow.parquet as pq
import pyarrow.compute as pc
import pyarrow as pa
import os
import time
import duckdb

### Asenna viimeisin version DuckDB -paketista?
#pip3 install --upgrade duckdb

def filter_dataset_duck(file_name, first_name="Alice", min_amount=500):
    
    # Yhdistä DuckDB
    con = duckdb.connect()

# Lue Parquet/ORC ja tee SQL-suodatus.
# Huom: älä anna käyttäjän syöttää tiedostonimeä. Tämä EI OLE 
# SQL-injektioturvallinen tapa lisätä tiedoston nimi kyselyyn! 
    query = f"""
    SELECT *
    FROM '{file_name}'
    WHERE name LIKE ? AND CAST(amount AS BIGINT) > ?
    """

    results = con.execute(query, (f"{first_name}%", min_amount)).fetchall()
    return results


def print_results(results=[]):
    for row in results:
            print(row)

def main():
    results=[]
    file_path = "output.parquet"
    """
    Lukee Parquet-tiedoston ja suodattaa rivit, joiden etunimi on first_name
    ja amount on suurempi kuin min_amount.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Tiedostoa ei löydy: {file_path}")
    
    start_time = time.time()  # Suorituskykymittaus alkaa
    results = filter_dataset_duck(file_path, first_name="Alice", min_amount=500)
    elapsed_time = (time.time() - start_time) * 1000  # ms
    print(f"Löydettiin {len(results)} riviä Parquet-tiedostosta, joissa etunimi 'Alice' ja amount > 500: Kesto: {elapsed_time}\n")
    print_results(results)

if __name__ == "__main__":
    main()
