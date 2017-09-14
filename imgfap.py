#!/usr/bin/python3
import urllib.request
import re
import os

while True:
    while True:
        try:
            URL = ""
            pnum = ""
            imglist = ""
            URL = input("Please input the gallery url: ")
            url = "http://www.imagefap.com/pictures/"
            galleryId = URL.replace(url, "")
            galleryId = galleryId.split("/")[0]
            URL = "{}{}/?grid={}&view=2".format(url, galleryId, galleryId)
            html = urllib.request.urlopen(URL).read()
            break
        except Exception:
            print("Input not formatted right")
            pass
    imglist = re.findall('<td id="([0-9]+)" align="center"  ?valign="top">', str(html))
    imglist2 = []
    for image in imglist:
        url = "http://www.imagefap.com/photo/{}/".format(image)
        html = urllib.request.urlopen(url).read()
        imglist2.append(re.findall('"contentUrl": "(.*?)",', str(html)))
        print("Processed {}/{}".format(str(len(imglist2)), str(len(imglist))))
    urls = imglist2
    image = urls[0]
    image = image[0]
    dir_name = str(image).split("/")[-3]
    os.mkdir(dir_name)
    print("Downloading {} images".format(str(len(urls))))
    for image in urls:
        image = str(image[0])
        name = image.split("/")[-1]
        with urllib.request.urlopen(image) as f:
            imageContent = f.read()
            with open(dir_name + '/' + name, "wb") as f:
                f.write(imageContent)
                print("downloaded " + name)
    exit_in = input("download another?[y/n]")
    if exit_in == "n":
        exit()
