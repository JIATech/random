import base64

with open("accept ui.png", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode()

with open("encoded_string.txt", "w") as file:
    file.write(encoded_string)
