import pydcard
from pprint import pprint


def main():
    print (pprint(pydcard.getPost(333656)))

    print (pprint(pydcard.getAllPage(3)))


if __name__ == '__main__':
    main()
