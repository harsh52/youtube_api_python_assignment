from Script.yt_search import run
from config.api_config import schedule_time
from apscheduler.schedulers.background import BackgroundScheduler
from db_app.schemas_and_app import application
sched = BackgroundScheduler()


# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    """
    Entry point of the application, running async scheduled job and flaks app.
    """
    sched.add_job(run, 'interval', seconds=schedule_time)
    sched.start()

    # app.run()
    application()