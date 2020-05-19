from bs4 import BeautifulSoup
from selenium import webdriver
import io
import re
import urllib.request

def getUrl(file):
    f = open(file, "r")
    atxt = f.read()
    soup = BeautifulSoup(atxt, 'html.parser')
    imurl = soup.find("meta", {"property":"og:image"})['content']
    imus = imurl.split("/slides/")
    print(imus[0])
    p = re.compile("small_slide_\([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\)\.png")
    res1 = p.findall(atxt)
    reslen = len(res1)
    for i in range(0, reslen//2):
        tpic = res1[i]
        tpic = tpic.replace("small_slide","large_slide")
        tpic = tpic.replace(".png",".jpg")
        turl = imus[0] + "/slide/" + tpic
        print(turl)
        urllib.request.urlretrieve(turl,"./download/p"+str(i+1)+".jpg")
        print("OK "+str(i))
