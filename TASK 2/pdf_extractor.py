import pandas as pd
import requests
from bs4 import BeautifulSoup
from pathlib import Path
from pdf2image import convert_from_path
from PIL import Image
import pytesseract
from urllib.parse import urlsplit
import json


from link_extractor import LinkExtractor
from pdf2processor import  Pdf2processor

pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files(x86)\Tesseract-OCR\tesseract.exe"

Url=pd.read_csv("data_pdf.csv")["Url"]

webbased_url=[]
pdfbased_url=[]


for x in Url:
    if ".pdf" in x:
        try:
            text_obj=Pdf2processor(x)
            pdfbased_url.append({"page-url":str(x),"pdf-url":str(x),"pdf-content":text_obj.generate_text()})
        except:
            continue
    else:
        try:
            obj=LinkExtractor(x)
            text_obj=Pdf2processor(obj.get_pdf_link())
            webbased_url.append({"page-url":str(x),"pdf-url":str(obj.get_pdf_link()),"pdf-content":text_obj.generate_text()})
        except:
            continue
        

json_object=webbased_url+pdfbased_url
json_object=json.dumps(json_object,indent=3)
print(json_object)

with open("pdf_extract.json", "w") as outfile:
    outfile.write(json_object)
