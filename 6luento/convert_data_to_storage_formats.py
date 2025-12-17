import csv
import os
import sys
import pyarrow as pa
import pyarrow.parquet as pq
import pyarrow.orc as orc


class DataProcessingError(Exception):
    """Yleinen virhe datan käsittelyyn"""
    pass


def read_csv_to_objects(csv_path):
    """
    Lukee CSV-tiedoston ja palauttaa listan sanakirjoja
    """
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"CSV-tiedostoa ei löydy: {csv_path}")

    if not csv_path.lower().endswith(".csv"):
        raise DataProcessingError("Syötetiedosto ei ole CSV-muotoinen")

    try:
        with open(csv_path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)

            if not reader.fieldnames:
                raise DataProcessingError("CSV-tiedostossa ei ole otsikkoriviä")

            rows = list(reader)

            if not rows:
                raise DataProcessingError("CSV-tiedosto on tyhjä")

            return rows

    except csv.Error as e:
        raise DataProcessingError(f"CSV-luku epäonnistui: {e}")


def write_orc(data, output_path):
    """
    Tallentaa datan ORC-muotoon
    """
    if not data:
        raise DataProcessingError("ORC-kirjoitus epäonnistui: data on tyhjä")

    try:
        table = pa.Table.from_pylist(data)

        with open(output_path, "wb") as f:
            orc.write_table(table, f)

    except pa.ArrowInvalid as e:
        raise DataProcessingError(f"Virhe ORC-skeemassa tai datassa: {e}")

    except OSError as e:
        raise DataProcessingError(f"ORC-tiedostoon kirjoitus epäonnistui: {e}")


def write_parquet(data, output_path):
    """
    Tallentaa datan Parquet-muotoon
    """
    if not data:
        raise DataProcessingError("Parquet-kirjoitus epäonnistui: data on tyhjä")

    try:
        table = pa.Table.from_pylist(data)
        pq.write_table(table, output_path)

    except pa.ArrowInvalid as e:
        raise DataProcessingError(f"Virhe Parquet-skeemassa tai datassa: {e}")

    except OSError as e:
        raise DataProcessingError(f"Parquet-tiedostoon kirjoitus epäonnistui: {e}")


def main():
    csv_file = "input.csv"
    orc_file = "output.orc"
    parquet_file = "output.parquet"

    try:
        data = read_csv_to_objects(csv_file)

        write_orc(data, orc_file)
        write_parquet(data, parquet_file)

        print("Tallennus valmis:")
        print(f"- ORC: {orc_file}")
        print(f"- Parquet: {parquet_file}")

    except FileNotFoundError as e:
        print(f"[VIRHE] {e}")
        sys.exit(1)

    except DataProcessingError as e:
        print(f"[VIRHE] {e}")
        sys.exit(2)

    except Exception as e:
        print(f"[ODOTTAMATON VIRHE] {e}")
        sys.exit(99)


if __name__ == "__main__":
    main()
