# -*- coding: utf-8 -*-

import urllib.request
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
}


def visit():
    url = 'http://qudong.pythonanywhere.com/'
    req = urllib.request.Request(url, headers=headers)
    text = urllib.request.urlopen(req).read()

    # print the title, check if you login to site sucessfully
    pat_title = re.compile('<title>(.+?)</title>')
    r = pat_title.search(str(text))
    if r:
        print(r.group(1))
        print(r.group(0))


if __name__ == '__main__':
    visit()


