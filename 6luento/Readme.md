
# Datan tallennus ja siirtomuodot

Esimerkki käyttää Apache Arrow pyarrow-kirjastoa, joka osaa 
muuntaa tallettaa dataa sekä ORC että Parquet -muotoihin.

* https://arrow.apache.org/docs/python/install.html
* https://arrow.apache.org/docs/python/getstarted.html


```
pip3 install pyarrow
```

* Luo tarvittava testidata, muokkaamalla create_fake_data.py -modulia. Vaihda luotavan datasetin kokoa esim. 100-> 2 000 000. Huomaa, että iso datasetti vie paljon levytilaa.

* Luo testidata input.csv ajamalla:

```
  python3 ./create_fake_data.py
```
* Muunna input.csv tiedosto orc ja parquet -muotoihin:

```
python3 ./convert_data_to_storage_formats.py
```

* Tarkista output-tiedostojen koot ls tai dir-komennolla terminaalissa.

* Lue tuloksena tulleet tiedostot read_files.py ohjelmalla ja tarkista, kauanko tiedostojen lukemiseen meni.

* Vertaa lukemia 100, 2000, 500 000 ja 1 000 000 objektia sisältävien datatiedostojen lukemisessa. 

* Muuta esimerkkiä niin, että tulostat tiedostoista viimeisen rivin. Muuttuvatko lukemat?

