from db_app.schemas_and_app import YT_search_info, last_script_run, session
from Script.helper import make_search_query_on_yt
from config.api_config import SEARCH_KEYWORD, script_name, key_list
from datetime import datetime


def convertDate(d):
    new_date = datetime.strptime(d, "%Y-%m-%dT%H:%M:%fZ")
    return new_date


def store_yt_search_in_db():
    try:
        data = fetch_last_run_script_time(script_name)
        res = make_search_query_on_yt(keyword=SEARCH_KEYWORD)
        for items in res['items']:
            yt_data = items.get('snippet')
            id = items.get('id')
            yt_db_data = session.query(YT_search_info).filter(YT_search_info.vid_id == id.get('videoId')).all()

            # if len(data) == 0 or data[0].last_run_time < convertDate(yt_data.get('publishTime')):
            if len(yt_db_data) == 0:
                search = YT_search_info(created_at=datetime.utcnow(), updated_at=datetime.utcnow(),
                                        vid_id=id.get('videoId'),
                                        title=yt_data.get('title'), desc=yt_data.get('description'),
                                        channel_title=yt_data.get('channelTitle'),
                                        publish_at=yt_data.get('publishTime'))
                session.add(search)
        if len(data) == 0:
            log_time_of_script = last_script_run(created_at=datetime.utcnow(), updated_at=datetime.utcnow(),
                                                 script_name=script_name, last_run_time=datetime.utcnow())
            session.add(log_time_of_script)
        else:
            update_time = session.query(last_script_run).filter(last_script_run.script_name == script_name).first()
            update_time = datetime.utcnow()


    except Exception as e:
        print(f"Not able to store data in db reason: {e}")


def fetch_last_run_script_time(script_name):
    data = session.query(last_script_run).filter(last_script_run.script_name == script_name).all()
    return data



def run():
    store_yt_search_in_db()
    session.commit()
