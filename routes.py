from flask import render_template, send_from_directory
from models import Course, Module, Lesson

def init_routes(app):
    @app.route('/')
    def home():
        courses = Course.query.all()
        return render_template('home.html', courses=courses)

    @app.route('/course/<int:course_id>')
    def course(course_id):
        course = Course.query.get_or_404(course_id)
        return render_template('course.html', course=course)

    @app.route('/lesson/<int:lesson_id>')
    def lesson(lesson_id):
        lesson = Lesson.query.get_or_404(lesson_id)
        return render_template('lesson.html', lesson=lesson)

    @app.route('/pdfs/<filename>')
    def download_pdf(filename):
        return send_from_directory('static/pdfs', filename)
