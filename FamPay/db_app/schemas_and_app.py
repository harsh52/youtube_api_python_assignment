from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import re

engine = create_engine('postgresql://postgres:toor@localhost:5432/postgres', echo=False)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:toor@localhost:5432/postgres'

db = SQLAlchemy(app)

class YT_search_info(db.Model):
    __tablename__ = "yt_search_info"
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    vid_id = Column(String(50), primary_key=True)
    title = Column(String)
    desc = Column(String)
    thumbnails_url = Column(String)
    channel_title = Column(String)
    publish_at = Column(DateTime)


class last_script_run(db.Model):
    __tablename__ = "last_script_run"
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    script_name = Column(String, primary_key=True)
    last_run_time = Column(DateTime)



db.Model.metadata.create_all(engine)


@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/yt_video_info', methods=['GET'])
def yt_video_info():
    '''
    A GET API which returns the stored video data in a paginated response sorted in descending order of published datetime.
    '''
    page = request.args.get('page', 1, type=int)
    # info = YT_search_info.query.paginate(page, per_page=2)
    info = YT_search_info.query.order_by(YT_search_info.publish_at.desc()).paginate(page, per_page=10)
    data = info.items
    list = []
    for item in data:
        dict = {}
        dict['vid_id'] = item.vid_id
        dict['channel_title'] = item.channel_title
        dict['desc'] = item.desc
        dict['publish_at'] = item.publish_at
        dict['title'] = item.title
        list.append(dict)
    return jsonify(list)

@app.route('/search_video', methods=['GET'])
def search_video():
    """
    A basic search API to search the stored videos using their title and description.

    """
    # title = request.args.get('title', type=str)
    # desc = request.args.get('desc', type=str)
    title = re.sub('\W+', ' ', request.args.get('title', type=str))
    desc = re.sub('\W+', ' ', request.args.get('desc', type=str))

    data = YT_search_info.query.filter(YT_search_info.title.like("%"+title+"%") | YT_search_info.title.like("%"+desc+"%")).all()
    list = []
    if len(data) == 0:
        return(f"No result found")
    for item in data:
        dict = {}
        dict['vid_id'] = item.vid_id
        dict['channel_title'] = item.channel_title
        dict['desc'] = item.desc
        dict['publish_at'] = item.publish_at
        dict['title'] = item.title
        list.append(dict)

    return jsonify(list)



def application():
    app.run(host='127.0.0.1', port=5000)


def optimize_search_query(title):
    all_title = session.query(YT_search_info.title).all()
