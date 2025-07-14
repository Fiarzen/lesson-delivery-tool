from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    modules = db.relationship('Module', backref='course')

class Module(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))
    lessons = db.relationship('Lesson', backref='module')

class Lesson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    description = db.Column(db.Text)
    youtube_url = db.Column(db.String(255))
    pdf_filename = db.Column(db.String(255))
    module_id = db.Column(db.Integer, db.ForeignKey('module.id'))
