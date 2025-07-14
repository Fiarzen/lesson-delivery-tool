from flask import request, redirect, url_for, flash, render_template, send_from_directory
from forms import CourseForm, ModuleForm, LessonForm
from models import db, Course, Module, Lesson
import os

UPLOAD_FOLDER = os.path.join("static", "pdfs")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def init_routes(app):
    # existing routes ...

    app.config['SECRET_KEY'] = 'dev'  # For forms
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
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
    @app.route('/admin')
    def admin():
        return render_template('admin.html')

    @app.route('/admin/course', methods=['GET', 'POST'])
    def admin_course():
        form = CourseForm()
        if form.validate_on_submit():
            db.session.add(Course(title=form.title.data))
            db.session.commit()
            flash("Course created!")
            return redirect(url_for('admin'))
        return render_template('admin_course.html', form=form)

    @app.route('/admin/module', methods=['GET', 'POST'])
    def admin_module():
        form = ModuleForm()
        form.course_id.choices = [(c.id, c.title) for c in Course.query.all()]
        if form.validate_on_submit():
            db.session.add(Module(title=form.title.data, course_id=form.course_id.data))
            db.session.commit()
            flash("Module created!")
            return redirect(url_for('admin'))
        return render_template('admin_module.html', form=form)

    @app.route('/admin/lesson', methods=['GET', 'POST'])
    def admin_lesson():
        form = LessonForm()
        form.module_id.choices = [(m.id, m.title) for m in Module.query.all()]
        if form.validate_on_submit():
            filename = None
            if form.pdf_file.data:
                filename = form.pdf_file.data.filename
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                form.pdf_file.data.save(filepath)
            lesson = Lesson(
                title=form.title.data,
                description=form.description.data,
                youtube_url=form.youtube_url.data,
                module_id=form.module_id.data,
                pdf_filename=filename
            )
            db.session.add(lesson)
            db.session.commit()
            flash("Lesson created!")
            return redirect(url_for('admin'))
        return render_template('admin_lesson.html', form=form)
