from flask import Flask, render_template, send_from_directory
from models import db, Course, Module, Lesson
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def home():
    courses = Course.query.all()
    return render_template('home.html', courses=courses)

@app.route('/course/<int:course_id>')
def view_course(course_id):
    course = Course.query.get(course_id)
    return render_template('course.html', course=course)

@app.route('/lesson/<int:lesson_id>')
def view_lesson(lesson_id):
    lesson = Lesson.query.get(lesson_id)
    return render_template('lesson.html', lesson=lesson)

@app.route('/pdfs/<filename>')
def get_pdf(filename):
    return send_from_directory('pdfs', filename)
