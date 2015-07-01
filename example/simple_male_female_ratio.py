import pydcard


def main():
    male = 0
    female = 0

    for page_num in range(1, 41):
        print ('Sending request to page %d' % page_num)
        page = pydcard.get_all_page(page_num)
        for post_thread in range(0, len(page)):
            if page[post_thread].get('member').get('gender') == 'M':
                male = male + 1
            elif page[post_thread].get('member').get('gender') == 'F':
                female = female + 1
            else:
                print ('Unknown gender')
                print (page[post_thread].get('member').get('gender'))
    print ('Female posts: %d, Male posts: %d' % (female, male))
    print ('Female to Male ratio: %f' % (female/male))

if __name__ == '__main__':
    main()
