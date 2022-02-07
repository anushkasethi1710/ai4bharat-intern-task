# Task1 wiki_extractor.py
# SUBMITTED BY ANUSHKA SETHI

# Libraries are imported
import requests     
from bs4 import BeautifulSoup
import json
import argparse


# Function having keyword, number of urls to be extracted and the output filename as input arguments
def wiki_extractor(keyword, num_urls, output_file_name):
    n = num_urls
    search_query = str(keyword)
    words = search_query.split(" ")
    search_keyword = '+'.join(x for x in words)
    url = "https://en.wikipedia.org/w/index.php?title=Special:Search&limit="+str(n)+"&offset=0&ns0=1&search=" +\
          search_keyword  # base query with num_urls and keyword as arguments
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    result = []
    for link in soup.findAll('div', {'class': 'mw-search-result-heading'}):  # Searching for particular div tags that
        # contain the anchor tag with the url of the title
        href = "https://en.wikipedia.org"+link.find('a')['href']
        url, text = get_url_and_para(href)  # This function will return the url as well as one paragraph from that page
        dict = {"url": url, "paragraph": text}
        result.append(dict)  # storing the result as a list of dictionaries
    output_file = output_file_name+".json"
    out_file = open(output_file, "w")
    json.dump(result, out_file, indent=2)  # saving the extracted data as a json file
    out_file.close()


def get_url_and_para(item_url):
    source_code = requests.get(item_url)   # Takes url of the related topic as input
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    data = soup.find('div', {'class' : 'mw-parser-output'}).findAll('p', {"class": None})  # Finds out the first
    # paragraph tag that does not have any class attribute
    return item_url, data[0].get_text()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--keyword', action='store', type=str, help='Enter keyword')
    parser.add_argument("--num_urls", action='store', type=int, help='Enter number of related urls to be extracted')
    parser.add_argument("--output", action='store', type=str, help="Enter output file name")
    args = parser.parse_args()
    wiki_extractor(args.keyword, args.num_urls, args.output)
