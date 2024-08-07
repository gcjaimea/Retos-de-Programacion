import os
import json
import xml.etree.ElementTree as ET


class Persona:
    def __init__(self,nombre, apellido, edad, fecha_nacimiento,lenguajes_programacion):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.fecha_nacimiento = fecha_nacimiento
        self.lenguajes_programacion = lenguajes_programacion
    
    def __repr__(self): #devuelve una cadena legible de un objeto
        return (f"Persona(Nombre={self.nombre}, Apellido={self.apellido}"
                f"Edad={self.edad}, Fecha de Nacimiento={self.fecha_nacimiento}"
                f"Lenguajes de Programacion={self.lenguajes_programacion})")
    
# Datos
data = {
    "Nombre": "Carlos",
    "Apellido": "Sanchez",
    "Edad": 50,
    "Fecha de Nacimiento": "1974-03-09",
    "Lenguajes de Programación" : ["Python"]
}

# Crear archivo JSON
json_filename = 'data.json'
with open(json_filename, 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, indent=4, ensure_ascii=False)
print(f"Archivo JSON '{json_filename}' creado.")

# Crear archivo XML
xml_filename = 'data.xml'
root = ET.Element("persona")
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
tree.write(xml_filename, encoding='utf-8', xml_declaration=True)
print(f"Archivo XML '{xml_filename}' creado.")

# Leer y transformar datos del archivo JSON
with open(json_filename, 'r', encoding='utf-8') as json_file:
    json_data = json.load(json_file)
persona_from_json = Persona(
    nombre=json_data["Nombre"],
    apellido=json_data["Apellido"],
    edad=json_data["Edad"],
    fecha_nacimiento=json_data["Fecha de Nacimiento"],
    lenguajes_programacion=json_data["Lenguajes de Programación"]
)
print("Datos transformados desde JSON:")
print(persona_from_json)

# Leer y transformar datos del archivo XML
tree = ET.parse(xml_filename)
root = tree.getroot()
xml_data = {}
for elem in root:
    if elem.tag == "Lenguajes_de_programacion":
        xml_data[elem.tag.replace("_", " ")] = [item.text for item in elem]
    else:
        xml_data[elem.tag.replace("_", " ")] = elem.text

persona_from_xml = Persona(
    nombre=xml_data["Nombre"],
    apellido=xml_data["Apellido"],
    edad=xml_data["Edad"],
    fecha_nacimiento=xml_data["Fecha de Nacimiento"],
    lenguajes_programacion=xml_data["Lenguajes de Programación"]
)
print("Datos transformados desde XML:")
print(persona_from_xml)

# Borrar archivos
os.remove(json_filename)
os.remove(xml_filename)
print(f"Archivos '{json_filename}' y '{xml_filename}' borrados.")