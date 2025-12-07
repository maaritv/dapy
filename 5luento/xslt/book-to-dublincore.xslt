<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:dc="http://purl.org/dc/elements/1.1/">

    <xsl:template match="/">
        <Records>
            <xsl:apply-templates select="Library/Books/Book"/>
        </Records>
    </xsl:template>

    <!-- Skeemakohdistus Book elementistä Dublin Core-elementiksi. -->
    <xsl:template match="Book">
        <dc:record>
            <dc:title><xsl:value-of select="Title"/></dc:title>
            <dc:creator><xsl:value-of select="Author"/></dc:creator>
            <dc:subject><xsl:value-of select="Genre"/></dc:subject>
            <dc:date><xsl:value-of select="PublishedYear"/></dc:date>
            <dc:identifier><xsl:value-of select="ISBN"/></dc:identifier>
            <dc:description><xsl:value-of select="Summary"/></dc:description>
        </dc:record>
    </xsl:template>

</xsl:stylesheet>
