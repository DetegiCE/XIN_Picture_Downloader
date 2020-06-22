import io
import re
import urllib.request
from bs4 import BeautifulSoup
from PIL import Image

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
    imgs = list()
    for i in range(0, reslen//2):
        tpic = res1[i]
        tpic = tpic.replace("small_slide","large_slide")
        tpic = tpic.replace(".png",".jpg")
        turl = imus[0] + "/slide/" + tpic
        urllib.request.urlretrieve(turl,"./download/p"+str(i+1)+".jpg")
        print(str(i+1)+"/"+str(reslen//2)+" Complete")
        if i == 0:
            img1 = Image.open("./download/p1.jpg")
            im1 = img1.convert("RGB")
        else:
            imgX = Image.open("./download/p"+str(i+1)+".jpg")
            imX = imgX.convert("RGB")
            imgs.append(imX)
    im1.save("./download/slide.pdf", save_all=True, append_images=imgs)
    print("Pictures Download & PDF conversion complete")
    print("MP4 Downloading...",end='')
    q = re.compile("main_\([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\)\.mp4")
    res2 = q.findall(atxt)
    aurl = imus[0].replace("web_files","media_files") + "/" + res2[0]
    urllib.request.urlretrieve(aurl, "./download/audio.mp4")
    print("done")
