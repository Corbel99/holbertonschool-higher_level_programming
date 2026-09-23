#!/usr/bin/env python3
"""Serialize and deserialize Python dictionaries using XML."""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a Python dictionary to XML and save it to a file."""
    root = ET.Element("data")

    for key, value in dictionary.items():
        element = ET.SubElement(root, key)
        element.text = value

    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """Deserialize an XML file and return a Python dictionary."""
    tree = ET.parse(filename)
    root = tree.getroot()

    dictionary = {}

    for element in root:
        dictionary[element.tag] = element.text

    return dictionary
