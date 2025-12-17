# XML skeemavalidointi pythonilla

Esimerkin rakennetta on muokattu:

* data - hakemisto sisältää nyt xml-tiedostot
* schemas - sisältää xsd-skeemat, joita validointi tarvitsee
* xslt sisältää muunnokseen tarvittavat säännöt

## Tiedon validointi

Validate varmistaa, että customer.xml on oikean muotoinen.

Aja sovellus <b>5luento-hakemistosta</b>: 

```
  python3 ./validate.py
```

## Tiedon muuntaminen

Transform muuttaa kirja.xml-tiedoston Dublin core XML-muotoon.

Aja sovellus <b>5luento-hakemistosta</b>: 

```
  python3 ./transform.py
```

Transform suorittaa ensin tiedon validoinnin, ja vasta sitten muuntaa tiedon, jos muunnettava tiedosto on validi.
Tähän tarkoitukseen otetaan import-komennolla mukaan validate-modulista validate_xml_with_xsd -funktio, jolla kirja ensin validoidaan.
