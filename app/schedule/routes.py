from flask import Blueprint, render_template, redirect, request, url_for
from flask_login import login_required
from datetime import datetime, timedelta, time
from app.extensions.database.models import Lesson, Subject, UserInSubject
from flask_login import current_user
from app.extensions.database.crud import db

blueprint = Blueprint("schedule", __name__)


@blueprint.get("/schedule")
@login_required
def schedule_no_date():
    return redirect("/schedule/" + datetime.now().strftime("%Y-%m-%d"))


@blueprint.post("/schedule")
@login_required
def schedule_post_date():
    date = request.form.get("date")
    return redirect(url_for("schedule.schedule", date_string=date))


@blueprint.route("/schedule/<date_string>")
@login_required
def schedule(date_string):
    list_of_schedule_times = []
    min_time_of_schedule = time(hour=23, minute=59, second=59)
    max_time_of_schedule = time(hour=0, minute=0, second=0)
    all_lessons_list = []
    given_date = datetime.strptime(date_string, "%Y-%m-%d")
    day_of_week = given_date.strftime("%w")
    if int(day_of_week) == 0:
        day_of_week = 7
    monday = given_date + timedelta(days=-int(day_of_week) + 1)
    tuesday = given_date + timedelta(days=-int(day_of_week) + 2)
    wednesday = given_date + timedelta(days=-int(day_of_week) + 3)
    thursday = given_date + timedelta(days=-int(day_of_week) + 4)
    friday = given_date + timedelta(days=-int(day_of_week) + 5)
    saturday = given_date + timedelta(days=-int(day_of_week) + 6)
    sunday = given_date + timedelta(days=-int(day_of_week) + 7)
    monday_string = monday.strftime("%d.%m.%Y")
    tuesday_string = tuesday.strftime("%d.%m.%Y")
    wednesday_string = wednesday.strftime("%d.%m.%Y")
    thursday_string = thursday.strftime("%d.%m.%Y")
    friday_string = friday.strftime("%d.%m.%Y")
    saturday_string = saturday.strftime("%d.%m.%Y")
    sunday_string = sunday.strftime("%d.%m.%Y")
    all_week_dates = [
        monday_string,
        tuesday_string,
        wednesday_string,
        thursday_string,
        friday_string,
        saturday_string,
        sunday_string,
    ]
    for date in all_week_dates:
        lessons_in_date = (
            db.session.query(Lesson, Subject)
            .filter(Lesson.formatted_date == date)
            .filter(Lesson.subject_id == Subject.id)
            .join(UserInSubject, Subject.id == UserInSubject.subject_id, full=True)
            .filter(
                (Subject.owner_user_id == current_user.id)
                | (UserInSubject.user_id == current_user.id)
            )
            .all()
        )
        all_lessons_list = all_lessons_list + lessons_in_date
        for lesson in lessons_in_date:
            if lesson.Lesson.start_time < min_time_of_schedule:
                min_time_of_schedule = lesson.Lesson.start_time
            if lesson.Lesson.end_time > max_time_of_schedule:
                max_time_of_schedule = lesson.Lesson.end_time
    min_time_of_schedule_rounded = min_time_of_schedule.replace(
        microsecond=0, second=0, minute=0
    )
    if max_time_of_schedule.replace(hour=0) > time(minute=0):
        max_time_of_schedule_rounded = max_time_of_schedule.replace(
            microsecond=0, second=0, minute=0, hour=max_time_of_schedule.hour + 1
        )
    else:
        max_time_rounded = max_time_of_schedule.replace(microsecond=0, second=0)
    if min_time_of_schedule_rounded > max_time_rounded:
        return render_template(
            "schedule/schedule.html", weekdates=all_week_dates, times=[], lessons=[]
        )
    time_of_schedule = min_time_of_schedule_rounded
    while time_of_schedule <= max_time_rounded:
        list_of_schedule_times.append(time_of_schedule)
        time_of_schedule = time_of_schedule.replace(hour=time_of_schedule.hour + 1)
    return render_template(
        "schedule/schedule.html",
        weekdates=all_week_dates,
        times=list_of_schedule_times,
        lessons=all_lessons_list,
    )
