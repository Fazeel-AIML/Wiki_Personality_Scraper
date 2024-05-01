from xml.etree import ElementTree as ET
import json
import math
import html
import urllib.request, urllib.parse, urllib.error
import numpy as np
import cv2 as cv
# import socket
import re
from bs4 import BeautifulSoup as bs

to_search = input("Name Personality:  ")
to_search = to_search.strip().replace(" ","_")
try:
    link = urllib.request.urlopen(f"https://en.wikipedia.org/wiki/{to_search}").read()
    soup = bs(link, "html.parser")
        #Title
    head = soup.find_all("h1",class_="firstHeading")
    for tag in head:
        title = tag.text
    title = str(title)
    print(f"========= Title: {title} =========")

    #Paragraphs
    count = 1
    para = soup.find_all("p")
    for tag in para:
        p_text = tag.text.strip()
        p_text = str(p_text)
        for a in tag.find_all("a"):
            a_link = a.text
            p_text =  p_text.replace(a_link,"\033[32m" + a_link + "\033[0m")
        print(p_text)
        count+=1
        if count==5:
            break
        
    #Title Image
    td_tags = soup.find_all('td',class_="infobox-image")
    for td in td_tags:
        for im in td.find_all("img"):
            url = im.get("src")
            url = str(url)
            url = url.replace("\\","/")
            full_url = urllib.parse.urljoin("https://en.wikipedia.org/wiki/Shah_Rukh_Khan",url)
            img_url = urllib.request.urlopen(full_url).read()
            image_array = np.array(bytearray(img_url),dtype=np.uint8)
            print(image_array)
            im = cv.imdecode(image_array,-1)
            cv.imshow(title,im)
            cv.waitKey(0)
except Exception as e:
    print("Check your Internet Connection Or Give Sophisticated Link")