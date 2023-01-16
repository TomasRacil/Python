def open_file(path:str)->str:
    with open(path, 'r',encoding='utf-8') as file:
        text = file.read()
    return text
def write_to_file(path:str, text: str)->None:
    with open(path, 'w',encoding='utf-8') as file:
        file.write(text)