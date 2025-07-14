from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, FileField, SubmitField
from wtforms.validators import DataRequired

class CourseForm(FlaskForm):
    title = StringField('Course Title', validators=[DataRequired()])
    submit = SubmitField('Create Course')

class ModuleForm(FlaskForm):
    title = StringField('Module Title', validators=[DataRequired()])
    course_id = SelectField('Course', coerce=int)
    submit = SubmitField('Create Module')

class LessonForm(FlaskForm):
    title = StringField('Lesson Title', validators=[DataRequired()])
    description = TextAreaField('Description')
    youtube_url = StringField('YouTube Embed URL')
    module_id = SelectField('Module', coerce=int)
    pdf_file = FileField('Upload PDF')
    submit = SubmitField('Create Lesson')
