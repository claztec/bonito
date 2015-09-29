# -*- coding: utf-8 -*-
class Book:
    book_id = 0
    name = ''
    image = ''
    booking = ''
    call_number = ''

    def to_json(self):
        # http://simplectic.com/blog/2014/flask-todomvc-sqlalchemy/
        return {
            "id" : self.book_id,
            "name" : self.name,
            "image" : self.image,
            "booking" : self.booking,
            "callnumber" : self.call_number
        }