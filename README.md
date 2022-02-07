# youtube api python assignment
## Project Goal

To make an API to fetch latest videos sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response.

## Basic Requirements:

- Server should call the YouTube API continuously in background (async) with some interval (say 10 seconds) for fetching the latest videos for a predefined search query and should store the data of videos (specifically these fields - Video title, description, publishing datetime, thumbnails URLs and any other fields you require) in a database with proper indexes.:white_check_mark:
- A GET API which returns the stored video data in a paginated response sorted in descending order of published datetime.:white_check_mark:
- A basic search API to search the stored videos using their title and description.:white_check_mark:
- It should be scalable and optimised.:white_check_mark:

## Bonus Points:

- Add support for supplying multiple API keys so that if quota is exhausted on one, it automatically uses the next available key.:white_check_mark:
- Optimise search api, so that it's able to search videos containing partial match for the search query in either video title or description.
    - Ex 1: A video with title *`How to make tea?`* should match for the search query `tea how`:white_check_mark:

## Tools used
- Python3.9, flask, sqlalchemy, postgreSQL

## How to start the program?
- Install `python3.9` and `postgreSQL` in your system.
- config youtube api key in api_config file eg: `key_list = ["key_1", "key_2","key_3", "key_4"]` and setup your db cred in `schemas_and_app.py`
- Navigate to `FamPay` folder
- Install all dependencies using `pip install -r requirements.txt`
- Run `main.py` it will take care of all the heavylifting.
- Voila! you will see application started working.
- Hit the postman and observe the result.
- Below is api output.

### API to show result in paginated format in descending order of published datetime.
![Show result in paginated format](https://user-images.githubusercontent.com/38341037/152645192-22d96586-5964-4761-aaf3-dbf8e9d957d2.jpg)

### A Optimise search api to search the stored videos using their title and description.
![image](https://user-images.githubusercontent.com/38341037/152645269-149030b6-d1e8-4253-a064-38d61c37c258.png)


## Reference:

- YouTube data v3 API: [https://developers.google.com/youtube/v3/getting-started](https://developers.google.com/youtube/v3/getting-started)
- Search API reference: [https://developers.google.com/youtube/v3/docs/search/list](https://developers.google.com/youtube/v3/docs/search/list)
    - To fetch the latest videos you need to specify these: type=video, order=date, publishedAfter=<SOME_DATE_TIME>
    - Without publishedAfter, it will give you cached results which will be too old


