class LinkExtractor:

    def __init__(self,url):
        self.url=url
        split_url=urlsplit(url)
        self.base_url="https://"+str(split_url.netloc)
    
    def get_pdf_link(self):
        response=requests.get(self.url)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a')
        for link in links:
            if ".pdf" in link.get("href",[]):
                self.total_url=self.base_url+link.get("href")
                return self.total_url