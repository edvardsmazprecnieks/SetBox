from flask import Blueprint, render_template, redirect
from flask_login import login_required
from datetime import datetime, timedelta, time
from app.extensions.database.models import Lesson, Subject
from flask_login import current_user

blueprint = Blueprint('schedule', __name__)


@blueprint.route('/schedule')
@login_required
def schedule_no_date():
    return redirect('/schedule/' + datetime.now().strftime('%Y-%m-%d'))


@blueprint.route('/schedule/<date_string>')
@login_required
def schedule(date_string):
    times = []
    min_time = time(hour=23, minute=59, second=59)
    max_time = time(hour=0, minute=0, second=0)
    lessons_list = []
    date = datetime.strptime(date_string, '%Y-%m-%d')
    day_of_week = date.strftime('%w')
    if int(day_of_week) == 0:
        day_of_week = 7
    monday = date + timedelta(days=-int(day_of_week)+1)
    tuesday = date + timedelta(days=-int(day_of_week)+2)
    wednesday = date + timedelta(days=-int(day_of_week)+3)
    thursday = date + timedelta(days=-int(day_of_week)+4)
    friday = date + timedelta(days=-int(day_of_week)+5)
    saturday = date + timedelta(days=-int(day_of_week)+6)
    sunday = date + timedelta(days=-int(day_of_week)+7)
    monday_1 = monday.strftime('%d.%m.%Y')
    tuesday_1 = tuesday.strftime('%d.%m.%Y')
    wednesday_1 = wednesday.strftime('%d.%m.%Y')
    thursday_1 = thursday.strftime('%d.%m.%Y')
    friday_1 = friday.strftime('%d.%m.%Y')
    saturday_1 = saturday.strftime('%d.%m.%Y')
    sunday_1 = sunday.strftime('%d.%m.%Y')
    weekdates = [monday_1, tuesday_1, wednesday_1, thursday_1, friday_1, saturday_1, sunday_1]
    for date in weekdates:
        lessons = Lesson.query.filter(Lesson.formatted_date == date).filter(Lesson.subject_id == Subject.id).filter(Subject.owner_user_id == current_user.id).all()
        lessons_list = lessons_list + lessons
        for lesson in lessons:
            if lesson.start_time < min_time:
                min_time = lesson.start_time
            if lesson.end_time > max_time:
                max_time = lesson.end_time
    min_time_rounded = min_time.replace(microsecond=0, second=0, minute=0)
    if max_time.replace(hour = 0) > time(minute = 0):
        max_time_rounded = max_time.replace(microsecond=0, second=0, minute=0, hour = max_time.hour + 1)
    else:
        max_time_rounded = max_time.replace(microsecond=0, second=0)
    if min_time_rounded > max_time_rounded:
        return render_template('schedule/schedule.html', weekdates = weekdates, times = [], lessons = [])
    time_1 = min_time_rounded
    while time_1 <= max_time_rounded:
        times.append(time_1)
        time_1 = time_1.replace(hour = time_1.hour + 1)
    return render_template('schedule/schedule.html', weekdates = weekdates, times = times, lessons = lessons_list)