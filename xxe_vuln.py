import xml.etree.ElementTree as ET

def parse_xml(data):
    root = ET.fromstring(data)  # Vulnerable to XXE if external entities are allowed
