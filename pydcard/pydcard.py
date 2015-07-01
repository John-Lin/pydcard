import requests
# from pprint import pprint
from urllib.parse import urljoin
from functools import wraps

from .api import FORUM_APIS, POST_CONTENT_API, TOP_POST_API


def pageassert(func):
    '''
    Decorator that assert page number
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        if args[0] < 1 or args[0] > 40:
            raise ValueError('Page Number not found')
        return func(*args, **kwargs)
    return wrapper


def get_post(post_id):
    post_api = urljoin(POST_CONTENT_API, str(post_id))
    r = requests.get(post_api)
    if r.status_code == requests.codes.ok:
        # print (pprint(r.json()))
        return r.json()
    else:
        print(r.status_code)
        return None


@pageassert
def get_all_top_posts(page_num=1):
    if page_num < 1 or page_num > 40:
        raise ValueError('Page Number not found')
        return None

    total_posts = []

    for i in range(1, page_num+1):
        top_posts_api = TOP_POST_API.replace('<PageNumber>', str(i))
        r = requests.get(top_posts_api)
        if r.status_code == requests.codes.ok:
            total_posts = total_posts + r.json()
        else:
            print(r.status_code)
            return None
    return total_posts


@pageassert
def get_all_new_posts(page_num=1):
    total_posts = []

    for i in range(1, page_num+1):
        new_posts_api = urljoin(FORUM_APIS.get('FORUM_ALL_API'), str(i))
        r = requests.get(new_posts_api)
        if r.status_code == requests.codes.ok:
            total_posts = total_posts + r.json()
        else:
            print(r.status_code)
            return None
    return total_posts


@pageassert
def get_all_page(page_num):
    pages_api = urljoin(FORUM_APIS.get('FORUM_ALL_API'), str(page_num))
    r = requests.get(pages_api)
    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        print(r.status_code)
        return None


@pageassert
def get_mother_page(page_num):
    pages_api = urljoin(FORUM_APIS.get('FORUM_MOTHER_API'), str(page_num))
    r = requests.get(pages_api)
    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        print(r.status_code)
        return None


@pageassert
def get_graduate_page(page_num):
    pages_api = urljoin(FORUM_APIS.get('FORUM_GRADUATE_API'), str(page_num))
    r = requests.get(pages_api)
    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        print(r.status_code)
        return None


@pageassert
def get_funny_page(page_num):
    pages_api = urljoin(FORUM_APIS.get('FORUM_FUNNY_API'), str(page_num))
    r = requests.get(pages_api)
    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        print(r.status_code)
        return None


@pageassert
def get_bg_page(page_num):
    pages_api = urljoin(FORUM_APIS.get('FORUM_BG_API'), str(page_num))
    r = requests.get(pages_api)
    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        print(r.status_code)
        return None


@pageassert
def get_trending_page(page_num):
    pages_api = urljoin(FORUM_APIS.get('FORUM_TRENDING_API'), str(page_num))
    r = requests.get(pages_api)
    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        print(r.status_code)
        return None


@pageassert
def get_talk_page(page_num):
    pages_api = urljoin(FORUM_APIS.get('FORUM_TALK_API'), str(page_num))
    r = requests.get(pages_api)
    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        print(r.status_code)
        return None


@pageassert
def get_girl_page(page_num):
    pages_api = urljoin(FORUM_APIS.get('FORUM_GIRL_API'), str(page_num))
    r = requests.get(pages_api)
    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        print(r.status_code)
        return None


@pageassert
def get_boy_page(page_num):
    pages_api = urljoin(FORUM_APIS.get('FORUM_BOY_API'), str(page_num))
    r = requests.get(pages_api)
    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        print(r.status_code)
        return None


@pageassert
def get_mood_page(page_num):
    pages_api = urljoin(FORUM_APIS.get('FORUM_MOOD_API'), str(page_num))
    r = requests.get(pages_api)
    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        print(r.status_code)
        return None


@pageassert
def get_music_page(page_num):
    pages_api = urljoin(FORUM_APIS.get('FORUM_MUSIC_API'), str(page_num))
    r = requests.get(pages_api)
    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        print(r.status_code)
        return None


@pageassert
def get_movie_page(page_num):
    pages_api = urljoin(FORUM_APIS.get('FORUM_MOVIE_API'), str(page_num))
    r = requests.get(pages_api)
    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        print(r.status_code)
        return None


@pageassert
def get_literature_page(page_num):
    pages_api = urljoin(FORUM_APIS.get('FORUM_LITERATURE_API'), str(page_num))
    r = requests.get(pages_api)
    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        print(r.status_code)
        return None


@pageassert
def get_sport_page(page_num):
    pages_api = urljoin(FORUM_APIS.get('FORUM_SPORT_API'), str(page_num))
    r = requests.get(pages_api)
    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        print(r.status_code)
        return None


@pageassert
def get_pet_page(page_num):
    pages_api = urljoin(FORUM_APIS.get('FORUM_PET_API'), str(page_num))
    r = requests.get(pages_api)
    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        print(r.status_code)
        return None


@pageassert
def get_food_page(page_num):
    pages_api = urljoin(FORUM_APIS.get('FORUM_FOOD_API'), str(page_num))
    r = requests.get(pages_api)
    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        print(r.status_code)
        return None


@pageassert
def get_job_page(page_num):
    pages_api = urljoin(FORUM_APIS.get('FORUM_JOB_API'), str(page_num))
    r = requests.get(pages_api)
    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        print(r.status_code)
        return None


@pageassert
def get_studyabroad_page(page_num):
    pages_api = urljoin(FORUM_APIS.get('FORUM_STUDYABROAD_API'), str(page_num))
    r = requests.get(pages_api)
    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        print(r.status_code)
        return None


@pageassert
def get_marvel_page(page_num):
    pages_api = urljoin(FORUM_APIS.get('FORUM_MARVEL_API'), str(page_num))
    r = requests.get(pages_api)
    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        print(r.status_code)
        return None


@pageassert
def get_sex_page(page_num):
    pages_api = urljoin(FORUM_APIS.get('FORUM_SEX_API'), str(page_num))
    r = requests.get(pages_api)
    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        print(r.status_code)
        return None


@pageassert
def get_dcard_page(page_num):
    pages_api = urljoin(FORUM_APIS.get('FORUM_DCARD_API'), str(page_num))
    r = requests.get(pages_api)
    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        print(r.status_code)
        return None


@pageassert
def get_delete_page(page_num):
    pages_api = urljoin(FORUM_APIS.get('FORUM_DELETE_API'), str(page_num))
    r = requests.get(pages_api)
    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        print(r.status_code)
        return None


@pageassert
def get_whysoserious_page(page_num):
    pages_api = urljoin(FORUM_APIS.get('FORUM_WHYSOSERIOUS_API'),
                        str(page_num))
    r = requests.get(pages_api)
    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        print(r.status_code)
        return None


if __name__ == '__main__':
    pass
