import requests
from bs4 import BeautifulSoup
from pprint import pprint

URL = "https://24.kg/"
HEADERS = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,"
             "image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
             "(KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}
def get_html(url):
    response = requests.get(url=url,headers=HEADERS)
    return response.text


def get_data(html):
    soup = BeautifulSoup (html,"parser.html")
    items = soup.find_all("div", class_ = "title" )

    parserd_data = []
    for item in items :
        parserd_data.append({
            "title":item.find("div", class_="title").find("span").gettext()
        })
    pprint(parserd_data)



html = get_html(URL)
print(html)