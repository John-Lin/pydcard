import time
from curses import wrapper
import sys

from tabulate import tabulate

import pydcard


class TitlesTable(object):
    def __init__(self, header=["Post ID", "Forum", "Likes", "♂ ♀",
                               "Come from", "Post title"]):
        self.headers = header
        self.table = []

    def append_to_table(self, *args, **kwargs):
        if kwargs:
            self.table.append([kwargs['pid'], kwargs['forum'], kwargs['likes'],
                               kwargs['gender'], kwargs['school'],
                               kwargs['title']])

    def table_to_str(self, tablefmt="Planet"):
        return tabulate(self.table, self.headers, tablefmt=tablefmt,
                        numalign='left', stralign='left')


def dcard_terminal(window):
    while True:
        ts = TitlesTable()
        try:
            page_one = pydcard.get_all_new_posts(1)
            for p in page_one:
                got_title = p.get('version')[0].get('title')
                got_like_count = str(p.get('likeCount'))
                got_post_id = str(p.get('id'))

                got_sex = '♂' if p.get('member').get('gender') == 'M' else '♀'

                got_school = p.get('member').get('school')
                if '大學' in got_school:
                    got_school = got_school.replace('大學', '')

                got_forum_name = p.get('forum_alias').title()
                ts.append_to_table(title=got_title, likes=got_like_count,
                                   pid=got_post_id, school=got_school,
                                   gender=got_sex, forum=got_forum_name)

                print_msg = str(ts.table_to_str())

            window.addstr(print_msg)
            window.refresh()
            window.erase()
            time.sleep(15)
        except (KeyboardInterrupt, SystemExit):
            sys.exit("Goodbye!")

if __name__ == '__main__':
    wrapper(dcard_terminal)
