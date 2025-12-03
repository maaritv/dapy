from lxml import etree

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
xml_file = 'books.xml'
xslt_file = 'book-to-dublincore.xslt'

result = transform(xml_file, xslt_file)
print(result)
