import unittest

# Crear Diccionario con los datos
data = {
    "name": "Carlos",
    "last_name": "Sanchez",
    "age": 45,
    "birth_date": "2000-08-16",
    "programming_languages": ["Python"]
}

print(data)

class TestData(unittest.TestCase):
    def test_campos_texto(self):
        self.assertIn("name", data)  # existe el campo name
        self.assertIn("last_name", data)  # existe el campo last_name
        self.assertIn("age", data)  # existe el campo age
        self.assertIn("birth_date", data)  # existe el campo birth date
        self.assertIn("programming_languages", data)  # existe el campo programming languages

    def test_datos_correctos(self):
        # Verificar que los datos introducidos son correctos
        self.assertEqual(data["name"], "Carlos")
        self.assertEqual(data["last_name"], "Sanchez")
        self.assertEqual(data["age"], 45)
        self.assertEqual(data["birth_date"], "2000-08-16")
        self.assertEqual(data["programming_languages"], ["Python"])    
        

# Ejecutar las pruebas
if __name__ == '__main__':
    unittest.main()
