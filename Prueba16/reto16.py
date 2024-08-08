import re

texto = "wy99w6k0icr3iw8bpifh3959z2f5x9"
patron = r"\d+"

numeros = re.findall(patron,texto)

print(f"Numeros encontrados : {numeros}")
