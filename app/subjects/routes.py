from flask import Blueprint, render_template, redirect, url_for, request
from app.extensions.database.crud import Session
from app.extensions.database.models import Subject, User, Lesson
from sqlalchemy import func
from flask_login import login_required, current_user
from datetime import datetime, timedelta

blueprint = Blueprint('subjects', __name__)

@blueprint.route('/subject')
@login_required
def subjects():
    s = Session()
    data = s.query(Subject).filter(User.id == Subject.owner_user_id).filter(Subject.owner_user_id == current_user.id).all()
    s.close()
    return render_template('subjects/subjects_page.html', subject_names=data)


@blueprint.route('/subject/<subject_id>')
@login_required
def subject(subject_id):
    s = Session()
    if current_user.id == s.query(Subject.owner_user_id).filter(Subject.id == subject_id).first()[0]:
        subject_name = s.query(Subject.name).filter(Subject.id == subject_id).first()
        data_query=s.query(Lesson).filter(Subject.id == Lesson.subject_id).filter(Subject.id == subject_id).order_by(Lesson.date.desc()).all()
        progress_query=s.query(func.avg(Lesson.progress).label('progress')).filter(Subject.id == Lesson.subject_id).filter(Subject.id == subject_id).first()
        if progress_query.progress is None:
            progress = 0
        else:
            progress = progress_query.progress
        s.close()
        return render_template('subjects/subject.html', subject_name=subject_name, subject_info=data_query, progress=progress)
    else:
        return redirect(url_for('subjects.subjects'))


@blueprint.get('/add_subject')
def addlesson():
    return render_template('subjects/subjectcreator.html')

@blueprint.post('/add_subject')
def add_lesson_func():
    s = Session()
    subject_name = request.form.get('subject_name')
    subject = Subject(name=subject_name, owner_user_id=current_user.id)
    s.add(subject)
    s.commit()
    start_date_str = request.form.get('start_date')
    start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
    selection = request.form.get('frequency')
    start_time = request.form.get('start_time')
    end_time = request.form.get('end_time')
    subject_id = s.query(Subject.id).filter(Subject.name == subject_name).filter(Subject.owner_user_id == current_user.id).first()[0]
    if selection == '1x':
        lesson = Lesson(subject_id = subject_id, date = start_date, start_time = start_time, end_time = end_time)
        s.add(lesson)
    elif selection == 'weekly':
        end_date_str = request.form.get('end_date')
        end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
        delta = end_date - start_date
        for days in range(delta.days + 1):
            date = start_date + timedelta(days=days)
            if date.strftime('%w') == start_date.strftime('%w'):
                lesson = Lesson(subject_id = subject_id, date = date, start_time = start_time, end_time = end_time)
                s.add(lesson)
    elif selection == 'monthly':
        end_date_str = request.form.get('end_date')
        end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
        delta = end_date - start_date
        for days in range(delta.days + 1):
            date = start_date + timedelta(days=days)
            if date.strftime('%-d') == start_date.strftime('%-d'):
                lesson = Lesson(subject_id = subject_id, date = date, start_time = start_time, end_time = end_time)
                s.add(lesson)
    s.commit()
    s.close()
    return redirect(url_for('subjects.subjects'))

