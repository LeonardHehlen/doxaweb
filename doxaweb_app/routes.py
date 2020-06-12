from flask import Flask, render_template, redirect, url_for, request, session
from flask_sqlalchemy import sqlalchemy, SQLAlchemy
from doxaweb_app import app, db
from doxaweb_app.models import Project

var_to_template = {}

@app.route("/")
def home():
    projects = Project.query.all()
    imgs = []

    return render_template('index.html', projects=projects, enumerate=enumerate, imgs=imgs)

@app.route("/test")
def test():
    projects = Project.query.all()

    return render_template("test.html", projects=projects)

@app.route("/project/<project_id>")
def project(project_id):
    project = Project.query.filter_by(id=project_id).first()
    print(project)

    return render_template("project.html", project=project)

@app.route("/admin", methods = ['GET', 'POST'])
def admin():
    projects = Project.query.all()

    if request.method == 'POST':
        project_id = request.form['delete-btn']
        project = Project.query.filter_by(id=project_id)
        project.delete()
        db.session.commit()
        return redirect(url_for('admin'))
    
    return render_template("admin.html", projects=projects)