# -*- coding: utf-8 -*-
class Library:
    library_id = 0
    name = ''
    image = ''
    website = ''

    def to_json(self):
        # http://simplectic.com/blog/2014/flask-todomvc-sqlalchemy/
        return {
            "id": self.library_id,
            "name": self.name,
            "image": self.image,
            "website": self.website
        }