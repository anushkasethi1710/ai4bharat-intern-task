class Pdf2processor:
    
    def __init__(self,pdf_url):
        self.pdf_url=pdf_url
    
    def process(self):
        filename= Path(self.pdf_url.split("/")[-1])
        response = requests.get(self.pdf_url)
        filename.write_bytes(response.content)
        self.images = convert_from_path(filename,poppler_path=r"C:\poppler-0.68.0\bin")
        return self.images
        
    def generate_text(self):
        images=self.process()
        pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        self.text=[]
        for x in images:
            try:
                page_text="\n"+str(((pytesseract.image_to_string(x,lang="hin"))))
                page_text = page_text.replace('-\n', '')
                self.text.append(page_text)
            except:
                continue
        return self.text

        