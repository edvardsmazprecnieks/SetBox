from flask import Blueprint, render_template, request, send_file, make_response, redirect, url_for
from app.extensions.database.crud import db
from app.extensions.database.models import Subject, Lesson, File
from datetime import datetime
from werkzeug.utils import secure_filename
from flask_login import login_required, current_user
import os

blueprint = Blueprint('lesson', __name__)
@blueprint.route('/lesson/<lesson_id>')
@login_required
def lesson(lesson_id):
    data_query=db.session.query(Lesson, Subject).filter(Subject.id == Lesson.subject_id).filter(Lesson.id == lesson_id).first()
    files=File.query.filter(File.lesson_id == Lesson.id).filter(Lesson.id == lesson_id).all()
    return render_template('lesson/lesson.html', info=data_query, files=files)

@blueprint.route('/upload/<lesson_id>', methods=['POST'])
@login_required
def upload(lesson_id):
    file = request.files['file']
    name = request.form['name']
    filename = str(lesson_id) + "_" + datetime.now().strftime('%Y%m%d%H%M%S') + "_" + secure_filename(file.filename)
    file.save("./files/" + filename)
    if filename.endswith('.pdf'):
        file_type = 'PDF'
    elif filename.endswith('.docx') or filename.endswith('.doc') or filename.endswith('.odt') or filename.endswith('.rtf'):
        file_type = 'Text Document'
    elif filename.endswith('.pptx') or filename.endswith('.ppt') or filename.endswith('.odp') or filename.endswith('.pps'):
        file_type = 'Presentation'
    elif filename.endswith('.xlsx') or filename.endswith('.xls'):
        file_type = 'Spreadsheet'
    elif filename.endswith('.jpeg') or filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.gif') or filename.endswith('.bmp') or filename.endswith('.tiff') or filename.endswith('.svg') or filename.endswith('.webp') or filename.endswith('.ico') or filename.endswith('.heic') or filename.endswith('.heif'):
        file_type = 'Image'
    else:
        file_type = 'Other'
    file_to_db = File(
        filename = filename,
        name = name,
        lesson_id = lesson_id,
        type = file_type
    )
    db.session.add(file_to_db)
    db.session.commit()
    return redirect(url_for('lesson.lesson', lesson_id=lesson_id))

@blueprint.route('/delete/<file_id>')
@login_required
def delete(file_id):
    file = File.query.filter(File.id == file_id).first()
    lesson_id = file.lesson_id
    os.remove("./files/" + file.filename)
    db.session.delete(file)
    db.session.commit()
    return redirect(url_for('lesson.lesson', lesson_id=lesson_id))

@blueprint.route('/done/<file_id>')
@login_required
def done(file_id):
    file = File.query.filter(File.id == file_id).first()
    file.reviewed = True
    db.session.commit()
    return redirect(url_for('lesson.lesson', lesson_id=file.lesson_id))

@blueprint.route('/files/<filename>', methods=['GET'])
@login_required
def download(filename):
    file_path = "../files/"+filename
    response = make_response(send_file(file_path))
    return response

@blueprint.get('/lessonadder')
@login_required
def addlesson():
    subjects = Subject.query.filter(Subject.owner_user_id == current_user.id).all()
    return render_template('lesson/lessonadder.html', subjects = subjects)

@blueprint.post('/lessonadder')
@login_required
def addlesson_post():
    name = request.form['lesson_name']
    subject_id = request.form['subjects']
    date = request.form['lesson_date']
    start_time = request.form['start_time']
    end_time = request.form['end_time']
    lesson = Lesson(
        subject_id = subject_id,
        date = date,
        start_time = start_time,
        end_time = end_time,
        name = name
    )
    subject = Subject.query.filter(Subject.id == subject_id).first()
    if subject.owner_user_id != current_user.id:
        return redirect(url_for('lesson.addlesson'))
    db.session.add(lesson)
    db.session.commit()
    return redirect(url_for('lesson.lesson', lesson_id=lesson.id))
