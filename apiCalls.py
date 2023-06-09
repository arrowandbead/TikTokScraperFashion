import requests
import datetime
from videoInfo import VideoInfo


def getExploreItemByCategory(category_type=7, count=16):
    # 16 seems to be the max for count
    base_url = "https://www.tiktok.com/api/explore/item_list/"

    query_params = {
        "aid": "1988",
        "app_language": "en",
        "app_name": "tiktok_web",
        "browser_language": "en-US",
        "browser_name": "Mozilla",
        "browser_online": "true",
        "browser_platform": "MacIntel",
        "categoryType": str(category_type),
        "channel": "tiktok_web",
        "cookie_enabled": "true",
        "count": str(count),
        "device_id": "7239103375194932779",
        "device_platform": "web_pc",
        "focus_state": "true",
        "history_len": "3",
        "is_page_visible": "true",
        "language": "en",
        "os": "mac",
        "region": "US",
        "screen_height": "900",
        "screen_width": "1440",
        "tz_name": "America/New_York",
        "webcast_language": "en"
    }

    
    url = base_url + "?" + "&".join([f"{key}={value}" for key, value in query_params.items()])
    # url = "https://www.tiktok.com/api/explore/item_list/?aid=1988&app_language=en&app_name=tiktok_web&browser_language=en-US&browser_name=Mozilla&browser_online=true&browser_platform=MacIntel&browser_version=5.0%20%28Macintosh%3B%20Intel%20Mac%20OS%20X%2010_15_7%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F112.0.0.0%20Safari%2F537.36&categoryType=2&channel=tiktok_web&cookie_enabled=true&count=16&device_id=7239103375194932779&device_platform=web_pc&focus_state=true&from_page=&history_len=3&is_fullscreen=true&is_page_visible=true&language=en&os=mac&priority_region=&referer=&region=US&screen_height=900&screen_width=1440&tz_name=America%2FNew_York&webcast_language=en"
    response = requests.get(url)
    if response.status_code == 200:
        try:
            return response.json()
        except Exception as e:
            return None

    return None

def buildVideoObjects(response):
    itemList = response['itemList']
    videoObjectList = []
    for i in itemList:
        try:
            date_posted = datetime.datetime.fromtimestamp(i['createTime'])
            account = i['author']['uniqueId']
            post_url = "https://www.tiktok.com/@{username}/video/{video_id}".format(username=account, video_id=i["id"])
            saved = i['stats']['collectCount']
            likes = i['stats']['diggCount']
            views = i['stats']['playCount']
            caption = i['desc']
            hashtags = i['contents'][0]['textExtra'] if 'textExtra' in i['contents'][0] else []

            videoObjectList.append(VideoInfo(post_url, account, views, likes, saved, caption, hashtags, date_posted))
        except Exception as e:
            continue

        
    return videoObjectList


# buildVideoObjects(getExploreItemByCategory(count=16))