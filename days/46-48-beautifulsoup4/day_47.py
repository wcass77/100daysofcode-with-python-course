import os.path
import sys

import bs4

from download_once import open_or_download

FILE = "nature.html"
URL = "https://www.nature.com/"


def main(force_download=False):
    path = os.path.join(os.path.dirname(__file__), FILE)
    text = open_or_download(URL, path, force_download)
    soup = bs4.BeautifulSoup(text, features="html.parser")
    news = soup.find(id="news-comment")
    articles = news.find_all("article")
    titles = [list(article.a.strings)[1].strip() for article in articles]
    for i, title in enumerate(titles):
        print(f"{i+1}. {title}")


if __name__ == "__main__":
    if len(sys.argv) == 1:
        main()
    elif len(sys.argv) == 2 and sys.argv[1] == "-d":
        main(force_download=True)
    else:
        print("Invalid argument: Valid arguments are: -d or none")
