from lxml import etree

def validate_xml_with_xsd(xml_file, xsd_file):
    """
    Validate an XML file against an XSD file.

    :param xml_file: Path to the XML file.
    :param xsd_file: Path to the XSD file.
    :return: True if the XML file is valid, False otherwise.
    """
    try:
        # Parse the XML and XSD files
        xml_doc = etree.parse(xml_file)
        with open(xsd_file, 'rb') as xsd_file_handle:
            xsd_doc = etree.XML(xsd_file_handle.read())

        # Create an XMLSchema object
        xmlschema = etree.XMLSchema(xsd_doc)

        # Validate the XML file
        xmlschema.assertValid(xml_doc)
        print(f"The XML file '{xml_file}' is valid against the XSD '{xsd_file}'.")
        return True
    except etree.XMLSchemaError as e:
        print(f"The XML file '{xml_file}' is not valid against the XSD '{xsd_file}'.")
        print(f"Error: {e}")
        return False
    except (etree.XMLSyntaxError, IOError) as e:
        print(f"An error occurred: {e}")
        return False

if __name__ == "__main__":
    # Example usage
    xml_file_path = 'customer.xml'  # Replace with your XML file path
    xsd_file_path = 'customer.xsd'   # Replace with your XSD file path

    result=validate_xml_with_xsd(xml_file_path, xsd_file_path)
