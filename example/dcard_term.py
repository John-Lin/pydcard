import time
from curses import wrapper
import sys

from prettytable import PrettyTable

import pydcard


def dcard_terminal(window):
    while True:
        ts = TitlesTable()
        try:
            page_one = pydcard.get_all_new_posts(1)
            for p in page_one:
                got_title = p.get('version')[0].get('title').replace('\n', '')
                got_like_count = str(p.get('likeCount'))
                got_post_id = str(p.get('id'))
                got_sex = '♂' if p.get('member').get('gender') == 'M' else '♀'
                got_author = got_sex + ' ' + p.get('member').get('school')

                got_forum_name = p.get('forum_name').title()
                ts.append_to_table(title=got_title, likes=got_like_count,
                                   pid=got_post_id, author=got_author,
                                   forum=got_forum_name)

                print_msg = str(ts.table_to_str())

            window.addstr(print_msg)
            window.refresh()
            window.erase()
            time.sleep(5)
        except (KeyboardInterrupt, SystemExit):
            sys.exit("Goodbye!")


class TitlesTable(object):
    def __init__(self):
        self.table = []
        self.x = PrettyTable(["Post ID", "討論區", "Likes", "作者", "文章主題"])
        self.x.align["文章主題"] = "l"
        self.x.align["Post ID"] = "l"
        self.x.align["作者"] = "l"

    def append_to_table(self, *args, **kwargs):
        if kwargs:
            self.x.add_row([kwargs['pid'], kwargs['forum'], kwargs['likes'],
                            kwargs['author'], kwargs['title']])

    def table_to_str(self):
        return self.x

if __name__ == '__main__':
    wrapper(dcard_terminal)
