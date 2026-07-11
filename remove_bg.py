from rembg import remove
from PIL import Image

input_path = "src/assets/Logo Print Studio.jpeg"
output_path = "src/assets/logo.png"

with open(input_path, "rb") as i:
    input_data = i.read()
    output_data = remove(input_data)

with open(output_path, "wb") as o:
    o.write(output_data)

print("Listo! Logo guardado en:", output_path)
