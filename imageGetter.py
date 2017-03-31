import requests
from bs4 import BeautifulSoup
import urlparse

def getImg():
    url = "https://www.walmart.com/ip/54649026"
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    
    imgs = []
    

    og_image = (soup.find('meta', property='og:image') or
                        soup.find('meta', attrs={'name': 'og:image'}))
    if og_image and og_image['content']:
        pass


    thumbnail_spec = soup.find('link', rel='image_src')
    if thumbnail_spec and thumbnail_spec['href']:
        pass


    for img in soup.findAll("img", src=True):

        if img["src"] not in imgs:
            imgs.append(img["src"])
    #Returns images   
    return imgs