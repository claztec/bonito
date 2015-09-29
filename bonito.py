# -*- coding: utf-8 -*-

import json
import sys
from flask import Flask, render_template, jsonify, make_response
from model.Library import Library


app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')

# @app.route('/phones/phones.json')
# def phones():
#     return render_template('phones.json')


@app.route('/libraries.json')
def libraries():
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

if __name__ == '__main__':
    print sys.path
    app.run(host='192.168.219.188')
