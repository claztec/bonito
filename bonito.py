# -*- coding: utf-8 -*-

import json
import sys
from flask import Flask, render_template, jsonify, make_response, request
from model.Library import Library
from search import get_books


app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')




@app.route('/api/libraries')
def get_libraries():
    library = Library()
    library.library_id = 1
    library.name = '분당도서관'
    library.website = 'http://bd.snlib.net'
    library.image = 'http://tong.visitkorea.or.kr/cms/resource/31/1785931_image2_1.jpg'

    library2 = Library()
    library2.library_id = 2
    library2.name = '성남중앙도서관'
    library2.website = 'http://ct.snlib.net'
    library2.image = 'http://tong.visitkorea.or.kr/cms/resource/49/1785949_image2_1.jpg'


    result = {}
    libraries = []
    libraries.append(library.to_json())
    libraries.append(library2.to_json())
    # result['libraries'] = libraries
    result_str = json.dumps(libraries, ensure_ascii=False)

    # try:
    #     result_str = jsonify(libraries=libraries)
    # except Exception, e:
    #     print e
    #     print result.to_json()

    response = make_response(result_str)
    response.headers['Content-Type'] = 'application/json;charset=UTF-8'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

@app.route('/api/libraries/<library_id>')
def get_library(library_id):
    library = Library()
    library.library_id = 1
    library.name = '분당도서관'
    library.website = 'http://bd.snlib.net'
    library.image = 'http://tong.visitkorea.or.kr/cms/resource/31/1785931_image2_1.jpg'
    result_str = json.dumps(library.to_json(), ensure_ascii=False)

    response = make_response(result_str)
    response.headers['Content-Type'] = 'application/json;charset=UTF-8'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


# http://ash84.net/2015/07/16/flask-euckr/
@app.route('/api/books/search', methods=['POST', 'GET'])
def search_books():
    if request.method == 'POST':
        form_data = decode_raw_data(request.get_data())
        query = form_data['query']
        find_books = get_books(query)

        books = []
        for book in find_books:
            books.append(book.to_json())

    else:
        books = ''

    result_str = json.dumps(books, ensure_ascii=False)
    response = make_response(result_str)
    response.headers['Content-Type'] = 'application/json;charset=UTF-8'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

def decode_raw_data(raw):
    try:
        data = dict()
        for r in raw.split('&'):
            c = r.split('=')
            data[c[0]] = c[1]
        return data
    except Exception as e:
        # TODO : Exception logging
        return None

if __name__ == '__main__':
    print sys.path
    app.run(host='192.168.219.188')
