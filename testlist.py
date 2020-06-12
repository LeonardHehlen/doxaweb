from flask_sqlalchemy import sqlalchemy, SQLAlchemy
from doxaweb_app import db
from doxaweb_app.models import Project

projects = Project.query.all()

for project in projects:
    imgs = project.img.split(",")
    imgs.pop(0)

print(imgs)