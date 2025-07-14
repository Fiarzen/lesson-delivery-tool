from flask import Flask, render_template, send_from_directory
from models import db, Course, Module, Lesson

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///courses.db'
db.init_app(app)

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
