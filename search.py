# -*- coding: utf-8 -*-
from urllib import urlopen, urlencode
from urllib2 import HTTPError

from bs4 import BeautifulSoup
from model.Book import Book

import re



def _search_library(keyword):
    url = 'http://search.snlib.net/search/resultSearchList'
    try:
        params = urlencode({'searchKeyword':keyword, 'searchKey':2, 'curPage':1, 'searchLibrary':'MB'})
        html = urlopen(url, params)
        print html
    except HTTPError as e:
        # print e
        return None

    try:
        bsObj = BeautifulSoup(html.read())
        booklist = bsObj.find('ul', {'class':'booklistText'})
        tags = booklist.find_all('a')

        search_books = []
        for tag in tags:
            book = Book()
            s = tag['onclick']

            p = re.compile('javascript:viewSearchDetail\((\d+)\)')
            m = p.search(s)

            book.name = tag.get_text()
            book.book_id = int(m.groups(0)[0])
            search_books.append(book)

    except AttributeError as e:
        return None
    return search_books


def _detail_library(book):
    url = 'http://search.snlib.net/search/viewSearchDetail'
    try:
        params = urlencode({'searchLibrary':'MB', 'bookId':book.book_id})
        html = urlopen(url, params)
        # print html.read()
    except HTTPError as e:
        # print e
        return None

    try:
        bsObj = BeautifulSoup(html.read())
        table = bsObj.find('div', {'class':'sojang'})
        tags = table.find_all('td')
        book.call_number = tags[1].get_text().strip()
        book.booking = tags[3].get_text().strip()

        photo = bsObj.find('div', {'class':'photo'}).find('img')
        book.image = photo['src']

        # for tag in tags:
        #     print tag.get_text()
        # tags = booklist.find_all('a')
        #
        # search_books = []
        # for tag in tags:
        #     book = Book()
        #     s = tag['onclick']
        #
        #     p = re.compile('javascript:viewSearchDetail\((\d+)\)')
        #     m = p.search(s)
        #
        #     book.name = tag.get_text()
        #     book.book_id = int(m.groups(0)[0])
        #     search_books.append(book)

    except AttributeError as e:
        print e


    return book



def get_books(keyword):
    search_books = _search_library(keyword)
    for index in range(len(search_books)):
        detail_book = _detail_library(search_books[index])
        search_books[index] = detail_book

    return search_books

if __name__ == "__main__":
    url = 'http://search.snlib.net/search/resultSearchList'
    # url = 'http://search.snlib.net/search/viewSearchDetail'
    keyword = '잉여의 미학'
    # %EC%8A%A4%ED%94%84%EB%A7%81

    books = get_books(keyword)

    for book in books:
        print book.name
        print book.book_id
        print book.booking
        print book.call_number
        print book.image
