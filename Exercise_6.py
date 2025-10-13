with open('output.txt', "wb") as file:
    text = "Hôm nay trời đẹp"
    binary_text = text.encode('utf-8')
    file.write(binary_text)