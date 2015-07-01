import pydcard
from pprint import pprint

# Get top posts in *all* forum. The parameter is page number.
page_one = pydcard.get_all_top_posts(1)

# Each page have 20 threads, now get the id in index 0
# e.g. the first thread's id
th_one_id = page_one[0].get('id')

# Using thread id to get the post content
pprint((pydcard.get_post(th_one_id)))
