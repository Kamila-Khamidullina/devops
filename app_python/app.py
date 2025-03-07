from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    date = datetime.now()
    date = str(date).split(' ')
    day = date[0].split('-')
    time = date[1].split(':')
    year, month, number = day[0], day[1], day[2]
    hour, minute, second = time[0], time[1], time[2].split('.')[0]
    return render_template(
        'index.html',
        year=year,
        month=month,
        number=number,
        hour=hour,
        minute=minute,
        second=second
    )
