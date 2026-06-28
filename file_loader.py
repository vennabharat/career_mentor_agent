from pypdf import PdfReader # importing pdf reader for extracting text from pdf files

import json 

# for reading txt file
def load_txt(file_path):
    with open(file_path) as file:
        data = file.read()
    
    return data

# for reading pdf file
def load_pdf(file_path):
    reader = PdfReader(file_path)
    
    text = ""
    
    for page in reader.pages:
        text += page.extract_text() + "\n"
        
    return text

# for reading json file
def load_json(file_path):
    with open(file_path) as file:
        data = json.load(file)
        
    return json.dumps(data, indent=2)