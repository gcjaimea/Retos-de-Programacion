import json
import xml.etree.ElementTree as ET
import os

# Data a ser guardada en el archivo
data = {
    "Nombre": "Juan Perez",
    "Edad": 50,
    "Fecha de nacimiento": "1974-03-30",
    "Lenguajes de programación": ["Python"]
}

# Crear el archivo JSON con los datos
json_filename = 'data.json'
with open(json_filename, 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, indent=4, ensure_ascii=False) # dump() para cargar el archivo e indent para crear unos espacios vacios
print(f"Archivo JSON '{json_filename}' creado.")

# Mostrar contenido del archivo JSON
with open(json_filename, 'r', encoding='utf-8') as json_file:
    json_content = json_file.read()
    print("Contenido del archivo JSON:")
    print(json_content)

    # Crear archivo XML con los datos
xml_filename = 'data.xml'
root = ET.Element("Persona")
for key, value in data.items():
    if isinstance(value, list):
        elem = ET.SubElement(root, key.replace(" ", "_"))
        for item in value:
            sub_elem = ET.SubElement(elem, "item")
            sub_elem.text = item
    else:
        elem = ET.SubElement(root, key.replace(" ", "_"))
        elem.text = str(value)

tree = ET.ElementTree(root)
tree.write(xml_filename, encoding='utf-8',xml_declaration=True)
print(f"Archivo XML '{xml_filename}' creado.")



# Mostrar contenido del archivo XML
tree = ET.parse(xml_filename)
root = tree.getroot()
print("Contenido del archivo XML:")
ET.dump(root)


# Borrar archivos
os.remove(json_filename)
os.remove(xml_filename)
print(f"Archivos '{json_filename}' y '{xml_filename}' borrados.")


