from flask_sqlalchemy import sqlalchemy, SQLAlchemy
from doxaweb_app import db
from doxaweb_app.models import Project
img = ''

title = input("title: ")
description = input("description: ")
short_description = input("short description: ")
link = input("link: ")

i = input("Combien d'images ?")
i =  int(i)

for c in range(i):
    img_link = input("Le lien de l'image: ")
    img = img + ',' + img_link

project = Project(title = title, short_description = short_description, description = description, link = link, img = img)

db.session.add(project)
db.session.commit()