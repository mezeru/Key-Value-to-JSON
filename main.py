import docx
import json
import os

dict = {}

def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        line = para.text.split(":")
        line[0] = line[0].strip()
        line[1] = line[1].strip()
        dict[line[0]] = line[1]


if __name__ == "__main__":
    print("Enter The name of the file : ", end="")
    name = "/Content.docx"
    name = str(os.getcwd()) + name
    print(name)
    try:
        getText(name)
    except:
        None

content_json = json.dumps(dict)

file = open("content.json", "w+")
file.write(content_json)
file.close()
