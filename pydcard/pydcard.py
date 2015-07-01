import requests
from pprint import pprint
from urllib.parse import urljoin

from .api import FORUM_APIS, POST_CONTENT_API, TOP_POST_API


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
    top_posts_api = TOP_POST_API.replace('<PageNumber>', '1')
    r = requests.get(top_posts_api)
    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        print(r.status_code)
        return None


def getAllNewPosts():
    new_posts_api = urljoin(FORUM_APIS.get('FORUM_ALL_API'), '1')
    r = requests.get(new_posts_api)
    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        print(r.status_code)
        return None


def getAllPage(page_num):
    pages_api = urljoin(FORUM_APIS.get('FORUM_ALL_API'), str(page_num))
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
