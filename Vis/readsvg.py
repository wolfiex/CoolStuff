from xml.dom import minidom

doc = minidom.parse(svg_file)  # parseString also exists
path_strings = [path.getAttribute('d') for path
                in doc.getElementsByTagName('path')]
doc.unlink()
