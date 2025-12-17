import pyarrow as pa
import pyarrow.parquet as pq
import pyarrow.orc as orc
import os
import sys
import time


class DataReadError(Exception):
    """Virhe datan lukemisessa"""
    pass


def show_file_content(file_path):
    """
    Lukee ORC- tai Parquet-tiedoston, mittaa lukuajan ja tulostaa sisällön
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Tiedostoa ei löydy: {file_path}")

    try:
        if file_path.lower().endswith(".orc"):
            with open(file_path, "rb") as f:
                table = orc.read_table(f)
        elif file_path.lower().endswith(".parquet"):
            table = pq.read_table(file_path)
        else:
            raise DataReadError("Tiedostomuoto ei ole ORC tai Parquet")

        # Muutetaan Arrow Table listaksi sanakirjoja
        
        data = table.to_pylist()
        '''
        for row in data:
            print(row)
        '''
        return data

    except Exception as e:
        raise DataReadError(f"Tiedoston '{file_path}' lukeminen epäonnistui: {e}")


def main():
    orc_file = "output.orc"
    parquet_file = "output.parquet"

    try:
        start_time = time.time()  # Suorituskykymittaus alkaa
        show_file_content(orc_file)
        elapsed_time = (time.time() - start_time) * 1000  # ms
        print(f"\nSisältö tiedostossa '{orc_file}' (luettu {elapsed_time:.2f} ms):")
        

        start_time = time.time()  # Suorituskykymittaus alkaa
        show_file_content(parquet_file)
        elapsed_time = (time.time() - start_time) * 1000  # ms
        print(f"\nSisältö tiedostossa '{parquet_file}' (luettu {elapsed_time:.2f} ms):")
        

    except FileNotFoundError as e:
        print(f"[VIRHE] {e}")
        sys.exit(1)

    except DataReadError as e:
        print(f"[VIRHE] {e}")
        sys.exit(2)

    except Exception as e:
        print(f"[ODOTTAMATON VIRHE] {e}")
        sys.exit(99)


if __name__ == "__main__":
    main()
