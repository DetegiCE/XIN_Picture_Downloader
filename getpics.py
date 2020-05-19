import io
import re
import urllib.request
from bs4 import BeautifulSoup

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
    print("Pictures Downloading...")
    for i in range(0, reslen//2):
        tpic = res1[i]
        tpic = tpic.replace("small_slide","large_slide")
        tpic = tpic.replace(".png",".jpg")
        turl = imus[0] + "/slide/" + tpic
        urllib.request.urlretrieve(turl,"./download/p"+str(i+1)+".jpg")
        print(str(i+1)+"/"+str(reslen//2)+" Complete")
    print("Pictures Downloading complete")
    print("MP4 Downloading...",end='')
    q = re.compile("main_\([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\)\.mp4")
    res2 = q.findall(atxt)
    aurl = imus[0].replace("web_files","media_files") + "/" + res2[0]
    urllib.request.urlretrieve(aurl, "./download/audio.mp4")
    print("done")


