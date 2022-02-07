# AI4Bharat-Data-Engineer-Internship-Task-2-Pdf-Extractor
Extract pdf content from all the url’s present in the google sheet


Libraries required : pandas, pytesseract (also download tesseract ocr and specify it's path in the Pdf2processor class in pdf2processor.py), pdf2image(also download poppler and specify it's path in the Pdf2processor class in pdf2processor.py), pillow, pathlib, BeautifulSoup.

Instructions: 

* Run pdf_extractor.py, if you have downloaded the csv file.


(If you want to use your own csv file)-->
* Download google sheet and save it in the project folder as "data_pdf.csv".
* Create url column for storing urls. The file can be accessed with pandas.
* Note: These 2 steps can be skipped as I have included the csv file in this project and you can download it directly.
          


There are 3 python files:
* link_extractor.py : It contains LinkExtractor class for extracting pdf links from html based websites. 
* pdf2processor.py : It contains Pdf2processor for extracting pdf files from the links and converting them to images for detecting devnagiri text(marathi in this case).
* pdf_extractor.py : Uses LinkExtractor and Pdf2processor to create JSON file from the urls present in the csv file.

