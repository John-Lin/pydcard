import requests
from pprint import pprint
from urllib.parse import urljoin

FORUM_ALL_API = 'https://www.dcard.tw/api/forum/all/'
POST_CONTENT_API = 'https://www.dcard.tw/api/post/all/'
TOP_POST_API = 'https://www.dcard.tw/api/forum/all/<Page-Number>/popular'

POST_URL = 'https://www.dcard.tw/f/all/p/'


def getPost(post_id):
    post_api = urljoin(POST_CONTENT_API, str(post_id))
    r = requests.get(post_api)
    if r.status_code == requests.codes.ok:
        # print (pprint(r.json()))
        return r.json()
    else:
        print(r.status_code)
        return None


def getAllTopPosts():
    top_posts_api = TOP_POST_API.replace('<Page-Number>', '1')
    r = requests.get(top_posts_api)
    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        print(r.status_code)
        return None


def getAllNewPosts():
    new_posts_api = urljoin(FORUM_ALL_API, '1')
    r = requests.get(new_posts_api)
    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        print(r.status_code)
        return None


def getAllPage(page_num):
    pages_api = urljoin(FORUM_ALL_API, str(page_num))
    r = requests.get(pages_api)
    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        print(r.status_code)
        return None


def getAllPages():
    pass

if __name__ == '__main__':
    pass
