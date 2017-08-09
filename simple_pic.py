import urllib.request
import re

def download(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'}
    req = urllib.request.Request(url,headers=headers)
    resp = urllib.request.urlopen(req)
    data = resp.read()
    return data

def get_image(html):
    regex = "https://[\S]*\.jpg|http://[\S]*\.jpg"
    pattern = re.compile(regex)
    get_img = re.findall(pattern,repr(html))
    num = 1
    file_path = "/Users/Jeff/Desktop/PC/Pic/"
    for img in get_img:
        print(img)
        image = download(img)
        with open(file_path+"%s.jpg"%num,"wb") as f:
            f.write(image)
            print("正在下载第%s张图片"%num)
            num += 1

url = "http://auto.ifeng.com/"
html = download(url)
get_image(html)
