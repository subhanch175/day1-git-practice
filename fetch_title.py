import requests
from bs4 import BeautifulSoup
import logging

logging.basicConfig(filename= "Error.log", level= logging.ERROR, format= "%(asctime)s - %(levelname)s - %(message)s")

def title_fatch(url):
    page = 1
    title = "Not Found"
    
    all_books = []
    while True:
        
        if page == 1:
        
            current_url = url
        else:
            current_url = f"http://books.toscrape.com/catalogue/page-{page}.html"
        
    
        try:
            responce = requests.get(current_url, timeout= 5)
            responce.raise_for_status()
        except requests.exceptions.HTTPError as e:
            logging.error(f"Network Error: {e}")
            break
        except requests.exceptions.RequestException as e:
            logging.error(f"Request Error: {e}")
            break
    
        soup = BeautifulSoup(responce.text, "html.parser")
        
        books = soup.find_all("article", class_= "product_pod")
        
        if not books:
            break
        
        for b in books:
            
            h3_tag = b.find("h3")
            
            if h3_tag is None:
                logging.error("H3 Tag Missing")
                continue
            
            a_tag = h3_tag.find("a")
            
            if a_tag is None:
                logging.error("A Tag Is Missing")
                continue
            title = a_tag.get("title")
            
            if title is None:
                logging.error("Title Not Found")
                continue
            all_books.append(title)
        page += 1
        
            
    return all_books

def main():
    url = "https://books.toscrape.com"
    
    all_books = title_fatch(url)
    
    print(all_books)

main()
    
            

        