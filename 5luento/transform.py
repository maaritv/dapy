from lxml import etree
import validate as validate


def transform(xml_file, xslt_file):
    xml = etree.parse(xml_file)
    xslt = etree.parse(xslt_file)

    # Create an XSLT transform object
    transform = etree.XSLT(xslt)

    # Apply the transformation
    result = transform(xml)
    # Print the result
    #print(str(result))
    return (str(result))

# Load the XML and XSLT files
xml_file = 'data/books.xml'
xslt_file = 'xslt/book-to-dublincore.xslt'
xsd_file="schemas/books.xsd"

try:
    validate.validate_xml_with_xsd(xml_file, xsd_file)
    result = transform(xml_file, xslt_file)
    print("Skeemamuunnos onnistui.")
    print(result)
except (ValueError) as e:
    print(f"Virhe {e}")
