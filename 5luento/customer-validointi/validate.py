from lxml import etree

def validate_xml_with_xsd(xml_file, xsd_file):
    try:
        # Parse the XML and XSD files
        xml_doc = etree.parse(xml_file)
        with open(xsd_file, 'rb') as xsd_file_handle:
            xsd_doc = etree.XML(xsd_file_handle.read())

        # Create an XMLSchema object
        xmlschema = etree.XMLSchema(xsd_doc)

        # Validate the XML file
        xmlschema.assertValid(xml_doc)
        return True
    except(etree.DocumentInvalid) as e:
        raise ValueError(f"The XML file '{xml_file}' is not valid against the XSD '{xsd_file}' {e}.")
    except (etree.XMLSyntaxError, IOError) as e:
        raise ValueError(f"Syntax error {e}")

if __name__ == "__main__":
    # Example usage
    xml_file_path = 'customer.xml'  # Replace with your XML file path
    xsd_file_path = 'customer.xsd'   # Replace with your XSD file path

    try:
        result=validate_xml_with_xsd(xml_file_path, xsd_file_path)
        print(f"The XML file '{xml_file_path}' is valid against the XSD '{xsd_file_path}'.")
    except (ValueError) as e:
        print(f"Validointivirhe! Customer.xml ei ole customer.xsd -skeeman mukainen. {e}")
