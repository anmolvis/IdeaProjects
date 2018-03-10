import requests
from bs4 import BeautifulSoup


def continue_crawl(sh, tu):

    response = requests.get(sh[-1])
    html = response.text
    print(html)
    soup = BeautifulSoup(html, 'html.parser')
    first_link = soup.a.href
    print(first_link)
    if first_link == tu:
        print("reached target url")
        return False
    elif len(sh) > 25:
        print("Searched url is greater than 25")
        return False
    elif first_link not in sh:
            sh.append(first_link)
            return True
    else:
        print("Cycle Occurred")
        return False

    return True
continue_crawl(['https://en.wikipedia.org/wiki/Floating_point'],
               'https://en.wikipedia.org/wiki/Philosophy')


