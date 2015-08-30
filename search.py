# -*- coding: utf-8 -*-
from urllib import urlopen, urlencode
from urllib2 import HTTPError

from bs4 import BeautifulSoup

def getTitle(url, keyword):
    try:
        params = urlencode({'searchKeyword':keyword, 'searchKey':2, 'curPage':1, 'searchLibrary':'MB'})
        html = urlopen(url, params)
        # print html.read()
    except HTTPError as e:
        print e
        return None
    try:
        bsObj = BeautifulSoup(html.read())
        booklist = bsObj.find('ul', {'class':'booklistText'})
        tags = booklist.find_all('a')

        list = []
        for tag in tags:
            print ">>>>>> %s" % (tag)
            list.append(tag.get_text())

    except AttributeError as e:
        return None
    return list

# http://search.snlib.net/search/resultSearchList?searchKey=2&amp;curPage=1&amp;searchLibrary=MB&amp;searchKeyword=spring


if __name__ == "__main__":
    url = 'http://search.snlib.net/search/resultSearchList'
    keyword = '객체 지향과 디자인 패턴'
    # %EC%8A%A4%ED%94%84%EB%A7%81
    title = getTitle(url, keyword)
    if title == None:
        print('title could not be found')
    else:
        for t in title:
            print t