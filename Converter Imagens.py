# Precisa atualizar o PIP Install

from PIL import image

image_file = Image.open(r".\Prism_3200x1800.png")

image_file = image_file.convert('L')

image_file.save(r".\Prism_preta_e_branca.png")