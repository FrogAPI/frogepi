from flask import Flask
from routes import api

from apscheduler.schedulers.background import BackgroundScheduler

from antibrute import reset_nad

scheduler = BackgroundScheduler()
scheduler.add_job(reset_nad, 'interval', hours=1)
scheduler.start()

app = Flask(__name__)

if __name__ == '__main__':
    app.register_blueprint(api, url_prefix='')
    app.run(debug=True)
