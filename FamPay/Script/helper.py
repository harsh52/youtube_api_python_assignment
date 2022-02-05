from config.api_config import key_list, SEARCH_KEYWORD
from apiclient.discovery import build

count = 0

def yt_resource(key):
    """
    Make resource for youtube api usage.
    key: youtube api key.
    """
    youtube = build('youtube', 'v3', developerKey=key)
    return youtube

def make_search_query_on_yt(keyword):
    """
    Responsible for making search query on youtube and if key is invalid automatically switch to next available key.
    keyword: Search keyword for youtube api
    """
    try:
        global count

        request = yt_resource(key=key_list[count]).search().list(q=keyword, part='snippet', type='video',maxResults=20)
        res = request.execute()
        return res
    except Exception as e:
        # if api fails increase the counter and use next available api.
        count = count + 1
        print(f"Not able to make api call reason {e}")




